# Electrode Prep Log — MMB1_10A

**Sample:** MMB1_10A (1000 °C, 180 °C/h)
**BioNa Exp #:** 43
**Covers:** slurry → coating → drying → thickness
**Standard reference:** `Processes/Slurry_Preparation_Standard.md`

---

## Slurry Formulation (as weighed)

| Step | Component | Target | As weighed | Notes |
|---|---|---|---|---|
| 1 | Water (1st) | 4.9 g | 4.6688 g | pipette |
| 2 | CMC | 0.100 g | 0.1002 g | |
| 3+4 | C45 + Water (2nd) | 0.167 g + 2.5 g | 0.1673 g + 2.5 mL | **OFF-STANDARD:** added together (saves ~10 min) |
| 5 | Hard carbon | 3.64 g | 3.6715 g | MMB1_10A |
| 6 | SBR | 5 drops | mass not recorded ("0.g") | calibrated 200 µL pipette |

All Thinky steps at standard settings (2000 rpm, 10 min).

> **Process interruption:** held for Pathick meeting while inside the Thinky Mixer — restarted 11:48 am.

---

## Coating

| Parameter | Value |
|---|---|
| Doctor blade gap | 100 µm |
| Tape | None |

**Coating failed** — blade caught kinks in the foil. Sample nonetheless carried through to drying.

---

## Drying

| Stage | Temp | Duration |
|---|---|---|
| 1 | 30 °C | 12 h *(standard is 6 h — times to be rectified)* |
| 2 | 80 °C | 2 h |

---

## Thickness — as-coated (total = coating + substrate)

> Measured on the **coated, not-yet-calendered** electrode — **calendering still pending** for this
> sample. Readings include the carbon-coated foil substrate (~0.016–0.017 mm). Table-top micrometer.
> *(Raw note says "calendared" — a habitual slip for "coated"; see `_raw/README.md`.)*
> Not the earlier MMB1_10A that was destroyed during calendering (see `Processes/Calendering_Notes.md`).

### Preliminary readings (superseded by the 18-point grid below)

| Location | Thickness (mm) |
|---|---|
| Top | 0.117 |
| Upper-center | 0.355 |
| Center | 0.183 |
| Bottom | 0.271 |

### Remeasured 18-point grid (2026-07-08)

18 points per sheet: **6 lengthwise × 3 widthwise**. Lengthwise spacing **3 cm** from the top; widthwise =
near each edge + centre of the ~6 cm-wide coating. Columns as recorded: **Left / Centre / Right**. Values in **mm**.

| From top | Left | Centre | Right |
|---|---|---|---|
| 0 cm  | 0.326 | 0.211 | 0.255 |
| 3 cm  | 0.362 | 0.297 | 0.320 |
| 6 cm  | 0.205 | 0.251 | 0.202 |
| 9 cm  | 0.253 | 0.241 | 0.253 |
| 12 cm | 0.263 | 0.180 | 0.251 |
| 15 cm | 0.223 | 0.220 | 0.199 |

**Summary:** mean 0.251 mm · min 0.180 · max 0.362 · range 0.182 mm (n = 18).
**Top ~5 cm is markedly thicker** (rows at 0–3 cm average ~0.30 mm vs ~0.23 mm below). Consistent with the
"bad and inhomogeneous" coating note. Heatmap: `images/Electrode_Calendering/MMB1_10A_thickness_heatmap.png`.

---

## Calendering (2026-07-08)

**Pre-calender cut:** Coating cut across **below the second measurement line (~4.5 cm from top)**. The thick,
uneven top band (0 cm + 3 cm rows, mean ~0.30 mm, peak 0.362) was **removed and saved separately**. Only the
**even lower section (6–15 cm rows, n = 12, mean 0.228 mm)** was calendered.

**Target:** 10% compression.
**Roll gap set: 0.205 mm** (total spacing).
**Reasoning:** 0.90 × 0.228 mm (mean total of the even section) = 0.205 mm; coating-only basis gives 0.207 mm
(within 2 µm). Gap based on the even section only so the discarded thick band could not skew it high — the
skew that likely destroyed the earlier 10A.

### Post-calender thickness

> Measured on the calendered even section. **Points do not map 1:1 to the pre-calender grid** (couldn't
> relocate the exact spots), so per-point deltas aren't meaningful — compare distributions/means only.
> 9 points: 3 lengthwise × 3 widthwise (Left / Centre / Right). Values in **mm**.

| Row | Left | Centre | Right |
|---|---|---|---|
| a | 0.266 | 0.235 | 0.252 |
| b | 0.171 | 0.185 | 0.232 |
| c | 0.253 | 0.220 | 0.227 |

**Summary:** mean 0.227 mm · min 0.171 · max 0.266 · range 0.095 mm (n = 9).

**Achieved compression ≈ 0%** (even-section mean 0.228 → 0.227 mm) — well short of the 10% target. Several
points still exceed the 0.205 mm set gap, so the nip either didn't reach the set gap or **spring-back
dominated**. Visually the electrode **calendered beautifully** (uniform, well-adhered), but thickness barely
moved. → For subsequent samples, expect to set the gap **tighter than the 10%-of-mean value** and/or use
multiple passes to actually reach target compression.

---

## Observations

- Coating looks **bad and inhomogeneous**.
- Doctor-blade square edges tore through the coated foil in multiple locations; the blade had to be
  relocated. This probably attached slurry to the **backside of the blade**, which then released in a
  **viscosity-dependent** manner behind the blade.
- Same **growing triangular scratch pattern** trailing the square edges after the blade was relocated.
