# Figures — CC19–CC41 cycling review

Generated 2026-07-21 from the raw instrument files. Full analysis and caveats:
`Processes/Cycling_Data_Review_2026-07-21.md`.

All capacities are normalised on the **measured** mass basis —
active = (disk − 5.5255 mg foil tare) × per-sample *f* — **not** the cycler's
5.55 mg / 91 % / 300 mAh g⁻¹ assumption. Regenerate with `plots.py` (see §Reproducing).

---

## Reading conventions used in every figure

| Convention | Meaning |
|---|---|
| **Colour = sample**, fixed across all figures | 600 °C blue · 800 °C orange · 1000 °C aqua · 1200 °C 1 °C/min yellow · 1200 °C 2 °C/min pink · **1200 °C (3 °C/min, standard) green** · Kuranode violet |
| **Marker shape = sample** | secondary encoding so the figures survive greyscale printing and colour-vision deficiency |
| **Full opacity** = first cell of a sample; **reduced opacity** = replicate cells | one line per *cell*, never an average — replicate scatter is part of the result |
| **Open red marker** | cell excluded from analysis (CC24, CC27, CC30, CC31) |
| Sodiation = discharge (Na in) · Desodiation = charge (Na out) | reversible capacity is the **desodiation** value |

> ⚠️ **1200 °C appears in two different roles.** `12A_3C` (3 °C/min) is the *standard* ramp,
> so it is the 1200 °C member of the **temperature** series **and** the 3 °C/min member of the
> **ramp** series. 600/800/1000 °C were all run at that same 3 °C/min.

---

## Standalone figures — `cells/CC**.png` (21 files)

One per cell with data. Two stacked panels sharing the cycle axis:

- **top** — sodiation and desodiation specific capacity per cycle
- **bottom** — coulombic efficiency, with a dashed 100 % reference

Header line carries cell ID, sample, instrument, ICE and active mass; excluded cells are
titled in red with the reason. CE values above 112 % are clipped to keep the axis readable
and labelled with their true value (only CC27 does this).

**Use these to sanity-check any individual cell before trusting it in a comparison.**
`CC31` has no figure — it produced no data at all.

---

## Comparison figures — what each one is *for*

### `01_systemic_fade_all_samples.png` — **the most important figure**
**Question:** is the capacity fade a property of the biochar, or of how the cells were built?

Capacity normalised to each cell's own cycle 2, so every cell starts at 100 % and only the
*shape* of the decay is compared. The **Kuranode commercial benchmark is drawn heavy** —
it is the control, and it fades as fast as or faster than every biochar sample.

**What to conclude:** the fade is a **cell-build / test-side artifact**, not a material
property. Do not report retention as a result until this is fixed. 600 °C and 800 °C are
omitted here because CC32 and CC30 are degenerate low-capacity cells whose flat retention
is not comparable — including them would falsely suggest low-temperature carbon is stable.

### `02_capacity_vs_cycle_temperature.png`
**Question:** how does reversible capacity depend on pyrolysis temperature (at fixed 3 °C/min)?

Absolute mAh g⁻¹ against cycle. 800 °C is absent — its only cell (CC30) is the failed coating.

**What to conclude:** 1000 °C is the highest performer here, above 1200 °C. Read cycle 1–2
only; later cycles are contaminated by the §01 artifact.

### `03_capacity_vs_cycle_ramprate.png`
**Question:** does the heating ramp rate at 1200 °C matter? — *this is the project's core question.*

**What to conclude:** 1 °C/min gives visibly higher capacity than 2 and 3 °C/min across
all cycles, with replicates well separated from the other groups. This is the cleanest
comparison in the dataset: same temperature, same electrode process, 3–4 cells each.
It is also the claim most worth confirming once the fade is fixed.

### `04_ICE_temperature_and_ramprate.png`
**Question:** how does *initial* coulombic efficiency behave? ICE is measured in cycle 1,
**before** the fade artifact appears, so it is the most trustworthy quantity available.

Left = temperature, right = ramp rate; replicates jittered on x; means annotated.

**What to conclude:** ICE **rises strongly with temperature** (34 % → 60 % → 66 %) — the
expected direction, since higher pyrolysis removes defects and surface functional groups
that consume Na irreversibly. ICE is **flat across ramp rate** (71/71/66 %). So temperature
drives ICE; ramp rate does not. The 800 °C mean is skipped — its only cell is excluded.

### `05_instrument_crosscheck.png`
**Question:** can Bio-Logic and Neware results be pooled?

Same three samples on both instruments; solid+circle = Bio-Logic, dashed+square = Neware.

**What to conclude: no, not directly.** The protocols differ — Bio-Logic desodiates at
**C/10 to 2.2 V**, Neware at **C/20 to 2.0 V** — and Neware reads consistently lower. Use
this figure to justify reporting the two instruments separately, or to state the offset
explicitly when pooling.

### `06_EIS_impedance_by_stage.png`
**Question:** is the fade caused by rising cell impedance?

|Z| at 1 Hz (log axis) at four stages, recovered from the `.mpr` binaries. One line per cell.

**What to conclude: no — the hypothesis is refuted.** Impedance *falls* 14–28 % from
post-formation to post-cycling in every cell. The rising desodiation onset voltage seen in
the raw data is therefore a *consequence* of less Na being inserted, not a cause.
CC30 and CC32 are labelled: they stay 4–8× more resistive throughout, independently
confirming both are degenerate.

**Caveat that matters:** these are **two-electrode** coin cells, so the spectrum lumps the
hard carbon with the Na counter. The big pre→post-formation drop is most likely the Na
surface activating, which could *mask* a working-electrode process. This rules out a gross
whole-cell impedance rise; it does not rule out localised contact loss in the coating.

---

## Suggested figure order for a supervisor update

1. `04` — ICE trends. The solid, defensible result.
2. `03` — ramp-rate effect. The project's actual question.
3. `01` — the fade problem, with the benchmark as proof it is not the material.
4. `06` — evidence that the obvious explanation was tested and rejected.
5. `02`, `05` — supporting detail.

---

## Reproducing

`plots.py` (session scratchpad) reads three JSON files produced by the parsers described in
the review doc's final section. Note two non-obvious requirements:

- Bio-Logic `.mpr` GCPL files need `galvani` patched with column ID **182 = `step time/s` (`<f8`)**,
  which is absent from the stock map. Verified against the text exports: point counts and
  capacities match exactly.
- Neware half-cycles must be rebuilt from the **`step`** sheet, never the `cycle` sheet.
