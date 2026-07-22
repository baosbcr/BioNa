
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

## Technique Notes & Best Practices

### CMC addition — disperse, don't dump
**Spread the CMC evenly across the water surface; never let it sit as a clump.** Undispersed CMC is the
main cause of agglomerates that survive many Thinky cycles — once a lump forms, its dry core is slow to
wet and can persist through repeated mixing (2C: a single persistent agglomerate needed **4 × 5 min = +20 min**
extra to break down). Sprinkling CMC across the water rather than dropping it in one spot is the key
preventive step. Progressive **warming** during repeated mixing does help dissolution, but it's a remedy,
not a substitute for good initial dispersion.

### Weighing substances & the evaporation problem — weighing "boats"
- **Water (solvent):** evaporates on the open scale even at ambient temperature, so the reading drifts down
  while weighing. This is **acceptable** — the water is meant to dry off during the drying step anyway, and the
  small evaporative loss has **negligible effect on slurry viscosity at coating time**. Record the **initial
  (peak) reading** and do **not** subtract evaporation.
- **SBR (and other retained components):** different story — SBR **stays in the electrode**, so a dosing/
  evaporation error there shifts the final composition. Dose precisely (200 µL calibrated pipette) and treat
  the recorded mass as approximate, not the water-style "peak reading."
- **Why boats:** because evaporation makes in-situ weighing on the mixing container unreliable, solids are
  weighed in **weighing boats** before addition.
  - ⚠️ **Boat-retention caveat:** trace material clings to the boat (static + fine powder), so the mass actually
    delivered is **slightly less than weighed**. No fix decided yet, but this loss is expected to be **roughly
    deterministic/repeatable** — for a given material, static state and particle size, a similar trace fraction
    stays behind each time, making it a **consistent (if unquantified) bias**, not random noise.
  - ~~**TODO:** quantify boat retention (weigh boat before/after transfer) if precision ever demands it.~~
    **CLOSED UNRESOLVED (2026-07-22).** The last slurry of the campaign (MMB1_8A batch #2, Exp 58) was made
    without reweighing the boat, and no further batches will be produced. Boat retention is therefore
    **never quantified for any sample in this study**. All recorded hard-carbon masses are **upper bounds**
    on the mass actually delivered; true active wt% sits slightly below the value stated in each prep log.
    Carry this into the report as a **stated limitation**. The usual defence — that a ~constant retained
    *fraction* is a ~constant wt% offset and so cancels in cross-sample comparison — holds **only if
    retention is independent of pyrolysis temperature**. It may not be: retention is set by particle size
    and static, and higher-temperature chars are harder and grind differently (see the grinding note
    below). A temperature-dependent retention would bias the *trend*, not just the absolute values.
    Scale for reference: 1% retention ≈ 1% underestimate of gravimetric capacity.

### Gloves & contamination — TODO: formalise a glove procedure
White gloves are worn to **protect the sample**, but they visibly pick up carbon (C45 / hard carbon) — black
dust is clearly transferred. Standard lab practice (**swap gloves frequently**) still applies here: change
gloves **as often as practical** to avoid cross-contaminating samples, surfaces and instruments with carbon.
**TODO:** write a proper glove / contamination-control procedure for electrode prep.

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
