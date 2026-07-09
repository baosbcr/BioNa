# Coin-Cell Disk Log — MMB1_12A_1C

**Sample:** MMB1_12A_1C (1200 °C, 60 °C/h = 1 °C/min ramp) — calendered electrode (roll gap 0.23 mm; see `MMB1_12A_1C_Electrode_Prep.md`)
**Date:** 2026-07-09
**Purpose:** working electrodes for **sodium half-cells** (Na counter, Na always in excess)
**Disks punched:** 20 → **3 discarded (light outliers), 17 kept** · **Cutting die:** 12.7 mm Ø (½″) → **area 1.2668 cm²**
**Foil tare (carbon-coated foil, conductive-C layer, no slurry):** 0.0055 g (5.50 mg) *(assumed same as 6A/8A — confirm)*
**Compute script:** `Processes/Electrode_Prep_Logs/disk_loading.py`

> **Disks are unlabeled and indistinguishable** — masses known as a *set* (same as 6A/8A/10A). See "Uncertainty".
>
> **First deliberate outlier cull.** 3 of 20 disks were discarded as low-mass outliers **before** the analysis:
> **19.52, 19.76, 19.42 mg** (0.01952 / 0.01976 / 0.01942 g). All three sit below the kept range (14.69–16.61 mg
> coating), so the cull removes low tails only — this **biases the reported mean slightly high** vs the full punch.
> Stats below are on the **17 kept**.

---

## Slurry solids composition (from 12A_1C prep log)

| Component | Mass (g) | wt% of dried solids |
|---|---|---|
| Hard carbon (MMB1_12A_1C) | 3.6398 | **88.73** |
| C45 | 0.1673 | 4.08 |
| SBR | 0.195 *(est.)* | 4.75 |
| CMC | 0.1000 | 2.44 |
| **Total solids** | 4.1021 | 100 |

**Active (hard-carbon) fraction f = 0.8873** — assumes the dried coating retains the batch ratio.
Coating mass = disk mass − foil tare. Hard-carbon mass = coating × f.

> ⚠️ **SBR mass not weighed** (200 µL calibrated pipette; deemed unreliable due to evaporation). Best estimate
> ≈ **0.195 g**. **The taped-blade coating (+35 µm) is irrelevant here** — it only affects *thickness*
> comparison across samples, not the *mass* on a punched disk.

---

## Per-disk results (17 kept)

Coating load = coating mass / 1.2668 cm². `± u` is the **per-disk measurement uncertainty** (device-limited,
**die-dominated** — coating is thick, tare term negligible).

| # | Disk wt (mg) | Coating (mg) | Coating load (mg/cm²) | Hard-C load (mg/cm²) |
|---|---|---|---|---|
| 1  | 20.82 | 15.32 | 12.094 ± 0.099 | 10.731 |
| 2  | 20.64 | 15.14 | 11.952 ± 0.098 | 10.605 |
| 3  | 20.19 | 14.69 | 11.596 ± 0.095 | 10.290 |
| 4  | 22.11 | 16.61 | 13.112 ± 0.107 | 11.634 |
| 5  | 21.16 | 15.66 | 12.362 ± 0.101 | 10.969 |
| 6  | 21.21 | 15.71 | 12.402 ± 0.101 | 11.004 |
| 7  | 20.24 | 14.74 | 11.636 ± 0.095 | 10.325 |
| 8  | 20.69 | 15.19 | 11.991 ± 0.098 | 10.640 |
| 9  | 20.62 | 15.12 | 11.936 ± 0.098 | 10.591 |
| 10 | 20.59 | 15.09 | 11.912 ± 0.097 | 10.570 |
| 11 | 20.90 | 15.40 | 12.157 ± 0.099 | 10.787 |
| 12 | 20.24 | 14.74 | 11.636 ± 0.095 | 10.325 |
| 13 | 20.46 | 14.96 | 11.810 ± 0.097 | 10.479 |
| 14 | 21.04 | 15.54 | 12.267 ± 0.100 | 10.885 |
| 15 | 20.87 | 15.37 | 12.133 ± 0.099 | 10.766 |
| 16 | 21.41 | 15.91 | 12.560 ± 0.102 | 11.144 |
| 17 | 21.28 | 15.78 | 12.457 ± 0.102 | 11.053 |

*Discarded (not in stats):* 19.52, 19.76, 19.42 mg.

### Population summary (n = 17 kept)

| Quantity | Mean | SD (spread) | CV | SEM | Min | Max |
|---|---|---|---|---|---|---|
| Coating mass (mg) | 15.351 | 0.492 | 3.2% | 0.119 | 14.690 | 16.610 |
| Coating load (mg/cm²) | **12.118** | 0.388 | 3.2% | 0.094 | 11.596 | 13.112 |
| Hard-carbon load (mg/cm²) | **10.753** | 0.345 | 3.2% | 0.084 | 10.290 | 11.634 |

---

## Uncertainty

**1. Measurement uncertainty (per disk): ≈ ±0.099 mg/cm² (±0.82%), die-dominated.**
u(load)/load = √[(u(coat)/coat)² + (2·u(d)/d)²], u(coat) = 0.034 mg. Coating (~15.4 mg) ≫ tare uncertainty,
so the **assumed ±0.05 mm die tolerance dominates** (0.79%) — same regime as 6A/10A.

**2. Disk-to-disk spread (physical): SD = 0.388 mg/cm² (3.2%).**
~4× the measurement uncertainty → **real coating non-uniformity**, consistent with the as-coated grid scatter
(sheets had CV 17% / 31%; the taped, particle-spiked coating). Note the cull already removed the low tail, so
the *true* punch-to-punch spread is somewhat wider than 3.2%.

### Consequence for the experiment

- **Highest loading of the set** (12.12 mg/cm² coating, 10.75 mg/cm² hard carbon).
- Unlabeled disks → a single cell's active mass known only as the population **10.75 ± 0.35 mg/cm² (±3.2%)**;
  propagates linearly into per-cell gravimetric capacity.
- **Na half-cell / Na in excess:** affects only working-electrode **mass normalisation**, not balancing.

### Recommendation

- **Label disks at punching** to unlock per-cell mAh/g.
- Record the **discard criterion** used for the 3 culled disks (visual defect vs a mass threshold) so the cull is
  reproducible and its bias on the mean is documented.
- Fill in the real **die** spec in `Instruments.md` (dominant term), then re-run `disk_loading.py`.

---

## Cross-sample loading comparison (running)

| Sample | Temp / ramp | n | Coating load (mg/cm²) | Hard-C load (mg/cm²) | CV | Meas. u | Note |
|---|---|---|---|---|---|---|---|
| 6A  | 600 °C  | 20 | 8.48  | 7.53  | 3.6% | ±0.85% (die)  | baseline |
| 8A  | 800 °C  | 21 | 0.479 | 0.430 | 4.3% | ±5.6% (tare)  | anomalously thin (~5 µm) |
| 10A | 1000 °C | 20 | 11.58 | 10.28 | 2.1% | ±0.82% (die)  | most uniform (top band cut) |
| 12A_1C | 1200 °C, 1 °C/min | 17 | **12.12** | **10.75** | 3.2% | ±0.82% (die) | heaviest; 3 outliers culled |

> **8A is the outlier** — its ~18–25× lighter loading (from the ~5 µm coating anomaly) makes it hard to compare
> on equal footing. 6A / 10A / 12A_1C form a consistent 7.5–10.8 mg/cm² hard-carbon band.
