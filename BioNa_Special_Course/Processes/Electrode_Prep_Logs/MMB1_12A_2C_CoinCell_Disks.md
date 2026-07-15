# Coin-Cell Disk Log — MMB1_12A_2C

**Sample:** MMB1_12A_2C (1200 °C, 120 °C/h = 2 °C/min ramp) — calendered electrode (roll gaps 0.23 mm sheet 1 / 0.28 mm sheet 2; see `MMB1_12A_2C_Electrode_Prep.md`)
**Date:** 2026-07-15
**Purpose:** working electrodes for **sodium half-cells** (Na counter, Na always in excess)
**Disks punched:** **38 (19 sheet 1 + 19 sheet 2), all kept** · **Cutting die:** 12.7 mm Ø (½″) → **area 1.2668 cm²**
**Foil tare (carbon-coated foil, conductive-C layer, no slurry):** 0.0055 g (5.50 mg) *(assumed same as 6A/8A/1C — confirm with a fresh blank)*
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
| 1 | 22.07 | 16.57 | 13.080 ± 0.106 | 11.607 |
| 2 | 25.08 | 19.58 | 15.456 ± 0.125 | 13.716 |
| 3 | 25.61 | 20.11 | 15.875 ± 0.128 | 14.087 |
| 4 | 22.23 | 16.73 | 13.207 ± 0.107 | 11.719 |
| 5 | 21.66 | 16.16 | 12.757 ± 0.104 | 11.320 |
| 6 | 21.93 | 16.43 | 12.970 ± 0.106 | 11.509 |
| 7 | 23.75 | 18.25 | 14.406 ± 0.117 | 12.784 |
| 8 | 25.43 | 19.93 | 15.733 ± 0.127 | 13.961 |
| 9 | 21.64 | 16.14 | 12.741 ± 0.104 | 11.306 |
| 10 | 23.26 | 17.76 | 14.020 ± 0.114 | 12.441 |
| 11 | 23.30 | 17.80 | 14.051 ± 0.114 | 12.469 |
| 12 | 24.00 | 18.50 | 14.604 ± 0.118 | 12.959 |
| 13 | 23.40 | 17.90 | 14.130 ± 0.114 | 12.539 |
| 14 | 23.58 | 18.08 | 14.272 ± 0.116 | 12.665 |
| 15 | 25.01 | 19.51 | 15.401 ± 0.124 | 13.667 |
| 16 | 24.94 | 19.44 | 15.346 ± 0.124 | 13.618 |
| 17 | 23.47 | 17.97 | 14.185 ± 0.115 | 12.588 |
| 18 | 22.40 | 16.90 | 13.341 ± 0.108 | 11.839 |
| 19 | 21.45 | 15.95 | 12.591 ± 0.103 | 11.173 |

### Population summary — Sheet 1 (n = 19)

| Quantity | Mean | SD (spread) | CV | SEM | Min | Max |
|---|---|---|---|---|---|---|
| Coating mass (mg) | 17.879 | 1.365 | 7.6% | 0.313 | 15.950 | 20.110 |
| Coating load (mg/cm²) | **14.114** | 1.078 | 7.6% | 0.247 | 12.591 | 15.875 |
| Hard-carbon load (mg/cm²) | **12.525** | 0.956 | 7.6% | 0.219 | 11.173 | 14.087 |

---

## Per-disk results — Sheet 2 (gap 0.28 mm, n = 19)

| # | Disk wt (mg) | Coating (mg) | Coating load (mg/cm²) | Hard-C load (mg/cm²) |
|---|---|---|---|---|
| 1 | 25.13 | 19.63 | 15.496 ± 0.125 | 13.751 |
| 2 | 22.43 | 16.93 | 13.364 ± 0.109 | 11.860 |
| 3 | 22.67 | 17.17 | 13.554 ± 0.110 | 12.028 |
| 4 | 22.44 | 16.94 | 13.372 ± 0.109 | 11.867 |
| 5 | 25.75 | 20.25 | 15.985 ± 0.129 | 14.185 |
| 6 | 21.87 | 16.37 | 12.922 ± 0.105 | 11.467 |
| 7 | 23.51 | 18.01 | 14.217 ± 0.115 | 12.616 |
| 8 | 21.49 | 15.99 | 12.622 ± 0.103 | 11.201 |
| 9 | 22.95 | 17.45 | 13.775 ± 0.112 | 12.224 |
| 10 | 22.09 | 16.59 | 13.096 ± 0.107 | 11.621 |
| 11 | 23.35 | 17.85 | 14.091 ± 0.114 | 12.504 |
| 12 | 22.53 | 17.03 | 13.443 ± 0.109 | 11.930 |
| 13 | 21.35 | 15.85 | 12.512 ± 0.102 | 11.103 |
| 14 | 23.90 | 18.40 | 14.525 ± 0.117 | 12.889 |
| 15 | 21.83 | 16.33 | 12.891 ± 0.105 | 11.439 |
| 16 | 23.64 | 18.14 | 14.320 ± 0.116 | 12.707 |
| 17 | 20.75 | 15.25 | 12.038 ± 0.099 | 10.683 |
| 18 | 23.83 | 18.33 | 14.470 ± 0.117 | 12.840 |
| 19 | 21.61 | 16.11 | 12.717 ± 0.104 | 11.285 |

### Population summary — Sheet 2 (n = 19)

| Quantity | Mean | SD (spread) | CV | SEM | Min | Max |
|---|---|---|---|---|---|---|
| Coating mass (mg) | 17.296 | 1.292 | 7.5% | 0.296 | 15.250 | 20.250 |
| Coating load (mg/cm²) | **13.653** | 1.020 | 7.5% | 0.234 | 12.038 | 15.985 |
| Hard-carbon load (mg/cm²) | **12.116** | 0.905 | 7.5% | 0.208 | 10.683 | 14.185 |

> **Sheet 2 is lighter than sheet 1** (12.12 vs 12.53 mg/cm² hard carbon) despite reading *thicker* on the
> pre-calender gauge (median 0.314 vs 0.255 mm). The gauge medians were inflated by large-particle spikes; the
> **disk mass — which integrates real coating — is the loading metric to trust**. The two sheets are within ~3%.

---

## Uncertainty

**1. Measurement uncertainty (per disk): ≈ ±0.11 mg/cm² (±0.81%), die-dominated.**
u(load)/load = √[(u(coat)/coat)² + (2·u(d)/d)²], u(coat) = 0.034 mg, die Ø 12.7 mm ± 0.05 mm. Coating (~17–18 mg)
≫ tare-uncertainty term, so the **assumed ±0.05 mm die tolerance dominates** (0.79%) — same regime as 6A/10A/1C.

**2. Disk-to-disk spread (physical): SD ≈ 0.9–1.0 mg/cm² (≈7.5%).**
~9× the measurement uncertainty → **real coating non-uniformity**, consistent with the as-coated grids (sheet 1
CV 22%, sheet 2 CV 36%). Both sheets calendered with **near-full spring-back**, so the coating mass distribution
was largely preserved rather than homogenised.

### Consequence for the experiment

- **Heavier than 1C** — 2C coating loads ~13.7–14.1 mg/cm² (hard carbon 12.1–12.5), above 1C's 10.75.
- Unlabeled disks → a cell's active mass known only as the population value; propagates linearly into per-cell
  gravimetric capacity. **Na half-cell / Na in excess** → affects only working-electrode mass normalisation.

### Recommendation

- **Label disks at punching** to unlock per-cell mAh/g.
- Punch and weigh a **fresh foil blank** to replace the assumed 5.50 mg tare.

---

## Cross-sample loading comparison (running)

| Sample | Temp / ramp | n | Coating load (mg/cm²) | Hard-C load (mg/cm²) | CV | Meas. u | Note |
|---|---|---|---|---|---|---|---|
| 6A  | 600 °C  | 20 | 8.48  | 7.53  | 3.6% | ±0.85% (die)  | baseline |
| 8A  | 800 °C  | 21 | 0.479 | 0.430 | 4.3% | ±5.6% (tare)  | anomalously thin (~5 µm) |
| 10A | 1000 °C | 20 | 11.58 | 10.28 | 2.1% | ±0.82% (die)  | most uniform (top band cut) |
| 12A_1C | 1200 °C, 1 °C/min | 17 | 12.12 | 10.75 | 3.2% | ±0.82% (die) | 3 outliers culled |
| **12A_2C sheet 1** | 1200 °C, 2 °C/min | 19 | **14.11** | **12.53** | 7.6% | ±0.81% (die) | gap 0.23 mm |
| **12A_2C sheet 2** | 1200 °C, 2 °C/min | 19 | **13.65** | **12.12** | 7.5% | ±0.81% (die) | gap 0.28 mm; lighter despite thicker gauge |
| 12A_3C standard | 1200 °C, 3 °C/min | 13 | 19.07 | 16.92 | 4.0% | ±0.80% (die) | heaviest biochar; std set |
| 12A_3C thick | 1200 °C, 3 °C/min | 6 | 22.97 | 20.38 | 7.2% | ±0.80% (die) | high-loading set, saved separately |
| Kuranode | commercial HC | 18 | 7.10 | 6.26 | 7.1% | ±0.88% (die) | off-standard mix; delaminated on calender |

> The 1200 °C series (1C→2C→3C) climbs steadily in loading (10.75 → 12.1–12.5 → 16.9 mg/cm² hard carbon), driven
> by coating thickness — **not** an intrinsic material change. Normalise capacity per gram, not per disk.
