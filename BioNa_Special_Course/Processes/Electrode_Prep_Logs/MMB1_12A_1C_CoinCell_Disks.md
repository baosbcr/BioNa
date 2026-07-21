# Coin-Cell Disk Log — MMB1_12A_1C

**Sample:** MMB1_12A_1C (1200 °C, 60 °C/h = 1 °C/min ramp) — calendered electrode (roll gap 0.23 mm; see `MMB1_12A_1C_Electrode_Prep.md`)
**Date:** 2026-07-09
**Purpose:** working electrodes for **sodium half-cells** (Na counter, Na always in excess)
**Disks punched:** 20 → **3 discarded (light outliers), 17 kept** · **Cutting die:** 12.7 mm Ø (½″) → **area 1.2668 cm²**
**Foil tare (carbon-coated foil, conductive-C layer, no slurry):** 0.0055255 g (5.53 mg) *(**MEASURED** 2026-07-21: mean of 11 blanks cut with this same 12.7 mm die, SD 0.057 mg — see `Processes/Foil_Tare_Measurement.md`)*
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
| 1  | 20.82 | 15.29 | 12.074 ± 0.106 | 10.713 |
| 2  | 20.64 | 15.11 | 11.932 ± 0.105 | 10.587 |
| 3  | 20.19 | 14.66 | 11.576 ± 0.102 | 10.272 |
| 4  | 22.11 | 16.58 | 13.092 ± 0.113 | 11.617 |
| 5  | 21.16 | 15.63 | 12.342 ± 0.108 | 10.951 |
| 6  | 21.21 | 15.68 | 12.382 ± 0.108 | 10.986 |
| 7  | 20.24 | 14.71 | 11.616 ± 0.102 | 10.307 |
| 8  | 20.69 | 15.16 | 11.971 ± 0.105 | 10.622 |
| 9  | 20.62 | 15.09 | 11.916 ± 0.105 | 10.573 |
| 10 | 20.59 | 15.06 | 11.892 ± 0.104 | 10.552 |
| 11 | 20.90 | 15.37 | 12.137 ± 0.106 | 10.769 |
| 12 | 20.24 | 14.71 | 11.616 ± 0.102 | 10.307 |
| 13 | 20.46 | 14.93 | 11.789 ± 0.104 | 10.461 |
| 14 | 21.04 | 15.51 | 12.247 ± 0.107 | 10.867 |
| 15 | 20.87 | 15.34 | 12.113 ± 0.106 | 10.748 |
| 16 | 21.41 | 15.88 | 12.539 ± 0.109 | 11.126 |
| 17 | 21.28 | 15.75 | 12.437 ± 0.108 | 11.035 |

*Discarded (not in stats):* 19.52, 19.76, 19.42 mg.

### Population summary (n = 17 kept)

| Quantity | Mean | SD (spread) | CV | SEM | Min | Max |
|---|---|---|---|---|---|---|
| Coating mass (mg) | 15.326 | 0.492 | 3.2% | 0.119 | 14.665 | 16.584 |
| Coating load (mg/cm²) | **12.098** | 0.388 | 3.2% | 0.094 | 11.576 | 13.092 |
| Hard-carbon load (mg/cm²) | **10.735** | 0.345 | 3.2% | 0.084 | 10.272 | 11.617 |

---

## Uncertainty

**1. Measurement uncertainty (per disk): ≈ ±0.106 mg/cm² (±0.88%), die-dominated.**
u(load)/load = √[(u(coat)/coat)² + (2·u(d)/d)²], u(coat) = 0.059 mg. Coating (~15.4 mg) ≫ tare uncertainty,
so the **assumed ±0.05 mm die tolerance dominates** (0.79%) — same regime as 6A/10A.

**2. Disk-to-disk spread (physical): SD = 0.388 mg/cm² (3.2%).**
~4× the measurement uncertainty → **real coating non-uniformity**, consistent with the as-coated grid scatter
(sheets had CV 17% / 31%; the taped, particle-spiked coating). Note the cull already removed the low tail, so
the *true* punch-to-punch spread is somewhat wider than 3.2%.

### Consequence for the experiment

- **Highest loading of the set** (12.10 mg/cm² coating, 10.74 mg/cm² hard carbon).
- Unlabeled disks → a single cell's active mass known only as the population **10.74 ± 0.35 mg/cm² (±3.2%)**;
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
| 6A  | 600 °C  | 20 | 8.46  | 7.51  | 3.6% | ±0.96% (die)  | baseline |
| 8A  | 800 °C  | 21 | 0.459 | 0.412 | 4.5% | ±10.1% (tare)  | anomalously thin (~5 µm) |
| 10A | 1000 °C | 20 | 11.56 | 10.27 | 2.2% | ±0.88% (die)  | most uniform (top band cut) |
| 12A_1C | 1200 °C, 1 °C/min | 17 | **12.10** | **10.73** | 3.2% | ±0.88% (die) | heaviest; 3 outliers culled |

> **8A is the outlier** — its ~18–25× lighter loading (from the ~5 µm coating anomaly) makes it hard to compare
> on equal footing. 6A / 10A / 12A_1C form a consistent 7.5–10.7 mg/cm² hard-carbon band.

---

## Cell Assembly & Cycling

> ⚠️ **Cycler C-rate basis differs from measured mass.** The cycling program's applied current (C-rate) was
> set from a flat **5.55 mg tare + 91% active-mass assumption**, not the measured values used below
> (**5.5255 mg** tare, measured 2026-07-21, and the per-sample f). The tare side is now nearly exact
> (+0.44%); the **active fraction is the dominant remaining difference**. See `Biona_Academy/Open_Questions.md` for the full note — recompute specific capacity from the
> measured mass, don't back it out from the nominal C-rate.

**3 sodium half-cells assembled 2026-07-14** from 12A_1C disks — **the first labelled cells** (addresses the
"label disks" recommendation above), so per-cell active mass is now known individually rather than as a set.

Electrode (total disk) mass recorded at assembly, rounded to 0.1 mg. Active mass = (disk − 5.5255 mg tare) × f,
f = 0.8873. Area 1.2668 cm².

| Cell | Disk mass (mg) | Coating (mg) | **Hard-carbon mass (mg)** | Coating load (mg/cm²) | Hard-C load (mg/cm²) | Status |
|---|---|---|---|---|---|---|
| CC19 | 20.2 | 14.67 | **13.021** | 11.584 | 10.279 | cycling |
| CC20 | 19.6 | 14.07 | **12.488** | 11.111 | 9.858 | cycling |
| CC21 | 20.0 | 14.47 | **12.843** | 11.426 | 10.139 | cycling |

**Use the per-cell hard-carbon mass** (13.021 / 12.488 / 12.843 mg) to normalise each cell's gravimetric
capacity (mAh/g) — no longer the population value.

> ⚠️ **Traceability notes:**
> - Masses are **as-recorded at assembly, rounded to 0.1 mg** (vs 0.01 mg in the punch table) → per-cell active
>   mass carries ~±0.1 mg extra rounding uncertainty (~±0.8% on hard-carbon mass).
> - **CC20 (19.6 mg) and CC21 (20.0 mg) sit at/below the 17-kept punch range** (min 20.19 mg); CC20 is near the
>   three culled low disks (19.42–19.76). Likely an assembly-day re-weigh or use of a low-mass disk — flagged so
>   the disk→cell mapping stays honest. Not a problem for cycling, only for cross-referencing the punch table.
> - **Na half-cell / Na in excess** → these masses set only the working-electrode normalisation, not balancing.

**Cycling:** started 2026-07-14, **in progress**. Capacity / rate results — _pending_.

### 2 more cells assembled 2026-07-16 (CC35, CC36)

Same formula as above (f = 0.8873, area 1.2668 cm², tare 5.5255 mg).

| Cell | Disk mass (mg) | Coating (mg) | **Hard-carbon mass (mg)** | Coating load (mg/cm²) | Hard-C load (mg/cm²) | Status |
|---|---|---|---|---|---|---|
| CC35 | 19.6 | 14.07 | **12.488** | 11.111 | 9.858 | cycling |
| CC36 | 18.9 | 13.37 | **11.867** | 10.558 | 9.368 | cycling |

CC35 matches CC20's disk mass exactly (19.6 mg → identical derived values); coincidence, not a duplicate
record — separate cell, separate assembly date. CC36 sits below the 17-kept punch range (min 20.19 mg), same
plausible-but-flagged caveat as CC20/CC21. **Cycling:** started 2026-07-16, **in progress**.
