# Coin-Cell Disk Log — MMB1_8A

**Sample:** MMB1_8A (800 °C, 180 °C/h) — calendered electrode (see `MMB1_8A_Electrode_Prep.md`)
**Date:** 2026-07-09
**Purpose:** working electrodes for **sodium half-cells** (Na counter, Na always in excess)
**Disks punched:** 21 · **Cutting die:** 12.7 mm Ø (½″) → **area 1.2668 cm²**
**Foil tare (carbon-coated foil, conductive-C layer, no slurry):** 0.0055255 g (5.53 mg) *(**MEASURED** 2026-07-21: mean of 11 blanks cut with this same 12.7 mm die, SD 0.057 mg — see `Processes/Foil_Tare_Measurement.md`)*
**Compute script:** `Processes/Electrode_Prep_Logs/disk_loading.py`

> **21 disks (one extra cut).** Some may be discarded later as outliers (as anticipated for 12A).
> Disks are **unlabeled and indistinguishable** — masses are known as a *set*; a given mass cannot be
> matched back to the disk built into a given cell (same as 6A). See "Uncertainty".

> ⚠️ **Read this before using these loadings.** 8A's coating is **anomalously thin** (~0.58 mg/disk,
> ~0.46 mg/cm² — about **18× lighter than 6A's 8.46 mg/cm²**), consistent with the ~5 µm as-coated
> thickness flagged in the prep log. The coating is only ~**11 % of the 5.53 mg foil tare**, so every
> loading here is a **small difference of two larger masses** and the numbers are dominated by
> tare-subtraction uncertainty, not by real coating variation. Treat absolute loadings as approximate.

---

## Slurry solids composition (from 8A prep log)

| Component | Mass (g) | wt% of dried solids |
|---|---|---|
| Hard carbon (MMB1_8A) | 3.6400 | **89.77** |
| C45 | 0.1665 | 4.11 |
| SBR | 0.148 *(est.)* | 3.65 |
| CMC | 0.1002 | 2.47 |
| **Total solids** | 4.0547 | 100 |

**Active (hard-carbon) fraction f = 0.8977** — assumes the dried coating retains the batch ratio.
Coating mass = disk mass − foil tare. Hard-carbon mass = coating × f.

> ⚠️ **SBR mass is uncertain for 8A.** The prep log records **0.1228 g measured + 1 unmeasured drop**
> (old burner-pipette dosing, before the 200 µL calibrated-pipette standard). Best estimate ≈ **0.148 g**.
> Sensitivity: using the bare 0.1228 g instead raises f to 0.9033 (+0.6 %), i.e. hard-carbon loads
> ~0.6 % higher — small next to the tare-driven uncertainty below.

---

## Per-disk results

Coating load = coating mass / 1.2668 cm². `± u` is the **per-disk measurement uncertainty**
(device-limited). For 8A it is **tare/mass-dominated** (not die-dominated as on 6A) — see below.

| # | Disk wt (mg) | Coating (mg) | Coating load (mg/cm²) | Hard-C load (mg/cm²) |
|---|---|---|---|---|
| 1  | 6.11 | 0.585 | 0.461 ± 0.046 | 0.414 |
| 2  | 6.08 | 0.554 | 0.438 ± 0.046 | 0.393 |
| 3  | 6.04 | 0.514 | 0.406 ± 0.046 | 0.365 |
| 4  | 6.12 | 0.595 | 0.469 ± 0.046 | 0.421 |
| 5  | 6.11 | 0.585 | 0.461 ± 0.046 | 0.414 |
| 6  | 6.09 | 0.564 | 0.446 ± 0.046 | 0.400 |
| 7  | 6.12 | 0.595 | 0.469 ± 0.046 | 0.421 |
| 8  | 6.08 | 0.554 | 0.438 ± 0.046 | 0.393 |
| 9  | 6.08 | 0.554 | 0.438 ± 0.046 | 0.393 |
| 10 | 6.11 | 0.585 | 0.461 ± 0.046 | 0.414 |
| 11 | 6.12 | 0.595 | 0.469 ± 0.046 | 0.421 |
| 12 | 6.12 | 0.595 | 0.469 ± 0.046 | 0.421 |
| 13 | 6.08 | 0.554 | 0.438 ± 0.046 | 0.393 |
| 14 | 6.14 | 0.614 | 0.485 ± 0.046 | 0.435 |
| 15 | 6.14 | 0.614 | 0.485 ± 0.046 | 0.435 |
| 16 | 6.13 | 0.604 | 0.477 ± 0.046 | 0.428 |
| 17 | 6.15 | 0.625 | 0.493 ± 0.046 | 0.443 |
| 18 | 6.09 | 0.564 | 0.446 ± 0.046 | 0.400 |
| 19 | 6.10 | 0.574 | 0.454 ± 0.046 | 0.407 |
| 20 | 6.12 | 0.595 | 0.469 ± 0.046 | 0.421 |
| 21 | 6.11 | 0.585 | 0.461 ± 0.046 | 0.414 |

### Population summary (n = 21)

| Quantity | Mean | SD (spread) | CV | SEM | Min | Max |
|---|---|---|---|---|---|---|
| Coating mass (mg) | 0.581 | 0.026 | 4.5% | 0.006 | 0.514 | 0.625 |
| Coating load (mg/cm²) | **0.459** | 0.020 | 4.5% | 0.004 | 0.406 | 0.493 |
| Hard-carbon load (mg/cm²) | **0.412** | 0.018 | 4.5% | 0.004 | 0.365 | 0.443 |

---

## Uncertainty

Two distinct uncertainties — **do not conflate them**:

**1. Measurement uncertainty (per disk, device-limited): ≈ ±0.046 mg/cm² (±10.1%).**
Propagated as u(load)/load = √[(u(coat)/coat)² + (2·u(d)/d)²], with u(coat) = 0.059 mg.

| Source | Value (1σ) | Contribution to load |
|---|---|---|
| Balance (Mettler Toledo AX205, fine range) | 0.015 mg | in u(coat) |
| Foil tare (measured SD, n=11 blanks) | 0.057 mg | **u(coat)/coat = 10.1% (dominant)** |
| Die diameter (CES cutter) | ±0.05 mm *(assumed)* | 2·0.05/12.70 = 0.79% |

> ⚠️ **Tare-dominated, unlike 6A.** Because the coating (~0.58 mg) is tiny next to the 5.53 mg foil tare,
> the u(coat)/coat term (~10.1%) now **swamps** the die term (0.79%) — the reverse of 6A. The single
> constant tare also hides any **disk-to-disk foil-mass variation**, which here could be comparable to the
> entire ~0.58 mg coating. **Getting a per-disk (or at least better-resolved) foil tare is the highest-value
> fix for 8A**, more so than the die spec.

**2. Disk-to-disk spread (physical): SD = 0.020 mg/cm² (4.5%).**
For 8A this spread (4.5%) is **less than half the measurement uncertainty (10.1%)** — so, unlike 6A (where
spread was ~4× the measurement noise), the disk-to-disk variation here is **not clearly resolvable above
measurement/tare noise**. It cannot be claimed as real coating non-uniformity.

### Consequence for the experiment

- **Absolute loading is weakly constrained** (~0.48 mg/cm², dominated by tare subtraction). The *batch mean*
  is the only well-defined quantity; individual-disk loadings should not be ranked.
- **Very low active mass (~0.43 mg/cm² hard carbon)** → any gravimetric specific capacity will divide by a
  small, uncertain mass, so 8A mAh/g will carry large error bars. Flag when reporting.
- **Na half-cell / Na in excess:** counter electrode is not capacity-limiting, so this affects only the
  **mass normalisation** of the working electrode, not cell balancing.

### Recommendation

- **This 8A coating is likely too thin/low-loaded to be a good working electrode** — cross-check against the
  ~5 µm coating anomaly (prep log flags the extra SBR drop and/or over-fine grind as the suspected cause)
  before committing cells.
- **Label disks at punching next time** (weigh → assign ID → track into the cell) to collapse per-cell mass
  ambiguity and unlock per-cell mAh/g.
- Fill in the real **balance**, **die**, and (critically for 8A) **foil-tare** specs in `Instruments.md`,
  then re-run `disk_loading.py`.

---

## Cell Assembly & Cycling

> ⚠️ **Cycler C-rate basis differs from measured mass.** The cycling program's applied current (C-rate) was
> set from a flat **5.55 mg tare + 91% active-mass assumption**, not the measured values used below
> (**5.5255 mg** tare, measured 2026-07-21, and the per-sample f). The tare side is now nearly exact
> (+0.44%); the **active fraction is the dominant remaining difference**. See `Biona_Academy/Open_Questions.md` for the full note — recompute specific capacity from the
> measured mass, don't back it out from the nominal C-rate.

**1 sodium half-cell assembled 2026-07-16** (CC30) from an 8A disk.

Electrode (total disk) mass recorded at assembly, rounded to 0.1 mg. Active mass = (disk − 5.5255 mg tare) × f,
f = 0.8977. Area 1.2668 cm².

| Cell | Disk mass (mg) | Coating (mg) | **Hard-carbon mass (mg)** | Coating load (mg/cm²) | Hard-C load (mg/cm²) | Status |
|---|---|---|---|---|---|---|
| CC30 | 6.5 | 0.97 | **0.875** | 0.769 | 0.691 | cycling |

> ⚠️ **Field observation (2026-07-16 batch):** on inspection this cell looked unusually thin and appeared
> under-loaded — enough to suspect the hard-carbon coating may have detached/delaminated post-assembly, fate
> unknown. Note the recorded **disk mass (6.5 mg) is actually the heaviest of any 8A disk seen** (punch-table
> range 6.04–6.15 mg, §"Per-disk results" above), so this isn't a mass-record error — the anomaly is
> physical/electrochemical, not in the weighing. Treat this cell's results with caution and flag in any
> cross-cell comparison.
>
> **Na half-cell / Na in excess** → this mass sets only the working-electrode normalisation, not balancing.

**Cycling:** started 2026-07-16, **in progress**. Capacity / rate results — _pending_.
