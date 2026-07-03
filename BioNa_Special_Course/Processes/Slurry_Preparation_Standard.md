
# Standard Slurry Preparation — Hard Carbon Anode

**Equipment:** Thinky Mixer ARE-250

---

## Formulation

| Component | Role | Mass (g) | wt% (dry basis) |
|---|---|---|---|
| Water | Solvent | 7.4 (split: 4.9 + 2.5) | — |
| Hard Carbon | Active material | 3.64 | ~93.1% |
| Carbon Black C45 | Conductive additive | 0.167 | ~4.3% |
| CMC | Binder | 0.1 | ~2.6% |
| SBR | Binder | 200 µL ≈ 0.195 g (**weigh each batch**) | TBD |

> Total dry mass (excl. SBR): ~3.91 g

---

## Procedure

All Thinky steps: **2000 rpm, 10 min**

| Step | Action |
|---|---|
| 1 | Add **4.9 g water** to Thinky container |
| 2 | Add **0.1 g CMC** |
| 3 | Mix — 2000 rpm, 10 min |
| 4 | Add **0.167 g C45** |
| 5 | Mix — 2000 rpm, 10 min |
| 6 | Add **2.5 g water** |
| 7 | Mix — 2000 rpm, 10 min |
| 8 | Add **3.64 g hard carbon** |
| 9 | Mix — 2000 rpm, 10 min |
| 10 | **Shake SBR before use.** Dispense **200 µL** with a calibrated pipette (≈0.195 g) — **record mass each batch** |
| 11 | Mix — 2000 rpm, 10 min |

> **SBR dosing:** switched from "5 drops" (imprecise) to a **200 µL calibrated pipette** for rigour.
> The 200 µL delivery has been weighed **only once** (0.195 g). **TODO: weigh it several times** to get
> a mean ± spread before treating 0.195 g as the reference value.
> See `Processes/Electrode_Prep_Logs/MMB1_8A_Electrode_Prep.md`.
>
> ⚠️ **Warm-slurry evaporation:** slurry exits the Thinky Mixer warm and loses water fast enough to
> shift scale readings noticeably. The SBR (and other) masses recorded per batch are therefore
> **biased low / noisy**. Weigh in a **sealed container** where possible (seal → tare → add → remeasure
> with lid), and treat recorded masses as approximate. Quantifying this loss is a **TODO**.

---

## Drying Protocol

| Stage | Temperature | Duration | Atmosphere |
|---|---|---|---|
| 1 | 30 °C | 6 h | Air |
| 2 | 80 °C | 2 h | Air |

---

## Pre-Slurry: Grinding

Hard carbon powder must be ground to a fine particle size before slurry preparation.  
Insufficient grinding → particle size too large → calendering failure.  
See `Processes/Calendering_Notes.md` for failure log and calendering settings.
