# Electrode Prep Log — Kuranode (commercial hard carbon)

**Sample:** Kuranode — Kuraray **commercial** hard carbon (Na-ion benchmark)
**BioNa Exp #:** 49 *(spun off from the aborted MMB1_12A_3C attempt #1, Exp #48 session)*
**Coating date:** 2026-07-09
**Covers:** slurry → coating → drying → thickness → calendering *(⚠️ delamination — see Calendering)*
**Standard reference:** `Processes/Slurry_Preparation_Standard.md`
**Raw notes:** `_raw/MMB1-12A_3C_attempt1-ABORTED-commercialHC_Slurry_prep.md`

> **Origin — serendipitous experiment.** This batch began as **MMB1_12A_3C attempt #1**, which was aborted
> when the hard carbon was **forgotten and SBR added first**. Rather than discard it, a **commercial hard
> carbon (Kuranode)** was added to the already-mixed CMC/C45/SBR/water base — a **commercial benchmark
> against the MMB1 biochar series**. The reserved MMB1_12A_3C hard carbon (3.64020 g) went to the proper
> 3C restart instead (`MMB1_12A_3C_Electrode_Prep.md`).

---

## ⚠️ OFF-STANDARD: mixing order

**SBR was split around the hard carbon** — the main dose (200 µL) went in **before** the hard carbon (the
reverse of the standard sequence, which adds SBR last), and an **extra drop** was added **after** the Kuranode
(supervisor's call). Consequences to keep in mind when interpreting this electrode:
- Binder (SBR) was mixed into the CMC/C45/water base **without active material present**, then hard carbon
  was introduced afterward → **binder distribution over the hard-carbon surface may differ** from a standard
  build, potentially affecting adhesion, calendering behaviour and rate performance.
- **Do not treat this as a clean "commercial HC vs biochar" comparison** — both the *material* (Kuranode) and
  the *process* (mix order) differ from the MMB1 series. It is a **qualitative "what happens" test**, not a
  controlled benchmark. A controlled Kuranode build (standard order) would be needed for a fair comparison.

---

## Slurry Formulation (as weighed)

| Step (as-run) | Component | Target | As weighed | Notes |
|---|---|---|---|---|
| 1 | Water (1st) | 4.9 g | 4.525 g | pipette; initial reading (evaporation, not subtracted) |
| 2 | CMC | 0.100 g | 0.10083 g | boat |
| 3 | C45 | 0.167 g | 0.16690 g | boat |
| 4 | Water (2nd) | 2.5 g | 2.5 mL — **not weighed** | pipette; evaporation |
| 5 | **SBR (1st)** | ~0.195 g / 200 µL | 200 µL — **not weighed** | ⚠️ **added here, before hard carbon (off-standard)** |
| 6 | **Hard carbon (Kuranode)** | 3.64 g | **3.64010 g** | ⚠️ **added after SBR** — commercial Kuraray Kuranode |
| 7 | **SBR (2nd)** | — | **+1 drop — not weighed** | ⚠️ **extra drop, old disposable/burner pipette, per supervisor**, after Kuranode, before mixing (~0.025 g est.) |

All Thinky steps at standard settings (2000 rpm, 10 min). No agglomerates reported after the CMC mix.

> ⚠️ **SBR is above standard AND split around the hard carbon.** Two additions: 200 µL (calibrated pipette,
> **before** HC) **+ 1 extra drop** (old disposable/burner pipette, **after** HC, on supervisor's instruction).
> Total SBR ≈ **0.22 g est.** (0.195 + ~0.025; per-drop ≈0.025 g from the 8A bench measurement, 0.1228 g / 5
> drops). Neither addition was weighed. This raises the binder fraction and further departs from a standard build.

> **Solids weighed in boats** — boat-retention caveat applies (see standard). Approx. dried-solids active
> fraction (if used later for loading): f = 3.64010 / (3.64010 + 0.16690 + 0.10083 + 0.22 est.) ≈ **0.882**
> (was ~0.887 before the extra SBR drop; still uncertain — SBR unweighed).

---

## Coating

| Parameter | Value |
|---|---|
| Sheets | **One** |
| Doctor blade gap | 100 µm |
| Tape | **Yes** → est. +35 µm added to gap (~135 µm effective), as on 1C/2C |

---

## Drying

| Stage | Temp | Duration | Status |
|---|---|---|---|
| 1 | 30 °C | 12 h | **In progress** — started 2026-07-09 |
| 2 | 80 °C | 2 h | Pending |

> Dried together with the 2C and 3C coatings in the same oven run.

---

## Thickness — as-coated (total = coating + substrate)

> Measured 2026-07-14 after drying. Table-top micrometer (Mahr MarCator 1075 R). Readings include the
> carbon-coated foil substrate (~0.016–0.017 mm). **One sheet**, gridded **6 lengthwise × 3 widthwise =
> 18 points**, rows **3.3 cm apart** over **180 mm usable length**. Columns as recorded: **Left / Centre /
> Right**. Values in **mm**.
>
> ⚠️ **Taped-blade run (+~35 µm):** subtract ~0.035 mm from the coating before cross-sample coating
> comparisons (irrelevant to the calender gap). Substrate ~0.0165 mm separate.

| From top | Left | Centre | Right |
|---|---|---|---|
| 0 cm    | 0.087 | 0.087 | 0.088 |
| 3.3 cm  | 0.106 | 0.103 | 0.106 |
| 6.6 cm  | 0.097 | 0.099 | 0.098 |
| 9.9 cm  | 0.100 | 0.101 | 0.104 |
| 13.2 cm | 0.097 | 0.101 | 0.095 |
| 16.5 cm | 0.099 | 0.102 | 0.099 |

**Summary:** **median 0.099** · mean 0.098 · std 0.0059 · **CV 6.0%** · min 0.087 · max 0.106 (n = 18).

> **Reference-grade uniformity.** CV **6.0%** vs **22–37%** for the MMB1 biochar sheets (1C/2C/3C) — an order
> of magnitude tighter. Thin, even coating; the only mild feature is the **top row (0.087–0.088)**, ~10 µm
> below the body. Attributed to the **properly ground, small commercial-HC particle size** — the biochar
> spikes are large-particle-under-gauge artefacts that simply aren't present here. Coating (median − substrate)
> ≈ 0.083 mm.

---

## Calendering (2026-07-14)

**Target:** 10% compression on the **median** total thickness (same basis as 1C/2C/3C).

| Sheet | Median total | Roll gap set |
|---|---|---|
| 1 (only) | 0.099 mm | **0.09 mm** |

Gap = 0.90 × 0.099 = 0.089 → **0.09 mm**. Well clear of the 0.04 mm regime that destroyed the original
10A — no large-particle risk given the tight distribution.

### Outcome — ⚠️ delamination (coating peeled off the foil)

**Adhesion failure, not compression.** At **~20 point-like regions** the calender **peeled the coating clean
off the carbon-coated foil — "band-aid" style — exposing bare current collector**. The remainder of the sheet
looks intact. This is *not* the near-zero-compression spring-back seen on 10A/1C (where a thick coating
rebounded); here a thin, even layer **failed at the coating–foil interface** under the nip.

**Prime suspect: the off-standard SBR-first mix order.** This electrode's binder (SBR) was mixed into the
CMC/C45/water base **before the hard carbon was present**, plus an extra drop after (see the OFF-STANDARD
note above). The log flagged at prep time that this could leave the **binder poorly distributed over the
hard-carbon surface → weak adhesion / calendering behaviour**. The band-aid peel-off is consistent with that
risk materialising. Secondary contributors to weigh: possible roll tack/temperature and the very thin layer
offering little cohesive reserve — but interfacial adhesion is the leading explanation.

**Implications:**
- Reinforces that this is a **qualitative "what happens" test, not a clean commercial-HC benchmark** — a
  **controlled Kuranode build (standard SBR-last order)** is needed before blaming the material.
- Areas with exposed foil are **unusable for coin-cell disks**; punch disks only from **intact regions**, and
  record which grid zones are bare.

**Post-calender thickness:** not gridded (points can't be relocated 1:1); the ~20 peel-off spots are visual /
mapped qualitatively.

---

## Observations

- **Coating/thickness:** Kuranode coated **exceptionally evenly** — CV 6.0% vs 22–37% for the MMB1 biochar
  sheets. Confirms the small, properly-ground commercial-HC particle size eliminates the large-particle
  thickness spikes seen across the biochar series.
- **Calendering:** ⚠️ **coating delaminated / peeled off the foil at ~20 spots (band-aid effect)** — an
  **adhesion failure**, most likely driven by the **off-standard SBR-first mix order** (binder distributed
  without active material present). See Calendering section. Needs a controlled standard-order Kuranode build
  to separate material vs process effects.
