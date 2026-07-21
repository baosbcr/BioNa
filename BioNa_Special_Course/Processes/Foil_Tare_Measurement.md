# Foil Tare Measurement — carbon-coated Al current collector

**Date:** 2026-07-21
**Operator:** João Côrte-Real
**Purpose:** measure the **foil tare** — the mass of a punched current-collector disk carrying no slurry —
which is subtracted from every electrode disk mass in the project to get coating mass.
**Balance:** Mettler Toledo AX205, fine range (readability 0.01 mg)
**Die:** **the same 12.7 mm Ø (½″) cutting die used for every electrode disk in this project** → area 1.2668 cm²
**Sample:** 11 blanks of carbon-coated Al foil (conductive-C layer, no slurry)

> **Why this matters:** the tare is the single input that shifts *every* published loading in the project.
> Before this measurement it was an **assumption** (5.50 mg recorded on the 6A punch day, vs the supervisor's
> 5.55 mg used to set the cycler C-rates) — see `Biona_Academy/Open_Questions.md`.
>
> **Same-die detail is what makes this valid.** A tare cut with a different die would carry a different
> area and be the wrong mass to subtract. These blanks match the electrode disks exactly.

---

## Method — cumulative weighing

Blanks were weighed **cumulatively** (weigh a batch, add one, reweigh, add one, reweigh) rather than
individually. This gives a very precise *mean* but only weak information on disk-to-disk *spread*.

| Step | Disks on pan | Cumulative mass (g) | Cumulative (mg) |
|---|---|---|---|
| 1 | **9** *(see correction below)* | 0.04960 | 49.60 |
| 2 | 10 | 0.05523 | 55.23 |
| 3 | 11 | 0.06078 | 60.78 |

---

## ⚠️ Count correction: the first weighing was **9 disks, not 10**

The first batch was believed to be 10 disks at the bench. It was **9**. Recorded here because the raw
numbers only reconcile under the corrected count.

**Evidence.** Steps 2 and 3 each added exactly one disk, so their differences are **direct single-disk
masses**, independent of any count:

- disk #10 = 55.23 − 49.60 = **5.63 mg**
- disk #11 = 60.78 − 55.23 = **5.55 mg**

Testing both counts against those two directly-measured disks:

| First batch assumed | Per-disk from the three totals | Verdict |
|---|---|---|
| 10 disks | 4.960 → 5.021 → 5.065 mg | first batch would be **11% lighter** than two disks from the same punch — impossible |
| **9 disks** | **5.511 → 5.523 → 5.5255 mg** | agrees with the singles to **1.4%** ✅ |

Two independent signatures confirm it:

1. **Magnitude.** Under the 10-count the first ten disks average 4.96 mg while two disks from the same
   batch weigh ~5.6 mg. Punched disks do not vary by 11%.
2. **Drift direction.** Under the 10-count the running mean *climbs* monotonically (4.960 → 5.021 → 5.065)
   — the classic signature of an **undercounted first weighing**, where each added disk drags the mean
   toward the truth. Under the 9-count it is flat and converged (5.511 → 5.523 → 5.5255, drift +0.3%).

> **Lesson for next time:** weigh blanks **individually**, or at minimum count onto the pan twice. The
> cumulative method only survived here because the two single-disk increments happened to pin down the
> per-disk mass independently of the count.

---

## Result

| Quantity | Value |
|---|---|
| **Foil tare (mean, n = 11)** | **5.5255 mg** (0.0055255 g) |
| Disk-to-disk SD | **0.057 mg (1.0%)** — *weak: 1 dof, see caveat* |
| Balance contribution | 0.01 mg resolution → **0.0003 mg** on the mean (negligible) |
| Individually resolved disks | 5.63, 5.55 mg |

**Both previous assumptions were within 0.5%, and the truth sits almost exactly between them:**

| Value | vs measured |
|---|---|
| 5.50 mg (old repo value, 6A punch day) | −0.46% |
| 5.55 mg (supervisor / cycler basis) | +0.44% |
| **5.5255 mg (measured)** | — |

> ⚠️ **The SD is the weak part, not the mean.** Only 2 of the 11 blanks were resolved individually, so the
> 0.057 mg disk-to-disk SD rests on **1 degree of freedom**. The *mean* is solid (11 disks, 0.01 mg balance);
> the *spread* is a rough estimate. It is nonetheless **larger than the 0.029 mg resolution-based placeholder
> it replaced**, so the old figure was understating per-disk uncertainty.

---

## Consequences for the dataset

Adopted repo-wide on 2026-07-21: `FOIL_TARE_G = 0.0055255` in `Processes/Electrode_Prep_Logs/disk_loading.py`,
with all `*_CoinCell_Disks.md` tables regenerated from it.

**1. Loadings barely moved** (tare fell 0.025 mg vs the 5.55 mg interim basis, so loadings rose ~0.2%):

| Sample | Hard-C load (mg/cm²) |
|---|---|
| 6A | 7.51 |
| 8A | **0.412** |
| 10A | 10.27 |
| 12A_1C | 10.74 |
| 12A_2C sheet 1 / 2 | 12.51 / 12.10 |
| 12A_3C standard / thick | 16.90 / 20.36 |
| Kuranode | 6.25 |

**2. Per-disk uncertainty rose, because the measured spread beat the old placeholder.**
u(coat) = √(0.015² + 0.057²) = **0.059 mg**, up from 0.034 mg. Effect by sample:

- **Thick coatings (6A, 10A, 1C, 2C, 3C):** u(load) 0.80–0.85% → **0.81–0.96%**. Still **die-dominated**
  (the assumed ±0.05 mm die tolerance, 0.79%, remains the largest single term).
- **Kuranode:** 0.87% → **1.02%**.
- **MMB1_8A: 6.1% → 10.1%.** Its coating is only ~0.58 mg — a *tenth* of the foil tare — so tare uncertainty
  dominates completely. **8A's 4.5% disk-to-disk spread is now less than half its 10.1% measurement
  uncertainty**, meaning 8A's disk-to-disk variation **cannot be claimed as real coating non-uniformity**.
  This is a measurement-limited sample, and it is the one being re-made (see
  `Processes/Electrode_Prep_Logs/_raw/MMB1-8A_attempt2_Slurry_prep.md`, BioNa Experiment 58).

---

## Follow-ups

- [ ] **Weigh the 11 blanks individually** — cheap, and converts the 1-dof SD into a proper n=11 spread.
      Highest value for **8A and Kuranode**, the two thinnest coatings.
- [ ] **Confirm the die tolerance** with the CES cutter spec. Now that the tare is measured, the assumed
      ±0.05 mm die diameter is the dominant uncertainty for every sample except 8A.
- [ ] Consider whether foil tare varies **roll to roll** — these blanks came from one foil source; older
      electrodes (6A, 8A) were coated earlier and may not be from the same roll.
