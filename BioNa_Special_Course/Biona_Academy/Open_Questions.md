# Open Questions & TODOs

Running list. When resolved, promote the answer into the relevant `Processes/` or `Instruments/`
doc and remove it here.

---

## Thickness measurement / micrometer

- **Substrate baseline:** the carbon-coated Al foil (current collector) is **~0.016–0.017 mm**
  (≈16–17 µm) on the table-top micrometer.
- **All reported coating thicknesses are TOTAL** (coating + substrate). To get coating-only,
  subtract ~0.017 mm.
- **TODO:** micrometer make/model is unknown → identify and add to `Instruments/Instruments.md`.
- **TODO:** quantify the **micrometer uncertainty** (instrument resolution + repeatability).
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
