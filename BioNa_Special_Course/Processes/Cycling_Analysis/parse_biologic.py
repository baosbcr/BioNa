"""Bio-Logic .mpr -> per-half-cycle capacities (biologic_cycles.json).

Reads the BINARY .mpr directly. The .txt exports this originally parsed were deleted
2026-07-21 as redundant (verified: identical point counts and capacities).

Two things the stock galvani cannot do unaided:
  1. Column ID 182 ('step time/s') is absent from its map and every GCPL file uses it.
     Without the patch below: NotImplementedError. PEIS files parse fine unpatched.
  2. 'ox/red' is a packed bit-flag, not a column -> unpack via MPRfile.flags_dict.
"""
import glob, json, os, re, sys, warnings
warnings.filterwarnings("ignore")
import numpy as np
from galvani import BioLogic

BioLogic.VMPdata_colID_dtype_map[182] = ("step time/s", "<f8")

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
SRC = os.path.join(REPO, "Experimental_Data", "Cycling", "BioLogic_CC19-CC33")
OUT = os.path.join(HERE, "data", "biologic_cycles.json")

# Header strings live in the 'VMP settings' module as latin-1 text.
META = [("Comments", "comments"), ("Electrode material", "electrode"),
        ("Loaded Setting File", "mps")]


def meta_from_settings(mpr):
    out = {}
    blob = next((m["data"] for m in mpr.modules if b"settings" in m["longname"]), b"")
    txt = blob.decode("latin-1", errors="replace")
    for key, tag in META:
        m = re.search(re.escape(key) + r"\s*:?\s*([^\x00\r\n]{0,160})", txt)
        if m:
            out[tag] = m.group(1).strip().strip(":").strip()
    return out


def parse(path):
    mpr = BioLogic.MPRfile(path)
    d = mpr.data
    meta = {"file": os.path.basename(path).replace(".mpr", ".txt"),
            "started": str(getattr(mpr, "timestamp", "") or mpr.startdate),
            "n_points": len(d)}
    meta.update(meta_from_settings(mpr))

    if len(d) == 0:                 # stub file from an aborted run (CC27 _07, CC31 C15)
        meta.update({"segments": [], "n_error_rows": 0})
        return meta

    mask, _ = mpr.flags_dict["ox/red"]
    ox = ((d["flags"] & mask) != 0).astype(np.int8)
    err_mask, _ = mpr.flags_dict.get("error", (0, 0))
    nerr = int(((d["flags"] & err_mask) != 0).sum()) if err_mask else 0

    ns = d["Ns"].astype(int)
    t, dq, e = d["time/s"], d["dq/mA.h"], d["Ewe/V"]

    # a half-cycle = a contiguous run of constant (Ns, ox/red)
    brk = np.r_[True, (np.diff(ns) != 0) | (np.diff(ox) != 0)]
    ids = np.cumsum(brk) - 1
    segs = []
    for i in range(ids.max() + 1):
        k = ids == i
        dur = float(t[k][-1] - t[k][0])
        q = float(np.abs(dq[k]).sum())
        segs.append({
            "ns": int(ns[k][0]), "ox": int(ox[k][0]), "q": q, "n": int(k.sum()),
            "t0": float(t[k][0]), "t1": float(t[k][-1]),
            "e0": float(e[k][0]), "e1": float(e[k][-1]),
            "emin": float(e[k].min()), "emax": float(e[k].max()),
            "dur_h": dur / 3600.0,
            # <I> is computed by EC-Lab on export, not stored: recover as dq/dt
            "i_mean_mA": (q * 3600.0 / dur) * (1 if ox[k][0] else -1) if dur else 0.0,
        })
    meta["segments"] = segs
    meta["n_error_rows"] = nerr
    return meta


if __name__ == "__main__":
    files = sorted(glob.glob(os.path.join(SRC, "*_GCPL_*.mpr")))
    if not files:
        sys.exit(f"no GCPL .mpr under {SRC}")
    print(f"{len(files)} GCPL .mpr files", flush=True)
    res = []
    for p in files:
        r = parse(p)
        res.append(r)
        print("  done", r["file"], r["n_points"], "pts", len(r["segments"]), "segs", flush=True)
    res.sort(key=lambda r: r["file"])
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    json.dump(res, open(OUT, "w"), indent=1)
    print("wrote", OUT)
