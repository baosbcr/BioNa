# Coin-Cell Disk Log — MMB1_10A

**Sample:** MMB1_10A (1000 °C, 180 °C/h) — calendered electrode (roll gap 0.205 mm; see `MMB1_10A_Electrode_Prep.md`)
**Date:** 2026-07-09
**Purpose:** working electrodes for **sodium half-cells** (Na counter, Na always in excess)
**Disks punched:** 20 · **Cutting die:** 12.7 mm Ø (½″) → **area 1.2668 cm²**
**Foil tare (carbon-coated foil, conductive-C layer, no slurry):** 0.0055 g (5.50 mg) *(assumed same as 6A/8A — confirm)*
**Compute script:** `Processes/Electrode_Prep_Logs/disk_loading.py`

> **Disks are unlabeled and indistinguishable** — masses known as a *set*; a given mass cannot be matched
> back to the disk built into a given cell (same as 6A/8A). See "Uncertainty".
>
> **Punched from the calendered even section only.** The thick, uneven top band (0–3 cm rows, mean ~0.30 mm)
> was cut off and saved separately before calendering (see prep log). So despite the "bad and inhomogeneous"
> coating note, these disks come from the uniform lower section — which shows in the low CV (2.1%).

---

## Slurry solids composition (from 10A prep log)

| Component | Mass (g) | wt% of dried solids |
|---|---|---|
| Hard carbon (MMB1_10A) | 3.6715 | **88.81** |
| C45 | 0.1673 | 4.05 |
| SBR | 0.195 *(est.)* | 4.72 |
| CMC | 0.1002 | 2.42 |
| **Total solids** | 4.1340 | 100 |

**Active (hard-carbon) fraction f = 0.8881** — assumes the dried coating retains the batch ratio.
Coating mass = disk mass − foil tare. Hard-carbon mass = coating × f.

> ⚠️ **SBR mass not weighed for 10A** (prep log records "0.g" — dosed with the 200 µL calibrated pipette but
> not recorded). Best estimate ≈ **0.195 g** (the calibrated-pipette standard). Sensitivity: dropping SBR to
> zero would raise f by only ~1%, so this has little effect on the hard-carbon load.

---

## Per-disk results

Coating load = coating mass / 1.2668 cm². `± u` is the **per-disk measurement uncertainty** (device-limited,
**die-dominated** — coating is thick, so the tare term is negligible here, unlike 8A).

| # | Disk wt (mg) | Coating (mg) | Coating load (mg/cm²) | Hard-C load (mg/cm²) |
|---|---|---|---|---|
| 1  | 20.23 | 14.73 | 11.628 ± 0.095 | 10.327 |
| 2  | 20.82 | 15.32 | 12.094 ± 0.099 | 10.741 |
| 3  | 20.05 | 14.55 | 11.486 ± 0.094 | 10.201 |
| 4  | 20.35 | 14.85 | 11.723 ± 0.096 | 10.411 |
| 5  | 20.14 | 14.64 | 11.557 ± 0.095 | 10.264 |
| 6  | 20.06 | 14.56 | 11.494 ± 0.094 | 10.208 |
| 7  | 20.37 | 14.87 | 11.739 ± 0.096 | 10.425 |
| 8  | 20.29 | 14.79 | 11.675 ± 0.096 | 10.369 |
| 9  | 19.96 | 14.46 | 11.415 ± 0.094 | 10.138 |
| 10 | 20.44 | 14.94 | 11.794 ± 0.097 | 10.474 |
| 11 | 19.76 | 14.26 | 11.257 ± 0.093 | 9.998 |
| 12 | 20.53 | 15.03 | 11.865 ± 0.097 | 10.537 |
| 13 | 20.36 | 14.86 | 11.731 ± 0.096 | 10.418 |
| 14 | 19.83 | 14.33 | 11.312 ± 0.093 | 10.047 |
| 15 | 19.53 | 14.03 | 11.075 ± 0.091 | 9.836 |
| 16 | 19.94 | 14.44 | 11.399 ± 0.094 | 10.124 |
| 17 | 20.05 | 14.55 | 11.486 ± 0.094 | 10.201 |
| 18 | 20.05 | 14.55 | 11.486 ± 0.094 | 10.201 |
| 19 | 20.66 | 15.16 | 11.967 ± 0.098 | 10.629 |
| 20 | 19.95 | 14.45 | 11.407 ± 0.094 | 10.131 |

### Population summary (n = 20)

| Quantity | Mean | SD (spread) | CV | SEM | Min | Max |
|---|---|---|---|---|---|---|
| Coating mass (mg) | 14.668 | 0.315 | 2.1% | 0.070 | 14.030 | 15.320 |
| Coating load (mg/cm²) | **11.579** | 0.249 | 2.1% | 0.056 | 11.075 | 12.094 |
| Hard-carbon load (mg/cm²) | **10.284** | 0.221 | 2.1% | 0.049 | 9.836 | 10.741 |

---

## Uncertainty

Two distinct uncertainties — **do not conflate them**:

**1. Measurement uncertainty (per disk, device-limited): ≈ ±0.095 mg/cm² (±0.82%).**
Propagated as u(load)/load = √[(u(coat)/coat)² + (2·u(d)/d)²], with u(coat) = 0.034 mg.

| Source | Value (1σ) | Contribution to load |
|---|---|---|
| Balance (Mettler Toledo AX205, fine range) | 0.015 mg | in u(coat) → 0.23% |
| Foil tare (recorded to 0.1 mg) | 0.029 mg | u(coat) = 0.034 mg total → 0.23% |
| **Die diameter (CES cutter)** | **±0.05 mm *(assumed)*** | 2·0.05/12.70 = **0.79% (dominant)** |

> **Die-dominated, like 6A.** The coating (~14.7 mg) is far larger than the foil tare uncertainty, so the die
> tolerance dominates — the CES cutter's die spec is the highest-value fix here. (Contrast 8A, where the ultra-thin
> coating made the tare dominate.)

**2. Disk-to-disk spread (physical): SD = 0.249 mg/cm² (2.1%).**
This is ~2.5× the measurement uncertainty (0.82%), so the disk-to-disk variation is **real coating
non-uniformity**, though modest — punching from the even lower section kept it tight (the inhomogeneous top
band was cut off before punching).

### Consequence for the experiment

- **Best-loaded and most uniform set so far** (11.58 mg/cm², CV 2.1%). Well-suited as working electrodes.
- Because the disks are **unlabeled**, a single cell's active mass is known only as the population:
  **10.28 ± 0.22 mg/cm² (1σ, ±2.1%)** hard carbon → propagates linearly into per-cell gravimetric capacity.
- **Na half-cell / Na in excess:** affects only the working-electrode **mass normalisation**, not cell balancing.
- Batch-average loading is well-constrained (SEM ≈ 0.05 mg/cm²); **between-sample trends** (6A vs 8A vs 10A) are
  meaningful at batch-mean loadings.

### Recommendation

- **Label disks at punching next time** to unlock per-cell mAh/g (collapses ±2.1% mass ambiguity to ~±0.8%).
- Fill in the real **die** spec in `Instruments.md` (dominant term here), then re-run `disk_loading.py`.

---

## Cross-sample loading comparison (so far)

| Sample | Coating load (mg/cm²) | Hard-C load (mg/cm²) | CV | Meas. u | Note |
|---|---|---|---|---|---|
| 6A  | 8.48  | 7.53  | 3.6% | ±0.85% (die) | baseline |
| 8A  | 0.479 | 0.430 | 4.3% | ±5.6% (tare) | anomalously thin (~5 µm) |
| 10A | **11.58** | **10.28** | 2.1% | ±0.82% (die) | heaviest, most uniform |
