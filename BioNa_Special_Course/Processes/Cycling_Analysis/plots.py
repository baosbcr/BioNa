"""Figures for the CC19-CC41 cycling review.

Palette: dataviz reference categorical slots, documented order (adjacent pairlist).
All-pairs forms (scatter) capped at 3 series per that palette's series cap.
Light mode only - these are report/print figures.
"""
import json, os, re, warnings
warnings.filterwarnings("ignore")
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data")
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
FIG = os.path.join(REPO, "Figures")
CELLDIR = os.path.join(FIG, "cells")
os.makedirs(CELLDIR, exist_ok=True)

SUM = {r["cell"]: r for r in json.load(open(os.path.join(DATA, "summary.json")))}
FIN = {r["cell"]: r for r in json.load(open(os.path.join(DATA, "final.json")))}
PEIS = json.load(open(os.path.join(DATA, "peis.json")))

# ---- design tokens ----
SURF = "#fcfcfb"
INK = "#0b0b0b"
INK2 = "#52514e"
MUTED = "#8a8a85"
GRID = "#e5e5e1"
SLOT = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#e87ba4", "#008300", "#4a3aa7", "#e34948"]
BAD = "#e34948"

plt.rcParams.update({
    "figure.facecolor": SURF, "axes.facecolor": SURF, "savefig.facecolor": SURF,
    "font.size": 9, "axes.labelsize": 9.5, "axes.titlesize": 11,
    "axes.edgecolor": GRID, "axes.labelcolor": INK2, "text.color": INK,
    "xtick.color": INK2, "ytick.color": INK2, "xtick.labelsize": 8.5, "ytick.labelsize": 8.5,
    "axes.grid": True, "grid.color": GRID, "grid.linewidth": 0.7,
    "axes.spines.top": False, "axes.spines.right": False,
    "legend.frameon": False, "legend.fontsize": 8.5,
    "lines.linewidth": 2, "lines.markersize": 5,
    "figure.dpi": 150, "savefig.dpi": 150, "savefig.bbox": "tight",
})

# sample -> (label, temperature C, ramp C/min)
SAMPLES = {
    "6A":       ("600 °C", 600, 3),
    "8A":       ("800 °C", 800, 3),
    "10A":      ("1000 °C", 1000, 3),
    "12A_3C":   ("1200 °C", 1200, 3),
    "12A_2C":   ("1200 °C, 2 °C/min", 1200, 2),
    "12A_1C":   ("1200 °C, 1 °C/min", 1200, 1),
    "Kuranode": ("Kuranode (commercial)", None, None),
}
# Colour follows the entity: one fixed sample -> slot map used by EVERY figure.
SAMPLE_ORDER = ["6A", "8A", "10A", "12A_1C", "12A_2C", "12A_3C", "Kuranode"]
COLOR = {s_: SLOT[i] for i, s_ in enumerate(SAMPLE_ORDER)}
# Secondary encoding, so identity never rests on colour alone (CVD / print / greyscale).
MARK = dict(zip(SAMPLE_ORDER, ["o", "v", "s", "D", "^", "P", "X"]))

TEMP_SERIES = ["6A", "8A", "10A", "12A_3C"]
RAMP_SERIES = ["12A_1C", "12A_2C", "12A_3C"]

EXCLUDE = {"CC24": "erratic contact", "CC27": "suspected short",
           "CC30": "failed 8A coating", "CC31": "no data"}


def cycles(cell):
    """-> (n[], sod mAh/g[], desod mAh/g[]) with truncated trailing cycle dropped."""
    r = SUM.get(cell)
    if not r or not r["n_cyc"]:
        return None
    m = r["mass"]
    ks = list(r["raw"])
    s = [r["raw"][k][0] / m * 1000 for k in ks]
    d = [r["raw"][k][1] / m * 1000 for k in ks]
    while len(d) > 1 and 100 * d[-1] / s[-1] < 92:
        s.pop(); d.pop(); ks.pop()
    return np.arange(1, len(d) + 1), np.array(s), np.array(d)


def cells_of(sample, good_only=True):
    out = []
    for c, r in SUM.items():
        if r["sample"] != sample or not r["n_cyc"]:
            continue
        if good_only and c in EXCLUDE:
            continue
        out.append(c)
    return sorted(out, key=lambda x: int(x[2:]))


def endlabel(ax, x, y, txt, color):
    ax.annotate(txt, (x, y), xytext=(5, 0), textcoords="offset points",
                va="center", ha="left", fontsize=8, color=INK2)


def save(fig, name):
    p = os.path.join(FIG, name)
    fig.savefig(p)
    plt.close(fig)
    print("wrote", os.path.relpath(p, REPO))


# ============ 1. Standalone: one figure per cell ============
for cell in sorted(SUM, key=lambda x: int(x[2:])):
    cy = cycles(cell)
    if cy is None:
        continue
    n, s, d = cy
    r, f = SUM[cell], FIN[cell]
    ce = 100 * d / s
    fig, (a1, a2) = plt.subplots(2, 1, figsize=(5.4, 5.2), sharex=True,
                                 gridspec_kw={"height_ratios": [2.4, 1]})
    a1.plot(n, s, "o-", color=SLOT[0], label="Sodiation (discharge)")
    a1.plot(n, d, "s-", color=SLOT[1], label="Desodiation (charge)")
    a1.set_ylabel("Specific capacity (mAh g$^{-1}$)")
    a1.set_ylim(bottom=0)
    a1.legend(loc="upper right")
    flag = f"  — EXCLUDED: {EXCLUDE[cell]}" if cell in EXCLUDE else ""
    restart_note = ("   ·   x = run order, not a clean cycle index (restart)"
                    if any(k.endswith("r") for k in r["raw"]) else "")
    a1.set_title(f"{cell}  ·  {SAMPLES[r['sample']][0]}  ·  {r['instr']}{flag}\n"
                 f"ICE {f['ice']:.1f}%   ·   active mass {r['mass']:.3f} mg{restart_note}",
                 color=BAD if cell in EXCLUDE else INK, loc="left", fontsize=10)
    a2.axhline(100, color=MUTED, lw=1, ls=(0, (4, 3)))
    cec = np.clip(ce, 0, 112)
    a2.plot(n, cec, "o-", color=SLOT[6])
    for xi, yi in zip(n, ce):
        if yi > 112:
            a2.annotate(f"{yi:.0f}%", (xi, 112), xytext=(0, -11),
                        textcoords="offset points", ha="center", fontsize=7.5, color=BAD)
    a2.set_ylabel("CE (%)")
    a2.set_xlabel("Cycle number")
    a2.set_ylim(min(40, ce.min() - 5), 118)
    a2.set_xticks(n)
    fig.savefig(os.path.join(CELLDIR, f"{cell}.png"))
    plt.close(fig)
print(f"wrote {len(os.listdir(CELLDIR))} per-cell figures -> Figures/cells/")


# ============ 2. Temperature series: capacity vs cycle ============
def series_fig(samples, title, fname, note=None):
    fig, ax = plt.subplots(figsize=(6.4, 4.2))
    ends = []
    for samp in samples:
        col = COLOR[samp]
        cs = cells_of(samp)
        if not cs:
            continue
        for j, c in enumerate(cs):
            n, s, d = cycles(c)
            ax.plot(n, d, marker=MARK[samp], ls="-", color=col,
                    alpha=1 if j == 0 else 0.55,
                    label=SAMPLES[samp][0] if j == 0 else None,
                    markersize=4.5)
    # Direct labels are selective: with only 3 series and a legend present, end
    # labels are redundant and collide at the right edge. Legend + marker shape
    # already carry identity without relying on colour.
    ax.set_xlabel("Cycle number")
    ax.set_ylabel("Reversible capacity (mAh g$^{-1}$)")
    ax.set_title(title, loc="left")
    ax.set_ylim(bottom=0)
    ax.set_xlim(0.5, 10.6)
    ax.legend(loc="upper right")
    if note:
        ax.annotate(note, (0.5, -0.22), xycoords="axes fraction", ha="center",
                    fontsize=8, color=MUTED)
    save(fig, fname)


series_fig(TEMP_SERIES,
           "Reversible capacity vs cycle — pyrolysis temperature series (3 °C/min)",
           "02_capacity_vs_cycle_temperature.png",
           "Replicate cells shown at reduced opacity. Excluded cells omitted: "
           "CC24, CC27, CC30, CC31.")

series_fig(RAMP_SERIES,
           "Reversible capacity vs cycle — ramp-rate series (1200 °C)",
           "03_capacity_vs_cycle_ramprate.png",
           "Replicate cells shown at reduced opacity.")


# ============ 3. THE headline: normalised fade, incl. benchmark ============
fig, ax = plt.subplots(figsize=(7.0, 4.6))
# Ordered low->high temperature, then ramp variants, benchmark last.
order = SAMPLE_ORDER
plot_order = ["10A", "12A_1C", "12A_2C", "12A_3C", "Kuranode"]
for samp in plot_order:
    cs = cells_of(samp)                     # healthy cells only
    if not cs:
        continue
    col = COLOR[samp]
    bench = samp == "Kuranode"
    for j, c in enumerate(cs):
        n, s, d = cycles(c)
        if len(d) < 2:
            continue
        ax.plot(n[1:], 100 * d[1:] / d[1], marker=MARK[samp], ls="-", color=col,
                markersize=6 if bench else 4, lw=3.2 if bench else 1.8,
                alpha=1 if (j == 0 or bench) else 0.5, zorder=5 if bench else 2,
                label=SAMPLES[samp][0] if j == 0 else None)
ax.axhline(100, color=MUTED, lw=1, ls=(0, (4, 3)))
ax.annotate("no fade", (10.4, 101.5), fontsize=8, color=MUTED, ha="right")
# call out the control
cbench = cells_of("Kuranode")[0]
n, s, d = cycles(cbench)
ax.annotate("commercial benchmark —\nfades as fast as the samples",
            (n[-1], 100 * d[-1] / d[1]), xytext=(9.9, 42), textcoords="data",
            fontsize=8.5, color=COLOR["Kuranode"], ha="right", va="top",
            arrowprops=dict(arrowstyle="-", color=COLOR["Kuranode"], lw=1.2,
                            connectionstyle="arc3,rad=-0.2"))
ax.set_xlabel("Cycle number")
ax.set_ylabel("Capacity retention, normalised to cycle 2 (%)")
ax.set_title("Every sample fades — including the commercial benchmark", loc="left")
ax.legend(loc="lower left", ncol=2)
ax.set_ylim(30, 112)
ax.set_xlim(1.7, 10.6)
ax.annotate("Healthy cells only. 600 °C (CC32) and 800 °C (CC30) omitted: both are degenerate\n"
            "low-capacity cells whose flat retention is not comparable — see review §4.3, §4.5.",
            (0.5, -0.20), xycoords="axes fraction", ha="center", fontsize=7.5, color=MUTED)
save(fig, "01_systemic_fade_all_samples.png")


# ============ 4. ICE vs temperature and vs ramp (dot plots, 1 series) ============
def ice_panel(ax, samples, xof, col, xlabel, title, xticks, jitter):
    """Replicates jittered on x; only excluded cells are labelled."""
    for samp in samples:
        x0 = xof(samp)
        cs = cells_of(samp, good_only=False)
        cs = [c for c in cs if FIN[c].get("ice") is not None]
        offs = np.linspace(-jitter, jitter, len(cs)) if len(cs) > 1 else [0]
        for c, o in zip(cs, offs):
            excl = c in EXCLUDE
            ec = COLOR[samp]
            ax.plot(x0 + o, FIN[c]["ice"], "o", ms=7.5, mew=1.8,
                    color=BAD if excl else ec,
                    mfc="none" if excl else ec, zorder=4)
            if excl:
                ax.annotate(c, (x0 + o, FIN[c]["ice"]), xytext=(8, -3),
                            textcoords="offset points", fontsize=7.5, color=BAD)
    pts = [(xof(s), np.mean([FIN[c]["ice"] for c in cells_of(s)]))
           for s in samples if cells_of(s)]
    if len(pts) > 1:
        ax.plot([p[0] for p in pts], [p[1] for p in pts], "-", color=col, lw=2, zorder=1)
    for x, v in pts:
        ax.annotate(f"{v:.0f}%", (x, v), xytext=(0, 14), textcoords="offset points",
                    ha="center", fontsize=8.5, color=INK2, fontweight="bold",
                    clip_on=False)
    ax.margins(x=0.12)
    ax.set_xlabel(xlabel)
    ax.set_ylabel("Initial coulombic efficiency (%)")
    ax.set_title(title, loc="left", fontsize=10)
    ax.set_xticks(xticks)
    ax.set_ylim(0, 100)


fig, (a1, a2) = plt.subplots(1, 2, figsize=(9.0, 4.0))
ice_panel(a1, TEMP_SERIES, lambda s: SAMPLES[s][1], INK2,
          "Pyrolysis temperature (°C)", "ICE rises with pyrolysis temperature",
          [600, 800, 1000, 1200], jitter=22)
a1.annotate("open red marker = excluded cell (not in mean)\nmean line skips 800 °C — only cell is CC30",
            (0.03, 0.05), xycoords="axes fraction", fontsize=7.5, color=MUTED)
ice_panel(a2, RAMP_SERIES, lambda s: SAMPLES[s][2], INK2,
          "Ramp rate (°C/min), 1200 °C", "ICE is flat across ramp rate",
          [1, 2, 3], jitter=0.11)
a2.annotate("n = 4, 3, 4 cells", (0.03, 0.05), xycoords="axes fraction",
            fontsize=7.5, color=MUTED)
save(fig, "04_ICE_temperature_and_ramprate.png")


# ============ 5. Instrument cross-check ============
fig, ax = plt.subplots(figsize=(6.2, 4.0))
pairs = [("12A_1C", "12A_1C"), ("12A_2C", "12A_2C"), ("12A_3C", "12A_3C")]
for i, samp in enumerate(["12A_1C", "12A_2C", "12A_3C"]):
    for c in cells_of(samp):
        n, s, d = cycles(c)
        instr = SUM[c]["instr"]
        ax.plot(n, d, "o-" if instr == "Bio-Logic" else "s--",
                color=COLOR[samp], alpha=0.9, markersize=4,
                label=None)
from matplotlib.lines import Line2D
h = [Line2D([], [], color=MUTED, marker="o", ls="-", label="Bio-Logic (C/10 desod, 2.2 V)"),
     Line2D([], [], color=MUTED, marker="s", ls="--", label="Neware (C/20 desod, 2.0 V)")]
h += [Line2D([], [], color=COLOR[s], marker="", ls="-", label=SAMPLES[s][0])
      for s in ["12A_1C", "12A_2C", "12A_3C"]]
ax.legend(handles=h, loc="upper right")
ax.set_xlabel("Cycle number")
ax.set_ylabel("Reversible capacity (mAh g$^{-1}$)")
ax.set_title("Instrument cross-check — protocols are not equivalent", loc="left")
ax.set_ylim(bottom=0)
save(fig, "05_instrument_crosscheck.png")


# ============ 6. EIS: |Z| at 1 Hz by stage ============
STAGE = {"01": "assembled", "03": "pre-formation", "06": "post-formation", "09": "post-cycling"}
fig, ax = plt.subplots(figsize=(6.6, 4.2))
rows = {}
for r in PEIS:
    if r["restart"] or not r["npts"] or r.get("fmin", 9e9) > 2:
        continue
    rows.setdefault(r["cell"], {})[r["stage"]] = r["Zmag_lowf"]
xpos = {s: i for i, s in enumerate(["01", "03", "06", "09"])}
for cell, st in sorted(rows.items(), key=lambda kv: int(kv[0][2:])):
    ks = [s for s in ["01", "03", "06", "09"] if s in st]
    if len(ks) < 3:
        continue
    samp = SUM[cell]["sample"]
    ax.plot([xpos[k] for k in ks], [st[k] for k in ks], "o-",
            color=COLOR[samp], markersize=5, alpha=0.85)
    if cell in ("CC30", "CC32"):
        ax.annotate(f"{cell} ({SAMPLES[samp][0]})", (xpos[ks[-1]], st[ks[-1]]),
                    xytext=(8, 0), textcoords="offset points", fontsize=8,
                    color=COLOR[samp], va="center", fontweight="bold")
ax.set_xticks(list(xpos.values()))
ax.set_xticklabels([STAGE[s] for s in xpos])
ax.set_yscale("log")
ax.set_ylabel("|Z| at 1 Hz (Ω)")
ax.set_title("Cell impedance FALLS across the run — it does not rise", loc="left")
ax.margins(x=0.16)
ax.annotate("One line per cell; colour = sample, as in Fig. 01. Only sweeps reaching ≤2 Hz shown.\n"
            "The two labelled cells are the degenerate ones — they stay far more resistive throughout.",
            (0.5, -0.18), xycoords="axes fraction", ha="center", fontsize=8, color=MUTED)
save(fig, "06_EIS_impedance_by_stage.png")

print("\nDONE")
