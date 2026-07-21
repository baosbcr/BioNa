# Coin-Cell Disk Log — Kuranode (commercial hard carbon)

**Sample:** Kuranode — Kuraray commercial hard carbon (Na-ion benchmark) — calendered electrode (roll gap 0.09 mm; ⚠️ delaminated in spots — see `Kuranode_CommercialHC_Electrode_Prep.md`)
**Punch ID:** KT19
**Date:** 2026-07-15
**Purpose:** working electrodes for **sodium half-cells** (Na counter, Na always in excess); **commercial benchmark** vs the MMB1 biochar series
**Disks punched:** **18, all kept** · **Cutting die:** 12.7 mm Ø (½″) → **area 1.2668 cm²**
**Foil tare (carbon-coated foil, conductive-C layer, no slurry):** 0.00555 g (5.55 mg) *(assumed same as 6A/8A/1C — confirm with a fresh blank; matters most here, see below)*
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
| 1 | 14.36 | 8.81 | 6.955 ± 0.061 | 6.134 |
| 2 | 14.31 | 8.76 | 6.915 ± 0.061 | 6.099 |
| 3 | 14.25 | 8.70 | 6.868 ± 0.060 | 6.057 |
| 4 | 14.21 | 8.66 | 6.836 ± 0.060 | 6.030 |
| 5 | 14.15 | 8.60 | 6.789 ± 0.060 | 5.988 |
| 6 | 14.21 | 8.66 | 6.836 ± 0.060 | 6.030 |
| 7 | 14.34 | 8.79 | 6.939 ± 0.061 | 6.120 |
| 8 | 14.31 | 8.76 | 6.915 ± 0.061 | 6.099 |
| 9 | 14.15 | 8.60 | 6.789 ± 0.060 | 5.988 |
| 10 | 14.38 | 8.83 | 6.970 ± 0.061 | 6.148 |
| 11 | 14.53 | 8.98 | 7.089 ± 0.062 | 6.252 |
| 12 | 14.10 | 8.55 | 6.749 ± 0.059 | 5.953 |
| 13 | 16.48 | 10.93 | 8.628 ± 0.073 | 7.610 |
| 14 | 14.39 | 8.84 | 6.978 ± 0.061 | 6.155 |
| 15 | 15.96 | 10.41 | 8.218 ± 0.070 | 7.248 |
| 16 | 14.42 | 8.87 | 7.002 ± 0.061 | 6.176 |
| 17 | 14.21 | 8.66 | 6.836 ± 0.060 | 6.030 |
| 18 | 14.18 | 8.63 | 6.813 ± 0.060 | 6.009 |

### Population summary (n = 18)

| Quantity | Mean | SD (spread) | CV | SEM | Min | Max |
|---|---|---|---|---|---|---|
| Coating mass (mg) | 8.947 | 0.643 | 7.2% | 0.152 | 8.550 | 10.930 |
| Coating load (mg/cm²) | **7.063** | 0.507 | 7.2% | 0.120 | 6.749 | 8.628 |
| Hard-carbon load (mg/cm²) | **6.229** | 0.448 | 7.2% | 0.105 | 5.953 | 7.610 |

> **Two disks (#13, #15) carry the whole spread.** The other 16 sit in a 6.75–7.09 mg/cm² band (range ~0.34,
> essentially punch-limited — the tightest coating population in the project). Excluding those two, CV drops to
> ~1.7%. **Median 6.92 mg/cm² coating / 6.10 hard carbon** is the robust representative. No low-tail (bare-foil)
> disks → the peel zones were avoided at punching.

---

## Uncertainty

**1. Measurement uncertainty (per disk): ≈ ±0.06 mg/cm² (±0.87%), die-dominated but tare-sensitive.**
u(load)/load = √[(u(coat)/coat)² + (2·u(d)/d)²], u(coat) = 0.034 mg, die Ø 12.7 mm ± 0.05 mm. Coating is thin
(~8.9 mg), so the tare/mass term (0.37%) is larger here than for the biochar disks, though the **die tolerance
(0.79%) still dominates**. A **fresh foil blank would tighten Kuranode's loading the most** of any sample.

**2. Disk-to-disk spread (physical): 7.2% overall, ~1.7% excluding the two high disks.**
Reference-grade uniformity across the bulk — consistent with the CV 6.0% as-coated thickness grid. The two high
disks are mild proud spots, not the delamination zones (which were avoided).

### Consequence for the experiment

- **Lightest electrodes of the set** (7.06 mg/cm² coating, 6.23 hard carbon) — thin, even coating + lower f.
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
| 6A  | 600 °C  | 20 | 8.44  | 7.50  | 3.6% | ±0.85% (die)  | baseline |
| 8A  | 800 °C  | 21 | 0.439 | 0.394 | 4.7% | ±6.1% (tare)  | anomalously thin (~5 µm) |
| 10A | 1000 °C | 20 | 11.54 | 10.25 | 2.2% | ±0.82% (die)  | most uniform (top band cut) |
| 12A_1C | 1200 °C, 1 °C/min | 17 | 12.08 | 10.72 | 3.2% | ±0.82% (die) | 3 outliers culled |
| 12A_2C sheet 1 | 1200 °C, 2 °C/min | 19 | 14.07 | 12.49 | 7.7% | ±0.81% (die) | gap 0.23 mm |
| 12A_2C sheet 2 | 1200 °C, 2 °C/min | 19 | 13.61 | 12.08 | 7.5% | ±0.81% (die) | gap 0.28 mm |
| 12A_3C standard | 1200 °C, 3 °C/min | 13 | 19.03 | 16.89 | 4.0% | ±0.80% (die) | most uniform biochar set |
| 12A_3C thick | 1200 °C, 3 °C/min | 6 | 22.93 | 20.34 | 7.2% | ±0.80% (die) | high-loading set, saved separately |
| **Kuranode** | commercial HC | 18 | **7.06** | **6.23** | 7.2% | ±0.87% (die) | off-standard mix; delaminated; qualitative only |

---

## Cell Assembly & Cycling

> ⚠️ **Cycler C-rate basis differs from measured mass.** The cycling program's applied current (C-rate) was
> set from a flat **91% active-mass assumption**, not the measured per-sample f used below. (The 5.55 mg
> foil tare now matches on both sides — adopted repo-wide 2026-07-21 — so the **active fraction is the only
> remaining difference**.) See `Biona_Academy/Open_Questions.md` for the full note — recompute specific capacity from the
> measured mass, don't back it out from the nominal C-rate.

**2 sodium half-cells assembled 2026-07-16** (CC33, CC34), cell-naming series **KT1-9**, from Kuranode disks.

Electrode (total disk) mass recorded at assembly, rounded to 0.1 mg. Active mass = (disk − 5.55 mg tare) × f,
f = 0.882. Area 1.2668 cm².

| Cell | Disk mass (mg) | Coating (mg) | **Hard-carbon mass (mg)** | Coating load (mg/cm²) | Hard-C load (mg/cm²) | Status |
|---|---|---|---|---|---|---|
| CC33 | 14.0 | 8.45 | **7.453** | 6.671 | 5.883 | cycling |
| CC34 | 13.8 | 8.25 | **7.277** | 6.513 | 5.744 | cycling |

Both sit just below the 18-disk punch range (min disk mass 14.10 mg) — minor, consistent with the ±3.6%-scale
disk-to-disk noise seen elsewhere; not flagged as anomalous.

> **Na half-cell / Na in excess** → these masses set only the working-electrode normalisation, not balancing.
> Recall this Kuranode batch is **off-standard** (SBR mixed before HC + extra drop, delaminated on
> calendering) — treat as a qualitative test, not a clean commercial-HC benchmark (see notes at top of file).

**Cycling:** started 2026-07-16, **in progress**. Capacity / rate results — _pending_.
