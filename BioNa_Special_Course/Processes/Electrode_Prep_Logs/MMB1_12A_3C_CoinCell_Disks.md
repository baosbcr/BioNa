# Coin-Cell Disk Log — MMB1_12A_3C

**Sample:** MMB1_12A_3C (1200 °C, 180 °C/h = 3 °C/min ramp — standard ramp; = base MMB1_12A) — calendered electrode (roll gap 0.43 mm; see `MMB1_12A_3C_Electrode_Prep.md`)
**Date:** 2026-07-15
**Purpose:** working electrodes for **sodium half-cells** (Na counter, Na always in excess)
**Disks punched:** **19 → split into 13 standard + 6 thick** · **Cutting die:** 12.7 mm Ø (½″) → **area 1.2668 cm²**
**Foil tare (carbon-coated foil, conductive-C layer, no slurry):** 0.0055 g (5.50 mg) *(assumed same as 6A/8A/1C — confirm with a fresh blank)*
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
| 1 | 28.28 | 22.78 | 17.982 ± 0.144 | 15.956 |
| 2 | 29.43 | 23.93 | 18.890 ± 0.151 | 16.761 |
| 3 | 30.37 | 24.87 | 19.632 ± 0.157 | 17.420 |
| 4 | 28.45 | 22.95 | 18.117 ± 0.145 | 16.075 |
| 5 | 30.46 | 24.96 | 19.703 ± 0.157 | 17.483 |
| 6 | 30.82 | 25.32 | 19.987 ± 0.160 | 17.735 |
| 7 | 29.82 | 24.32 | 19.198 ± 0.154 | 17.034 |
| 8 | 30.04 | 24.54 | 19.372 ± 0.155 | 17.188 |
| 9 | 30.82 | 25.32 | 19.987 ± 0.160 | 17.735 |
| 10 | 29.82 | 24.32 | 19.198 ± 0.154 | 17.034 |
| 11 | 27.72 | 22.22 | 17.540 ± 0.141 | 15.563 |
| 12 | 29.52 | 24.02 | 18.961 ± 0.152 | 16.824 |
| 13 | 30.02 | 24.52 | 19.356 ± 0.155 | 17.174 |

### Population summary — Standard set (n = 13)

| Quantity | Mean | SD (spread) | CV | SEM | Min | Max |
|---|---|---|---|---|---|---|
| Coating mass (mg) | 24.159 | 0.973 | 4.0% | 0.270 | 22.220 | 25.320 |
| Coating load (mg/cm²) | **19.071** | 0.768 | 4.0% | 0.213 | 17.540 | 19.987 |
| Hard-carbon load (mg/cm²) | **16.922** | 0.682 | 4.0% | 0.189 | 15.563 | 17.735 |

---

## Per-disk results — Thick set (n = 6, stored separately)

| # | Disk wt (mg) | Coating (mg) | Coating load (mg/cm²) | Hard-C load (mg/cm²) |
|---|---|---|---|---|
| 1 | 37.53 | 32.03 | 25.284 ± 0.201 | 22.435 |
| 2 | 33.96 | 28.46 | 22.466 ± 0.179 | 19.934 |
| 3 | 31.93 | 26.43 | 20.864 ± 0.166 | 18.512 |
| 4 | 34.65 | 29.15 | 23.011 ± 0.183 | 20.417 |
| 5 | 36.46 | 30.96 | 24.440 ± 0.194 | 21.685 |
| 6 | 33.04 | 27.54 | 21.740 ± 0.173 | 19.290 |

### Population summary — Thick set (n = 6)

| Quantity | Mean | SD (spread) | CV | SEM | Min | Max |
|---|---|---|---|---|---|---|
| Coating mass (mg) | 29.095 | 2.099 | 7.2% | 0.857 | 26.430 | 32.030 |
| Coating load (mg/cm²) | **22.967** | 1.657 | 7.2% | 0.676 | 20.864 | 25.284 |
| Hard-carbon load (mg/cm²) | **20.379** | 1.470 | 7.2% | 0.600 | 18.512 | 22.435 |

> The split works: the **standard set is the most uniform biochar population to date (CV 4.0%)**, while the thick
> set sits ~3.5 mg/cm² higher and is more scattered (7.2%). Build routine cells from the standard set; the thick
> set is a **high-loading option (~20.4 mg/cm² hard carbon)** if a loading-dependence point is wanted.

---

## Uncertainty

**1. Measurement uncertainty (per disk): ≈ ±0.15–0.20 mg/cm² (±0.80%), die-dominated.**
u(load)/load = √[(u(coat)/coat)² + (2·u(d)/d)²], u(coat) = 0.034 mg, die Ø 12.7 mm ± 0.05 mm. Thick coating
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
- Fresh **foil blank** to replace the assumed 5.50 mg tare.

---

## Cross-sample loading comparison (running)

| Sample | Temp / ramp | n | Coating load (mg/cm²) | Hard-C load (mg/cm²) | CV | Meas. u | Note |
|---|---|---|---|---|---|---|---|
| 6A  | 600 °C  | 20 | 8.48  | 7.53  | 3.6% | ±0.85% (die)  | baseline |
| 8A  | 800 °C  | 21 | 0.479 | 0.430 | 4.3% | ±5.6% (tare)  | anomalously thin (~5 µm) |
| 10A | 1000 °C | 20 | 11.58 | 10.28 | 2.1% | ±0.82% (die)  | most uniform (top band cut) |
| 12A_1C | 1200 °C, 1 °C/min | 17 | 12.12 | 10.75 | 3.2% | ±0.82% (die) | 3 outliers culled |
| 12A_2C sheet 1 | 1200 °C, 2 °C/min | 19 | 14.11 | 12.53 | 7.6% | ±0.81% (die) | gap 0.23 mm |
| 12A_2C sheet 2 | 1200 °C, 2 °C/min | 19 | 13.65 | 12.12 | 7.5% | ±0.81% (die) | gap 0.28 mm |
| **12A_3C standard** | 1200 °C, 3 °C/min | 13 | **19.07** | **16.92** | 4.0% | ±0.80% (die) | most uniform biochar set |
| **12A_3C thick** | 1200 °C, 3 °C/min | 6 | **22.97** | **20.38** | 7.2% | ±0.80% (die) | high-loading set, saved separately |
| Kuranode | commercial HC | 18 | 7.10 | 6.26 | 7.1% | ±0.88% (die) | off-standard mix; delaminated on calender |
