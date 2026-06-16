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
| MMB1_6A | 26-05-2026 | NS | 600 | 180 | 10.0015 | 6.8485 | 68.47% | NOT DONE | DONE | — | — | — |
| MMB1_8A | 27-05-2026 | JM+NS | 800 | 180 | 10.0002 | 6.5844 | 65.84% | NOT DONE | DONE | — | — | — |
| MMB1_10A | 28-05-2026 | JM+NS | 1000 | 180 | 10.0095 | 6.3498 | 63.43% | NOT DONE | DONE | — | — | — |
| MMB1_12A | 01-06-2026 | JM+NS | 1200 | 180 | 10.0062 | 6.2284 | 62.24% | NOT DONE | DONE | — | — | — |
| MMB1_12A_1Crm | 29-06-2026 | NS | 1200 | 60 | 10.0015 | 6.3281 | 63.27% | — | DONE | — | — | — |
| MMB1_12A_10Crm | xx-06-2026 | JM+NS | 1200 | 600 | — | — | — | — | — | — | — | — |

> MMB1_12A_10Crm: **NOT DONE** — pyrolysis pending as of 2026-06-16.

---

## Notes

- XRD raw data on BioNa Teams → General Results → MMB1A folder.
- Grinding completed for all existing samples before slurry prep.
- MMB1_10A: material may be limited — first coating attempt failed (calendering). Assess remaining powder before remaking slurry. See `Processes/Calendering_Notes.md`.
