"""Final per-cell table: drops truncated trailing half-cycles before scoring."""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data")
rows = json.load(open(os.path.join(DATA, "summary.json")))

out = []
for r in rows:
    if not r["n_cyc"]:
        out.append({**r, "verdict": "NO DATA"})
        continue
    m = r["mass"]
    ks = list(r["raw"])
    cyc = [(k, s / m * 1000, d / m * 1000) for k, (s, d) in r["raw"].items()]
    # trailing cycle is truncated (run still live / aborted) if its CE < 92%
    trunc = None
    while len(cyc) > 1 and 100 * cyc[-1][2] / cyc[-1][1] < 92:
        trunc = cyc.pop()
    body = cyc[1:]          # cycles 2..N, excluding formation
    r2 = {
        "cell": r["cell"], "sample": r["sample"], "instr": r["instr"], "mass": m,
        "ncomplete": len(cyc), "truncated": trunc[0] if trunc else None,
        "ice": 100 * cyc[0][2] / cyc[0][1],
        "sod1": cyc[0][1], "desod1": cyc[0][2],
        "c2": body[0][2] if body else None,
        "clast": body[-1][2] if body else None,
        "nbody": len(body),
    }
    if body and len(body) > 1:
        r2["ret_2_last"] = 100 * body[-1][2] / body[0][2]
        r2["fade_per_cyc"] = (1 - (body[-1][2] / body[0][2]) ** (1 / (len(body) - 1))) * 100
    out.append(r2)

json.dump(out, open(os.path.join(DATA, "final.json"), "w"), indent=1)

h = "%-6s %-9s %-9s %7s %5s %6s %7s %7s %7s %7s %7s %8s"
print(h % ("cell", "sample", "instr", "mass", "ncyc", "ICE%", "sod1", "desod1",
           "c2", "clast", "ret%", "fade/cyc"))
print("-" * 100)
for r in out:
    if r.get("verdict") == "NO DATA":
        print("%-6s %-9s %-9s %7.3f  -- NO CYCLING DATA" % (r["cell"], r["sample"], r["instr"] or "?", r["mass"]))
        continue
    n = lambda v, d=1: ("%.*f" % (d, v)) if isinstance(v, (int, float)) else "--"
    print(h % (r["cell"], r["sample"], r["instr"], n(r["mass"], 3), r["ncomplete"],
               n(r["ice"]), n(r["sod1"], 0), n(r["desod1"], 0), n(r["c2"], 0),
               n(r["clast"], 0), n(r.get("ret_2_last")), n(r.get("fade_per_cyc"), 2)))
print()
print("truncated trailing cycle dropped for:",
      {r["cell"]: r["truncated"] for r in out if r.get("truncated")})
