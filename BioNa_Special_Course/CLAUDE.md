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

## Characterization

- **Raman:** `Processes/RamanSesh.md` (calibration: Si reference @ 520.5 cm⁻¹, WiRE 4.4).
  - Standard acquisition: 532 nm green laser, 5% power, 60 s × 4 accumulations, cosmic-ray
    removal ON, static mode (D/G bands ~1350/1580 cm⁻¹).
  - Raw `.txt` spectra (tab-separated `#Wave  #Intensity`): `Experimental_Data/Raman/`,
    named `<SampleID>_<accumTime>-<nAccum>-LP<power%>.txt` (e.g. `MMB1_8A_60s-4Ac-LP5.txt`).
    Full file→sample mapping and provenance in `Processes/RamanSesh.md`.

## Directory Structure

```
BioNa_Special_Course/
├── Experimental_Data/   # Raw data per sample/experiment (gitignored — OneDrive)
│                        #   └── Raman/  raw .txt spectra
├── Formal_Docs/         # Reports, supervisor updates, thesis chapters
├── images/              # Lab photos by process step (Pyrolysis, Raman, XRD,
│                        #   Electrode_Calendering, Sample_Prep); see images/README.md
├── Instruments/         # Equipment names and specs
├── Literature_Review/   # Papers (PDFs gitignored) and reading log
├── Processes/           # Standard operating procedures and failure logs
└── Samples/             # Sample naming, pyrolysis matrix, and status tracking
```
