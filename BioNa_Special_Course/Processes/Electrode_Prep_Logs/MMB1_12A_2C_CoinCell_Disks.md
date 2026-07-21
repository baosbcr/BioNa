# Coin-Cell Disk Log — MMB1_12A_2C

**Sample:** MMB1_12A_2C (1200 °C, 120 °C/h = 2 °C/min ramp) — calendered electrode (roll gaps 0.23 mm sheet 1 / 0.28 mm sheet 2; see `MMB1_12A_2C_Electrode_Prep.md`)
**Date:** 2026-07-15
**Purpose:** working electrodes for **sodium half-cells** (Na counter, Na always in excess)
**Disks punched:** **38 (19 sheet 1 + 19 sheet 2), all kept** · **Cutting die:** 12.7 mm Ø (½″) → **area 1.2668 cm²**
**Foil tare (carbon-coated foil, conductive-C layer, no slurry):** 0.0055255 g (5.53 mg) *(**MEASURED** 2026-07-21: mean of 11 blanks cut with this same 12.7 mm die, SD 0.057 mg — see `Processes/Foil_Tare_Measurement.md`)*
**Compute script:** `Processes/Electrode_Prep_Logs/disk_loading.py`

> **Disks are unlabeled and indistinguishable** — masses known as a *set* (same as 6A/8A/10A/1C). No outlier cull
> applied (contrast 1C): all 19+19 disks retained. See "Uncertainty".
>
> **Two sheets tracked separately.** Sheet 1 (gap 0.23 mm) and sheet 2 (gap 0.28 mm) were punched and weighed as
> independent populations — sheet 2 read thicker on the gauge but carries slightly *less* mass (see comparison).

---

## Slurry solids composition (from 12A_2C prep log)

| Component | Mass (g) | wt% of dried solids |
|---|---|---|
| Hard carbon (MMB1_12A_2C) | 3.64361 | **88.74** |
| C45 | 0.16707 | 4.07 |
| SBR | 0.195 *(est.)* | 4.75 |
| CMC | 0.10019 | 2.44 |
| **Total solids** | 4.10587 | 100 |

**Active (hard-carbon) fraction f = 0.8874** — assumes the dried coating retains the batch ratio.
Coating mass = disk mass − foil tare. Hard-carbon mass = coating × f.

> ⚠️ **SBR mass not weighed** (200 µL calibrated pipette; deemed unreliable due to evaporation), est. ≈ 0.195 g.
> The **taped-blade coating (+35 µm) is irrelevant here** — it affects *thickness* comparison, not *mass* on a disk.

---

## Per-disk results — Sheet 1 (gap 0.23 mm, n = 19)

Coating load = coating mass / 1.2668 cm². `± u` = per-disk measurement uncertainty (device-limited, **die-dominated**).

| # | Disk wt (mg) | Coating (mg) | Coating load (mg/cm²) | Hard-C load (mg/cm²) |
|---|---|---|---|---|
| 1 | 22.07 | 16.54 | 13.060 ± 0.113 | 11.590 |
| 2 | 25.08 | 19.55 | 15.437 ± 0.130 | 13.698 |
| 3 | 25.61 | 20.08 | 15.855 ± 0.133 | 14.070 |
| 4 | 22.23 | 16.70 | 13.187 ± 0.114 | 11.702 |
| 5 | 21.66 | 16.13 | 12.737 ± 0.110 | 11.303 |
| 6 | 21.93 | 16.40 | 12.950 ± 0.112 | 11.492 |
| 7 | 23.75 | 18.22 | 14.387 ± 0.122 | 12.767 |
| 8 | 25.43 | 19.90 | 15.713 ± 0.132 | 13.944 |
| 9 | 21.64 | 16.11 | 12.721 ± 0.110 | 11.289 |
| 10 | 23.26 | 17.73 | 14.000 ± 0.120 | 12.423 |
| 11 | 23.30 | 17.77 | 14.031 ± 0.120 | 12.451 |
| 12 | 24.00 | 18.47 | 14.584 ± 0.124 | 12.942 |
| 13 | 23.40 | 17.87 | 14.110 ± 0.120 | 12.521 |
| 14 | 23.58 | 18.05 | 14.252 ± 0.121 | 12.648 |
| 15 | 25.01 | 19.48 | 15.381 ± 0.130 | 13.649 |
| 16 | 24.94 | 19.41 | 15.326 ± 0.129 | 13.600 |
| 17 | 23.47 | 17.94 | 14.166 ± 0.121 | 12.571 |
| 18 | 22.40 | 16.87 | 13.321 ± 0.115 | 11.821 |
| 19 | 21.45 | 15.92 | 12.571 ± 0.109 | 11.155 |

### Population summary — Sheet 1 (n = 19)

| Quantity | Mean | SD (spread) | CV | SEM | Min | Max |
|---|---|---|---|---|---|---|
| Coating mass (mg) | 17.854 | 1.365 | 7.6% | 0.313 | 15.924 | 20.084 |
| Coating load (mg/cm²) | **14.094** | 1.078 | 7.6% | 0.247 | 12.571 | 15.855 |
| Hard-carbon load (mg/cm²) | **12.507** | 0.957 | 7.6% | 0.219 | 11.155 | 14.070 |

---

## Per-disk results — Sheet 2 (gap 0.28 mm, n = 19)

| # | Disk wt (mg) | Coating (mg) | Coating load (mg/cm²) | Hard-C load (mg/cm²) |
|---|---|---|---|---|
| 1 | 25.13 | 19.60 | 15.476 ± 0.130 | 13.733 |
| 2 | 22.43 | 16.90 | 13.345 ± 0.115 | 11.842 |
| 3 | 22.67 | 17.14 | 13.534 ± 0.116 | 12.010 |
| 4 | 22.44 | 16.91 | 13.352 ± 0.115 | 11.849 |
| 5 | 25.75 | 20.22 | 15.965 ± 0.134 | 14.168 |
| 6 | 21.87 | 16.34 | 12.903 ± 0.112 | 11.450 |
| 7 | 23.51 | 17.98 | 14.197 ± 0.121 | 12.599 |
| 8 | 21.49 | 15.96 | 12.603 ± 0.109 | 11.183 |
| 9 | 22.95 | 17.42 | 13.755 ± 0.118 | 12.206 |
| 10 | 22.09 | 16.56 | 13.076 ± 0.113 | 11.604 |
| 11 | 23.35 | 17.82 | 14.071 ± 0.120 | 12.486 |
| 12 | 22.53 | 17.00 | 13.424 ± 0.115 | 11.912 |
| 13 | 21.35 | 15.82 | 12.492 ± 0.109 | 11.085 |
| 14 | 23.90 | 18.37 | 14.505 ± 0.123 | 12.872 |
| 15 | 21.83 | 16.30 | 12.871 ± 0.111 | 11.422 |
| 16 | 23.64 | 18.11 | 14.300 ± 0.122 | 12.690 |
| 17 | 20.75 | 15.22 | 12.018 ± 0.105 | 10.665 |
| 18 | 23.83 | 18.30 | 14.450 ± 0.123 | 12.823 |
| 19 | 21.61 | 16.08 | 12.697 ± 0.110 | 11.268 |

### Population summary — Sheet 2 (n = 19)

| Quantity | Mean | SD (spread) | CV | SEM | Min | Max |
|---|---|---|---|---|---|---|
| Coating mass (mg) | 17.270 | 1.292 | 7.5% | 0.296 | 15.224 | 20.224 |
| Coating load (mg/cm²) | **13.633** | 1.020 | 7.5% | 0.234 | 12.018 | 15.965 |
| Hard-carbon load (mg/cm²) | **12.098** | 0.905 | 7.5% | 0.208 | 10.665 | 14.168 |

> **Sheet 2 is lighter than sheet 1** (12.10 vs 12.51 mg/cm² hard carbon) despite reading *thicker* on the
> pre-calender gauge (median 0.314 vs 0.255 mm). The gauge medians were inflated by large-particle spikes; the
> **disk mass — which integrates real coating — is the loading metric to trust**. The two sheets are within ~3%.

---

## Uncertainty

**1. Measurement uncertainty (per disk): ≈ ±0.12 mg/cm² (±0.85%), die-dominated.**
u(load)/load = √[(u(coat)/coat)² + (2·u(d)/d)²], u(coat) = 0.059 mg, die Ø 12.7 mm ± 0.05 mm. Coating (~17.2–17.8 mg)
≫ tare-uncertainty term, so the **assumed ±0.05 mm die tolerance dominates** (0.79%) — same regime as 6A/10A/1C.

**2. Disk-to-disk spread (physical): SD ≈ 0.9–1.1 mg/cm² (≈7.5–7.7%).**
~9× the measurement uncertainty → **real coating non-uniformity**, consistent with the as-coated grids (sheet 1
CV 22%, sheet 2 CV 36%). Both sheets calendered with **near-full spring-back**, so the coating mass distribution
was largely preserved rather than homogenised.

### Consequence for the experiment

- **Heavier than 1C** — 2C coating loads ~13.6–14.1 mg/cm² (hard carbon 12.1–12.5), above 1C's 10.74.
- Unlabeled disks → a cell's active mass known only as the population value; propagates linearly into per-cell
  gravimetric capacity. **Na half-cell / Na in excess** → affects only working-electrode mass normalisation.

### Recommendation

- **Label disks at punching** to unlock per-cell mAh/g.
- ~~Punch and weigh a fresh foil blank~~ — **DONE 2026-07-21** (11 blanks, 5.5255 mg; see `Processes/Foil_Tare_Measurement.md`). Next: weigh them **individually** to firm up the 0.057 mg SD (currently 1 dof).

---

## Cross-sample loading comparison (running)

| Sample | Temp / ramp | n | Coating load (mg/cm²) | Hard-C load (mg/cm²) | CV | Meas. u | Note |
|---|---|---|---|---|---|---|---|
| 6A  | 600 °C  | 20 | 8.46  | 7.51  | 3.6% | ±0.96% (die)  | baseline |
| 8A  | 800 °C  | 21 | 0.459 | 0.412 | 4.5% | ±10.1% (tare)  | anomalously thin (~5 µm) |
| 10A | 1000 °C | 20 | 11.56 | 10.27 | 2.2% | ±0.88% (die)  | most uniform (top band cut) |
| 12A_1C | 1200 °C, 1 °C/min | 17 | 12.10 | 10.73 | 3.2% | ±0.88% (die) | 3 outliers culled |
| **12A_2C sheet 1** | 1200 °C, 2 °C/min | 19 | **14.09** | **12.51** | 7.6% | ±0.85% (die) | gap 0.23 mm |
| **12A_2C sheet 2** | 1200 °C, 2 °C/min | 19 | **13.63** | **12.10** | 7.5% | ±0.86% (die) | gap 0.28 mm; lighter despite thicker gauge |
| 12A_3C standard | 1200 °C, 3 °C/min | 13 | 19.05 | 16.90 | 4.0% | ±0.82% (die) | heaviest biochar; std set |
| 12A_3C thick | 1200 °C, 3 °C/min | 6 | 22.95 | 20.36 | 7.2% | ±0.81% (die) | high-loading set, saved separately |
| Kuranode | commercial HC | 18 | 7.08 | 6.25 | 7.2% | ±1.02% (die) | off-standard mix; delaminated on calender |

> The 1200 °C series (1C→2C→3C) climbs steadily in loading (10.74 → 12.1–12.5 → 16.9 mg/cm² hard carbon), driven
> by coating thickness — **not** an intrinsic material change. Normalise capacity per gram, not per disk.

---

## Cell Assembly & Cycling

> ⚠️ **Cycler C-rate basis differs from measured mass.** The cycling program's applied current (C-rate) was
> set from a flat **5.55 mg tare + 91% active-mass assumption**, not the measured values used below
> (**5.5255 mg** tare, measured 2026-07-21, and the per-sample f). The tare side is now nearly exact
> (+0.44%); the **active fraction is the dominant remaining difference**. See `Biona_Academy/Open_Questions.md` for the full note — recompute specific capacity from the
> measured mass, don't back it out from the nominal C-rate.

**3 sodium half-cells assembled 2026-07-15** (CC22, CC23, CC24) from 12A_2C disks — **the first cells built
from this sample**, before the labelled-disk practice below. Disk masses **received 2026-07-21** (previously
pending from supervisor). Active mass = (disk − **5.5255 mg** tare) × f, f = 0.8874. Area 1.2668 cm².

| Cell | Disk mass (mg) | Coating (mg) | **Hard-carbon mass (mg)** | Coating load (mg/cm²) | Hard-C load (mg/cm²) | Status |
|---|---|---|---|---|---|---|
| CC22 | 20.8 | 15.27 | **13.555** | 12.058 | 10.700 | cycling |
| CC23 | 24.1 | 18.57 | **16.483** | 14.663 | 13.012 | cycling |
| CC24 | 20.2 | 14.67 | **13.022** | 11.584 | 10.280 | cycling |

> ⚠️ **All three sit at or below the punch-population range** (sheet 1+2 disk masses 20.75–25.75 mg): CC24 (20.2)
> and CC22 (20.8) are at/below the observed minimum, and all three fall below both sheet means (22.9 / 22.7 mg).
> Two readings apart it could be spread; three-for-three low is a pattern. Most likely causes: these were the
> **first cells built**, punched/selected before the process settled, or the supervisor's balance/tare basis
> differs from the punch-day weighing. **Do not treat these as drawn from the same population as CC37/CC38**
> without checking. Values recorded to 0.1 mg, vs 0.01 mg for the punch set.

**Cycling:** started 2026-07-15, **in progress**.

### 2 more cells assembled 2026-07-16 (CC37, CC38)

Electrode (total disk) mass recorded at assembly, rounded to 0.1 mg. Active mass = (disk − 5.5255 mg tare) × f,
f = 0.8874. Area 1.2668 cm².

| Cell | Disk mass (mg) | Coating (mg) | **Hard-carbon mass (mg)** | Coating load (mg/cm²) | Hard-C load (mg/cm²) | Status |
|---|---|---|---|---|---|---|
| CC37 | 22.5 | 16.97 | **15.063** | 13.400 | 11.891 | cycling |
| CC38 | 23.4 | 17.87 | **15.862** | 14.110 | 12.521 | cycling |

Both fall within the sheet 1/sheet 2 punch ranges (20.75–25.75 mg disk mass) — no anomaly flagged.

> **Na half-cell / Na in excess** → these masses set only the working-electrode normalisation, not balancing.

**Cycling:** started 2026-07-16, **in progress**. Capacity / rate results — _pending_ for all 5 cells.
