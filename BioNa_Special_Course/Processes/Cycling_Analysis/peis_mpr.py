"""Pull impedance out of the .mpr binaries (the .txt exports lack the Z columns).

Stage codes: 01 = after assembly, 03 = after OCV / pre-formation,
06 = after formation, 09 = after cycling.
Each PEIS contains 3 repeat sweeps ('cycle number'); the last is used.
"""
import glob, json, os, re, warnings
warnings.filterwarnings("ignore")
import numpy as np
from galvani import BioLogic

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
DATA = os.path.join(HERE, "data")
SRC = os.path.join(REPO, "Experimental_Data", "Cycling", "BioLogic_CC19-CC33")
OUT = os.path.join(DATA, "peis.json")

res = []
for p in sorted(glob.glob(os.path.join(SRC, "*_PEIS_*.mpr"))):
    b = os.path.basename(p)
    m = re.match(r"BNa_(CC\d+)J?_\d+(_restart)?_(\d+)_PEIS_(C\d+)\.mpr", b)
    if not m:
        print("skip", b)
        continue
    cell, restart, stage, chan = m.group(1), bool(m.group(2)), m.group(3), m.group(4)
    try:
        d = BioLogic.MPRfile(p).data
    except Exception as e:
        print("ERR", b, e)
        continue
    rec = {"cell": cell, "stage": stage, "chan": chan, "restart": restart,
           "file": b, "npts": len(d)}
    if len(d):
        cyc = d["cycle number"]
        sel = d[cyc == cyc.max()]           # last repeat sweep
        f, re_, im = sel["freq/Hz"], sel["Re(Z)/Ohm"], sel["-Im(Z)/Ohm"]
        o = np.argsort(f)
        f, re_, im = f[o], re_[o], im[o]
        rec.update({
            "n_sweep": len(sel), "fmax": float(f[-1]), "fmin": float(f[0]),
            "Rs_ohm": float(re_[-1]),                     # highest frequency
            "Re_lowf": float(re_[0]), "Im_lowf": float(im[0]),
            "Zmag_lowf": float(np.hypot(re_[0], im[0])),
        })
    res.append(rec)

os.makedirs(DATA, exist_ok=True)
json.dump(res, open(OUT, "w"), indent=1)

cells = sorted({r["cell"] for r in res}, key=lambda c: int(c[2:]))
print("%-6s %-5s | %s" % ("cell", "chan", "  ".join("%-22s" % s for s in
                                                    ["01 assembled", "03 pre-form", "06 post-form", "09 post-cycle"])))
print("-" * 104)
for c in cells:
    for chan in sorted({r["chan"] for r in res if r["cell"] == c}):
        cellrows = [r for r in res if r["cell"] == c and r["chan"] == chan and not r["restart"]]
        out = []
        for s in ("01", "03", "06", "09"):
            r = next((x for x in cellrows if x["stage"] == s), None)
            if r is None:
                out.append("%-22s" % "-")
            elif not r["npts"]:
                out.append("%-22s" % "EMPTY")
            else:
                out.append("%-22s" % ("Rs%.1f  Zlf%.0f" % (r["Rs_ohm"], r["Zmag_lowf"])))
        print("%-6s %-5s | %s" % (c, chan, "  ".join(out)))
