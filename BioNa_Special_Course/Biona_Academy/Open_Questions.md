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

## Missing coin-cell electrode weights (first 6 cells: 12A_2C ×3 + 12A_3C ×3)

- **TODO:** hard-carbon electrode (disk) weights for the **first 6 cells built and put on cycling**
  — three MMB1_12A_2C + three MMB1_12A_3C, assembled/cycling **before** the MMB1_10A batch (whose
  cells carry the first recorded weights: 18.9, 18.4 mg) — are still missing.
- **Source:** supervisor has these values; pending hand-off to João.
- Once received, add them to the "Cell Assembly & Cycling" section of `MMB1_12A_2C_CoinCell_Disks.md`
  and `MMB1_12A_3C_CoinCell_Disks.md`, following the format established for 12A_1C (CC19-21).

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
