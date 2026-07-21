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

- **Basis applied:** **5.5255 mg measured foil tare** (see the tare item below), sample-specific f
  (0.8874 / 0.8873), area 1.2668 cm². Values are to 0.1 mg, vs 0.01 mg for the punch-day sets.
- ⚠️ **Follow-up:** the three 12A_2C cells all fall at or below the punch-population range (20.75–25.75 mg)
  and below both sheet means — see the note in `MMB1_12A_2C_CoinCell_Disks.md`. Worth confirming the
  supervisor's balance/tare basis before comparing CC22–24 against CC37/CC38 as one population.
- The cell→value mapping assumes the six numbers were given in **CC22→CC27 order**; the 3C values fitting
  the 3C range and the 2C values the 2C range supports this, but confirm if any result looks off.

## Cycling / electrochemical-testing instruments — ~~identification~~ RESOLVED 2026-07-21; protocols still open

- ~~**Make/model of both cyclers**~~ — **DONE.** Both are **Bio-Logic SAS**, on one PC / one EC-Lab
  session: **VMP3 (s/n 0509)** and **MPG-2 (s/n 0124)**, software **EC-Lab V11.62**. Full specs in
  `Instruments/Instruments.md`; photos in `images/Cycling/`.
- ✅ **Resolved: there are THREE cyclers, not two.** Alongside the two Bio-Logic units there is a
  **Neware BTS** system (DevType 27, device 79, 5 V / ±100 mA channels) on its own PC — this is what the
  "Kuwara"/"Kuwahara" note was pointing at. Identifiers in `Instruments/Instruments.md`.
- **TODO:** the Neware **model name** is not stored in the export (Neware writes a numeric DevType).
  João to read it off the chassis plate / BTS Client → *Device info* (2026-07-21).
- ⚠️ **TODO (affects existing data): record which instrument + channel each cell ran on.** CC19–CC41
  carry no assignment, and the dataset now spans **three** cyclers. Recoverable from the raw files:
  EC-Lab filenames carry the channel (`..._C01`, `_C02`, …) and Neware filenames encode
  `<DevType><DevID>-<unit>-<channel>-<testID>` (e.g. `270079-4-6-151` → device 79, unit 4, ch 6).
  Known so far: **CC39, CC40 → Neware** (unit 4, ch 6/7).
- **TODO (still open):** the specific programs/protocols run on each (e.g. **OCV**, **PEIS**,
  **GCPL**/GSCD-type galvanostatic cycling) and their settings (voltage windows, rates, rest times).
  Document in a new `Processes/` doc, analogous to `RamanSesh.md`.
- **TODO (still open):** the **Coin-Cell Crimper / Press** stub in `Instruments/Instruments.md`.

## Coin-cell assembly SOP

- **TODO:** document the full coin-cell assembly process — stacking order, electrolyte type/volume,
  separator, Na counter-electrode prep, crimping pressure/settings — in a new `Processes/` doc.
- **Source:** João to detail.

## MMB2_13A reference sample — composition/tare unknown

- **TODO:** confirm the slurry/coating composition (hard-carbon mass fraction f) and current-collector
  foil tare used by the supervisor for the MMB2_13A pre-cut reference electrode (CC41). Without these,
  its coating/hard-carbon load cannot be computed — see
  `Processes/Electrode_Prep_Logs/MMB2_13A_CoinCell_Disks.md`.

## ~~Foil tare: 5.50 vs 5.55 mg~~ — **RESOLVED 2026-07-21 by measurement**

- **Measured: 5.5255 mg** (mean of 11 carbon-coated foil blanks cut with the **same 12.7 mm die** as every
  electrode disk). Full record, including the 9-vs-10 count correction: `Processes/Foil_Tare_Measurement.md`.
- **Both prior assumptions were within 0.5%** and the truth sits between them: 5.50 mg was −0.46%,
  the supervisor's 5.55 mg +0.44%. Neither was meaningfully wrong for normal coatings.
- Adopted repo-wide as `FOIL_TARE_G = 0.0055255` in `disk_loading.py`; all tables regenerated from it.
- ⚠️ **The remaining weakness is the spread, not the mean.** Only 2 of the 11 blanks were resolved
  individually → the 0.057 mg disk-to-disk SD has **1 dof**. It is still *larger* than the 0.029 mg
  resolution-based placeholder it replaced, so per-disk uncertainty went **up**, not down:
  thick coatings 0.80–0.85% → 0.81–0.96%, Kuranode → 1.02%, and **8A 6.1% → 10.1%**.
- **Consequence for 8A:** its 4.5% disk-to-disk spread is now less than half its 10.1% measurement
  uncertainty — 8A's variation is **not resolvable above tare noise** and cannot be reported as real
  coating non-uniformity.
- **TODO:** weigh the 11 blanks **individually** to convert the 1-dof SD into a proper n=11 estimate.
- **TODO:** the **die tolerance (±0.05 mm, assumed)** is now the dominant uncertainty for every sample
  except 8A — get the CES cutter spec.

## ⚠️ Cycler C-rate mass basis differs from the measured electrode data (applies to ALL cells, CC19–41)

- **The cycling programs (theoretical-capacity → C-rate current calculation) use a different, flat mass
  basis than the per-cell measured values recorded in the Electrode_Prep_Logs:**
  - **Foil tare: 5.55 mg** (cycler) vs the **measured 5.5255 mg** now used here — a +0.44% difference,
    small enough to ignore next to the f mismatch below.
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
  offset is now **dominated by f** (~1.3–3.2% relative); the tare difference contributes only +0.44%.
- Applies to **every cell cycled to date** (CC19–CC21, CC22–CC41).
