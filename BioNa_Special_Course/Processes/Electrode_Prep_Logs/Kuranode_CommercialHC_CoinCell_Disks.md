# Coin-Cell Disk Log — Kuranode (commercial hard carbon)

**Sample:** Kuranode — Kuraray commercial hard carbon (Na-ion benchmark) — calendered electrode (roll gap 0.09 mm; ⚠️ delaminated in spots — see `Kuranode_CommercialHC_Electrode_Prep.md`)
**Punch ID:** KT19
**Date:** 2026-07-15
**Purpose:** working electrodes for **sodium half-cells** (Na counter, Na always in excess); **commercial benchmark** vs the MMB1 biochar series
**Disks punched:** **18, all kept** · **Cutting die:** 12.7 mm Ø (½″) → **area 1.2668 cm²**
**Foil tare (carbon-coated foil, conductive-C layer, no slurry):** 0.0055255 g (5.53 mg) *(**MEASURED** 2026-07-21: mean of 11 blanks cut with this same 12.7 mm die, SD 0.057 mg — see `Processes/Foil_Tare_Measurement.md`)*
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
| 1 | 14.36 | 8.83 | 6.974 ± 0.072 | 6.151 |
| 2 | 14.31 | 8.78 | 6.935 ± 0.072 | 6.116 |
| 3 | 14.25 | 8.72 | 6.887 ± 0.071 | 6.075 |
| 4 | 14.21 | 8.68 | 6.856 ± 0.071 | 6.047 |
| 5 | 14.15 | 8.62 | 6.808 ± 0.071 | 6.005 |
| 6 | 14.21 | 8.68 | 6.856 ± 0.071 | 6.047 |
| 7 | 14.34 | 8.81 | 6.958 ± 0.072 | 6.137 |
| 8 | 14.31 | 8.78 | 6.935 ± 0.072 | 6.116 |
| 9 | 14.15 | 8.62 | 6.808 ± 0.071 | 6.005 |
| 10 | 14.38 | 8.85 | 6.990 ± 0.072 | 6.165 |
| 11 | 14.53 | 9.00 | 7.108 ± 0.073 | 6.269 |
| 12 | 14.10 | 8.57 | 6.769 ± 0.071 | 5.970 |
| 13 | 16.48 | 10.95 | 8.648 ± 0.082 | 7.627 |
| 14 | 14.39 | 8.86 | 6.998 ± 0.072 | 6.172 |
| 15 | 15.96 | 10.43 | 8.237 ± 0.080 | 7.265 |
| 16 | 14.42 | 8.89 | 7.021 ± 0.072 | 6.193 |
| 17 | 14.21 | 8.68 | 6.856 ± 0.071 | 6.047 |
| 18 | 14.18 | 8.65 | 6.832 ± 0.071 | 6.026 |

### Population summary (n = 18)

| Quantity | Mean | SD (spread) | CV | SEM | Min | Max |
|---|---|---|---|---|---|---|
| Coating mass (mg) | 8.971 | 0.643 | 7.2% | 0.152 | 8.575 | 10.954 |
| Coating load (mg/cm²) | **7.082** | 0.507 | 7.2% | 0.120 | 6.769 | 8.648 |
| Hard-carbon load (mg/cm²) | **6.246** | 0.448 | 7.2% | 0.105 | 5.970 | 7.627 |

> **Two disks (#13, #15) carry the whole spread.** The other 16 sit in a 6.77–7.11 mg/cm² band (range ~0.34,
> essentially punch-limited — the tightest coating population in the project). Excluding those two, CV drops to
> ~1.7%. **Median 6.93 mg/cm² coating / 6.12 hard carbon** is the robust representative. No low-tail (bare-foil)
> disks → the peel zones were avoided at punching.

---

## Uncertainty

**1. Measurement uncertainty (per disk): ≈ ±0.07 mg/cm² (±1.02%), die-dominated but tare-sensitive.**
u(load)/load = √[(u(coat)/coat)² + (2·u(d)/d)²], u(coat) = 0.059 mg, die Ø 12.7 mm ± 0.05 mm. Coating is thin
(~9.0 mg), so the tare/mass term (0.65%) is larger here than for the biochar disks, though the **die tolerance
(0.79%) still dominates**. The tare is now **measured** (5.5255 ± 0.057 mg, n=11); weighing the blanks individually would tighten Kuranode's loading further.

**2. Disk-to-disk spread (physical): 7.2% overall, ~1.7% excluding the two high disks.**
Reference-grade uniformity across the bulk — consistent with the CV 6.0% as-coated thickness grid. The two high
disks are mild proud spots, not the delamination zones (which were avoided).

### Consequence for the experiment

- **Lightest electrodes of the set** (7.08 mg/cm² coating, 6.25 hard carbon) — thin, even coating + lower f.
- **Interpret with care:** off-standard mix order + delamination → not a controlled commercial-HC benchmark. A
  **standard-order Kuranode rebuild** is needed before comparing capacity/rate against the MMB1 series.

### Recommendation

- **Controlled Kuranode rebuild (standard SBR-last order)** for a fair benchmark.
- ~~Punch a fresh foil blank~~ — **DONE 2026-07-21** (see `Processes/Foil_Tare_Measurement.md`). Weighing the 11 blanks individually is the remaining gain here, given the thin coating.
- **Label disks** at punching for per-cell mAh/g.

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
| 12A_3C standard | 1200 °C, 3 °C/min | 13 | 19.05 | 16.90 | 4.0% | ±0.82% (die) | most uniform biochar set |
| 12A_3C thick | 1200 °C, 3 °C/min | 6 | 22.95 | 20.36 | 7.2% | ±0.81% (die) | high-loading set, saved separately |
| **Kuranode** | commercial HC | 18 | **7.08** | **6.25** | 7.2% | ±1.02% (die) | off-standard mix; delaminated; qualitative only |

---

## Cell Assembly & Cycling

> ⚠️ **Cycler C-rate basis differs from measured mass.** The cycling program's applied current (C-rate) was
> set from a flat **5.55 mg tare + 91% active-mass assumption**, not the measured values used below
> (**5.5255 mg** tare, measured 2026-07-21, and the per-sample f). The tare side is now nearly exact
> (+0.44%); the **active fraction is the dominant remaining difference**. See `Biona_Academy/Open_Questions.md` for the full note — recompute specific capacity from the
> measured mass, don't back it out from the nominal C-rate.

**2 sodium half-cells assembled 2026-07-16** (CC33, CC34), cell-naming series **KT1-9**, from Kuranode disks.

Electrode (total disk) mass recorded at assembly, rounded to 0.1 mg. Active mass = (disk − 5.5255 mg tare) × f,
f = 0.882. Area 1.2668 cm².

| Cell | Disk mass (mg) | Coating (mg) | **Hard-carbon mass (mg)** | Coating load (mg/cm²) | Hard-C load (mg/cm²) | Status |
|---|---|---|---|---|---|---|
| CC33 | 14.0 | 8.47 | **7.475** | 6.690 | 5.900 | cycling |
| CC34 | 13.8 | 8.27 | **7.298** | 6.532 | 5.761 | cycling |

Both sit just below the 18-disk punch range (min disk mass 14.10 mg) — minor, consistent with the ±3.6%-scale
disk-to-disk noise seen elsewhere; not flagged as anomalous.

> **Na half-cell / Na in excess** → these masses set only the working-electrode normalisation, not balancing.
> Recall this Kuranode batch is **off-standard** (SBR mixed before HC + extra drop, delaminated on
> calendering) — treat as a qualitative test, not a clean commercial-HC benchmark (see notes at top of file).

**Cycling:** started 2026-07-16, **in progress**. Capacity / rate results — _pending_.
