# Sample Nomenclature & Pyrolysis Matrix

## Naming Convention

```
MMB1_10A - 1C/min
│    │ │      └─ Ramp rate suffix (1200 °C variants only)
│    │ └──────── Series letter: "A" = first synthesis run/batch
│    └────────── Temperature code: temp(°C) ÷ 100  (e.g. 10 = 1000 °C)
└─────────────── Material: MMB1 = BioNa standard biochar
                 (MMB2 exists but not used in this study)
```

> Path-safe ramp suffix for file/folder naming: use `xCrm` instead of `x C/min`  
> e.g. `MMB1_12A_10Crm`

---

## Pyrolysis Conditions (all samples)

| Parameter | Value |
|---|---|
| Atmosphere | N2 (50%) |
| Hold time | 2 h |
| Standard ramp | 180 °C/h (= 3 °C/min) |

---

## Full Sample Matrix

| Sample ID | Date | By | Temp (°C) | Ramp (°C/h) | Mass in (g) | Mass out (g) | Yield (%) | Coin Cell | XRD | XRF | N2-BET | Raman |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| MMB1A (base biochar) | — | — | — | — | — | — | — | — | PENDING | — | — | DONE |
| MMB1_6A | 26-05-2026 | NS | 600 | 180 | 10.0015 | 6.8485 | 68.47% | NOT DONE | DONE | — | — | DONE |
| MMB1_8A | 27-05-2026 | JM+NS | 800 | 180 | 10.0002 | 6.5844 | 65.84% | NOT DONE | DONE | — | — | DONE |
| MMB1_10A | 28-05-2026 | JM+NS | 1000 | 180 | 10.0095 | 6.3498 | 63.43% | NOT DONE | DONE | — | — | DONE |
| MMB1_12A | 01-06-2026 | JM+NS | 1200 | 180 | 10.0062 | 6.2284 | 62.24% | NOT DONE | DONE | — | — | DONE |
| MMB1_12A_1Crm | 29-06-2026 | NS | 1200 | 60 | 10.0015 | 6.3281 | 63.27% | — | DONE | — | — | DONE |
| MMB1_12A_10Crm | — | — | 1200 | 600 | — | — | — | — | — | — | — | — |
| MMB1_12A_2Crm | xx-2026 | (given to JCR) | 1200 | 120 | — | — | — | — | DONE | — | — | INBOUND |

> **MMB1_12A_10Crm: CANCELLED** — the furnace cannot achieve a 10 °C/min (600 °C/h) ramp.
> Replaced by **MMB1_12A_2Crm** (1200 °C, 120 °C/h = 2 °C/min), which has already been synthesised
> and handed to JCR. **XRD now done** (supervisor re-run, 2026-07); **Raman still inbound**.
>
> ⚠️ Study impact: the 1200 °C ramp series is now **1 / 2 / 3 °C/min** (all slow ramps) instead of
> **1 / 3 / 10 °C/min** — the fast-ramp end of the design is lost.

---

## Notes

- XRD raw data on BioNa Teams → General Results → MMB1A folder.
- **XRD re-run (2026-07)** by supervisor on all **post-pyrolysis** samples (6A / 8A / 10A / 12A / 1Crm / 2Crm).
  Only the **base biochar (MMB1A)** remains — João **ground it finely on 2026-07-14** and handed it over for the
  test, so its XRD is **PENDING**.
- Grinding completed for all existing samples before slurry prep.
- MMB1_10A: material may be limited — first coating attempt failed (calendering). Assess remaining powder before remaking slurry. See `Processes/Calendering_Notes.md`.
