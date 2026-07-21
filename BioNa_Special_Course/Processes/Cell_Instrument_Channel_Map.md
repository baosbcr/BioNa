# Cell → Instrument / Channel Map

**Built 2026-07-21** by reading the raw data files, not from memory:
- **Bio-Logic:** instrument from the `Device :` line inside each `.mps` (plain text); channel from the
  `_Cnn` suffix on the `.mpr` filenames.
- **Neware:** unit/channel from the `.ndax` filename pattern `<DevType><DevID>-<unit>-<channel>-<testID>`
  and the exported `..._<unit>_<channel>.ndax` names.

Instrument specs: `Instruments/Instruments.md`. Cell masses/loadings: `Processes/Electrode_Prep_Logs/`.

> This closes the "no per-cell instrument assignment" gap flagged in `Biona_Academy/Open_Questions.md`.
> **The split is clean: CC19–CC33 on the two Bio-Logic units, CC34–CC47 on the Neware.**

---

## Bio-Logic (EC-Lab V11.62) — CC19–CC33

| Cell | Instrument | Channel | Sample |
|---|---|---|---|
| CC19 | **VMP3** (s/n 0509) | C01 | 12A_1C |
| CC20 | VMP3 | C02 | 12A_1C |
| CC21 | VMP3 | C03 | 12A_1C |
| CC22 | VMP3 | C04 | 12A_2C |
| CC23 | VMP3 | C05 | 12A_2C |
| CC24 | VMP3 | C06 | 12A_2C |
| CC25 | VMP3 | C07 | 12A_3C |
| CC26 | VMP3 | C08 | 12A_3C |
| CC27 | **MPG-2** (s/n 0124) | C09 | 12A_3C — *has a `_restart` file set, also on C09* |
| CC28 | MPG-2 | C10 | 10A |
| CC29 | MPG-2 | C11 | 10A |
| CC30 | MPG-2 | C12 | 8A |
| CC31 | MPG-2 | **C13** ✅ | 6A — **dead run, no data** (see below) |
| CC32 | MPG-2 | C15 ✅ | 6A |
| CC33 | MPG-2 | C16 | Kuranode |

> **Channel numbering appears continuous across the two instruments** (VMP3 = C01–C08, MPG-2 = C09–C16),
> consistent with both devices being in one EC-Lab session. Confirm against the EC-Lab channel view before
> relying on it to identify a *physical* channel.

### ✅ CC31 / CC32 channel conflict — RESOLVED 2026-07-21. No data is mislabelled.

The apparent conflict (`CC31` carrying a full duplicate technique set on **both C13 and C15**, colliding
with `CC32` on C15) was a **template artifact, not a mix-up**. Three independent lines agree:

1. **João's own tracking sheet** assigns CC31 → Ch13 and CC32 → Ch15.
2. **Timestamps rule out a swap.** CC33 started **16:39:31** and loads `BNa_CC31J_20260716.mps` — i.e.
   *before* CC31's own run started at **16:40:54**. CC31's `.mps` was therefore authored first with
   **both C13 and C15 selected**, then reused as the template for CC32 (16:40:31) and CC33. That is
   where the phantom C15 set came from.
3. **The CC31-on-C15 files are empty stubs**; the real C15 data is CC32's.

> ⚠️ **CC31 is a dead run.** `BNa_CC31J_20260716_04_GCPL_C13` holds **67 points**: a 60-point rest, then
> sodiation ran **6 points over 3.6 s at −0.48 µA** and stopped. There is no `_07` file. Open circuit /
> no contact — **no recoverable data**. The 6A (600 °C) condition therefore rests on **CC32 alone, with
> no replicate**. Full analysis: `Processes/Cycling_Data_Review_2026-07-21.md` §4.2–4.3.

---

## Neware BTS85 (device 79) — CC34–CC47

| Cell | Unit | Channel | Test ID | Sample |
|---|---|---|---|---|
| CC34 | 4 | 1 | 146 | Kuranode |
| CC35 | 4 | 2 | 147 | 12A_1C |
| CC36 | 4 | 3 | 148 | 12A_1C |
| CC37 | 4 | 4 | 149 | 12A_2C |
| CC38 | 4 | 5 | 150 | 12A_2C |
| CC39 | 4 | 6 | 151 | 12A_3C |
| CC40 | 4 | 7 | 152 | 12A_3C |
| CC41 | 4 | 8 | 153 | MMB2_13A (supervisor reference) |
| CC42 | 5 | 1 | 154 | ❓ **ownership unconfirmed** |
| CC43 | 5 | 2 | 155 | ❓ **ownership unconfirmed** |
| CC44 | 5 | 3 | 156 | ❓ **ownership unconfirmed** |
| CC45 | 5 | 4 | 157 | ❓ **ownership unconfirmed** |
| CC46 | 5 | 5 | 158 | ❓ **ownership unconfirmed** |
| CC47 | 5 | 6 | 159 | ❓ **ownership unconfirmed** |

> ⚠️ **CC42–CC47 may not be this project's cells.** They appear in no disk log, sit on **unit 5** (João
> used only unit 4), lack the `J` suffix carried by CC28J–CC41J, and their schedules were **copied from
> CC41** — so their `Creator = negsa` is *inherited*, not evidence of ownership (all six share CC41's
> `PN = 2026-07-16 17-29-21`). **Confirm with the lab before including them.**
> Detail: `ToProcessWClaude/Notes_21_7_26.md` §2, §4b.

---

## Naming traps in the raw files

- **Schedule name ≠ cell name.** Several Neware files start with the *template* name, e.g.
  `Rate_260701_CC79_..._BNa_CC34J_..._4_1.ndax` — `CC79` there is the schedule/device label, **not** a
  cell. The real cell is the `BNa_CCnnJ` segment.
- **Two different CC37/CC38 exist.** `Rate_260617_CC37` / `Rate_260616_CC38` (builder **`patbin`**,
  June 2026, active mass 6.779 mg) are **not** João's CC37/CC38 (2C, assembled 2026-07-16, ~15–16 mg
  active). Different person, different cells, same numbers. João's carry the `J` suffix (`BNa_CC37J`).
- **`_restart` sets** (e.g. CC27) are re-runs of the same cell — do not treat as separate cells.
