# Electrode Prep Log — MMB1_12A_3C

**Sample:** MMB1_12A_3C (1200 °C, 180 °C/h = 3 °C/min ramp — **standard ramp**; = base MMB1_12A)
**BioNa Exp #:** 48
**Coating date:** 2026-07-09
**Covers:** slurry → coating → drying → thickness → calendering *(stamping next)*
**Standard reference:** `Processes/Slurry_Preparation_Standard.md`

> Prepared in the same session as **MMB1_12A_2C** (2C mixed first, then 3C). See
> `MMB1_12A_2C_Electrode_Prep.md`.
>
> ⚠️ **This is 3C attempt #2 (restart).** Attempt #1 was aborted — hard carbon was forgotten (SBR added
> before HC) — and **repurposed as a commercial-hard-carbon experiment** ("check what happens"). The real
> MMB1_12A_3C hard carbon (**3.64020 g**) was weighed in attempt 1 but never added there, so it is **reused
> in this restart**. Raw of the aborted batch: `_raw/MMB1-12A_3C_attempt1-ABORTED-commercialHC_Slurry_prep.md`.

---

## Slurry Formulation (as weighed)

| Step | Component | Target | As weighed | Notes |
|---|---|---|---|---|
| 1 | Water (1st) | 4.9 g | 4.177 g | pipette; initial reading — **notably low, see note** |
| 2 | CMC | 0.100 g | 0.10003 g | sprinkled across water (still agglomerated — see mixing note) |
| 3 | C45 | 0.167 g | 0.16745 g | boat |
| 4 | Water (2nd) | 2.5 g | 2.5 mL — **not weighed** | pipette; mass deemed unreliable (evaporation) |
| 5 | Hard carbon | 3.64 g | 3.64020 g | MMB1_12A_3C — **weighed in attempt 1, reused** (boat set aside) |
| 6 | SBR | ~0.195 g / 200 µL | 200 µL — **not weighed** | calibrated pipette; mass deemed unreliable (evaporation) |

All Thinky steps at standard settings (2000 rpm, 10 min).

> **Mixing note:** agglomerate(s) after CMC despite sprinkling → **+15 min @ 2000 rpm** before proceeding.
> (Between 1C's +5 min and 2C's +20 min — the sprinkle helped but didn't fully prevent it.)

### Notes on weighing
- **Water (1st) — notably low at 4.177 g** vs 1C (4.5697 g) and 2C (4.591 g) for the same 4.9 mL nominal
  (~0.4 g / ~9 % lower). Likely a short pipette dispense; not corrected. Low consequence — water is the
  solvent and dries off, so this shifts wet viscosity slightly but not the dried electrode composition.
- **Water (2nd) and SBR not weighed** — pipette; masses deemed unreliable (evaporation), as on 1C/2C.
- **Solids (CMC, C45, hard carbon) weighed in boats** — boat-retention caveat applies (see standard).

---

## Coating

| Parameter | Value |
|---|---|
| Doctor blade gap | 100 µm |
| Tape | **Yes** → est. +35 µm added to gap (~135 µm effective), as on 1C/2C |
| Sheets | **One** |

> **Taped run** — subtract ~35 µm from the coating layer when comparing thickness against untaped samples.

---

## Drying

| Stage | Temp | Duration | Status |
|---|---|---|---|
| 1 | 30 °C | 12 h | **In progress** — started 2026-07-09 |
| 2 | 80 °C | 2 h | Pending |

> Dried together with the 2C and Kuranode coatings in the same oven run.

---

## Thickness — as-coated (total = coating + substrate)

> Measured 2026-07-14 after drying. Table-top micrometer (Mahr MarCator 1075 R). Readings include the
> carbon-coated foil substrate (~0.016–0.017 mm). **One sheet**, gridded **6 lengthwise × 3 widthwise =
> 18 points**, rows **3 cm apart** over **150 mm usable length**. Columns as recorded: **Left / Centre /
> Right**. Values in **mm**.
>
> ⚠️ **Taped-blade run (+~35 µm):** subtract ~0.035 mm from the coating before cross-sample coating
> comparisons (irrelevant to the calender gap). Substrate ~0.0165 mm separate.
>
> ⚠️ **Visible wave** ran across the **9 cm row** and happened to coincide with the measurement line — those
> three readings (0.614 / 0.640 / 0.595) reflect real coating **waviness/topography**, not gauge artefacts.

| From top | Left | Centre | Right |
|---|---|---|---|
| 0 cm  | 0.704 | 0.400 | 0.406 |
| 3 cm  | 0.285 | 0.280 | 0.209 |
| 6 cm  | 0.562 | 0.439 | 0.284 |
| 9 cm  | 0.614 | 0.640 | 0.595 |
| 12 cm | 0.455 | 0.472 | 0.509 |
| 15 cm | 0.596 | 0.659 | 0.476 |

**Summary:** **median 0.474** · mean 0.477 · std 0.146 · CV 30.7% · min 0.209 · max 0.704 (n = 18).

> **Thickest coating in the series** — median 0.474 mm total vs ~0.25–0.31 for 1C/2C (same taped, standard-order
> process). Coating (median − substrate) ≈ 0.458 mm; adjusted for the ~35 µm blade tape, untaped-equivalent
> ≈ 0.42 mm. The high scatter (CV 31%) is a mix of the 9 cm wave and general heavy-coat non-uniformity.

---

## Calendering (2026-07-14)

**Target:** 10% compression on the **median** total thickness (same basis as 1C/2C, and Kuranode).

| Sheet | Median total | Roll gap set |
|---|---|---|
| 1 (only) | 0.474 mm | **0.43 mm** |

Gap = 0.90 × 0.474 = 0.427 → **0.43 mm**.

### Outcome — mostly spring-back, high spots took a set

Sheet looks **mostly unaffected** — **near-full spring-back to ~0% permanent compression**, same tendency as
10A and 1C. The **exceptions are the high spots** (incl. the 9 cm wave / proud regions), which **were flattened**
where they exceeded the 0.43 mm gap. **No delamination** — the coating stayed well adhered (contrast Kuranode's
band-aid peel-off; this is a standard-order biochar build). Consistent with the recurring lesson: to actually
reach 10% on these biochar coatings, set the gap **tighter than 10%-of-median** and/or use **multiple stepped
passes**.

**Post-calender thickness:** not gridded (points can't be relocated 1:1); the flattened high spots are visual.

---

## Observations

- **Thickest coating in the biochar series** (median 0.474 mm total) — a genuinely heavy layer, plus a
  **visible wave** across the 9 cm row.
- **Calendered well, held together** (no delamination), but **near-full spring-back** at the 0.43 mm gap —
  only the high spots / wave took a permanent set. Same rebound tendency as 10A/1C.
