# Coin-Cell Disk Log — MMB1_12A_2C

**Sample:** MMB1_12A_2C (1200 °C, 120 °C/h = 2 °C/min ramp) — calendered electrode (roll gaps 0.23 mm sheet 1 / 0.28 mm sheet 2; see `MMB1_12A_2C_Electrode_Prep.md`)
**Date:** 2026-07-15
**Purpose:** working electrodes for **sodium half-cells** (Na counter, Na always in excess)
**Disks punched:** **38 (19 sheet 1 + 19 sheet 2), all kept** · **Cutting die:** 12.7 mm Ø (½″) → **area 1.2668 cm²**
**Foil tare (carbon-coated foil, conductive-C layer, no slurry):** 0.00555 g (5.55 mg) *(assumed same as 6A/8A/1C — confirm with a fresh blank)*
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
| 1 | 22.07 | 16.52 | 13.041 ± 0.106 | 11.573 |
| 2 | 25.08 | 19.53 | 15.417 ± 0.124 | 13.681 |
| 3 | 25.61 | 20.06 | 15.836 ± 0.127 | 14.052 |
| 4 | 22.23 | 16.68 | 13.167 ± 0.107 | 11.685 |
| 5 | 21.66 | 16.11 | 12.717 ± 0.104 | 11.285 |
| 6 | 21.93 | 16.38 | 12.931 ± 0.105 | 11.475 |
| 7 | 23.75 | 18.20 | 14.367 ± 0.116 | 12.750 |
| 8 | 25.43 | 19.88 | 15.693 ± 0.126 | 13.926 |
| 9 | 21.64 | 16.09 | 12.702 ± 0.103 | 11.271 |
| 10 | 23.26 | 17.71 | 13.980 ± 0.113 | 12.406 |
| 11 | 23.30 | 17.75 | 14.012 ± 0.113 | 12.434 |
| 12 | 24.00 | 18.45 | 14.565 ± 0.118 | 12.925 |
| 13 | 23.40 | 17.85 | 14.091 ± 0.114 | 12.504 |
| 14 | 23.58 | 18.03 | 14.233 ± 0.115 | 12.630 |
| 15 | 25.01 | 19.46 | 15.362 ± 0.124 | 13.632 |
| 16 | 24.94 | 19.39 | 15.307 ± 0.123 | 13.583 |
| 17 | 23.47 | 17.92 | 14.146 ± 0.114 | 12.553 |
| 18 | 22.40 | 16.85 | 13.302 ± 0.108 | 11.804 |
| 19 | 21.45 | 15.90 | 12.552 ± 0.102 | 11.138 |

### Population summary — Sheet 1 (n = 19)

| Quantity | Mean | SD (spread) | CV | SEM | Min | Max |
|---|---|---|---|---|---|---|
| Coating mass (mg) | 17.829 | 1.365 | 7.7% | 0.313 | 15.900 | 20.060 |
| Coating load (mg/cm²) | **14.075** | 1.078 | 7.7% | 0.247 | 12.552 | 15.836 |
| Hard-carbon load (mg/cm²) | **12.490** | 0.957 | 7.7% | 0.219 | 11.138 | 14.052 |

---

## Per-disk results — Sheet 2 (gap 0.28 mm, n = 19)

| # | Disk wt (mg) | Coating (mg) | Coating load (mg/cm²) | Hard-C load (mg/cm²) |
|---|---|---|---|---|
| 1 | 25.13 | 19.58 | 15.457 ± 0.125 | 13.716 |
| 2 | 22.43 | 16.88 | 13.325 ± 0.108 | 11.825 |
| 3 | 22.67 | 17.12 | 13.515 ± 0.110 | 11.993 |
| 4 | 22.44 | 16.89 | 13.333 ± 0.108 | 11.832 |
| 5 | 25.75 | 20.20 | 15.946 ± 0.128 | 14.151 |
| 6 | 21.87 | 16.32 | 12.883 ± 0.105 | 11.433 |
| 7 | 23.51 | 17.96 | 14.178 ± 0.115 | 12.581 |
| 8 | 21.49 | 15.94 | 12.583 ± 0.103 | 11.166 |
| 9 | 22.95 | 17.40 | 13.736 ± 0.111 | 12.189 |
| 10 | 22.09 | 16.54 | 13.057 ± 0.106 | 11.587 |
| 11 | 23.35 | 17.80 | 14.051 ± 0.114 | 12.469 |
| 12 | 22.53 | 16.98 | 13.404 ± 0.109 | 11.895 |
| 13 | 21.35 | 15.80 | 12.473 ± 0.102 | 11.068 |
| 14 | 23.90 | 18.35 | 14.486 ± 0.117 | 12.855 |
| 15 | 21.83 | 16.28 | 12.852 ± 0.105 | 11.405 |
| 16 | 23.64 | 18.09 | 14.280 ± 0.116 | 12.672 |
| 17 | 20.75 | 15.20 | 11.999 ± 0.098 | 10.648 |
| 18 | 23.83 | 18.28 | 14.430 ± 0.117 | 12.806 |
| 19 | 21.61 | 16.06 | 12.678 ± 0.103 | 11.250 |

### Population summary — Sheet 2 (n = 19)

| Quantity | Mean | SD (spread) | CV | SEM | Min | Max |
|---|---|---|---|---|---|---|
| Coating mass (mg) | 17.246 | 1.292 | 7.5% | 0.296 | 15.200 | 20.200 |
| Coating load (mg/cm²) | **13.614** | 1.020 | 7.5% | 0.234 | 11.999 | 15.946 |
| Hard-carbon load (mg/cm²) | **12.081** | 0.905 | 7.5% | 0.208 | 10.648 | 14.151 |

> **Sheet 2 is lighter than sheet 1** (12.08 vs 12.49 mg/cm² hard carbon) despite reading *thicker* on the
> pre-calender gauge (median 0.314 vs 0.255 mm). The gauge medians were inflated by large-particle spikes; the
> **disk mass — which integrates real coating — is the loading metric to trust**. The two sheets are within ~3%.

---

## Uncertainty

**1. Measurement uncertainty (per disk): ≈ ±0.11 mg/cm² (±0.81%), die-dominated.**
u(load)/load = √[(u(coat)/coat)² + (2·u(d)/d)²], u(coat) = 0.034 mg, die Ø 12.7 mm ± 0.05 mm. Coating (~17–18 mg)
≫ tare-uncertainty term, so the **assumed ±0.05 mm die tolerance dominates** (0.79%) — same regime as 6A/10A/1C.

**2. Disk-to-disk spread (physical): SD ≈ 0.9–1.1 mg/cm² (≈7.5–7.7%).**
~9× the measurement uncertainty → **real coating non-uniformity**, consistent with the as-coated grids (sheet 1
CV 22%, sheet 2 CV 36%). Both sheets calendered with **near-full spring-back**, so the coating mass distribution
was largely preserved rather than homogenised.

### Consequence for the experiment

- **Heavier than 1C** — 2C coating loads ~13.6–14.1 mg/cm² (hard carbon 12.1–12.5), above 1C's 10.72.
- Unlabeled disks → a cell's active mass known only as the population value; propagates linearly into per-cell
  gravimetric capacity. **Na half-cell / Na in excess** → affects only working-electrode mass normalisation.

### Recommendation

- **Label disks at punching** to unlock per-cell mAh/g.
- Punch and weigh a **fresh foil blank** to replace the adopted 5.55 mg tare.

---

## Cross-sample loading comparison (running)

| Sample | Temp / ramp | n | Coating load (mg/cm²) | Hard-C load (mg/cm²) | CV | Meas. u | Note |
|---|---|---|---|---|---|---|---|
| 6A  | 600 °C  | 20 | 8.44  | 7.50  | 3.6% | ±0.85% (die)  | baseline |
| 8A  | 800 °C  | 21 | 0.439 | 0.394 | 4.7% | ±6.1% (tare)  | anomalously thin (~5 µm) |
| 10A | 1000 °C | 20 | 11.54 | 10.25 | 2.2% | ±0.82% (die)  | most uniform (top band cut) |
| 12A_1C | 1200 °C, 1 °C/min | 17 | 12.08 | 10.72 | 3.2% | ±0.82% (die) | 3 outliers culled |
| **12A_2C sheet 1** | 1200 °C, 2 °C/min | 19 | **14.07** | **12.49** | 7.7% | ±0.81% (die) | gap 0.23 mm |
| **12A_2C sheet 2** | 1200 °C, 2 °C/min | 19 | **13.61** | **12.08** | 7.5% | ±0.81% (die) | gap 0.28 mm; lighter despite thicker gauge |
| 12A_3C standard | 1200 °C, 3 °C/min | 13 | 19.03 | 16.89 | 4.0% | ±0.80% (die) | heaviest biochar; std set |
| 12A_3C thick | 1200 °C, 3 °C/min | 6 | 22.93 | 20.34 | 7.2% | ±0.80% (die) | high-loading set, saved separately |
| Kuranode | commercial HC | 18 | 7.06 | 6.23 | 7.2% | ±0.87% (die) | off-standard mix; delaminated on calender |

> The 1200 °C series (1C→2C→3C) climbs steadily in loading (10.72 → 12.1–12.5 → 16.9 mg/cm² hard carbon), driven
> by coating thickness — **not** an intrinsic material change. Normalise capacity per gram, not per disk.

---

## Cell Assembly & Cycling

> ⚠️ **Cycler C-rate basis differs from measured mass.** The cycling program's applied current (C-rate) was
> set from a flat **91% active-mass assumption**, not the measured per-sample f used below. (The 5.55 mg
> foil tare now matches on both sides — adopted repo-wide 2026-07-21 — so the **active fraction is the only
> remaining difference**.) See `Biona_Academy/Open_Questions.md` for the full note — recompute specific capacity from the
> measured mass, don't back it out from the nominal C-rate.

**3 sodium half-cells assembled 2026-07-15** (CC22, CC23, CC24) from 12A_2C disks — **the first cells built
from this sample**, before the labelled-disk practice below. Disk masses **received 2026-07-21** (previously
pending from supervisor). Active mass = (disk − **5.55 mg** tare) × f, f = 0.8874. Area 1.2668 cm².

| Cell | Disk mass (mg) | Coating (mg) | **Hard-carbon mass (mg)** | Coating load (mg/cm²) | Hard-C load (mg/cm²) | Status |
|---|---|---|---|---|---|---|
| CC22 | 20.8 | 15.25 | **13.533** | 12.039 | 10.683 | cycling |
| CC23 | 24.1 | 18.55 | **16.461** | 14.644 | 12.995 | cycling |
| CC24 | 20.2 | 14.65 | **13.000** | 11.565 | 10.263 | cycling |

> ⚠️ **All three sit at or below the punch-population range** (sheet 1+2 disk masses 20.75–25.75 mg): CC24 (20.2)
> and CC22 (20.8) are at/below the observed minimum, and all three fall below both sheet means (22.9 / 22.7 mg).
> Two readings apart it could be spread; three-for-three low is a pattern. Most likely causes: these were the
> **first cells built**, punched/selected before the process settled, or the supervisor's balance/tare basis
> differs from the punch-day weighing. **Do not treat these as drawn from the same population as CC37/CC38**
> without checking. Values recorded to 0.1 mg, vs 0.01 mg for the punch set.

**Cycling:** started 2026-07-15, **in progress**.

### 2 more cells assembled 2026-07-16 (CC37, CC38)

Electrode (total disk) mass recorded at assembly, rounded to 0.1 mg. Active mass = (disk − 5.55 mg tare) × f,
f = 0.8874. Area 1.2668 cm².

| Cell | Disk mass (mg) | Coating (mg) | **Hard-carbon mass (mg)** | Coating load (mg/cm²) | Hard-C load (mg/cm²) | Status |
|---|---|---|---|---|---|---|
| CC37 | 22.5 | 16.95 | **15.041** | 13.381 | 11.874 | cycling |
| CC38 | 23.4 | 17.85 | **15.840** | 14.091 | 12.504 | cycling |

Both fall within the sheet 1/sheet 2 punch ranges (20.75–25.75 mg disk mass) — no anomaly flagged.

> **Na half-cell / Na in excess** → these masses set only the working-electrode normalisation, not balancing.

**Cycling:** started 2026-07-16, **in progress**. Capacity / rate results — _pending_ for all 5 cells.
