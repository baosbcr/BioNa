# Cycling analysis pipeline — CC19–CC41

Turns the raw instrument files in `Experimental_Data/Cycling/` into the results in
`Processes/Cycling_Data_Review_2026-07-21.md` and the figures in `Figures/`.

**Everything here is tracked in git except nothing** — the scripts *and* their JSON output
(228 KB) are committed, so the figures and tables can be regenerated **without** the 553 MB of
raw data (which lives on OneDrive and is gitignored). Only re-run the two parsers if the raw
data changes.

## Requirements

```
pip install galvani openpyxl numpy matplotlib
```

## Run order

```bash
python parse_biologic.py   # .mpr  -> data/biologic_cycles.json   (~2 min, reads 553 MB)
python parse_neware.py     # .xlsx -> data/neware_cycles.json
python peis_mpr.py         # .mpr  -> data/peis.json  (impedance)
python analyse.py          # -> data/summary.json   + per-cell table
python final.py            # -> data/final.json     + scored table (ICE, retention, fade)
python plots.py            # -> Figures/*.png and Figures/cells/*.png
```

Steps 4–6 need only the JSON, so they run anywhere the repo is checked out.

| File | Role |
|---|---|
| `parse_biologic.py` | EC-Lab `.mpr` → half-cycle capacities |
| `parse_neware.py` | Neware BTS `.xlsx` → metadata + steps/cycles |
| `peis_mpr.py` | EC-Lab PEIS `.mpr` → impedance per stage |
| `analyse.py` | joins both instruments, normalises on measured mass |
| `final.py` | drops truncated trailing cycles, scores ICE / retention / fade |
| `plots.py` | all figures |
| `reorg.py` | ⚠️ **historical, do not run.** One-shot script that dismantled `ToProcessWClaude/` on 2026-07-21. Kept as the record of what was moved and deleted. |

## Four things that will bite you

**1. galvani cannot read the GCPL files unpatched.** Column ID **182** (`step time/s`) is
missing from its map and every GCPL file uses it → `NotImplementedError: Column ID 182 ... is
unknown`. `parse_biologic.py` patches it:

```python
BioLogic.VMPdata_colID_dtype_map[182] = ("step time/s", "<f8")
```

The width was determined empirically, not guessed: with `<f8` the record size resolves to
exactly 136 190 points for `CC19_04_GCPL`, matching the old text export, and the capacities
agree to 4 decimals (sod 2.8832, desod 2.1009 mAh). A wrong width shifts every field and the
mismatch is immediate. **Verified across all 30 files that had a text export: 0 mismatches.**

**2. `ox/red` is a packed bit-flag, not a column.** Unpack via `MPRfile(...).flags_dict`,
which also carries `mode`, `error`, `control changes`, `Ns changes`, `counter inc.`.

**3. Neware's `cycle` sheet is wrong — use `step`.** It merges the formation half-cycles with
the first steady-state ones into "Cycle Index 1". Taking it at face value gives **ICE 79 %**
(true: 68 %) and a fabricated 63 % cycle-1→2 crash.

**4. Some `.mpr` files are empty stubs** (0 points) from aborted runs — CC27 `_07`, CC31 on
C15. The parsers guard for this; anything you write must too.

## Mass basis

Specific capacities use the **measured** basis: active = (disk − **5.5255 mg** foil tare) ×
per-sample *f*, from `Processes/Electrode_Prep_Logs/`. This is **not** the cycler's
5.55 mg / 91 % / 300 mAh g⁻¹ assumption, which understates mAh g⁻¹ by ~2.4 %.

The mass table is hardcoded at the top of `analyse.py` — **update it there** if a disk log
changes. CC30 was corrected 6.5 → 6.15 mg on 2026-07-21 (transcription typo); CC41 has no
mass and cannot be normalised until *f* and tare for the supplied MMB2_13A electrode are known.
