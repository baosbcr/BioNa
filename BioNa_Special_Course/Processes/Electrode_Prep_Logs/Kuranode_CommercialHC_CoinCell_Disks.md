# Coin-Cell Disk Log — Kuranode (commercial hard carbon)

**Sample:** Kuranode — Kuraray commercial hard carbon (Na-ion benchmark) — calendered electrode (roll gap 0.09 mm; ⚠️ delaminated in spots — see `Kuranode_CommercialHC_Electrode_Prep.md`)
**Punch ID:** KT19
**Date:** 2026-07-15
**Purpose:** working electrodes for **sodium half-cells** (Na counter, Na always in excess); **commercial benchmark** vs the MMB1 biochar series
**Disks punched:** **18, all kept** · **Cutting die:** 12.7 mm Ø (½″) → **area 1.2668 cm²**
**Foil tare (carbon-coated foil, conductive-C layer, no slurry):** 0.0055 g (5.50 mg) *(assumed same as 6A/8A/1C — confirm with a fresh blank; matters most here, see below)*
**Compute script:** `Processes/Electrode_Prep_Logs/disk_loading.py`

> ⚠️ **Read alongside the prep log's OFF-STANDARD notes.** SBR was mixed **before** the hard carbon (+ an extra
> drop after), and the electrode **delaminated at ~20 spots on calendering** ("band-aid" peel). Disks were punched
> **clear of the peel zones** — consistent with the mass data (no ultra-light bare-foil disks). This is a
> **qualitative "what happens" test, NOT a clean commercial-HC benchmark** (both material and process differ).
>
> **Disks unlabeled and indistinguishable** — masses known as a set.

---

## Slurry solids composition (from Kuranode prep log)

| Component | Mass (g) | wt% of dried solids |
|---|---|---|
| Hard carbon (Kuranode) | 3.64010 | **88.18** |
| C45 | 0.16690 | 4.04 |
| SBR | 0.22 *(est.: 0.195 + ~0.025 extra drop)* | 5.33 |
| CMC | 0.10083 | 2.44 |
| **Total solids** | 4.12783 | 100 |

**Active (hard-carbon) fraction f = 0.882** — lower than the MMB1 series (0.887) because of the **extra SBR drop**.
Coating mass = disk mass − foil tare. Hard-carbon mass = coating × f.

> ⚠️ **SBR above standard AND split around the hard carbon** — total ≈ 0.22 g est., neither addition weighed.
> This both lowers f and is the leading suspect for the calendering delamination (poor binder distribution over
> the HC surface). See prep log.

---

## Per-disk results (n = 18)

Coating load = coating mass / 1.2668 cm². `± u` = per-disk measurement uncertainty (die-dominated).

| # | Disk wt (mg) | Coating (mg) | Coating load (mg/cm²) | Hard-C load (mg/cm²) |
|---|---|---|---|---|
| 1 | 14.36 | 8.86 | 6.994 ± 0.061 | 6.169 |
| 2 | 14.31 | 8.81 | 6.955 ± 0.061 | 6.134 |
| 3 | 14.25 | 8.75 | 6.907 ± 0.061 | 6.092 |
| 4 | 14.21 | 8.71 | 6.876 ± 0.060 | 6.064 |
| 5 | 14.15 | 8.65 | 6.828 ± 0.060 | 6.022 |
| 6 | 14.21 | 8.71 | 6.876 ± 0.060 | 6.064 |
| 7 | 14.34 | 8.84 | 6.978 ± 0.061 | 6.155 |
| 8 | 14.31 | 8.81 | 6.955 ± 0.061 | 6.134 |
| 9 | 14.15 | 8.65 | 6.828 ± 0.060 | 6.022 |
| 10 | 14.38 | 8.88 | 7.010 ± 0.061 | 6.183 |
| 11 | 14.53 | 9.03 | 7.128 ± 0.062 | 6.287 |
| 12 | 14.10 | 8.60 | 6.789 ± 0.060 | 5.988 |
| 13 | 16.48 | 10.98 | 8.668 ± 0.073 | 7.645 |
| 14 | 14.39 | 8.89 | 7.018 ± 0.061 | 6.190 |
| 15 | 15.96 | 10.46 | 8.257 ± 0.070 | 7.283 |
| 16 | 14.42 | 8.92 | 7.041 ± 0.062 | 6.210 |
| 17 | 14.21 | 8.71 | 6.876 ± 0.060 | 6.064 |
| 18 | 14.18 | 8.68 | 6.852 ± 0.060 | 6.043 |

### Population summary (n = 18)

| Quantity | Mean | SD (spread) | CV | SEM | Min | Max |
|---|---|---|---|---|---|---|
| Coating mass (mg) | 8.997 | 0.643 | 7.1% | 0.152 | 8.600 | 10.980 |
| Coating load (mg/cm²) | **7.102** | 0.507 | 7.1% | 0.120 | 6.789 | 8.668 |
| Hard-carbon load (mg/cm²) | **6.264** | 0.448 | 7.1% | 0.105 | 5.988 | 7.645 |

> **Two disks (#13, #15) carry the whole spread.** The other 16 sit in a 6.79–7.13 mg/cm² band (range ~0.34,
> essentially punch-limited — the tightest coating population in the project). Excluding those two, CV drops to
> ~1.6%. **Median 6.96 mg/cm² coating / 6.13 hard carbon** is the robust representative. No low-tail (bare-foil)
> disks → the peel zones were avoided at punching.

---

## Uncertainty

**1. Measurement uncertainty (per disk): ≈ ±0.06 mg/cm² (±0.88%), die-dominated but tare-sensitive.**
u(load)/load = √[(u(coat)/coat)² + (2·u(d)/d)²], u(coat) = 0.034 mg, die Ø 12.7 mm ± 0.05 mm. Coating is thin
(~9 mg), so the tare/mass term (0.39%) is larger here than for the biochar disks, though the **die tolerance
(0.79%) still dominates**. A **fresh foil blank would tighten Kuranode's loading the most** of any sample.

**2. Disk-to-disk spread (physical): 7.1% overall, ~1.6% excluding the two high disks.**
Reference-grade uniformity across the bulk — consistent with the CV 6.0% as-coated thickness grid. The two high
disks are mild proud spots, not the delamination zones (which were avoided).

### Consequence for the experiment

- **Lightest electrodes of the set** (7.10 mg/cm² coating, 6.26 hard carbon) — thin, even coating + lower f.
- **Interpret with care:** off-standard mix order + delamination → not a controlled commercial-HC benchmark. A
  **standard-order Kuranode rebuild** is needed before comparing capacity/rate against the MMB1 series.

### Recommendation

- **Controlled Kuranode rebuild (standard SBR-last order)** for a fair benchmark.
- Punch a **fresh foil blank** — highest-value here given the thin coating.
- **Label disks** at punching for per-cell mAh/g.

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
| 12A_3C standard | 1200 °C, 3 °C/min | 13 | 19.07 | 16.92 | 4.0% | ±0.80% (die) | most uniform biochar set |
| 12A_3C thick | 1200 °C, 3 °C/min | 6 | 22.97 | 20.38 | 7.2% | ±0.80% (die) | high-loading set, saved separately |
| **Kuranode** | commercial HC | 18 | **7.10** | **6.26** | 7.1% | ±0.88% (die) | off-standard mix; delaminated; qualitative only |
