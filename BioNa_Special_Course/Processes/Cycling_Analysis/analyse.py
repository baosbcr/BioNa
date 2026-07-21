"""Combine Bio-Logic + Neware parses -> per-cell specific capacity, ICE, retention."""
import json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data")

# Measured-mass basis: (disk - 5.5255 mg tare) * f. From Processes/Electrode_Prep_Logs/.
MASS = {  # mg hard carbon
    "CC19": 13.021, "CC20": 12.488, "CC21": 12.843, "CC22": 13.555, "CC23": 16.483,
    "CC24": 13.022, "CC25": 20.119, "CC26": 20.119, "CC27": 18.966, "CC28": 11.878,
    "CC29": 11.434, "CC30": 0.561, "CC31": 8.411, "CC32": 8.411, "CC33": 7.475,
    "CC34": 7.298, "CC35": 12.488, "CC36": 11.867, "CC37": 15.063, "CC38": 15.862,
    "CC39": 18.699, "CC40": 20.474, "CC41": None,
}
SAMPLE = {}
for cs, s in [("19 20 21 35 36", "12A_1C"), ("22 23 24 37 38", "12A_2C"),
              ("25 26 27 39 40", "12A_3C"), ("28 29", "10A"), ("30", "8A"),
              ("31 32", "6A"), ("33 34", "Kuranode"), ("41", "MMB2_13A")]:
    for c in cs.split():
        SAMPLE["CC" + c] = s

cells = {}


def cell(name):
    return cells.setdefault(name, {"cell": name, "sample": SAMPLE.get(name),
                                   "mass_mg": MASS.get(name), "cycles": {},
                                   "instrument": None, "notes": []})


# ---- Bio-Logic ----
for r in json.load(open(os.path.join(DATA, "biologic_cycles.json"))):
    m = re.match(r"BNa_(CC\d+)J?_", r["file"])
    c = cell(m.group(1))
    c["instrument"] = "Bio-Logic"
    c["start"] = r.get("started")
    c["comments"] = r.get("comments")
    c["mps"] = os.path.basename(r.get("mps", ""))
    restart = "_restart_" in r["file"]
    segs = [s for s in r["segments"] if s["q"] > 1e-6]
    if "_04_GCPL_" in r["file"]:          # formation = cycle 1
        so = sum(s["q"] for s in segs if s["ox"] == 0)
        de = sum(s["q"] for s in segs if s["ox"] == 1)
        key = "1r" if restart else "1"
        c["cycles"][key] = {"sod": so, "desod": de}
    elif "_07_GCPL_" in r["file"]:        # cycles 2..N
        pairs, cur = [], None
        for s in segs:
            if s["ox"] == 0:
                cur = {"sod": s["q"], "desod": None}
                pairs.append(cur)
            elif cur is not None and cur["desod"] is None:
                cur["desod"] = s["q"]
        for i, p in enumerate(pairs, start=2):
            c["cycles"][f"{i}r" if restart else str(i)] = p

# ---- Neware ----
for r in json.load(open(os.path.join(DATA, "neware_cycles.json"))):
    m = re.search(r"(CC\d+)J", r.get("remark", "") or "")
    if not m:
        continue
    c = cell(m.group(1))
    if c["instrument"] == "Neware":
        continue  # duplicate export of same TestID
    c["instrument"] = "Neware"
    c["start"] = r.get("start")
    c["end"] = r.get("end")
    c["scq"] = r.get("scq")
    c["stepname"] = r.get("stepname")
    # NOTE: do NOT use the 'cycle' sheet. Neware lumps the multi-step formation
    # sodiation AND the first steady-state sodiation into "Cycle Index 1" (same for
    # the two desodiations), which inflates ICE and fabricates a cycle-1->2 crash.
    # Rebuild half-cycles from the 'step' sheet: a run of consecutive CC DChg steps
    # is one sodiation, a run of consecutive CC Chg steps is one desodiation.
    halves, cur = [], None
    for s in r["steps"]:
        t = (s.get("type") or "")
        kind = "sod" if "DChg" in t else ("desod" if "Chg" in t else None)
        if kind is None:                      # Rest
            cur = None
            continue
        try:
            q = float(s.get("cap") or 0)
        except (TypeError, ValueError):
            q = 0.0
        if cur is None or cur["kind"] != kind:
            cur = {"kind": kind, "q": 0.0}
            halves.append(cur)
        cur["q"] += q
    halves = [h for h in halves if h["q"] > 1e-9]
    pairs, cur = [], None
    for h in halves:
        if h["kind"] == "sod":
            cur = {"sod": h["q"], "desod": None}
            pairs.append(cur)
        elif cur is not None and cur["desod"] is None:
            cur["desod"] = h["q"]
    for i, p in enumerate(pairs, start=1):
        c["cycles"][str(i)] = p

# ---- derive ----
rows = []
for name in sorted(cells, key=lambda x: int(x[2:])):
    c = cells[name]
    mass = c["mass_mg"]
    ks = sorted(c["cycles"], key=lambda k: (int(re.sub(r"\D", "", k)), k))
    seq = [(k, c["cycles"][k]) for k in ks
           if c["cycles"][k]["sod"] and c["cycles"][k]["desod"]]
    if not seq:
        rows.append({**c, "mass": c["mass_mg"], "instr": c["instrument"], "n_cyc": 0})
        continue
    k1, c1 = seq[0]
    ice = 100 * c1["desod"] / c1["sod"] if c1["sod"] else None
    last = seq[-1][1]
    ret = 100 * last["desod"] / seq[0][1]["desod"] if seq[0][1]["desod"] else None
    g = (lambda q: q / mass * 1000 if mass else None)
    rows.append({
        "cell": name, "sample": c["sample"], "instr": c["instrument"], "mass": mass,
        "start": c.get("start"), "comments": c.get("comments"), "mps": c.get("mps"),
        "scq": c.get("scq"), "stepname": c.get("stepname"),
        "n_cyc": len(seq), "first_key": k1,
        "sod1": g(c1["sod"]), "desod1": g(c1["desod"]), "ice": ice,
        "desod_last": g(last["desod"]), "ret": ret,
        "raw": {k: (round(v["sod"], 4), round(v["desod"], 4)) for k, v in seq},
    })

json.dump(rows, open(os.path.join(DATA, "summary.json"), "w"), indent=1)

f = "%-6s %-9s %-9s %7s %5s %8s %8s %6s %8s %6s"
print(f % ("cell", "sample", "instr", "mass", "ncyc", "sod1", "desod1", "ICE%", "last", "ret%"))
print("-" * 86)
for r in rows:
    n = lambda v, d=1: ("%.*f" % (d, v)) if isinstance(v, (int, float)) else "--"
    print(f % (r["cell"], r["sample"] or "?", r.get("instr") or "?", n(r.get("mass"), 3),
               r["n_cyc"], n(r.get("sod1")), n(r.get("desod1")), n(r.get("ice")),
               n(r.get("desod_last")), n(r.get("ret"))))
