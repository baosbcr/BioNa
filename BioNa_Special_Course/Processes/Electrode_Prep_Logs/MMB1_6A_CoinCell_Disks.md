# Coin-Cell Disk Log — MMB1_6A

**Sample:** MMB1_6A (600 °C, 180 °C/h) — calendered electrode (roll gap 0.175 mm; see `MMB1_6A_Electrode_Prep.md`)
**Date:** 2026-07-08
**Purpose:** working electrodes for **sodium half-cells** (Na counter, Na always in excess)
**Disks punched:** 20 · **Cutting die:** 12.7 mm Ø (½″) → **area 1.2668 cm²**
**Foil tare (carbon-coated foil, conductive-C layer, no slurry):** 0.0055255 g (5.53 mg) *(**MEASURED** 2026-07-21: mean of 11 blanks cut with this same 12.7 mm die, SD 0.057 mg — see `Processes/Foil_Tare_Measurement.md`)*
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
| 1  | 16.72 | 11.19 | 8.84 ± 0.08 | 7.85 |
| 2  | 16.10 | 10.57 | 8.35 ± 0.08 | 7.41 |
| 3  | 16.51 | 10.98 | 8.67 ± 0.08 | 7.70 |
| 4  | 16.62 | 11.09 | 8.76 ± 0.08 | 7.78 |
| 5  | 15.81 | 10.28 | 8.12 ± 0.08 | 7.21 |
| 6  | 15.76 | 10.23 | 8.08 ± 0.08 | 7.17 |
| 7  | 15.98 | 10.45 | 8.25 ± 0.08 | 7.33 |
| 8  | 15.86 | 10.33 | 8.16 ± 0.08 | 7.24 |
| 9  | 15.89 | 10.36 | 8.18 ± 0.08 | 7.26 |
| 10 | 16.49 | 10.96 | 8.66 ± 0.08 | 7.68 |
| 11 | 16.45 | 10.92 | 8.62 ± 0.08 | 7.66 |
| 12 | 15.83 | 10.30 | 8.13 ± 0.08 | 7.22 |
| 13 | 16.60 | 11.07 | 8.74 ± 0.08 | 7.76 |
| 14 | 16.83 | 11.30 | 8.92 ± 0.08 | 7.92 |
| 15 | 16.89 | 11.36 | 8.97 ± 0.08 | 7.96 |
| 16 | 16.17 | 10.64 | 8.40 ± 0.08 | 7.46 |
| 17 | 15.61 | 10.08 | 7.96 ± 0.08 | 7.07 |
| 18 | 16.08 | 10.55 | 8.33 ± 0.08 | 7.40 |
| 19 | 16.32 | 10.79 | 8.52 ± 0.08 | 7.57 |
| 20 | 16.42 | 10.89 | 8.60 ± 0.08 | 7.64 |

### Population summary (n = 20)

| Quantity | Mean | SD (spread) | CV | SEM | Min | Max |
|---|---|---|---|---|---|---|
| Coating mass (mg) | 10.72 | 0.39 | 3.6% | 0.09 | 10.08 | 11.36 |
| Coating load (mg/cm²) | **8.46** | 0.31 | 3.6% | 0.07 | 7.96 | 8.97 |
| Hard-carbon load (mg/cm²) | **7.51** | 0.27 | 3.6% | 0.06 | 7.07 | 7.96 |

---

## Uncertainty

Two distinct uncertainties — **do not conflate them**:

**1. Measurement uncertainty (per disk, device-limited): ≈ ±0.08 mg/cm² (±0.96%).**
Propagated as u(load)/load = √[(u(coat)/coat)² + (2·u(d)/d)²].

| Source | Value (1σ) | Contribution to load |
|---|---|---|
| Balance (Mettler Toledo AX205, fine range) | 0.015 mg | in u(coat) → 0.32% |
| Foil tare (measured SD, n=11 blanks) | 0.057 mg | u(coat) = 0.059 mg total → 0.32% |
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
half-cell**, the normalising mass is known only as the population: **8.46 ± 0.31 mg/cm² (1σ), i.e. ±3.6%**
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

---

## Cell Assembly & Cycling

> ⚠️ **Cycler C-rate basis differs from measured mass.** The cycling program's applied current (C-rate) was
> set from a flat **5.55 mg tare + 91% active-mass assumption**, not the measured values used below
> (**5.5255 mg** tare, measured 2026-07-21, and the per-sample f). The tare side is now nearly exact
> (+0.44%); the **active fraction is the dominant remaining difference**. See `Biona_Academy/Open_Questions.md` for the full note — recompute specific capacity from the
> measured mass, don't back it out from the nominal C-rate.

**2 sodium half-cells assembled 2026-07-16** (CC31, CC32) from 6A disks.

Electrode (total disk) mass recorded at assembly, rounded to 0.1 mg. Active mass = (disk − 5.5255 mg tare) × f,
f = 0.8878. Area 1.2668 cm².

| Cell | Disk mass (mg) | Coating (mg) | **Hard-carbon mass (mg)** | Coating load (mg/cm²) | Hard-C load (mg/cm²) | Status |
|---|---|---|---|---|---|---|
| CC31 | 15.0 | 9.47 | **8.411** | 7.479 | 6.640 | cycling |
| CC32 | 15.0 | 9.47 | **8.411** | 7.479 | 6.640 | cycling |

> ⚠️ **Both cells sit just below the 20-disk punch range** (min disk mass 15.61 mg vs 15.0 mg here) — same
> plausible-but-flagged caveat as the 10A cells above.
>
> **Na half-cell / Na in excess** → these masses set only the working-electrode normalisation, not balancing.

**Cycling:** started 2026-07-16, **in progress**. Capacity / rate results — _pending_.
