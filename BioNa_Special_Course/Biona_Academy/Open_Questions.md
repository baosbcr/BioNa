# Open Questions & TODOs

Running list. When resolved, promote the answer into the relevant `Processes/` or `Instruments/`
doc and remove it here.

---

## Thickness measurement / micrometer

- **Substrate baseline:** the carbon-coated Al foil (current collector) is **~0.016–0.017 mm**
  (≈16–17 µm) on the table-top micrometer.
- **All reported coating thicknesses are TOTAL** (coating + substrate). To get coating-only,
  subtract ~0.017 mm.
- Make/model + uncertainty resolved in `Instruments/Instruments.md`: Mahr MarCator 1075 R **digital**
  indicator (order no. 4336030) + 820 NG/FG stand; manufacturer span of error **±0.005 mm (5 µm)**.
- **Offer:** more coating measurements can be taken on request.

## SBR dosing & weighing

- **Re-measure the 200 µL pipette SBR loading** — currently weighed only once (0.195 g). Repeat
  several times for a mean ± spread before treating 0.195 g as the reference.
- **Quantify warm-slurry evaporation** — slurry exits the Thinky Mixer warm; water loss biases the
  recorded SBR (and other) masses. Weigh sealed where possible; quantify the typical loss.

## Calendering standardisation

- **Open decision:** define a target for calendering — either a fixed **compression ratio**, or a
  fixed **final thickness** to which *all* samples are calendered.
- **Leaning:** standardise as much upstream as possible so every sample enters calendering at a
  similar coating thickness, then calender all to the same target thickness.
- **TODO:** determine the appropriate compression rate / target and record it in
  `Processes/Calendering_Notes.md` + `Instruments/Instruments.md`.

## Doctor blade / coating table

- **TODO:** identify and spec the **doctor blade** and the **coating table / film applicator**; add
  both to `Instruments/Instruments.md` and pick standard values to use henceforth.
- **Standardise blade speed** — observed to be critical to coating quality (see MMB1_8A log).
- **Test: tape vs no tape** — success rate of running the blade through the coated foil with vs
  without tape. Blade tolerances reportedly make the tape's added uncertainty near-negligible;
  confirm experimentally.
- Recurring failure mode: square edges of the blade catch particles/kinks and leave a **growing
  triangular scratch pattern** (seen on 6A and 10A).

## ~~Missing coin-cell electrode weights (first 6 cells: 12A_2C ×3 + 12A_3C ×3)~~ — RESOLVED 2026-07-21

- Disk weights for the **first 6 cells built and put on cycling** (CC22–CC27) received from supervisor
  and entered in `MMB1_12A_2C_CoinCell_Disks.md` (CC22–24) and `MMB1_12A_3C_CoinCell_Disks.md` (CC25–27):

  | Cell | Sample | Disk mass (mg) |
  |---|---|---|
  | CC22 | 12A_2C | 20.8 |
  | CC23 | 12A_2C | 24.1 |
  | CC24 | 12A_2C | 20.2 |
  | CC25 | 12A_3C | 28.2 |
  | CC26 | 12A_3C | 28.2 |
  | CC27 | 12A_3C | 26.9 |

- **Assumptions applied:** **5.55 mg foil tare** (supervisor's value, adopted 2026-07-21 — see the tare
  conflict item below), sample-specific f (0.8874 / 0.8873), area 1.2668 cm². Values are to 0.1 mg, vs
  0.01 mg for the punch-day sets.
- ⚠️ **Follow-up:** the three 12A_2C cells all fall at or below the punch-population range (20.75–25.75 mg)
  and below both sheet means — see the note in `MMB1_12A_2C_CoinCell_Disks.md`. Worth confirming the
  supervisor's balance/tare basis before comparing CC22–24 against CC37/CC38 as one population.
- The cell→value mapping assumes the six numbers were given in **CC22→CC27 order**; the 3C values fitting
  the 3C range and the 2C values the 2C range supports this, but confirm if any result looks off.

## Cycling / electrochemical-testing instruments (Biologic + second cycler)

- **TODO:** make/model for both cyclers used for coin-cell galvanostatic cycling and electrochemical
  characterisation: a **Biologic** potentiostat/cycler, and a second instrument (name TBC — sounds
  like "Kuwara"/"Kuwahara"? — confirm spelling).
- **TODO:** the specific programs/protocols run on each (e.g. **OCV**, **PEIS**, **GCPL**/GSCD-type
  galvanostatic cycling) and their settings (voltage windows, rates, rest times, etc.).
- **Source:** pending from João.
- Once received, add both instruments to `Instruments/Instruments.md` (there are already TBD stubs
  for "Battery Cycler / Potentiostat" and "Coin-Cell Crimper / Press") and document the standard
  cycling protocol in a new `Processes/` doc (analogous to `RamanSesh.md`).

## Coin-cell assembly SOP

- **TODO:** document the full coin-cell assembly process — stacking order, electrolyte type/volume,
  separator, Na counter-electrode prep, crimping pressure/settings — in a new `Processes/` doc.
- **Source:** João to detail.

## MMB2_13A reference sample — composition/tare unknown

- **TODO:** confirm the slurry/coating composition (hard-carbon mass fraction f) and current-collector
  foil tare used by the supervisor for the MMB2_13A pre-cut reference electrode (CC41). Without these,
  its coating/hard-carbon load cannot be computed — see
  `Processes/Electrode_Prep_Logs/MMB2_13A_CoinCell_Disks.md`.

## ⚠️ Foil tare: switched 5.50 → 5.55 mg repo-wide (2026-07-21) — value still UNCONFIRMED

- **What changed.** The whole dataset was recomputed on the **supervisor's 5.55 mg** foil tare on
  **2026-07-21**, on João's instruction, replacing the 5.50 mg recorded here since the 6A punch
  (2026-07-08). Every per-disk table, population summary, cell-assembly table and cross-sample comparison
  in all `*_CoinCell_Disks.md` files was regenerated; `disk_loading.py` now carries the value once as
  `FOIL_TARE_G = 0.00555`. **The repo is internally consistent — one tare everywhere.**
- **The value itself is still not confirmed.** 5.50 mg was a reading recorded to 0.1 mg on the AX205;
  5.55 mg is the supervisor's number and the basis the cycler C-rate programs were built on. Neither has
  been verified against a freshly weighed blank.
- **Effect of the switch (loadings all shifted DOWN slightly):**

  | Sample | Hard-C load before → after (mg/cm²) |
  |---|---|
  | 6A | 7.53 → 7.50 |
  | 8A | 0.430 → **0.394** |
  | 10A | 10.28 → 10.25 |
  | 12A_1C | 10.75 → 10.72 |
  | 12A_2C sheet 1 / 2 | 12.53 → 12.49 / 12.12 → 12.08 |
  | 12A_3C standard / thick | 16.92 → 16.89 / 20.38 → 20.34 |
  | Kuranode | 6.26 → 6.23 |

- **Negligible for every sample except 8A.** For normal coatings (9–29 mg) the 0.05 mg shift is ~0.2–0.4%,
  well inside the ±0.8% die-dominated measurement uncertainty. **8A's coating is only ~0.55 mg**, so the
  same shift moved it **~8%** (0.430 → 0.394 mg/cm² hard carbon; CC30's hard-carbon mass 0.898 → 0.853 mg).
  8A is **tare-dominated** — its per-disk measurement uncertainty rose 5.6% → **6.1%**, which now **exceeds
  its 4.7% disk-to-disk spread**, so 8A's spread is no longer resolvable above tare noise. **Any 8A
  conclusion must state the tare used.**
- **TODO (settles this properly):** punch and weigh **several fresh foil blanks** for a mean ± spread,
  rather than deferring to either number. Highest value for 8A and Kuranode (thinnest coatings).
- **To change the tare again:** edit `FOIL_TARE_G` in `disk_loading.py` and regenerate every table — it is
  the single input that moves every published loading in the project.

## ⚠️ Cycler C-rate mass basis differs from the measured electrode data (applies to ALL cells, CC19–41)

- **The cycling programs (theoretical-capacity → C-rate current calculation) use a different, flat mass
  basis than the per-cell measured values recorded in the Electrode_Prep_Logs:**
  - ~~**Foil tare: 5.55 vs 5.50 mg**~~ — **no longer a difference.** The repo adopted the cycler's
    5.55 mg on 2026-07-21 (see the tare item above), so both sides now use the same tare.
  - **Active (hard-carbon) mass fraction: flat 91%** applied to *every* electrode on the cycler side,
    regardless of sample — vs the actual per-sample measured values (**87.7–89.8%**, f = 0.877–0.898,
    see each sample's "Slurry solids composition" table). Reason: João did not have the per-sample f
    data on hand when cycling programs were set up, so a round-number placeholder was used.
- **Consequence:** the cycler's **applied current** (mA) for a given nominal C-rate (e.g. "C/10", "1C")
  was computed from the flat 91% assumption — **not** from the true per-cell hard-carbon mass
  in the tables below. The **actual C-rate delivered to each cell differs slightly from the nominal one
  programmed**, and post-hoc **specific capacity (mAh/g) should be (re)computed from the measured
  hard-carbon mass**, not backed out from the nominal C-rate/theoretical capacity used to set the current.
- **TODO:** for each cell, quantify the offset between the assumed 91% f and the measured per-sample f
  (0.882–0.898) so the true delivered C-rate can be corrected when reporting rate-capability data. The
  offset is now **f-only** (~1.3–3.2% relative), since the tare halves agree.
- Applies to **every cell cycled to date** (CC19–CC21, CC22–CC41).
