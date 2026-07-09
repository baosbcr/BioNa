# Electrode Prep Log — MMB1_6A

**Sample:** MMB1_6A (600 °C, 180 °C/h)
**BioNa Exp #:** 41
**Covers:** slurry → coating → drying → thickness
**Standard reference:** `Processes/Slurry_Preparation_Standard.md`

---

## Slurry Formulation (as weighed)

| Step | Component | Target | As weighed | Notes |
|---|---|---|---|---|
| 1 | Water (1st) | 4.9 g | 4.9 mL (mass not recorded) | pipette |
| 2 | CMC | 0.100 g | 0.0999 g | |
| 3 | C45 | 0.167 g | 0.166 g | |
| 4 | Water (2nd) | 2.5 g | 2.5 mL | |
| 5 | Hard carbon | 3.64 g | 3.6399 g | MMB1_6A |
| 6 | SBR | 5 drops | 0.1940 g | burette/burner pipette; shake before adding |

All Thinky steps at standard settings (2000 rpm, 10 min).

> **Process interruption:** held for Pathick meeting while inside the Thinky Mixer — restarted 11:48 am.

---

## Coating

| Parameter | Value |
|---|---|
| Doctor blade gap | 100 µm |
| Tape | None |

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

### Preliminary readings (superseded by the 18-point grid below)

| Location | Thickness (mm) |
|---|---|
| Top | 0.177 |
| Upper-center | 0.189 |
| Center | 0.205 |
| Bottom | 0.281 |
| Random 1 | 0.132 |
| Random 2 | 0.171 |
| Random 3 | 0.161 |

### Remeasured 18-point grid (2026-07-08)

18 points per sheet: **6 lengthwise × 3 widthwise**. Lengthwise spacing **3 cm**, starting from the top
of the ~180 mm usable coating; widthwise = near each edge + centre of the ~6 cm-wide coating.
Columns as recorded: **Left / Centre / Right**. All values in **mm** (total = coating + substrate).

| From top | Left | Centre | Right |
|---|---|---|---|
| 0 cm  | 0.128 | 0.160 | 0.201 |
| 3 cm  | 0.208 | 0.246 | 0.206 |
| 6 cm  | 0.150 | 0.181 | 0.190 |
| 9 cm  | 0.130 | 0.209 | 0.198 |
| 12 cm | 0.256 | 0.215 | 0.173 |
| 15 cm | 0.214 | 0.178 | 0.273 |

**Summary:** mean 0.195 mm · min 0.128 · max 0.273 · range 0.145 mm (n = 18).
Scattered, no clear lengthwise gradient. Heatmap: `images/Electrode_Calendering/MMB1_6A_thickness_heatmap.png`.

---

## Calendering (2026-07-08)

**Full sheet — no pre-calender cut** (n = 18, mean total 0.195 mm, range 0.128–0.273, CV 20%).

**Target:** 10% compression.
**Roll gap set: 0.175 mm** (total spacing) — 0.90 × 0.195 mm mean. **Done as recommended.**
**Reasoning / caveats:**
- Nominal 10%-of-mean gap, same basis as 10A.
- 10A at its nominal gap achieved ~0% actual compression (full spring-back) — 6A likely behaves similarly; a
  tighter gap and/or multiple passes would be needed to actually reach 10%.
- Fixed gap over a high-variability sheet: thinnest cells (~0.128) pass untouched, thickest (~0.273) see ~36%.

**Post-calender thickness:** not gridded — exact pre-calender points can't be relocated, so per-point deltas
aren't meaningful (see 10A for the same limitation).

---

## Observations

- Coating looks good.
- Doctor-blade square edges caught particles underneath while coating, producing a **growing triangular scratch pattern** trailing the square edges of the blade.
