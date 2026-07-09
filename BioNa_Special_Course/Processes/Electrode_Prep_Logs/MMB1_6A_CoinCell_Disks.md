# Coin-Cell Disk Log — MMB1_6A

**Sample:** MMB1_6A (600 °C, 180 °C/h) — calendered electrode (roll gap 0.175 mm; see `MMB1_6A_Electrode_Prep.md`)
**Date:** 2026-07-08
**Purpose:** working electrodes for **sodium half-cells** (Na counter, Na always in excess)
**Disks punched:** 20 · **Cutting die:** 12.7 mm Ø (½″) → **area 1.2668 cm²**
**Foil tare (carbon-coated foil, conductive-C layer, no slurry):** 0.0055 g (5.50 mg)
**Compute script:** `Processes/Electrode_Prep_Logs/disk_loading.py`

> **Disks are unlabeled and now indistinguishable** — the 20 masses below are known as a *set*, but a
> given mass cannot be matched back to the specific disk built into a given cell. See "Uncertainty" for the
> consequence on per-cell specific capacity.

---

## Slurry solids composition (from 6A prep log)

| Component | Mass (g) | wt% of dried solids |
|---|---|---|
| Hard carbon (MMB1_6A) | 3.6399 | **88.78** |
| C45 | 0.166 | 4.05 |
| SBR | 0.194 | 4.73 |
| CMC | 0.0999 | 2.44 |
| **Total solids** | 4.0998 | 100 |

**Active (hard-carbon) fraction f = 0.8878** — assumes the dried coating retains the batch ratio.
Coating mass = disk mass − foil tare. Hard-carbon mass = coating × f.

---

## Per-disk results

Coating load = coating mass / 1.2668 cm². `± u` is the **per-disk measurement uncertainty** (device-limited,
die-dominated — see below). It is **not** the disk-to-disk spread.

| # | Disk wt (mg) | Coating (mg) | Coating load (mg/cm²) | Hard-C load (mg/cm²) |
|---|---|---|---|---|
| 1  | 16.72 | 11.22 | 8.86 ± 0.07 | 7.86 |
| 2  | 16.10 | 10.60 | 8.37 ± 0.07 | 7.43 |
| 3  | 16.51 | 11.01 | 8.69 ± 0.07 | 7.72 |
| 4  | 16.62 | 11.12 | 8.78 ± 0.07 | 7.79 |
| 5  | 15.81 | 10.31 | 8.14 ± 0.07 | 7.23 |
| 6  | 15.76 | 10.26 | 8.10 ± 0.07 | 7.19 |
| 7  | 15.98 | 10.48 | 8.27 ± 0.07 | 7.35 |
| 8  | 15.86 | 10.36 | 8.18 ± 0.07 | 7.26 |
| 9  | 15.89 | 10.39 | 8.20 ± 0.07 | 7.28 |
| 10 | 16.49 | 10.99 | 8.68 ± 0.07 | 7.70 |
| 11 | 16.45 | 10.95 | 8.64 ± 0.07 | 7.67 |
| 12 | 15.83 | 10.33 | 8.16 ± 0.07 | 7.24 |
| 13 | 16.60 | 11.10 | 8.76 ± 0.07 | 7.78 |
| 14 | 16.83 | 11.33 | 8.94 ± 0.07 | 7.94 |
| 15 | 16.89 | 11.39 | 8.99 ± 0.07 | 7.98 |
| 16 | 16.17 | 10.67 | 8.42 ± 0.07 | 7.48 |
| 17 | 15.61 | 10.11 | 7.98 ± 0.07 | 7.09 |
| 18 | 16.08 | 10.58 | 8.35 ± 0.07 | 7.42 |
| 19 | 16.32 | 10.82 | 8.54 ± 0.07 | 7.58 |
| 20 | 16.42 | 10.92 | 8.62 ± 0.07 | 7.65 |

### Population summary (n = 20)

| Quantity | Mean | SD (spread) | CV | SEM | Min | Max |
|---|---|---|---|---|---|---|
| Coating mass (mg) | 10.75 | 0.39 | 3.6% | 0.09 | 10.11 | 11.39 |
| Coating load (mg/cm²) | **8.48** | 0.31 | 3.6% | 0.07 | 7.98 | 8.99 |
| Hard-carbon load (mg/cm²) | **7.53** | 0.27 | 3.6% | 0.06 | 7.09 | 7.98 |

---

## Uncertainty

Two distinct uncertainties — **do not conflate them**:

**1. Measurement uncertainty (per disk, device-limited): ≈ ±0.07 mg/cm² (±0.83%).**
Propagated as u(load)/load = √[(u(coat)/coat)² + (2·u(d)/d)²].

| Source | Value (1σ) | Contribution to load |
|---|---|---|
| Balance (Mettler Toledo AX205, fine range) | 0.015 mg | in u(coat) → 0.32% |
| Foil tare (recorded to 0.1 mg) | 0.029 mg | u(coat) = 0.034 mg total → 0.32% |
| **Die diameter (CES cutter)** | **±0.05 mm *(assumed)*** | 2·0.05/12.70 = **0.79% (dominant)** |

> ⚠️ **Balance is now known (AX205), die tolerance is still assumed.** The **die diameter dominates** the
> loading uncertainty, and the CES cutter's die tolerance is undocumented — getting the real value is the
> single highest-value fix. Micrometer (MarCator 1075 R) doesn't enter this calc (mass/area only).
> Update `disk_loading.py` (U_D_MM) once the die spec is known.

**2. Disk-to-disk spread (physical): SD = 0.31 mg/cm² (3.6%).**
This is ~4× larger than the measurement uncertainty, so the variation between disks is **real coating
non-uniformity** (consistent with the as-coated 6A grid, CV 20% over the full sheet), not measurement noise.
The spread also folds in any disk-to-disk foil-mass variation, since a single constant tare was subtracted.

### Consequence for the experiment (why this matters)

Because the disks are **unlabeled**, a cell's active mass cannot be matched to its disk. So for **any single
half-cell**, the normalising mass is known only as the population: **8.48 ± 0.31 mg/cm² (1σ), i.e. ±3.6%**
(full range 7.98–8.99 → up to ≈ ±6%). This uncertainty propagates **directly and linearly** into that cell's
gravimetric specific capacity (mAh g⁻¹): a capacity computed with the mean mass could be off by ~±3.6% (1σ)
purely from not knowing which disk it was.

- **Na half-cell / Na in excess:** the counter electrode is not capacity-limiting, so this does **not**
  affect balancing — it affects only the **mass normalisation** of the working electrode.
- **What is well-constrained:** the *batch-average* loading, to ±0.07 mg/cm² (SEM ≈ measurement u). Trends
  *between samples* (6A vs 8A vs 10A) remain meaningful if each is treated at its batch-mean loading.
- **What is not:** ranking or fine comparison of *individual* 6A cells by specific capacity — the ±3.6%
  mass ambiguity likely exceeds real cell-to-cell differences.

### Recommendation

- **Label disks at punching next time** (weigh → assign an ID → track into the cell). That collapses the
  per-cell mass uncertainty from ±3.6% to the ~±0.8% measurement value and unlocks per-cell mAh/g.
- Fill in the real **balance**, **die**, and **micrometer** specs in `Instruments.md`, then re-run the script.
