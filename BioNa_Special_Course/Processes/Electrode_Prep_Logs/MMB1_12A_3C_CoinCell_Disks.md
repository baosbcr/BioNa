# Coin-Cell Disk Log — MMB1_12A_3C

**Sample:** MMB1_12A_3C (1200 °C, 180 °C/h = 3 °C/min ramp — standard ramp; = base MMB1_12A) — calendered electrode (roll gap 0.43 mm; see `MMB1_12A_3C_Electrode_Prep.md`)
**Date:** 2026-07-15
**Purpose:** working electrodes for **sodium half-cells** (Na counter, Na always in excess)
**Disks punched:** **19 → split into 13 standard + 6 thick** · **Cutting die:** 12.7 mm Ø (½″) → **area 1.2668 cm²**
**Foil tare (carbon-coated foil, conductive-C layer, no slurry):** 0.0055255 g (5.53 mg) *(**MEASURED** 2026-07-21: mean of 11 blanks cut with this same 12.7 mm die, SD 0.057 mg — see `Processes/Foil_Tare_Measurement.md`)*
**Compute script:** `Processes/Electrode_Prep_Logs/disk_loading.py`

> **Disks are unlabeled and indistinguishable within each set** — masses known per-set (same as 6A/8A/10A/1C).
>
> **Deliberate two-population split.** 3C is the thickest coating in the series, with a visible wave and heavy
> patches. Disks were sorted at punching by **qualitative appearance + scale weight** into a **standard set**
> (13, uniform) and a **thick set** (6, high-mass, stored in a separate container). Same philosophy as the 10A
> pre-calender cut — keep the cell-building population uniform, isolate the heavies for optional high-loading use.

---

## Slurry solids composition (from 12A_3C prep log)

| Component | Mass (g) | wt% of dried solids |
|---|---|---|
| Hard carbon (MMB1_12A_3C) | 3.64020 | **88.73** |
| C45 | 0.16745 | 4.08 |
| SBR | 0.195 *(est.)* | 4.75 |
| CMC | 0.10003 | 2.44 |
| **Total solids** | 4.10268 | 100 |

**Active (hard-carbon) fraction f = 0.8873** — assumes the dried coating retains the batch ratio.
Coating mass = disk mass − foil tare. Hard-carbon mass = coating × f.

> ⚠️ **SBR mass not weighed** (200 µL calibrated pipette; evaporation), est. ≈ 0.195 g. Taped-blade coating
> (+35 µm) is irrelevant to disk *mass*.

---

## Per-disk results — Standard set (n = 13)

Coating load = coating mass / 1.2668 cm². `± u` = per-disk measurement uncertainty (die-dominated).

| # | Disk wt (mg) | Coating (mg) | Coating load (mg/cm²) | Hard-C load (mg/cm²) |
|---|---|---|---|---|
| 1 | 28.28 | 22.75 | 17.963 ± 0.149 | 15.938 |
| 2 | 29.43 | 23.90 | 18.870 ± 0.156 | 16.744 |
| 3 | 30.37 | 24.84 | 19.612 ± 0.161 | 17.402 |
| 4 | 28.45 | 22.92 | 18.097 ± 0.150 | 16.057 |
| 5 | 30.46 | 24.93 | 19.684 ± 0.162 | 17.465 |
| 6 | 30.82 | 25.29 | 19.968 ± 0.164 | 17.717 |
| 7 | 29.82 | 24.29 | 19.178 ± 0.158 | 17.017 |
| 8 | 30.04 | 24.51 | 19.352 ± 0.159 | 17.171 |
| 9 | 30.82 | 25.29 | 19.968 ± 0.164 | 17.717 |
| 10 | 29.82 | 24.29 | 19.178 ± 0.158 | 17.017 |
| 11 | 27.72 | 22.19 | 17.521 ± 0.145 | 15.546 |
| 12 | 29.52 | 23.99 | 18.942 ± 0.156 | 16.807 |
| 13 | 30.02 | 24.49 | 19.336 ± 0.159 | 17.157 |

### Population summary — Standard set (n = 13)

| Quantity | Mean | SD (spread) | CV | SEM | Min | Max |
|---|---|---|---|---|---|---|
| Coating mass (mg) | 24.134 | 0.973 | 4.0% | 0.270 | 22.194 | 25.294 |
| Coating load (mg/cm²) | **19.051** | 0.768 | 4.0% | 0.213 | 17.521 | 19.968 |
| Hard-carbon load (mg/cm²) | **16.904** | 0.682 | 4.0% | 0.189 | 15.546 | 17.717 |

---

## Per-disk results — Thick set (n = 6, stored separately)

| # | Disk wt (mg) | Coating (mg) | Coating load (mg/cm²) | Hard-C load (mg/cm²) |
|---|---|---|---|---|
| 1 | 37.53 | 32.00 | 25.265 ± 0.204 | 22.417 |
| 2 | 33.96 | 28.43 | 22.446 ± 0.183 | 19.917 |
| 3 | 31.93 | 26.40 | 20.844 ± 0.171 | 18.495 |
| 4 | 34.65 | 29.12 | 22.991 ± 0.187 | 20.400 |
| 5 | 36.46 | 30.93 | 24.420 ± 0.198 | 21.668 |
| 6 | 33.04 | 27.51 | 21.720 ± 0.177 | 19.272 |

### Population summary — Thick set (n = 6)

| Quantity | Mean | SD (spread) | CV | SEM | Min | Max |
|---|---|---|---|---|---|---|
| Coating mass (mg) | 29.070 | 2.099 | 7.2% | 0.857 | 26.404 | 32.005 |
| Coating load (mg/cm²) | **22.948** | 1.657 | 7.2% | 0.676 | 20.844 | 25.265 |
| Hard-carbon load (mg/cm²) | **20.362** | 1.470 | 7.2% | 0.600 | 18.495 | 22.417 |

> The split works: the **standard set is the most uniform biochar population to date (CV 4.0%)**, while the thick
> set sits ~3.9 mg/cm² higher and is more scattered (7.2%). Build routine cells from the standard set; the thick
> set is a **high-loading option (~20.4 mg/cm² hard carbon)** if a loading-dependence point is wanted.

---

## Uncertainty

**1. Measurement uncertainty (per disk): ≈ ±0.16–0.19 mg/cm² (±0.82%), die-dominated.**
u(load)/load = √[(u(coat)/coat)² + (2·u(d)/d)²], u(coat) = 0.059 mg, die Ø 12.7 mm ± 0.05 mm. Thick coating
(~22–32 mg) makes the tare term negligible; the **die tolerance (0.79%) dominates** — same regime as 6A/10A/1C.

**2. Disk-to-disk spread (physical): standard 4.0%, thick 7.2%.**
The standard-set spread (~0.68 mg/cm²) is ~5× the measurement uncertainty → real (mild) non-uniformity, but the
lowest of the biochar series thanks to the appearance/mass sort. The thick set is deliberately the high tail.

### Consequence for the experiment

- **Highest-loading electrodes of the whole series** (standard 16.9, thick 20.4 mg/cm² hard carbon) — a heavy
  coating, not an intrinsic material effect.
- Unlabeled disks within a set → per-cell active mass known as the set population value.

### Recommendation

- **Label disks** (and record which set) at punching to unlock per-cell mAh/g.
- ~~Fresh foil blank~~ — **DONE 2026-07-21** (11 blanks, 5.5255 mg; see `Processes/Foil_Tare_Measurement.md`). Next: weigh them **individually** to firm up the 0.057 mg SD (currently 1 dof).

---

## Cross-sample loading comparison (running)

| Sample | Temp / ramp | n | Coating load (mg/cm²) | Hard-C load (mg/cm²) | CV | Meas. u | Note |
|---|---|---|---|---|---|---|---|
| 6A  | 600 °C  | 20 | 8.46  | 7.51  | 3.6% | ±0.96% (die)  | baseline |
| 8A  | 800 °C  | 21 | 0.459 | 0.412 | 4.5% | ±10.1% (tare)  | anomalously thin (~5 µm) |
| 10A | 1000 °C | 20 | 11.56 | 10.27 | 2.2% | ±0.88% (die)  | most uniform (top band cut) |
| 12A_1C | 1200 °C, 1 °C/min | 17 | 12.10 | 10.73 | 3.2% | ±0.88% (die) | 3 outliers culled |
| 12A_2C sheet 1 | 1200 °C, 2 °C/min | 19 | 14.09 | 12.51 | 7.6% | ±0.85% (die) | gap 0.23 mm |
| 12A_2C sheet 2 | 1200 °C, 2 °C/min | 19 | 13.63 | 12.10 | 7.5% | ±0.86% (die) | gap 0.28 mm |
| **12A_3C standard** | 1200 °C, 3 °C/min | 13 | **19.05** | **16.90** | 4.0% | ±0.82% (die) | most uniform biochar set |
| **12A_3C thick** | 1200 °C, 3 °C/min | 6 | **22.95** | **20.36** | 7.2% | ±0.81% (die) | high-loading set, saved separately |
| Kuranode | commercial HC | 18 | 7.08 | 6.25 | 7.2% | ±1.02% (die) | off-standard mix; delaminated on calender |

---

## Cell Assembly & Cycling

> ⚠️ **Cycler C-rate basis differs from measured mass.** The cycling program's applied current (C-rate) was
> set from a flat **5.55 mg tare + 91% active-mass assumption**, not the measured values used below
> (**5.5255 mg** tare, measured 2026-07-21, and the per-sample f). The tare side is now nearly exact
> (+0.44%); the **active fraction is the dominant remaining difference**. See `Biona_Academy/Open_Questions.md` for the full note — recompute specific capacity from the
> measured mass, don't back it out from the nominal C-rate.

**3 sodium half-cells assembled 2026-07-15** (CC25, CC26, CC27) from 12A_3C disks — **the first cells built
from this sample**, before the labelled-disk practice below. Disk masses **received 2026-07-21** (previously
pending from supervisor). Active mass = (disk − **5.5255 mg** tare) × f, f = 0.8873. Area 1.2668 cm².

| Cell | Disk mass (mg) | Coating (mg) | **Hard-carbon mass (mg)** | Coating load (mg/cm²) | Hard-C load (mg/cm²) | Status |
|---|---|---|---|---|---|---|
| CC25 | 28.2 | 22.67 | **20.119** | 17.899 | 15.882 | cycling |
| CC26 | 28.2 | 22.67 | **20.119** | 17.899 | 15.882 | cycling |
| CC27 | 26.9 | 21.37 | **18.966** | 16.873 | 14.972 | cycling |

CC25 and CC26 land within the **standard set** range (27.72–30.82 mg); CC27 (26.9) sits just below it, in the
same slightly-low band as CC39 (26.6) — not flagged, consistent with the 4% disk-to-disk CV. **CC25 and CC26
share an identical recorded mass** (28.2 mg) and therefore identical derived values — plausible at 0.1 mg
rounding, but they are two separate cells, not a duplicated record.

**Cycling:** started 2026-07-15, **in progress**.

### 2 more cells assembled 2026-07-16 (CC39, CC40)

Electrode (total disk) mass recorded at assembly, rounded to 0.1 mg. Active mass = (disk − 5.5255 mg tare) × f,
f = 0.8873. Area 1.2668 cm².

| Cell | Disk mass (mg) | Coating (mg) | **Hard-carbon mass (mg)** | Coating load (mg/cm²) | Hard-C load (mg/cm²) | Status |
|---|---|---|---|---|---|---|
| CC39 | 26.6 | 21.07 | **18.699** | 16.636 | 14.761 | cycling |
| CC40 | 28.6 | 23.07 | **20.474** | 18.215 | 16.162 | cycling |

Both sit within/near the **standard set** range (27.72–30.82 mg disk mass) — CC39 slightly below (26.6 mg),
CC40 near the low end (28.6 mg); not flagged as anomalous, consistent with normal disk-to-disk spread (CV 4%).

> **Na half-cell / Na in excess** → these masses set only the working-electrode normalisation, not balancing.

**Cycling:** started 2026-07-16, **in progress**. Capacity / rate results — _pending_ for all 5 cells.
