# Electrode Prep Log — MMB1_12A_2C

**Sample:** MMB1_12A_2C (1200 °C, 120 °C/h = 2 °C/min ramp)
**BioNa Exp #:** 47
**Coating date:** 2026-07-09
**Covers:** slurry → coating → drying → thickness → calendering *(stamping next)*
**Standard reference:** `Processes/Slurry_Preparation_Standard.md`

> Prepared in the same session as **MMB1_12A_3C** (2C mixed first). See
> `MMB1_12A_3C_Electrode_Prep.md`.

---

## Slurry Formulation (as weighed)

| Step | Component | Target | As weighed | Notes |
|---|---|---|---|---|
| 1 | Water (1st) | 4.9 g | 4.591 g | pipette; initial reading — see evaporation note |
| 2 | CMC | 0.100 g | 0.10019 g | |
| 3 | C45 | 0.167 g | 0.16707 g | weighed in boat — see boat-retention caveat in standard |
| 4 | Water (2nd) | 2.5 g | 2.5 mL — **not weighed** | pipette; mass deemed unreliable (evaporation) |
| 5 | Hard carbon | 3.64 g | 3.64361 g | MMB1_12A_2C (weighed in boat) |
| 6 | SBR | ~0.195 g / 200 µL | 200 µL — **not weighed** | calibrated pipette; mass deemed unreliable (evaporation) |

All Thinky steps at standard settings (2000 rpm, 10 min).

> **Mixing note:** a **persistent agglomerate** after CMC → **+20 min @ 2000 rpm total (4 × 5 min)** before
> proceeding. It **shrank with each extra mix**, and the mix **warmed progressively** — the rising temperature
> likely aided CMC dissolution. (Much more than the 1C run, which needed only +5 min.)

### Notes on weighing
- **Water (1st) — evaporation observed while dispensing:** scale read **4.591 g** initially, then
  drifted to **4.5884 g and kept falling** at ambient temperature. The peak (initial) reading is the
  best estimate of the mass actually dispensed; evaporative loss is **not** subtracted. Consistent with
  the evaporation caveat on 8A/10A/1C. Value is on target vs 1C (4.5697 g for the same 4.9 mL nominal).
- **Water (2nd) and SBR not weighed** — added by pipette; masses deemed unreliable (evaporation),
  consistent with 1C.
- **Solids (CMC, C45, hard carbon) weighed in boats** — subject to the boat-retention caveat (trace
  material left behind; roughly deterministic bias). See `Processes/Slurry_Preparation_Standard.md`.

---

## Coating

| Parameter | Value |
|---|---|
| Doctor blade gap | 100 µm |
| Tape | **Yes** → est. +35 µm added to gap (~135 µm effective), as on 1C |
| Sheets | Two |

> **Taped run** — subtract ~35 µm from the coating layer when comparing thickness against untaped samples
> (6A/8A/10A), same as 1C.

---

## Drying

| Stage | Temp | Duration | Status |
|---|---|---|---|
| 1 | 30 °C | 12 h | **In progress** — started 2026-07-09 |
| 2 | 80 °C | 2 h | Pending |

> Dried together with the 3C and Kuranode coatings in the same oven run.

---

## Thickness — as-coated (total = coating + substrate)

> Measured 2026-07-14 after drying. Table-top micrometer (Mahr MarCator 1075 R). Readings include the
> carbon-coated foil substrate (~0.016–0.017 mm). **Two sheets coated**, both gridded: **6 lengthwise ×
> 3 widthwise = 18 points**, rows **3 cm apart** over **150 mm usable length**. Columns as recorded:
> **Left / Right / Centre**. Values in **mm**.
>
> ⚠️ **Taped-blade run (+~35 µm):** coating applied with a taped blade (~135 µm effective), so the coating
> layer is ~35 µm thicker than an untaped run. **Subtract ~0.035 mm** from the coating before comparing
> against untaped 6A/8A/10A. Substrate ~0.0165 mm is separate. *(Tape is irrelevant to the calender gap —
> see below.)*
>
> ⚠️ **Large-particle artefacts:** the high outliers (esp. sheet 2's 0.619, 0.417) are **large particles
> under the gauge, not region-dependent coating variation** — same as 1C. **Median is the representative
> thickness**, not mean/max.

### Sheet 1 — 150 mm usable · 3 cm lengthwise spacing

| From top | Left | Right | Centre |
|---|---|---|---|
| 0 cm  | 0.216 | 0.318 | 0.250 |
| 3 cm  | 0.203 | 0.275 | 0.288 |
| 6 cm  | 0.197 | 0.133 | 0.200 |
| 9 cm  | 0.241 | 0.241 | 0.260 |
| 12 cm | 0.197 | 0.316 | 0.282 |
| 15 cm | 0.277 | 0.266 | 0.370 |

**Summary:** **median 0.255** · mean 0.252 · std 0.056 · CV 22.2% · min 0.133 · max 0.370 (n = 18).

### Sheet 2 — 150 mm usable · 3 cm lengthwise spacing

| From top | Left | Right | Centre |
|---|---|---|---|
| 0 cm  | 0.125 | 0.284 | 0.221 |
| 3 cm  | 0.328 | 0.316 | 0.190 |
| 6 cm  | 0.417 | 0.231 | 0.311 |
| 9 cm  | 0.619 | 0.322 | 0.369 |
| 12 cm | 0.195 | 0.380 | 0.267 |
| 15 cm | 0.363 | 0.356 | 0.223 |

**Summary:** **median 0.314** · mean 0.307 · std 0.110 · CV 36.0% · min 0.125 · max 0.619 (n = 18).
Much higher scatter than sheet 1 (CV 36% vs 22%); the thickest points (0.619, 0.417) sit on the **left
edge**, consistent with particle-driven spikes rather than a uniform thick band.

> **Representative thickness:** sheet 1 **median 0.255 mm**, sheet 2 **median 0.314 mm** total. Sheet 2 is
> genuinely thicker (not just noisier). Coating (median − substrate) ≈ 0.239 / 0.298 mm; adjusted for the
> ~35 µm blade tape, untaped-equivalent coating ≈ 0.20 / 0.26 mm.

---

## Calendering (2026-07-15)

Gap set on **median** total thickness, 10% compression target, same basis as 1C/3C/Kuranode (large-particle
spikes make the mean unrepresentative, esp. sheet 2).

| Sheet | Median total | Roll gap set |
|---|---|---|
| 1 | 0.255 mm | **0.23 mm** |
| 2 | 0.314 mm | **0.28 mm** |

**Reasoning / caveats:**
- Gap = 0.90 × median (0.2295 → **0.23 mm**; 0.2822 → **0.28 mm**).
- **Blade tape (+35 µm) is irrelevant to the gap** — we compress the *measured* thickness; tape only matters
  for cross-sample coating comparisons.
- **Sheet 2 (CV 36%)** will calender less uniformly; scatter is particle-driven (left-edge spikes), not a
  clean band, so the large agglomerates get crushed hardest at 0.28 mm.

### Outcome — mostly spring-back, no delamination

Both sheets: **near-full spring-back to ~0% permanent compression**, same as 3C (and 10A/1C) — only proud
high spots took a set. **No delamination** — coating stayed well adhered (standard-order biochar build;
contrast Kuranode's band-aid peel-off). Reinforces the recurring lesson: to actually reach 10% on these
biochar coatings, set the gap **tighter than 10%-of-median** and/or use **multiple stepped passes**.

**Post-calender thickness:** not gridded 1:1 (exact points can't be relocated, as with 6A/8A/10A/1C).

---

## Observations

- **Two sheets**, sheet 2 genuinely thicker (median 0.314 vs 0.255 mm) and much more scattered (CV 36% vs 22%).
- **Calendered well, held together** (no delamination); **near-full spring-back** at the 0.23/0.28 mm gaps —
  only high spots took a permanent set. Same rebound tendency as 3C/10A/1C.
