# Electrode Prep Log — MMB1_8A

**Sample:** MMB1_8A (800 °C, 180 °C/h)
**BioNa Exp #:** 42
**Covers:** slurry → coating → drying → thickness
**Standard reference:** `Processes/Slurry_Preparation_Standard.md`

---

## Slurry Formulation (as weighed — final batch)

| Step | Component | Target | As weighed | Notes |
|---|---|---|---|---|
| 1 | Water (1st) | 4.9 g | 4.51 g | pipette |
| 2 | CMC | 0.100 g | 0.1002 g | |
| 3 | C45 | 0.167 g | 0.1665 g | |
| 4 | Water (2nd) | 2.5 g | 2.375 g | see evaporation note below |
| 5 | Hard carbon | 3.64 g | 3.6400 g | MMB1_8A |
| 6 | SBR | 5 drops (burner pipette) | 0.1228 g → **+1 drop** | 0.1228 g was too little → added 1 more drop |

All Thinky steps at standard settings (2000 rpm, 10 min).

### Mixing issues (2 restarts before this batch)
- Attempt 1: not well mixed after C45 → **restart**.
- Attempt 2: not well mixed → extra mixing (+4 min, then +3 min) before proceeding.

### Notes on weighing
- **Water evaporation:** visible weight loss when leaving the Thinky Mixer; could not tare the scale.
  Method used: seal container → tare → add water → re-measure with lid → record the increase.
  Evaporative losses are **not** subtracted.
- **SBR dosing — three figures, don't conflate them:**
  - **Old burner pipette:** 5 drops weighed on the scale = **0.1228 g** (bench measurement of per-drop
    loading, ≈0.025 g/drop). Too low → **+1 drop added, not weighed** (so the batch's true SBR mass is
    unknown, ≈0.1228 g + one unmeasured drop).
  - **~0.2 g/drop:** supervisor's off-hand estimate ("should be about 0.2 g") — not measured. It's what
    prompted the move to a rigorous, repeatable method.
  - **200 µL calibrated pipette:** weighed **once** at **0.195 g / 200 µL** — adopted as the standard
    going forward (see `Processes/Slurry_Preparation_Standard.md`). Still to be re-measured several
    times for a mean ± spread.

---

## Coating

| Parameter | Value |
|---|---|
| Doctor blade gap | 100 µm |
| Tape | None |

Coated as **two sheets**:
1. With ruler + ethanol on top → **failed halfway** (blade caught a kink in the foil and got stuck).
2. Without ethanol → OK.

---

## Drying

| Stage | Temp | Duration |
|---|---|---|
| 1 | 30 °C | 12 h *(standard is 6 h — times to be rectified)* |
| 2 | 80 °C | 2 h |

---

## Thickness — as-coated (total = coating + substrate)

> Measured on the **coated, not-yet-calendered** electrode — **calendering still pending** for this
> sample. Readings include the carbon-coated foil substrate (~0.016–0.017 mm). Table-top micrometer.
> *(Raw note says "calendared" — a habitual slip for "coated"; see `_raw/README.md`.)*
> ⚠️ These readings are **~10× thinner** than 6A/10A (~0.02 mm total → only ~5 µm coating). See observations.

**Coating #1**

| Location | Thickness (mm) |
|---|---|
| Top | 0.022 |
| Center | 0.022 |
| Lower-center | 0.022 |
| Bottom | 0.023 |

**Coating #2**

| Location | Thickness (mm) |
|---|---|
| Top | 0.019 |
| Center | 0.024 |
| Bottom | 0.022 |
| Edge 1 | 0.024 |
| Edge 2 | 0.024 |

### Remeasured 18-point grid (2026-07-08)

18 points on **one sheet only** — the second sheet was not gridded as the readings were conclusively
uniform. **6 lengthwise × 3 widthwise**. Lengthwise spacing **2.5 cm** from the top; widthwise = near
each edge + centre of the ~6 cm-wide coating. Columns as recorded: **Left / Centre / Right**. Values in **mm**.

| From top | Left | Centre | Right |
|---|---|---|---|
| 0 cm    | 0.022 | 0.022 | 0.021 |
| 2.5 cm  | 0.022 | 0.023 | 0.022 |
| 5 cm    | 0.022 | 0.022 | 0.022 |
| 7.5 cm  | 0.021 | 0.022 | 0.022 |
| 10 cm   | 0.022 | 0.021 | 0.022 |
| 12.5 cm | 0.022 | 0.023 | 0.022 |

**Summary:** mean 0.022 mm · min 0.021 · max 0.023 · range 0.002 mm (n = 18).
Extremely uniform — coating is essentially at substrate thickness (~5–6 µm of active material).
Heatmap: `images/Electrode_Calendering/MMB1_8A_thickness_heatmap.png`.

---

## Calendering (2026-07-08)

**Both sheets, full — no cut** (sheet 1 gridded: n = 18, mean 0.022 mm, CV 2.5%; sheet 2 confirmed uniform, ungridded).

**Target:** 10% compression (nominal).
**Roll gap set: 0.020 mm** (total spacing), both sheets — 0.90 × 0.022 mm mean. **Done as recommended.**
**Reasoning / caveats:**
- Same 10%-of-total-mean convention as 6A/10A.
- Coating is only ~5–6 µm over a ~16.5 µm incompressible substrate, so 10%-of-total (2 µm) is really ~35–40%
  of the *active* layer; 10%-of-coating (~0.5 µm) is below micrometer resolution.
- Given full spring-back on 10A/6A, expect **no measurable thickness change** — effectively a contact/kiss
  pass; risk of embossing the foil if pressed harder.

**Post-calender thickness:** not gridded — coating too thin (~5 µm) for a 10% change to be measurable, and
exact points can't be relocated.

---

## Observations

- Coating looks terrific — no particles visible by hand (so clean it prompted doubt about whether hard
  carbon was added; **confirmed added**: the container is missing the expected powder mass and the weight
  is logged). Possibly just very finely ground.
- **Suspiciously thin coating (~5 µm)** — hypothesised to be caused by the **extra SBR drop** (and/or the very
  fine grind). Flagged for follow-up.
- Doctor-blade square edges were strikingly clean — traversed both sheets without issue.
- **Blade speed appears critical** and should be standardised. Recommended tests:
  - Success rate of running the blade through the coated foil **with vs without tape** (blade tolerances
    reportedly make the tape's added uncertainty near-negligible).
  - → See `Biona_Academy/Open_Questions.md` (doctor blade / coating table).
