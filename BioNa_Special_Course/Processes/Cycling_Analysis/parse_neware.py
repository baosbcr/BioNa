"""Parse Neware BTS xlsx exports -> test metadata + per-cycle capacities (JSON)."""
import glob, json, os, warnings
warnings.filterwarnings("ignore")
import openpyxl

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
DATA = os.path.join(HERE, "data")
ROOT = os.path.join(REPO, "Experimental_Data", "Cycling", "Neware_CC34-CC41")
OUT = os.path.join(DATA, "neware_cycles.json")


def rows(ws):
    ws.reset_dimensions()
    return list(ws.iter_rows(values_only=True))


def parse(path):
    wb = openpyxl.load_workbook(path, read_only=True)
    d = {"file": os.path.relpath(path, ROOT).replace("\\", "/")}

    for r in rows(wb["unit"]):
        if r and r[0] == "device":
            d["device"], d["unit"], d["channel"] = r[1], r[2], r[3]
        if r and r[0] == "Start time":
            d["start"], d["end"] = str(r[2]), str(r[6]) if len(r) > 6 else None

    for r in rows(wb["test"]):
        if not r:
            continue
        cells = [str(x) if x is not None else "" for x in r]
        for i, c in enumerate(cells):
            for key, tag in [("Remarks", "remark"), ("Builder", "builder"), ("P/N", "pn"),
                             ("Step Name", "stepname"), ("Cycle count", "cycle_count"),
                             ("Active material", "scq"), ("Nominal specific capacity", "nom_cap"),
                             ("Start step ID", "start_step")]:
                if c == key and i + 2 < len(cells):
                    d[tag] = cells[i + 2]

    cyc = rows(wb["cycle"])
    hdr = [str(x) for x in cyc[0]]
    d["cycles"] = []
    for r in cyc[1:]:
        if r[0] is None:
            continue
        rec = dict(zip(hdr, r))
        try:
            d["cycles"].append({
                "n": int(rec["Cycle Index"]),
                "chg_mAh": float(rec["Chg. Cap.(mAh)"]),
                "dchg_mAh": float(rec["DChg. Cap.(mAh)"]),
            })
        except (ValueError, TypeError, KeyError):
            pass

    st = rows(wb["step"])
    sh = [str(x) for x in st[0]]
    d["steps"] = []
    for r in st[1:]:
        if r[0] is None:
            continue
        rec = dict(zip(sh, r))
        d["steps"].append({
            "cyc": rec.get("Cycle Index"), "idx": rec.get("Step Index"),
            "type": rec.get("Step Type"), "time": rec.get("Step Time"),
            "cap": rec.get("Capacity(mAh)"), "v0": rec.get("Oneset Volt.(V)"),
            "v1": rec.get("End Voltage(V)"), "t0": str(rec.get("Oneset Date")),
        })
    wb.close()
    return d


if __name__ == "__main__":
    files = [p for p in glob.glob(os.path.join(ROOT, "**", "*.xlsx"), recursive=True)
             if "~$" not in p]
    res = []
    for p in sorted(files):
        r = parse(p)
        res.append(r)
        print("done", r["file"], r.get("remark"), len(r["cycles"]), "cycles", flush=True)
    os.makedirs(DATA, exist_ok=True)
    with open(OUT, "w") as f:
        json.dump(res, f, indent=1, default=str)
    print("wrote", OUT)
