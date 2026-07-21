# Coin-Cell Disk Log — MMB1_12A_3C

**Sample:** MMB1_12A_3C (1200 °C, 180 °C/h = 3 °C/min ramp — standard ramp; = base MMB1_12A) — calendered electrode (roll gap 0.43 mm; see `MMB1_12A_3C_Electrode_Prep.md`)
**Date:** 2026-07-15
**Purpose:** working electrodes for **sodium half-cells** (Na counter, Na always in excess)
**Disks punched:** **19 → split into 13 standard + 6 thick** · **Cutting die:** 12.7 mm Ø (½″) → **area 1.2668 cm²**
**Foil tare (carbon-coated foil, conductive-C layer, no slurry):** 0.00555 g (5.55 mg) *(assumed same as 6A/8A/1C — confirm with a fresh blank)*
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
| 1 | 28.28 | 22.73 | 17.943 ± 0.144 | 15.921 |
| 2 | 29.43 | 23.88 | 18.851 ± 0.151 | 16.727 |
| 3 | 30.37 | 24.82 | 19.593 ± 0.157 | 17.385 |
| 4 | 28.45 | 22.90 | 18.077 ± 0.145 | 16.040 |
| 5 | 30.46 | 24.91 | 19.664 ± 0.157 | 17.448 |
| 6 | 30.82 | 25.27 | 19.948 ± 0.159 | 17.700 |
| 7 | 29.82 | 24.27 | 19.159 ± 0.153 | 17.000 |
| 8 | 30.04 | 24.49 | 19.333 ± 0.155 | 17.154 |
| 9 | 30.82 | 25.27 | 19.948 ± 0.159 | 17.700 |
| 10 | 29.82 | 24.27 | 19.159 ± 0.153 | 17.000 |
| 11 | 27.72 | 22.17 | 17.501 ± 0.140 | 15.529 |
| 12 | 29.52 | 23.97 | 18.922 ± 0.151 | 16.790 |
| 13 | 30.02 | 24.47 | 19.317 ± 0.154 | 17.140 |

### Population summary — Standard set (n = 13)

| Quantity | Mean | SD (spread) | CV | SEM | Min | Max |
|---|---|---|---|---|---|---|
| Coating mass (mg) | 24.109 | 0.973 | 4.0% | 0.270 | 22.170 | 25.270 |
| Coating load (mg/cm²) | **19.032** | 0.768 | 4.0% | 0.213 | 17.501 | 19.948 |
| Hard-carbon load (mg/cm²) | **16.887** | 0.682 | 4.0% | 0.189 | 15.529 | 17.700 |

---

## Per-disk results — Thick set (n = 6, stored separately)

| # | Disk wt (mg) | Coating (mg) | Coating load (mg/cm²) | Hard-C load (mg/cm²) |
|---|---|---|---|---|
| 1 | 37.53 | 31.98 | 25.245 ± 0.201 | 22.400 |
| 2 | 33.96 | 28.41 | 22.427 ± 0.179 | 19.900 |
| 3 | 31.93 | 26.38 | 20.825 ± 0.166 | 18.478 |
| 4 | 34.65 | 29.10 | 22.972 ± 0.183 | 20.383 |
| 5 | 36.46 | 30.91 | 24.401 ± 0.194 | 21.651 |
| 6 | 33.04 | 27.49 | 21.701 ± 0.173 | 19.255 |

### Population summary — Thick set (n = 6)

| Quantity | Mean | SD (spread) | CV | SEM | Min | Max |
|---|---|---|---|---|---|---|
| Coating mass (mg) | 29.045 | 2.099 | 7.2% | 0.857 | 26.380 | 31.980 |
| Coating load (mg/cm²) | **22.928** | 1.657 | 7.2% | 0.676 | 20.825 | 25.245 |
| Hard-carbon load (mg/cm²) | **20.344** | 1.470 | 7.2% | 0.600 | 18.478 | 22.400 |

> The split works: the **standard set is the most uniform biochar population to date (CV 4.0%)**, while the thick
> set sits ~3.9 mg/cm² higher and is more scattered (7.2%). Build routine cells from the standard set; the thick
> set is a **high-loading option (~20.3 mg/cm² hard carbon)** if a loading-dependence point is wanted.

---

## Uncertainty

**1. Measurement uncertainty (per disk): ≈ ±0.15–0.20 mg/cm² (±0.80%), die-dominated.**
u(load)/load = √[(u(coat)/coat)² + (2·u(d)/d)²], u(coat) = 0.034 mg, die Ø 12.7 mm ± 0.05 mm. Thick coating
(~22–32 mg) makes the tare term negligible; the **die tolerance (0.79%) dominates** — same regime as 6A/10A/1C.

**2. Disk-to-disk spread (physical): standard 4.0%, thick 7.2%.**
The standard-set spread (~0.68 mg/cm²) is ~5× the measurement uncertainty → real (mild) non-uniformity, but the
lowest of the biochar series thanks to the appearance/mass sort. The thick set is deliberately the high tail.

### Consequence for the experiment

- **Highest-loading electrodes of the whole series** (standard 16.9, thick 20.3 mg/cm² hard carbon) — a heavy
  coating, not an intrinsic material effect.
- Unlabeled disks within a set → per-cell active mass known as the set population value.

### Recommendation

- **Label disks** (and record which set) at punching to unlock per-cell mAh/g.
- Fresh **foil blank** to replace the adopted 5.55 mg tare.

---

## Cross-sample loading comparison (running)

| Sample | Temp / ramp | n | Coating load (mg/cm²) | Hard-C load (mg/cm²) | CV | Meas. u | Note |
|---|---|---|---|---|---|---|---|
| 6A  | 600 °C  | 20 | 8.44  | 7.50  | 3.6% | ±0.85% (die)  | baseline |
| 8A  | 800 °C  | 21 | 0.439 | 0.394 | 4.7% | ±6.1% (tare)  | anomalously thin (~5 µm) |
| 10A | 1000 °C | 20 | 11.54 | 10.25 | 2.2% | ±0.82% (die)  | most uniform (top band cut) |
| 12A_1C | 1200 °C, 1 °C/min | 17 | 12.08 | 10.72 | 3.2% | ±0.82% (die) | 3 outliers culled |
| 12A_2C sheet 1 | 1200 °C, 2 °C/min | 19 | 14.07 | 12.49 | 7.7% | ±0.81% (die) | gap 0.23 mm |
| 12A_2C sheet 2 | 1200 °C, 2 °C/min | 19 | 13.61 | 12.08 | 7.5% | ±0.81% (die) | gap 0.28 mm |
| **12A_3C standard** | 1200 °C, 3 °C/min | 13 | **19.03** | **16.89** | 4.0% | ±0.80% (die) | most uniform biochar set |
| **12A_3C thick** | 1200 °C, 3 °C/min | 6 | **22.93** | **20.34** | 7.2% | ±0.80% (die) | high-loading set, saved separately |
| Kuranode | commercial HC | 18 | 7.06 | 6.23 | 7.2% | ±0.87% (die) | off-standard mix; delaminated on calender |

---

## Cell Assembly & Cycling

> ⚠️ **Cycler C-rate basis differs from measured mass.** The cycling program's applied current (C-rate) was
> set from a flat **91% active-mass assumption**, not the measured per-sample f used below. (The 5.55 mg
> foil tare now matches on both sides — adopted repo-wide 2026-07-21 — so the **active fraction is the only
> remaining difference**.) See `Biona_Academy/Open_Questions.md` for the full note — recompute specific capacity from the
> measured mass, don't back it out from the nominal C-rate.

**3 sodium half-cells assembled 2026-07-15** (CC25, CC26, CC27) from 12A_3C disks — **the first cells built
from this sample**, before the labelled-disk practice below. Disk masses **received 2026-07-21** (previously
pending from supervisor). Active mass = (disk − **5.55 mg** tare) × f, f = 0.8873. Area 1.2668 cm².

| Cell | Disk mass (mg) | Coating (mg) | **Hard-carbon mass (mg)** | Coating load (mg/cm²) | Hard-C load (mg/cm²) | Status |
|---|---|---|---|---|---|---|
| CC25 | 28.2 | 22.65 | **20.097** | 17.880 | 15.865 | cycling |
| CC26 | 28.2 | 22.65 | **20.097** | 17.880 | 15.865 | cycling |
| CC27 | 26.9 | 21.35 | **18.944** | 16.854 | 14.954 | cycling |

CC25 and CC26 land within the **standard set** range (27.72–30.82 mg); CC27 (26.9) sits just below it, in the
same slightly-low band as CC39 (26.6) — not flagged, consistent with the 4% disk-to-disk CV. **CC25 and CC26
share an identical recorded mass** (28.2 mg) and therefore identical derived values — plausible at 0.1 mg
rounding, but they are two separate cells, not a duplicated record.

**Cycling:** started 2026-07-15, **in progress**.

### 2 more cells assembled 2026-07-16 (CC39, CC40)

Electrode (total disk) mass recorded at assembly, rounded to 0.1 mg. Active mass = (disk − 5.55 mg tare) × f,
f = 0.8873. Area 1.2668 cm².

| Cell | Disk mass (mg) | Coating (mg) | **Hard-carbon mass (mg)** | Coating load (mg/cm²) | Hard-C load (mg/cm²) | Status |
|---|---|---|---|---|---|---|
| CC39 | 26.6 | 21.05 | **18.678** | 16.617 | 14.744 | cycling |
| CC40 | 28.6 | 23.05 | **20.452** | 18.196 | 16.145 | cycling |

Both sit within/near the **standard set** range (27.72–30.82 mg disk mass) — CC39 slightly below (26.6 mg),
CC40 near the low end (28.6 mg); not flagged as anomalous, consistent with normal disk-to-disk spread (CV 4%).

> **Na half-cell / Na in excess** → these masses set only the working-electrode normalisation, not balancing.

**Cycling:** started 2026-07-16, **in progress**. Capacity / rate results — _pending_ for all 5 cells.
