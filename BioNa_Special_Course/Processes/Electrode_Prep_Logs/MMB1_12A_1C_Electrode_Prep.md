# Electrode Prep Log — MMB1_12A_1C

**Sample:** MMB1_12A_1C (1200 °C, 60 °C/h = 1 °C/min ramp)
**BioNa Exp #:** 46
**Coating date:** 2026-07-07
**Covers:** slurry → coating → drying → thickness *(calendering pending)*
**Standard reference:** `Processes/Slurry_Preparation_Standard.md`

---

## Slurry Formulation (as weighed)

| Step | Component | Target | As weighed | Notes |
|---|---|---|---|---|
| 1 | Water (1st) | 4.9 g | 4.5697 g | pipette (5 × 980 µL = 4.9 mL nominal) |
| 2 | CMC | 0.100 g | 0.1000 g | |
| 3 | C45 | 0.167 g | 0.1673 g | |
| 4 | Water (2nd) | 2.5 g | 2.5 mL — **not weighed** | pipette; mass deemed unreliable (evaporation) |
| 5 | Hard carbon | 3.64 g | 3.6398 g | MMB1_12A_1C |
| 6 | SBR | ~0.195 g / 200 µL | 200 µL — **not weighed** | calibrated pipette; mass deemed unreliable (evaporation) |

All Thinky steps at standard settings (2000 rpm, 10 min).

> **Mixing note:** one agglomerate found after CMC → **+5 min @ 2000 rpm** before proceeding.

### Notes on weighing
- **Water (2nd) and SBR not weighed** this run — consistent with the evaporation caveat on 8A/10A
  (visible weight loss at the Thinky Mixer, scale cannot be reliably tared). SBR dosed by the
  **200 µL calibrated pipette** adopted as standard from 8A onward.

---

## Coating

| Parameter | Value |
|---|---|
| Doctor blade gap | 100 µm |
| Tape | **Yes — first taped run** (est. +35 µm added to gap → ~135 µm effective) |
| Sheets | Two — coated onto **two separate carbon-coated foil substrates** |

> **OFF-STANDARD / new method:** blade taped this run. Est. +35 µm addition to thickness — must be
> subtracted when comparing coating thickness against untaped 6A/8A/10A. See the open question on
> taped-vs-untaped coating success in `Biona_Academy/Open_Questions.md`.

---

## Drying

| Stage | Temp | Duration |
|---|---|---|
| 1 | 30 °C | 12 h *(≥12 h — see note; standard is 6 h)* |
| 2 | 80 °C | 2 h |

> **Left overnight:** stage 1 finishes at dawn, so actual dwell at 30 °C is **somewhat longer than
> 12 h** (electrode left in the furnace overnight rather than pulled at exactly 12 h). Consistent with
> the extended 12 h stage-1 used on 8A/10A ("standard is 6 h — times to be rectified").

---

## Thickness — as-coated (total = coating + substrate)

> Measured 2026-07-08 after drying (80 °C / 2 h out of the furnace). Table-top micrometer (Mahr MarCator
> 1075 R). Readings include the carbon-coated foil substrate (~0.016–0.017 mm). **Two sheets coated**;
> both gridded. Columns = **Left / Centre / Right** (widthwise). Values in **mm**.
>
> ⚠️ **Taped-blade run (+~35 µm):** this coating was applied with a taped blade, so the coating layer is
> ~35 µm thicker than an equivalent untaped run. **Subtract ~0.035 mm** from the coating thickness before
> comparing against the untaped 6A/8A/10A. (Substrate ~0.0165 mm is separate.)
>
> ⚠️ **Large-particle artefacts:** the high outliers (e.g. 0.440, 0.379, 0.361, 0.349) are **large
> particles under the gauge, not region-dependent coating variation** (per bench observation). **Median is
> the representative thickness**, not the mean/max.

### Sheet 1 — "very nice" · 180 mm usable · 3 cm lengthwise spacing

| From top | Left | Centre | Right |
|---|---|---|---|
| 0 cm  | 0.231 | 0.257 | 0.261 |
| 3 cm  | 0.240 | 0.264 | 0.236 |
| 6 cm  | 0.183 | 0.255 | 0.201 |
| 9 cm  | 0.349 | 0.225 | 0.253 |
| 12 cm | 0.328 | 0.202 | 0.269 |
| 15 cm | 0.264 | 0.275 | 0.199 |

**Summary:** **median 0.254** · mean 0.250 · std 0.042 · CV 17.0% · min 0.183 · max 0.349 (n = 18).
Heatmap: `images/Electrode_Calendering/MMB1_12A_1C_sheet1_thickness_heatmap.png`.

### Sheet 2 — "good, less impeccable; slurry ran out mid-coating" · 150 mm usable · 2.5 cm spacing

| From top | Left | Centre | Right |
|---|---|---|---|
| 0 cm    | 0.177 | 0.131 | 0.302 |
| 2.5 cm  | 0.317 | 0.231 | 0.199 |
| 5 cm    | 0.440 | 0.229 | 0.175 |
| 7.5 cm  | 0.192 | 0.259 | 0.203 |
| 10 cm   | 0.361 | 0.261 | 0.247 |
| 12.5 cm | 0.349 | 0.379 | 0.258 |

**Summary:** **median 0.253** · mean 0.262 · std 0.082 · CV 31.3% · min 0.131 · max 0.440 (n = 18).
Much higher scatter than sheet 1 (slurry ran out mid-coating). Heatmap:
`images/Electrode_Calendering/MMB1_12A_1C_sheet2_thickness_heatmap.png`.

> **Representative thickness:** both sheets have **median ≈ 0.253–0.254 mm total** despite different means —
> the particle-driven highs inflate sheet 2's mean/CV. Coating (median − substrate) ≈ 0.237 mm; adjusted for
> the ~35 µm blade tape, the untaped-equivalent coating ≈ **0.20 mm**, comparable to 6A/10A.

---

## Calendering (2026-07-08)

Both sheets, full — no pre-calender cut. **Done as recommended.**

**Target:** 10% compression, based on **median** total thickness — the large-particle spikes make the mean
unrepresentative (esp. sheet 2), so the gap is set on the median (see thickness section).

| Sheet | Median total | Roll gap set |
|---|---|---|
| 1 (nice) | 0.254 mm | **0.23 mm** |
| 2 (slurry ran out) | 0.253 mm | **0.23 mm** |

**Reasoning / caveats:**
- Gap = 0.90 × median (0.229 / 0.228 mm → **0.23 mm** for both). Coating-basis cross-check gives 0.229–0.230 mm
  (within 2 µm), so 0.23 mm covers both bases.
- **Blade tape (+35 µm) is irrelevant to the gap** — we compress the *measured* thickness; the tape only
  matters when comparing coating thickness across samples.
- **Spring-back:** 10A came back to ~0% permanent compression at its nominal gap — expect the same tendency
  here; a tighter gap and/or multiple passes would be needed to actually reach 10%.
- **Sheet 2 (CV 31%, slurry ran out mid-coating)** will calender less uniformly than sheet 1; the scatter is
  particle-driven (not banded), so no clean cut helps — the large agglomerates get crushed hardest at 0.23 mm.

**Post-calender thickness:** not gridded — exact pre-calender points can't be relocated (as with 6A/8A/10A).

---

## Observations

*None recorded yet in the raw bench note.*
