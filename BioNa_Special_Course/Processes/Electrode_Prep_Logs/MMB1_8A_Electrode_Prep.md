# Electrode Prep Log — MMB1_8A

**Sample:** MMB1_8A (800 °C, 180 °C/h)
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
| 6 | SBR | 5 drops | 0.1228 g → **+1 drop** | 0.1228 g was too low; +1 drop (≈0.195 g/drop) |

All Thinky steps at standard settings (2000 rpm, 10 min).

### Mixing issues (2 restarts before this batch)
- Attempt 1: not well mixed after C45 → **restart**.
- Attempt 2: not well mixed → extra mixing (+4 min, then +3 min) before proceeding.

### Notes on weighing
- **Water evaporation:** visible weight loss when leaving the Thinky Mixer; could not tare the scale.
  Method used: seal container → tare → add water → re-measure with lid → record the increase.
  Evaporative losses are **not** subtracted.
- **SBR drop mass (measured experimentally):** 1 drop from the 200 µL pipette ≈ **0.195 g**.

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

## Thickness (total = coating + substrate)

> All readings include the carbon-coated foil substrate (~0.016–0.017 mm). Table-top micrometer.
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
