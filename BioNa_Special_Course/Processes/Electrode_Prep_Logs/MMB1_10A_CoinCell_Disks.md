# Coin-Cell Disk Log — MMB1_10A

**Sample:** MMB1_10A (1000 °C, 180 °C/h) — calendered electrode (roll gap 0.205 mm; see `MMB1_10A_Electrode_Prep.md`)
**Date:** 2026-07-09
**Purpose:** working electrodes for **sodium half-cells** (Na counter, Na always in excess)
**Disks punched:** 20 · **Cutting die:** 12.7 mm Ø (½″) → **area 1.2668 cm²**
**Foil tare (carbon-coated foil, conductive-C layer, no slurry):** 0.0055255 g (5.53 mg) *(**MEASURED** 2026-07-21: mean of 11 blanks cut with this same 12.7 mm die, SD 0.057 mg — see `Processes/Foil_Tare_Measurement.md`)*
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
| 1  | 20.23 | 14.70 | 11.608 ± 0.102 | 10.309 |
| 2  | 20.82 | 15.29 | 12.074 ± 0.106 | 10.723 |
| 3  | 20.05 | 14.52 | 11.466 ± 0.101 | 10.183 |
| 4  | 20.35 | 14.82 | 11.703 ± 0.103 | 10.393 |
| 5  | 20.14 | 14.61 | 11.537 ± 0.102 | 10.246 |
| 6  | 20.06 | 14.53 | 11.474 ± 0.101 | 10.190 |
| 7  | 20.37 | 14.84 | 11.718 ± 0.103 | 10.407 |
| 8  | 20.29 | 14.76 | 11.655 ± 0.103 | 10.351 |
| 9  | 19.96 | 14.43 | 11.395 ± 0.101 | 10.120 |
| 10 | 20.44 | 14.91 | 11.774 ± 0.104 | 10.456 |
| 11 | 19.76 | 14.23 | 11.237 ± 0.100 | 9.979 |
| 12 | 20.53 | 15.00 | 11.845 ± 0.104 | 10.519 |
| 13 | 20.36 | 14.83 | 11.711 ± 0.103 | 10.400 |
| 14 | 19.83 | 14.30 | 11.292 ± 0.100 | 10.029 |
| 15 | 19.53 | 14.00 | 11.055 ± 0.099 | 9.818 |
| 16 | 19.94 | 14.41 | 11.379 ± 0.101 | 10.106 |
| 17 | 20.05 | 14.52 | 11.466 ± 0.101 | 10.183 |
| 18 | 20.05 | 14.52 | 11.466 ± 0.101 | 10.183 |
| 19 | 20.66 | 15.13 | 11.947 ± 0.105 | 10.610 |
| 20 | 19.95 | 14.42 | 11.387 ± 0.101 | 10.113 |

### Population summary (n = 20)

| Quantity | Mean | SD (spread) | CV | SEM | Min | Max |
|---|---|---|---|---|---|---|
| Coating mass (mg) | 14.643 | 0.315 | 2.2% | 0.070 | 14.005 | 15.294 |
| Coating load (mg/cm²) | **11.559** | 0.249 | 2.2% | 0.056 | 11.055 | 12.074 |
| Hard-carbon load (mg/cm²) | **10.266** | 0.221 | 2.2% | 0.049 | 9.818 | 10.723 |

---

## Uncertainty

Two distinct uncertainties — **do not conflate them**:

**1. Measurement uncertainty (per disk, device-limited): ≈ ±0.102 mg/cm² (±0.88%).**
Propagated as u(load)/load = √[(u(coat)/coat)² + (2·u(d)/d)²], with u(coat) = 0.059 mg.

| Source | Value (1σ) | Contribution to load |
|---|---|---|
| Balance (Mettler Toledo AX205, fine range) | 0.015 mg | in u(coat) → 0.23% |
| Foil tare (measured SD, n=11 blanks) | 0.057 mg | u(coat) = 0.059 mg total → 0.23% |
| **Die diameter (CES cutter)** | **±0.05 mm *(assumed)*** | 2·0.05/12.70 = **0.79% (dominant)** |

> **Die-dominated, like 6A.** The coating (~14.6 mg) is far larger than the foil tare uncertainty, so the die
> tolerance dominates — the CES cutter's die spec is the highest-value fix here. (Contrast 8A, where the ultra-thin
> coating made the tare dominate.)

**2. Disk-to-disk spread (physical): SD = 0.249 mg/cm² (2.2%).**
This is ~2.5× the measurement uncertainty (0.82%), so the disk-to-disk variation is **real coating
non-uniformity**, though modest — punching from the even lower section kept it tight (the inhomogeneous top
band was cut off before punching).

### Consequence for the experiment

- **Best-loaded and most uniform set so far** (11.56 mg/cm², CV 2.2%). Well-suited as working electrodes.
- Because the disks are **unlabeled**, a single cell's active mass is known only as the population:
  **10.27 ± 0.22 mg/cm² (1σ, ±2.2%)** hard carbon → propagates linearly into per-cell gravimetric capacity.
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
| 6A  | 8.46  | 7.51  | 3.6% | ±0.96% (die) | baseline |
| 8A  | 0.459 | 0.412 | 4.5% | ±10.1% (tare) | anomalously thin (~5 µm) |
| 10A | **11.56** | **10.27** | 2.2% | ±0.88% (die) | heaviest, most uniform |

---

## Cell Assembly & Cycling

> ⚠️ **Cycler C-rate basis differs from measured mass.** The cycling program's applied current (C-rate) was
> set from a flat **5.55 mg tare + 91% active-mass assumption**, not the measured values used below
> (**5.5255 mg** tare, measured 2026-07-21, and the per-sample f). The tare side is now nearly exact
> (+0.44%); the **active fraction is the dominant remaining difference**. See `Biona_Academy/Open_Questions.md` for the full note — recompute specific capacity from the
> measured mass, don't back it out from the nominal C-rate.

**2 sodium half-cells assembled 2026-07-16** (CC28, CC29) from 10A disks.

Electrode (total disk) mass recorded at assembly, rounded to 0.1 mg. Active mass = (disk − 5.5255 mg tare) × f,
f = 0.8881. Area 1.2668 cm².

| Cell | Disk mass (mg) | Coating (mg) | **Hard-carbon mass (mg)** | Coating load (mg/cm²) | Hard-C load (mg/cm²) | Status |
|---|---|---|---|---|---|---|
| CC28 | 18.9 | 13.37 | **11.878** | 10.558 | 9.377 | cycling |
| CC29 | 18.4 | 12.87 | **11.434** | 10.163 | 9.026 | cycling |

**Use the per-cell hard-carbon mass** (11.877 / 11.432 mg) to normalise each cell's gravimetric capacity
(mAh/g) — no longer the population value (10.27 ± 0.22 mg/cm² above).

> ⚠️ **Both cells sit just below the 20-disk punch range** (min disk mass 19.53 mg vs 18.9/18.4 mg here) —
> plausible (assembly-day re-weigh, or drawn from a lower-mass disk not in the retained punch table), but
> flagged for traceability, same caveat as noted for CC20/CC21 on 12A_1C.
>
> **Na half-cell / Na in excess** → these masses set only the working-electrode normalisation, not balancing.

**Cycling:** started 2026-07-16, **in progress**. Capacity / rate results — _pending_.
