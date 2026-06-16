# BioNa Special Course — Project Context

## What this project is

Hard carbon anode materials for sodium-ion batteries (Na-ion / BioNa).
Investigating the effect of pyrolysis temperature and ramp rate on electrochemical performance.

## Sample Naming Convention

```
MMB1_10A
│    │ └── Series letter: "A" = first synthesis run
│    └──── Temperature code: temp(°C) ÷ 100
└───────── Material: MMB1 = BioNa standard biochar
```

Ramp rate variants (1200 °C only) append `-xC/min`; use `-xCrm` for path-safe filenames.  
See `Samples/Sample_Nomenclature.md` for the full matrix.

## Pyrolysis Conditions

- **Temperatures:** 600, 800, 1000, 1200 °C (other temps exist in lab but out of scope)
- **Atmosphere:** N2 (50%)
- **Standard ramp:** 180 °C/h (3 °C/min); 1200 °C also run at 60 °C/h (1°C/min) and 600 °C/h (10°C/min)
- **Hold time:** 2 h
- **Total samples: 6** (5 completed, 1 pending — MMB1_12A_10Crm)

## Standard Processes

- **Slurry preparation:** `Processes/Slurry_Preparation_Standard.md`
  - Thinky Mixer ARE-250, aqueous CMC/SBR binder system, C45 conductive carbon

## Directory Structure

```
BioNa_Special_Course/
├── Experimental_Data/   # Raw data per sample/experiment (gitignored — OneDrive)
├── Formal_Docs/         # Reports, supervisor updates, thesis chapters
├── Instruments/         # Equipment names and specs
├── Literature_Review/   # Papers (PDFs gitignored) and reading log
├── Processes/           # Standard operating procedures and failure logs
└── Samples/             # Sample naming, pyrolysis matrix, and status tracking
```
