"""
Thickness heatmaps for as-coated (pre-calendering) MMB1 electrodes.

18-point grids: 6 lengthwise (rows, top -> bottom) x 3 widthwise (cols: Left / Centre / Right).
Data remeasured 2026-07-08. Values in mm (total = coating + carbon-coated foil substrate).

Run:  python thickness_heatmaps.py
Output PNGs -> images/Electrode_Calendering/
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

# repo root = two levels up from this file (Processes/Electrode_Prep_Logs/..)
ROOT = Path(__file__).resolve().parents[2]
OUTDIR = ROOT / "images" / "Electrode_Calendering"
OUTDIR.mkdir(parents=True, exist_ok=True)

COLS = ["Left", "Centre", "Right"]

# (label, lengthwise spacing cm, 6x3 array top->bottom, note)
SAMPLES = {
    "MMB1_6A": dict(
        temp="600 °C", spacing=3.0,
        data=[[0.128, 0.160, 0.201],
              [0.208, 0.246, 0.206],
              [0.150, 0.181, 0.190],
              [0.130, 0.209, 0.198],
              [0.256, 0.215, 0.173],
              [0.214, 0.178, 0.273]],
    ),
    "MMB1_8A": dict(
        temp="800 °C", spacing=2.5,
        data=[[0.022, 0.022, 0.021],
              [0.022, 0.023, 0.022],
              [0.022, 0.022, 0.022],
              [0.021, 0.022, 0.022],
              [0.022, 0.021, 0.022],
              [0.022, 0.023, 0.022]],
    ),
    "MMB1_10A": dict(
        temp="1000 °C", spacing=3.0,
        data=[[0.326, 0.211, 0.255],
              [0.362, 0.297, 0.320],
              [0.205, 0.251, 0.202],
              [0.253, 0.241, 0.253],
              [0.263, 0.180, 0.251],
              [0.223, 0.220, 0.199]],
    ),
    # 12A_1C: 1200 °C, 1 °C/min, TAPED blade (+~35 µm). Columns Left/Centre/Right.
    # High points are spurious (large particles under the gauge), not region-dependent.
    "MMB1_12A_1C_sheet1": dict(
        temp="1200 °C, 1 °C/min · sheet 1", spacing=3.0,
        cols=["Left", "Centre", "Right"],
        data=[[0.231, 0.257, 0.261],
              [0.240, 0.264, 0.236],
              [0.183, 0.255, 0.201],
              [0.349, 0.225, 0.253],
              [0.328, 0.202, 0.269],
              [0.264, 0.275, 0.199]],
    ),
    "MMB1_12A_1C_sheet2": dict(
        temp="1200 °C, 1 °C/min · sheet 2", spacing=2.5,
        cols=["Left", "Centre", "Right"],
        data=[[0.177, 0.131, 0.302],
              [0.317, 0.231, 0.199],
              [0.440, 0.229, 0.175],
              [0.192, 0.259, 0.203],
              [0.361, 0.261, 0.247],
              [0.349, 0.379, 0.258]],
    ),
}


def make_heatmap(name, meta):
    arr = np.array(meta["data"], dtype=float)
    spacing = meta["spacing"]
    ylabels = [f"{i*spacing:g} cm" for i in range(arr.shape[0])]
    row_mean = arr.mean(axis=1)

    fig = plt.figure(figsize=(6.2, 6.6))
    gs = GridSpec(1, 2, width_ratios=[3, 1], wspace=0.05)
    ax = fig.add_subplot(gs[0])
    axr = fig.add_subplot(gs[1], sharey=ax)

    im = ax.imshow(arr, cmap="viridis", aspect="auto")

    # annotate each cell
    vmin, vmax = arr.min(), arr.max()
    thr = (vmin + vmax) / 2
    for i in range(arr.shape[0]):
        for j in range(arr.shape[1]):
            v = arr[i, j]
            ax.text(j, i, f"{v:.3f}", ha="center", va="center",
                    color="white" if v < thr else "black", fontsize=9)

    cols = meta.get("cols", COLS)
    ax.set_xticks(range(len(cols)))
    ax.set_xticklabels(cols)
    ax.set_yticks(range(len(ylabels)))
    ax.set_yticklabels(ylabels)
    ax.set_xlabel("Width position")
    ax.set_ylabel("Distance from top of coating")
    ax.set_title(f"{name}  ({meta['temp']})\nas-coated thickness (mm), n=18",
                 fontsize=11)

    # row-mean side strip
    axr.imshow(row_mean.reshape(-1, 1), cmap="viridis",
               aspect="auto", vmin=arr.min(), vmax=arr.max())
    for i, m in enumerate(row_mean):
        axr.text(0, i, f"{m:.3f}", ha="center", va="center",
                 color="white" if m < thr else "black", fontsize=9)
    axr.set_xticks([0]); axr.set_xticklabels(["row mean"])
    axr.tick_params(axis="y", labelleft=False)

    cbar = fig.colorbar(im, ax=[ax, axr], fraction=0.046, pad=0.08)
    cbar.set_label("Thickness (mm)")

    stats = (f"mean {arr.mean():.3f}  ·  std {arr.std(ddof=1):.3f}  ·  "
             f"CV {100*arr.std(ddof=1)/arr.mean():.1f}%  ·  "
             f"min {arr.min():.3f}  ·  max {arr.max():.3f}  ·  range {np.ptp(arr):.3f} mm")
    fig.text(0.5, 0.02, stats, ha="center", fontsize=8.5)

    out = OUTDIR / f"{name}_thickness_heatmap.png"
    fig.savefig(out, dpi=150, bbox_inches="tight")
    plt.close(fig)
    return arr, out


if __name__ == "__main__":
    for name, meta in SAMPLES.items():
        arr, out = make_heatmap(name, meta)
        rm = arr.mean(axis=1)
        print(f"\n=== {name} ({meta['temp']}) ===")
        print(f"  mean {arr.mean():.4f}  median {np.median(arr):.4f}  std {arr.std(ddof=1):.4f}  "
              f"CV {100*arr.std(ddof=1)/arr.mean():.1f}%  "
              f"min {arr.min():.3f}  max {arr.max():.3f}  range {np.ptp(arr):.3f}")
        print("  row means (top->bottom): " +
              "  ".join(f"{i*meta['spacing']:g}cm={m:.3f}" for i, m in enumerate(rm)))
        print(f"  -> {out}")
