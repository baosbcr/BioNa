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

## ⚠️ Foil tare conflict: 5.50 vs 5.55 mg — UNRESOLVED, repo currently mixed

- **Two competing values are in use:**
  - **5.50 mg** — recorded in this repo since the 6A punch (2026-07-08), to 0.1 mg on the AX205.
    Used for **every per-disk table and population statistic** in all `*_CoinCell_Disks.md` files, and
    hard-coded as `foil_g=0.0055` in `disk_loading.py`.
  - **5.55 mg** — the supervisor's value, and the basis the **cycler C-rate programs** were built on.
- **Decision 2026-07-21 (João):** go with the **supervisor's 5.55 mg** until confirmation numbers arrive.
  Applied so far to **CC22–CC27 only**; the rest of the repo is still on 5.50 mg → **the repo is currently
  mixed and cross-cell comparisons are not clean.**
- **Impact is small for most samples but NOT for 8A:**
  - Typical disks (coating 15–23 mg): 0.05 mg shift = **~0.3%**, well inside the ±0.8% die-dominated
    measurement uncertainty. Effectively cosmetic.
  - **MMB1_8A (coating ~0.6 mg): 0.05 mg shift = ~8%**, and for CC30 (disk 6.5 mg) the coating goes
    1.00 → 0.95 mg, hard carbon 0.898 → 0.853 mg. 8A is **tare-dominated**, so the tare choice materially
    changes its numbers. Any 8A conclusion must state which tare was used.
- **TODO (resolves this properly):** punch and weigh a **fresh foil blank** — several, for a mean ± spread.
  This is already an open action in the 2C/3C disk logs and would settle it without deferring to either value.
- **TODO:** once settled, recompute *all* disk tables from `disk_loading.py` on the single agreed tare so the
  dataset is internally consistent.

## ⚠️ Cycler C-rate mass basis differs from the measured electrode data (applies to ALL cells, CC19–41)

- **The cycling programs (theoretical-capacity → C-rate current calculation) use a different, flat mass
  basis than the per-cell measured values recorded in the Electrode_Prep_Logs:**
  - **Foil tare: 5.55 mg** on the cycler side vs **5.50 mg** used throughout the disk-loading math here
    (`Instruments.md`, `disk_loading.py`, all "Cell Assembly & Cycling" tables).
  - **Active (hard-carbon) mass fraction: flat 91%** applied to *every* electrode on the cycler side,
    regardless of sample — vs the actual per-sample measured values (**87.7–89.8%**, f = 0.877–0.898,
    see each sample's "Slurry solids composition" table). Reason: João did not have the per-sample f
    data on hand when cycling programs were set up, so a round-number placeholder was used.
- **Consequence:** the cycler's **applied current** (mA) for a given nominal C-rate (e.g. "C/10", "1C")
  was computed from the flat 5.55 mg / 91% assumption — **not** from the true per-cell hard-carbon mass
  in the tables below. The **actual C-rate delivered to each cell differs slightly from the nominal one
  programmed**, and post-hoc **specific capacity (mAh/g) should be (re)computed from the measured
  hard-carbon mass**, not backed out from the nominal C-rate/theoretical capacity used to set the current.
- **TODO:** for each cell, quantify the offset between the assumed capacity basis (5.55 mg tare, 91% f)
  and the measured basis (5.50 mg tare, sample-specific f) so the true delivered C-rate can be corrected
  when reporting rate-capability data.
- Applies to **every cell cycled to date** (CC19–CC21, CC22–CC41).
