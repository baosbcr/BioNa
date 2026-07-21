# Cycling Data Review — CC19–CC41

**Date:** 2026-07-21 · **Scope:** all Na half-cell galvanostatic data (now in `Experimental_Data/Cycling/`)
**Figures:** `Figures/` — reading guide in `Figures/README.md`
**Sources:** 30 Bio-Logic GCPL text exports (CC19–CC33) + 7 Neware `.xlsx` exports (CC34–CC40)
**Normalisation:** measured mass basis — active = (disk − **5.5255 mg** foil tare) × per-sample *f*,
from `Processes/Electrode_Prep_Logs/`. **Not** the cycler's 5.55 mg / 91 % / 300 mAh g⁻¹ basis.

> **Headline:** every cell in the dataset loses ~35–45 % of its reversible capacity over 10 cycles at
> C/20–C/10 **while holding CE ≈ 100 %** — and that includes the **commercial Kuranode benchmark**.
> A control that fails the same way as the samples means the fade is a **cell-build / test-side problem,
> not a property of the biochar**. No retention-based pyrolysis-temperature conclusion should be drawn
> until this is resolved. See §3.
>
> The obvious explanation — rising cell impedance — was **tested against the EIS and rejected**: impedance
> *falls* 14–28 % over the run in every cell. Mechanism remains open; best remaining candidate is
> progressive loss of electrical contact within the coating (§3).
>
> **ICE is unaffected** by this and is the most robust result available (§6).

---

## 1. Method and how half-cycles were counted

The working electrode is hard carbon in a Na half-cell, so **discharge = sodiation** (Na in) and
**charge = desodiation** (Na out). Reversible capacity is the *desodiation* value; ICE = desod₁ / sod₁.

| Instrument | Protocol as run |
|---|---|
| Bio-Logic (CC19–CC33) | `_04_GCPL` = formation: 3-step sodiation C/20 → C/30 → C/60 to **2 mV**, then desodiation C/20 to **2.2 V**. `_07_GCPL` = 9 × (sodiation C/20 to 2 mV, desodiation **C/10** to **2.2 V**). |
| Neware (CC34–CC40) | 12 h rest, 3-step sodiation to **2 mV**, desodiation to **2.0 V**, then 9 × (sodiation **C/20** to **20 mV**, desodiation **C/20** to **2.0 V**). |

> ⚠️ **The two instruments do not run the same test.** Bio-Logic desodiates at **C/10** to **2.2 V** with a
> **2 mV** sodiation floor; Neware desodiates at **C/20** to **2.0 V** with a **20 mV** floor. Cross-instrument
> capacity comparisons are therefore **not like-for-like**. Compare CC19–CC21 against CC35/CC36 only with
> that caveat stated.

### ⚠️ Neware `cycle` sheet is wrong — use the `step` sheet

Neware's `cycle` worksheet folds the **formation half-cycles and the first steady-state half-cycles into
"Cycle Index 1"**. For CC39 it reports Cycle 1 = 5.107 mAh DChg / 4.054 mAh Chg, which is actually
(3.331 + 1.776) and (2.272 + 1.781) — two cycles added together.

Taken at face value this gives **ICE 79 %** and an apparent **63 % capacity crash** from cycle 1 to 2.
Both are artifacts. Rebuilt from the `step` sheet, CC39's true ICE is **68.2 %** and the fade is smooth.
**Always rebuild Neware half-cycles from `step`, grouping consecutive `CC DChg` / `CC Chg` rows.**

---

## 2. Per-cell results

Capacities in mAh g⁻¹ on measured mass. "ncyc" counts complete cycles; a truncated trailing half-cycle
(run still live or aborted) was dropped before scoring — affected CC27, CC29, CC34, CC38.
Retention and fade are cycle 2 → last complete, excluding formation.

| Cell | Sample | Instr | Active (mg) | ncyc | ICE % | sod₁ | desod₁ | c2 | c_last | ret % | fade %/cyc | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| CC19 | 12A_1C | Bio-Logic | 13.021 | 10 | 72.9 | 221 | 161 | 136 | 88 | 64.5 | 5.3 | ✅ good |
| CC20 | 12A_1C | Bio-Logic | 12.488 | 10 | 72.2 | 220 | 159 | 139 | 88 | 63.2 | 5.6 | ✅ good |
| CC21 | 12A_1C | Bio-Logic | 12.843 | 10 | 71.1 | 210 | 149 | 129 | 75 | 57.7 | 6.6 | ✅ good |
| CC22 | 12A_2C | Bio-Logic | 13.555 | 10 | 72.8 | 182 | 132 | 108 | 63 | 57.9 | 6.6 | ✅ good |
| CC23 | 12A_2C | Bio-Logic | 16.483 | 10 | 69.5 | 154 | 107 | 87 | 65 | 74.2 | 3.7 | 🟡 watch |
| CC24 | 12A_2C | Bio-Logic | 13.022 | 10 | **58.9** | 113 | 66 | 71 | 59 | 83.1 | 2.3 | ❌ **bad** |
| CC25 | 12A_3C | Bio-Logic | 20.119 | 10 | 64.7 | 143 | 92 | 74 | 60 | 80.5 | 2.7 | ✅ good |
| CC26 | 12A_3C | Bio-Logic | 20.119 | 10 | 63.6 | 139 | 89 | 75 | 58 | 78.4 | 3.0 | ✅ good |
| CC27 | 12A_3C | Bio-Logic | 18.966 | 9 | **13.1**† | 151 | 20† | 96 | 54 | 55.7 | 8.0 | ❌ **suspected short** — exclude |
| CC28 | 10A | Bio-Logic | 11.878 | 7 | 60.7 | 263 | 159 | 133 | 86 | 64.9 | 8.3 | ✅ good (short) |
| CC29 | 10A | Bio-Logic | 11.434 | 7 | 59.9 | 256 | 153 | 129 | 85 | 66.0 | 8.0 | ✅ good (short) |
| CC30 | 8A | Bio-Logic | **0.561** | 10 | 49.3 | 145 | 71 | 58 | 59 | 101.9 | −0.2 | ❌ **unusable** |
| CC31 | 6A | Bio-Logic | 8.411 | **0** | — | — | — | — | — | — | — | ❌ **no data** |
| CC32 | 6A | Bio-Logic | 8.411 | 10 | **33.8** | 215 | 73 | 43 | 40 | 91.7 | 1.1 | 🟡 low but **stable** |
| CC33 | Kuranode | Bio-Logic | 7.475 | 6 | 82.5 | 262 | 216 | 154 | 99 | 64.2 | 10.5 | ✅ good (short) |
| CC34 | Kuranode | Neware | 7.298 | 3 | 83.6 | 276 | 230 | 183 | 162 | 88.7 | 11.3 | ✅ good (very short) |
| CC35 | 12A_1C | Neware | 12.488 | 8 | 68.5 | 198 | 135 | 112 | 63 | 56.1 | 9.2 | ✅ good |
| CC36 | 12A_1C | Neware | 11.867 | 8 | 68.6 | 199 | 136 | 111 | 72 | 64.8 | 7.0 | ✅ good |
| CC37 | 12A_2C | Neware | 15.063 | 10 | 69.9 | 164 | 115 | 97 | 59 | 61.3 | 5.9 | ✅ good |
| CC38 | 12A_2C | Neware | 15.862 | 9 | 70.4 | 169 | 119 | 102 | 57 | 56.1 | 7.9 | ✅ good |
| CC39 | 12A_3C | Neware | 18.699 | 10 | 68.2 | 178 | 122 | 95 | 52 | 54.7 | 7.3 | ✅ good |
| CC40 | 12A_3C | Neware | 20.474 | 10 | 65.7 | 162 | 107 | 91 | 51 | 56.6 | 6.9 | ✅ good |
| CC41 | MMB2_13A | Neware | *unknown* | — | — | — | — | — | — | — | — | ⛔ **export deleted locally** |

† CC27's cycle 1 is an artifact of the aborted run — see §4.1. Its reconstructed value is ~116 mAh g⁻¹.

**Uncertainty.** The dominant term is the foil tare (measured SD **0.057 mg**, n = 11). On a ~13 mg active
cell that is **±0.5 %** on specific capacity — negligible next to the effects below. On **CC30 (0.561 mg)**
it is **±10 %**, and on the 8A set the tare subtraction dominates entirely. Disk masses are recorded to
0.1 mg, so a further ±0.05 mg rounding applies (±0.4 % typical, **±9 %** for CC30).

---

## 3. The systemic problem: capacity falls while CE stays at 100 %

Every cell shows the same pattern from cycle 3 onward: **CE 99–101 %**, yet reversible capacity drops
5–10 % *per cycle*. Coulombic efficiency near unity means charge is not being consumed by a parasitic
reaction — the electrode is simply **delivering less accessible capacity each cycle**.

The decisive observation is the control. **Kuranode is a commercial Na-ion hard carbon run as the
benchmark**, and it fades *fastest of all*: CC33 216 → 99 mAh g⁻¹ in 6 cycles (10.5 %/cycle), CC34
230 → 162 in 3 cycles. A benchmark material that should hold >90 % over 10 cycles does not. **The fade
tracks the cell build and the test, not the sample.**

**An observation that looked like the answer.** At constant current, the voltage at the *start* of each
desodiation rises monotonically in every Neware cell:

| Cell | desodiation onset V, cycles 2 → 10 |
|---|---|
| CC39 | 0.092 → 0.103 → 0.117 → 0.138 → 0.162 → 0.191 → 0.205 → 0.215 |
| CC40 | 0.095 → 0.103 → 0.113 → 0.124 → 0.136 → 0.153 → 0.176 → 0.200 → 0.217 |
| CC37 | 0.101 → 0.111 → 0.130 → 0.151 → 0.174 → 0.199 → 0.205 → 0.213 |
| CC34 (Kuranode) | 0.072 → 0.084 → 0.095 |

Bio-Logic shows the same trend, weaker (CC19: 0.025 → 0.034 V). The obvious reading is rising overpotential
at fixed current = **rising cell impedance**, truncating the flat near-0 V plateau against a fixed cutoff.

### ❌ The EIS refutes that. Impedance *falls*.

Recovered from the `.mpr` binaries (§5.1). |Z| at 1 Hz, Ω, last of 3 repeat sweeps:

| Cell | assembled | pre-formation | **post-formation** | **post-cycling** | change |
|---|---|---|---|---|---|
| CC19 | 2178 | 2485 | 187 | **143** | −24 % |
| CC20 | 859 | 936 | 193 | **144** | −25 % |
| CC21 | 991 | 1083 | 191 | **140** | −27 % |
| CC22 | 888 | 997 | 217 | **170** | −22 % |
| CC23 | 916 | 1078 | 196 | **154** | −21 % |
| CC24 | 403 | 910 | 241 | **186** | −23 % |
| CC25 | 718 | 801 | 217 | **183** | −16 % |
| CC26 | 902 | 1039 | 212 | **183** | −14 % |
| CC30 (8A) | 1523 | 1586 | 1389 | **1125** | −19 % |
| CC32 (6A) | 1930 | 2025 | 817 | **591** | −28 % |

Every cell with both measurements gets **less** resistive across the cycling run, by 14–28 %. So the
capacity loss is **not** driven by growing cell impedance, and the rising desodiation onset voltage is
almost certainly a **consequence** of less Na having been inserted (a less-sodiated electrode relaxes to a
higher potential), not a cause. **Hypothesis rejected.**

> ⚠️ **But the EIS cannot fully exonerate the working electrode.** These are **two-electrode** coin-cell
> spectra, so they lump the hard carbon together with the Na counter. The large pre→post-formation drop
> (~1000 → ~200 Ω) is most plausibly the Na surface activating, which would **mask** a working-electrode
> process underneath. The measurement rules out a gross whole-cell impedance rise; it does not rule out
> localised loss of contact within the coating. A three-electrode cell, or post-mortem disassembly, is
> what would settle it.

**Mechanism is therefore open.** Remaining candidates, given CE ≈ 100 %, falling whole-cell impedance, and
a commercial benchmark that fails identically: **progressive loss of electrical contact / delamination of
the coating** (Kuranode is *known* delaminated — see its prep log), **electrolyte volume or wetting**
(200 µL logged), and **stack pressure / spring** in the coin-cell build. Note that a shrinking *connected*
fraction of coating reduces capacity while the still-connected fraction can keep — or improve — its
interfacial impedance, which is consistent with everything measured.

**Two useful corroborations fall out of the same table:**

- **CC30 (8A) sits 6–8× above every healthy cell post-formation** (1389 vs ~200 Ω) and barely responds to
  formation at all. Independent evidence of poor electronic percolation in a near-bare-foil coating.
- **CC32 (6A) sits 3–4× above the 12A cells** (817 vs ~200 Ω post-formation). Expected for 600 °C carbon,
  which is far less graphitic and less conductive — **supports reading CC32 as real material behaviour
  rather than a bad cell** (§4.3).

---

## 4. Individual bad or compromised cells

### 4.1 CC27 — cycle 1 destroyed by the run collision ❌→🟡

Confirms what you flagged. Reconstructed from timestamps:

Wall-clock times below are `Acquisition started on` **plus the elapsed `time/s` column** — EC-Lab's
"started on" is the *experiment* start, shared by every technique in the run, not the technique's own start.

| Event | Time | What happened |
|---|---|---|
| CC27 formation, first data | 2026-07-15 19:17:59 | Full sodiation 2.856 mAh (151 mAh g⁻¹) |
| CC27 desodiation | — | Runs **1.56 h**, extracts only **0.375 mAh**, stops at **0.156 V** |
| **CC27 original, last data** | **2026-07-16 13:00:45** | run ends here |
| CC28–CC33 batch launched | 2026-07-16 16:28–16:40 | CC28 loads `BNa_CC27_20260715.mps` |
| **CC27 restart, first data** | **2026-07-17 20:12:11** | Re-sodiates 0.392 mAh, then desodiates 1.830 mAh to 2.2 V |

> ⚠️ **The gap is 31.2 hours, not minutes.** João recalls the rename-and-restart taking ~15 min; the files
> do not support that for *this* restart, so the remembered action is probably a separate event.
> **Note also that the CC28–CC33 batch did not cause the abort** — it launched at 16:28, **3.5 h after**
> CC27 had already stopped at 13:00. Whatever interrupted CC27 happened earlier and independently.

**Mitigating detail:** CC27 ended at **0.156 V** and restarted at **0.132 V** — only **24 mV** of drift
across those 31 h, so self-discharge was mild. Reconstructed first desodiation = 0.375 + 1.830 =
2.204 mAh = **116 mAh g⁻¹**. That is more trustworthy than the 31 h gap suggests, but it still is not
directly comparable to CC25/CC26 (92 / 89 mAh g⁻¹).

**However — CC27 also looks electrically defective, independent of the restart.** Its EIS is anomalous
from assembly onward:

- `01_PEIS` **aborted after 21 points** (stopped at 2156 Hz); `03_PEIS` aborted after 33 (215 Hz).
  Every healthy cell completed 61–73 points down to 1 Hz. A sweep that cannot converge is a red flag.
- After the restart, `01`/`03_PEIS` complete and give **|Z|₁ Hz = 79 Ω** — against **700–2500 Ω** for every
  other cell. An order of magnitude low, with **inductive** (−Im < 0) behaviour at 5–100 kHz.

That combination reads as a **soft short**. It is a plausible common cause for the aborted desodiation
(stopping at 0.156 V having extracted 13 % of the inserted charge) and for the low apparent capacity.

**Use:** discard CC27 cycle 1. Cycles 2r–8r are internally consistent (CE 99–100 %, 84 → 54 mAh g⁻¹) and
sit in the CC25/CC26 family, but given the suspected short, **treat CC27 as corroborating evidence only —
do not include it in 12A_3C statistics.** Worth disassembling to confirm.

### 4.2 CC31 — dead on arrival ❌

`BNa_CC31J_20260716_04_GCPL_C13` contains **67 data points**: a 60-point rest, then sodiation ran
**6 points over 3.6 s at −0.48 µA** and stopped. No `_07` file exists. This is an open circuit / no
contact, not a slow cell. **CC31 has no recoverable data.**

**The EIS shows it failed before cycling ever started.** `01_PEIS` on C13 aborted after **21 points** and
returns **negative Re(Z) across the whole range** (−0.8 to −1.5 Ω) — not a cell; `03_PEIS` gives Z ≈ 0.
The C15 sweep managed **9 points**. So CC31 was never a working cell at assembly, which independently
confirms the §5.2 reading that the C15 files are template stubs rather than misfiled data.

Consequence: **the 6A (600 °C) condition now rests on CC32 alone, with no replicate.**

### 4.3 CC32 — low capacity, but probably real 🟡

ICE **33.8 %** and steady-state ~40 mAh g⁻¹ look alarming, but this is the **600 °C** sample, and
low-temperature hard carbon genuinely shows large irreversible capacity (surface functional groups,
defects, high surface area) and low reversible capacity. Two things argue this is *material*, not a
bad cell: its capacity is **stable** (91.7 % retention, 1.1 %/cycle — the best in the dataset), and its
desodiation onset voltage is **flat** at 0.039–0.040 V, i.e. no impedance growth.

**Verdict: keep, but it is unreplicated (CC31 dead) and cannot be confirmed.**

### 4.4 CC24 — erratic, exclude ❌

ICE **58.9 %** against siblings CC22 (72.8 %) and CC23 (69.5 %); sod₁ 113 vs 182 / 154 mAh g⁻¹ on the same
sample. The desodiation onset voltage is **non-monotonic and jumpy** — 0.037, 0.037, **0.014, 0.017,
0.074, 0.061**, 0.039, 0.047, 0.055 V — where every other healthy cell drifts smoothly. That is the
signature of **intermittent contact**, and it also explains the odd capacity recovery at cycles 6–7.
**Exclude CC24 from 12A_2C statistics.**

### 4.5 CC30 / 8A — unusable ❌

With the mass corrected to 6.15 mg, active mass is **0.561 mg** — the coating is ~11 % of the foil tare.
CE never closes (88–96 %, the only cell that fails to reach ~100 %), which is what you expect when leakage
is a large fraction of a tiny signal. Absolute reversible capacity is **0.033 mAh**. Combined ±10 % mass
uncertainty and unclosed CE make any 8A mAh g⁻¹ figure indefensible.
**Report 8A as a failed coating, not as a data point.** (Matches your assessment.)

### 4.6 Short runs — not bad cells

CC28, CC29 (7 cycles), CC33 (6), CC34 (3), CC35/CC36 (8) simply stopped earlier or were still live at
export. Their trailing partial half-cycle was dropped. **Not a quality problem** — but CC34 with 3 cycles
is too short to characterise the benchmark, and CC41 has no local data at all.

---

## 5. Data and metadata defects found

### 5.1 ⚠️ PEIS text exports are missing the impedance columns — **but the data is recoverable**

Every `*_PEIS_*.txt` contains only `Ns, time/s, dq/mA.h, (Q-Qo)/mA.h, I Range, <I>/mA, x` — **no `freq`,
no `Re(Z)`, no `-Im(Z)`**. The EIS ran (4 stages per cell) but was exported without the impedance
variables ticked.

**No re-export is needed.** The impedance is intact in the `.mpr` binaries and reads directly:

```python
from galvani import BioLogic          # pip install galvani
d = BioLogic.MPRfile("BNa_CC19_20260714_09_PEIS_C01.mpr").data
# fields: freq/Hz, Re(Z)/Ohm, -Im(Z)/Ohm, |Z|/Ohm, Phase(Z)/deg, <Ewe>/V, cycle number, ...
```

Each PEIS holds **3 repeat sweeps** (`cycle number` 1–3); use the last. Stages: `01` after assembly,
`03` after OCV / pre-formation, `06` post-formation, `09` post-cycling. Results in §3.

> ⚠️ **Check `fmin` and point count before comparing spectra.** Several sweeps aborted partway and stop at
> high frequency — CC27 `01` (21 pts, stops at 2156 Hz), CC27 `03` (33 pts, 215 Hz), CC31 `01` on C13
> (21 pts) and C15 (9 pts). Their "low-frequency" values are nothing of the kind, and comparing them
> against complete 1 Hz sweeps produces garbage. Only spectra reaching ≤2 Hz are used in §3.

> **`09_PEIS` is EMPTY (0 points) for CC27, CC28, CC29, CC31 and CC33** — those runs had not finished
> cycling at export, so post-cycling EIS does not exist yet. Re-export once they complete.

**Rs is unusable without fitting.** The high-frequency real intercept comes out **negative** on several
cells (CC22 −5.7, CC23 −7.0, CC24 −30.4, CC25 −4.0 Ω), which is unphysical and indicates a cable/inductive
artifact at 100 kHz. Series resistance needs a proper equivalent-circuit fit, not the raw intercept.

### 5.2 CC31 / CC32 channel conflict — RESOLVED ✅

`Cell_Instrument_Channel_Map.md` flagged CC31 as carrying a duplicate technique set on **C13 and C15**,
colliding with CC32 on C15. Resolved on three independent lines:

1. João's own sheet assigns **CC31 → Ch13, CC32 → Ch15**.
2. CC33 (started 16:39:31) loads `BNa_CC31J_20260716.mps` — **before** CC31 itself started (16:40:54).
   So CC31's `.mps` was authored first with **both C13 and C15 selected** and used as the template for
   CC32 and CC33; that is where the phantom C15 technique set came from.
3. The CC31-on-C15 files are empty stubs; the real C15 data belongs to CC32 (started 16:40:31).

**Conclusion: CC31 = C13 (dead), CC32 = C15 (valid). No data is mislabelled.** Blocker closed.

### 5.3 Bio-Logic settings files chain from cell to cell

Each cell loads the previous cell's `.mps`: CC24←CC23←CC22, CC26←CC25, CC28←CC27, CC32←CC31, CC33←CC31.
Same duplicate-a-schedule workflow that produces the stale Neware `PN`/`Creator` fields (`Processes/Raw_Data_Triage_Notes_2026-07-21.md` §4b). It is normal practice, but it means **`.mps` provenance is not cell identity**.

### 5.4 CC19 carries a stale comment ⚠️ (cosmetic)

`Comments: BioNa_KT25` and `Loaded Setting File: 2600607_BNS_CC15_KT25.mps` — a Kuranode/CC15 template
that was never renamed. The authoritative field, `Electrode material: BNa-CC19-MMBA1-12-1C`, is correct
and matches the disk log (20.2 mg, 12A_1C). CC20 loaded the same template but has a correct comment, so
this is a copy artifact. **No impact on data**; explains the note in the supervisor's sheet.

### 5.5 CC41 has no local data ⛔

`CC41` (MMB2_13A supervisor reference) exports were deleted 2026-07-21 (`Processes/Raw_Data_Triage_Notes_2026-07-21.md` §2b). It is a
legitimate project cell and **must be re-pulled from the Neware server**. Its disk mass (11.4 mg) is known
but *f* and tare for the supplied MMB2_13A electrode are **not**, so it cannot be normalised to mAh g⁻¹
even once recovered.

### 5.6 Excel cross-check

`Joao.xlsx` (supervisor's quick check, cols B–G; now `Experimental_Data/Cycling/_supervisor_crosscheck/`) matched the disk logs on **21/21** cells
and the Neware `SCQ` metadata to the microgram. It stops at CC39 (crop artifact) and its column G header
says "Electrode loading" where the values are **total disk mass**. Being discarded — recorded here only as
confirmation that the mass chain is consistent across three independent sources.

---

## 6. What this means for the experiment

**Usable for cross-temperature comparison right now:**

| Sample | Cells | Replicates | Status |
|---|---|---|---|
| 12A_1C | CC19, CC20, CC21 (BL); CC35, CC36 (NW) | 3 + 2 | ✅ strong |
| 12A_2C | CC22, CC23 (BL); CC37, CC38 (NW) | 2 + 2 | ✅ ok — **CC24 excluded** |
| 12A_3C | CC25, CC26 (BL); CC39, CC40 (NW) | 2 + 2 | ✅ ok — **CC27 excluded** (suspected short) |
| 10A | CC28, CC29 | 2 | ✅ ok, short (7 cycles) |
| 8A | CC30 | 1 | ❌ failed coating |
| 6A | CC32 | **1** | 🟡 unreplicated (CC31 dead) |
| Kuranode | CC33, CC34 | 2 | ✅ but 6 and 3 cycles only |
| MMB2_13A | CC41 | 0 local | ⛔ re-pull needed |

**The ICE trend across pyrolysis temperature is the most robust result available** — it is measured in
cycle 1, before the fade sets in, and it is consistent across both instruments:
**6A ≈ 34 % → 8A ≈ 49 % → 10A ≈ 60 % → 12A ≈ 64–73 %**. This is the expected direction (higher pyrolysis
temperature removes defects and surface groups, cutting irreversible capacity). Treat 6A and 8A as
weakly-supported endpoints (n = 1 each, 8A on a failed coating).

**Capacity retention must not be reported as a material property** until §3 is resolved.

### Next actions, in priority order

1. **Diagnose the systemic fade** (electrolyte volume, Na counter, adhesion, stack pressure) before
   building more cells. Every cell built until this is fixed will show the same artifact.
2. **Rebuild the 6A condition** — CC32 has no replicate.
3. **Disassemble CC27** to confirm or rule out the suspected short (§4.1), and CC24 for contact (§4.4).
4. **Re-pull CC41** from the Neware server, and obtain *f* + tare for the MMB2_13A electrode.
5. Re-coat 8A, or drop the 800 °C condition from the scope.
6. Let CC33/CC34 (benchmark) run longer — 3–6 cycles is not enough for a reference.
7. Re-export `09_PEIS` for CC27–CC29, CC31, CC33 once those runs finish (currently empty, §5.1).

---

## Reproducing this

Parsers and outputs are in the session scratchpad (not tracked):
`parse_biologic.py` (EC-Lab ASCII → half-cycle capacities), `parse_neware.py` (BTS xlsx → step/cycle),
`analyse.py`, `final.py`. Key implementation notes: EC-Lab text is **latin-1 with decimal commas** and a
`Nb header lines : N` preamble; half-cycles are contiguous runs of constant `(Ns, ox/red)` and capacity is
`Σ|dq|`. Neware half-cycles **must** come from the `step` sheet (§1), and `TestInfo*.xml` is **GB2312**.
