# BioNa Special Course — Project Context

## What this project is

Hard carbon anode materials for sodium-ion batteries (Na-ion / BioNa).
Investigating the effect of pyrolysis temperature and ramp rate on electrochemical performance.

## Sample Naming Convention

```
MMB1 - A10
│       │└─ Temperature code: digit × 100 = pyrolysis temp in °C
│       └── Series (A = hard carbon temperature series)
└────────── Material/batch series (MMB1)
```

See `Samples/Sample_Nomenclature.md` for the full matrix.

## Pyrolysis Conditions

- **Temperatures:** 600, 800, 1000, 1200 °C
- **Ramp rates:** 600/800/1000 °C → 3 °C/min only; 1200 °C → 1, 3, 10 °C/min
- **Ramp rate naming suffix** (1200 °C only): `-xCrm` e.g. `MMB1-A12-10Crm` (no `/` for path safety)
- **Total samples: 6**

## Standard Processes

- **Slurry preparation:** `Processes/Slurry_Preparation_Standard.md`
  - Thinky Mixer ARE-250, aqueous CMC/SBR binder system, C45 conductive carbon

## Directory Structure

```
BioNa_Special_Course/
├── Experimental_Data/   # Raw data per sample/experiment
├── Formal_Docs/         # Reports, thesis chapters
├── Literature_Review/   # Papers and summaries
├── Processes/           # Standard operating procedures
└── Samples/             # Sample naming, matrix, and status tracking
```
