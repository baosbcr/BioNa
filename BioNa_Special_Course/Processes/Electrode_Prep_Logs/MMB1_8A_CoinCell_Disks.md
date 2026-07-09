# Coin-Cell Disk Log — MMB1_8A

**Sample:** MMB1_8A (800 °C, 180 °C/h) — calendered electrode (see `MMB1_8A_Electrode_Prep.md`)
**Date:** 2026-07-09
**Purpose:** working electrodes for **sodium half-cells** (Na counter, Na always in excess)
**Disks punched:** 21 · **Cutting die:** 12.7 mm Ø (½″) → **area 1.2668 cm²**
**Foil tare (carbon-coated foil, conductive-C layer, no slurry):** 0.0055 g (5.50 mg)
**Compute script:** `Processes/Electrode_Prep_Logs/disk_loading.py`

> **21 disks (one extra cut).** Some may be discarded later as outliers (as anticipated for 12A).
> Disks are **unlabeled and indistinguishable** — masses are known as a *set*; a given mass cannot be
> matched back to the disk built into a given cell (same as 6A). See "Uncertainty".

> ⚠️ **Read this before using these loadings.** 8A's coating is **anomalously thin** (~0.6 mg/disk,
> ~0.48 mg/cm² — about **18× lighter than 6A's 8.48 mg/cm²**), consistent with the ~5 µm as-coated
> thickness flagged in the prep log. The coating is only ~**11 % of the 5.50 mg foil tare**, so every
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
| 1  | 6.11 | 0.610 | 0.482 ± 0.027 | 0.432 |
| 2  | 6.08 | 0.580 | 0.458 ± 0.027 | 0.411 |
| 3  | 6.04 | 0.540 | 0.426 ± 0.027 | 0.383 |
| 4  | 6.12 | 0.620 | 0.489 ± 0.027 | 0.439 |
| 5  | 6.11 | 0.610 | 0.482 ± 0.027 | 0.432 |
| 6  | 6.09 | 0.590 | 0.466 ± 0.027 | 0.418 |
| 7  | 6.12 | 0.620 | 0.489 ± 0.027 | 0.439 |
| 8  | 6.08 | 0.580 | 0.458 ± 0.027 | 0.411 |
| 9  | 6.08 | 0.580 | 0.458 ± 0.027 | 0.411 |
| 10 | 6.11 | 0.610 | 0.482 ± 0.027 | 0.432 |
| 11 | 6.12 | 0.620 | 0.489 ± 0.027 | 0.439 |
| 12 | 6.12 | 0.620 | 0.489 ± 0.027 | 0.439 |
| 13 | 6.08 | 0.580 | 0.458 ± 0.027 | 0.411 |
| 14 | 6.14 | 0.640 | 0.505 ± 0.027 | 0.454 |
| 15 | 6.14 | 0.640 | 0.505 ± 0.027 | 0.454 |
| 16 | 6.13 | 0.630 | 0.497 ± 0.027 | 0.446 |
| 17 | 6.15 | 0.650 | 0.513 ± 0.027 | 0.461 |
| 18 | 6.09 | 0.590 | 0.466 ± 0.027 | 0.418 |
| 19 | 6.10 | 0.600 | 0.474 ± 0.027 | 0.425 |
| 20 | 6.12 | 0.620 | 0.489 ± 0.027 | 0.439 |
| 21 | 6.11 | 0.610 | 0.482 ± 0.027 | 0.432 |

### Population summary (n = 21)

| Quantity | Mean | SD (spread) | CV | SEM | Min | Max |
|---|---|---|---|---|---|---|
| Coating mass (mg) | 0.607 | 0.026 | 4.3% | 0.006 | 0.540 | 0.650 |
| Coating load (mg/cm²) | **0.479** | 0.020 | 4.3% | 0.004 | 0.426 | 0.513 |
| Hard-carbon load (mg/cm²) | **0.430** | 0.018 | 4.3% | 0.004 | 0.383 | 0.461 |

---

## Uncertainty

Two distinct uncertainties — **do not conflate them**:

**1. Measurement uncertainty (per disk, device-limited): ≈ ±0.027 mg/cm² (±5.6%).**
Propagated as u(load)/load = √[(u(coat)/coat)² + (2·u(d)/d)²], with u(coat) = 0.034 mg.

| Source | Value (1σ) | Contribution to load |
|---|---|---|
| Balance (Mettler Toledo AX205, fine range) | 0.015 mg | in u(coat) |
| Foil tare (recorded to 0.1 mg) | 0.029 mg | **u(coat)/coat = 5.5% (dominant)** |
| Die diameter (CES cutter) | ±0.05 mm *(assumed)* | 2·0.05/12.70 = 0.79% |

> ⚠️ **Tare-dominated, unlike 6A.** Because the coating (~0.6 mg) is tiny next to the 5.50 mg foil tare,
> the u(coat)/coat term (~5.5%) now **swamps** the die term (0.79%) — the reverse of 6A. The single
> constant tare also hides any **disk-to-disk foil-mass variation**, which here could be comparable to the
> entire ~0.6 mg coating. **Getting a per-disk (or at least better-resolved) foil tare is the highest-value
> fix for 8A**, more so than the die spec.

**2. Disk-to-disk spread (physical): SD = 0.020 mg/cm² (4.3%).**
For 8A this spread (4.3%) is **comparable to the measurement uncertainty (5.6%)** — so, unlike 6A (where
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
