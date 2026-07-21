# Coin-Cell Disk Log — MMB1_10A

**Sample:** MMB1_10A (1000 °C, 180 °C/h) — calendered electrode (roll gap 0.205 mm; see `MMB1_10A_Electrode_Prep.md`)
**Date:** 2026-07-09
**Purpose:** working electrodes for **sodium half-cells** (Na counter, Na always in excess)
**Disks punched:** 20 · **Cutting die:** 12.7 mm Ø (½″) → **area 1.2668 cm²**
**Foil tare (carbon-coated foil, conductive-C layer, no slurry):** 0.00555 g (5.55 mg) *(assumed same as 6A/8A — confirm)*
**Compute script:** `Processes/Electrode_Prep_Logs/disk_loading.py`

> **Disks are unlabeled and indistinguishable** — masses known as a *set*; a given mass cannot be matched
> back to the disk built into a given cell (same as 6A/8A). See "Uncertainty".
>
> **Punched from the calendered even section only.** The thick, uneven top band (0–3 cm rows, mean ~0.30 mm)
> was cut off and saved separately before calendering (see prep log). So despite the "bad and inhomogeneous"
> coating note, these disks come from the uniform lower section — which shows in the low CV (2.2%).

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
| 1  | 20.23 | 14.68 | 11.589 ± 0.095 | 10.292 |
| 2  | 20.82 | 15.27 | 12.054 ± 0.099 | 10.705 |
| 3  | 20.05 | 14.50 | 11.446 ± 0.094 | 10.166 |
| 4  | 20.35 | 14.80 | 11.683 ± 0.096 | 10.376 |
| 5  | 20.14 | 14.59 | 11.517 ± 0.094 | 10.229 |
| 6  | 20.06 | 14.51 | 11.454 ± 0.094 | 10.173 |
| 7  | 20.37 | 14.82 | 11.699 ± 0.096 | 10.390 |
| 8  | 20.29 | 14.74 | 11.636 ± 0.095 | 10.334 |
| 9  | 19.96 | 14.41 | 11.375 ± 0.093 | 10.102 |
| 10 | 20.44 | 14.89 | 11.754 ± 0.096 | 10.439 |
| 11 | 19.76 | 14.21 | 11.218 ± 0.092 | 9.962 |
| 12 | 20.53 | 14.98 | 11.825 ± 0.097 | 10.502 |
| 13 | 20.36 | 14.81 | 11.691 ± 0.096 | 10.383 |
| 14 | 19.83 | 14.28 | 11.273 ± 0.093 | 10.011 |
| 15 | 19.53 | 13.98 | 11.036 ± 0.091 | 9.801 |
| 16 | 19.94 | 14.39 | 11.360 ± 0.093 | 10.088 |
| 17 | 20.05 | 14.50 | 11.446 ± 0.094 | 10.166 |
| 18 | 20.05 | 14.50 | 11.446 ± 0.094 | 10.166 |
| 19 | 20.66 | 15.11 | 11.928 ± 0.098 | 10.593 |
| 20 | 19.95 | 14.40 | 11.368 ± 0.093 | 10.095 |

### Population summary (n = 20)

| Quantity | Mean | SD (spread) | CV | SEM | Min | Max |
|---|---|---|---|---|---|---|
| Coating mass (mg) | 14.619 | 0.315 | 2.2% | 0.070 | 13.980 | 15.270 |
| Coating load (mg/cm²) | **11.540** | 0.249 | 2.2% | 0.056 | 11.036 | 12.054 |
| Hard-carbon load (mg/cm²) | **10.249** | 0.221 | 2.2% | 0.049 | 9.801 | 10.705 |

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

**2. Disk-to-disk spread (physical): SD = 0.249 mg/cm² (2.2%).**
This is ~2.5× the measurement uncertainty (0.82%), so the disk-to-disk variation is **real coating
non-uniformity**, though modest — punching from the even lower section kept it tight (the inhomogeneous top
band was cut off before punching).

### Consequence for the experiment

- **Best-loaded and most uniform set so far** (11.54 mg/cm², CV 2.2%). Well-suited as working electrodes.
- Because the disks are **unlabeled**, a single cell's active mass is known only as the population:
  **10.25 ± 0.22 mg/cm² (1σ, ±2.2%)** hard carbon → propagates linearly into per-cell gravimetric capacity.
- **Na half-cell / Na in excess:** affects only the working-electrode **mass normalisation**, not cell balancing.
- Batch-average loading is well-constrained (SEM ≈ 0.05 mg/cm²); **between-sample trends** (6A vs 8A vs 10A) are
  meaningful at batch-mean loadings.

### Recommendation

- **Label disks at punching next time** to unlock per-cell mAh/g (collapses ±2.2% mass ambiguity to ~±0.8%).
- Fill in the real **die** spec in `Instruments.md` (dominant term here), then re-run `disk_loading.py`.

---

## Cross-sample loading comparison (so far)

| Sample | Coating load (mg/cm²) | Hard-C load (mg/cm²) | CV | Meas. u | Note |
|---|---|---|---|---|---|
| 6A  | 8.44  | 7.50  | 3.6% | ±0.85% (die) | baseline |
| 8A  | 0.439 | 0.394 | 4.7% | ±6.1% (tare) | anomalously thin (~5 µm) |
| 10A | **11.54** | **10.25** | 2.2% | ±0.82% (die) | heaviest, most uniform |

---

## Cell Assembly & Cycling

> ⚠️ **Cycler C-rate basis differs from measured mass.** The cycling program's applied current (C-rate) was
> set from a flat **91% active-mass assumption**, not the measured per-sample f used below. (The 5.55 mg
> foil tare now matches on both sides — adopted repo-wide 2026-07-21 — so the **active fraction is the only
> remaining difference**.) See `Biona_Academy/Open_Questions.md` for the full note — recompute specific capacity from the
> measured mass, don't back it out from the nominal C-rate.

**2 sodium half-cells assembled 2026-07-16** (CC28, CC29) from 10A disks.

Electrode (total disk) mass recorded at assembly, rounded to 0.1 mg. Active mass = (disk − 5.55 mg tare) × f,
f = 0.8881. Area 1.2668 cm².

| Cell | Disk mass (mg) | Coating (mg) | **Hard-carbon mass (mg)** | Coating load (mg/cm²) | Hard-C load (mg/cm²) | Status |
|---|---|---|---|---|---|---|
| CC28 | 18.9 | 13.35 | **11.856** | 10.539 | 9.359 | cycling |
| CC29 | 18.4 | 12.85 | **11.412** | 10.144 | 9.009 | cycling |

**Use the per-cell hard-carbon mass** (11.856 / 11.412 mg) to normalise each cell's gravimetric capacity
(mAh/g) — no longer the population value (10.25 ± 0.22 mg/cm² above).

> ⚠️ **Both cells sit just below the 20-disk punch range** (min disk mass 19.53 mg vs 18.9/18.4 mg here) —
> plausible (assembly-day re-weigh, or drawn from a lower-mass disk not in the retained punch table), but
> flagged for traceability, same caveat as noted for CC20/CC21 on 12A_1C.
>
> **Na half-cell / Na in excess** → these masses set only the working-electrode normalisation, not balancing.

**Cycling:** started 2026-07-16, **in progress**. Capacity / rate results — _pending_.
