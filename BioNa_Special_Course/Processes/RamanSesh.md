# Raman Spectroscopy — SOP & Session Record

Software: **WiRE 4.4**. Instrument per `Instruments/Instruments.md`.

## Calibration (run first, every session)

1. Run a calibration with the **silicon** reference.
2. Ensure the laser is closed and open the cabinet doors.
3. Calibrate using the **shiny side** of the Si wafer.
4. The laser must sit within the dot at the centre of the image; with sufficient
   resolution, run and look for the Si peak at **520.5 cm⁻¹**.
5. If off-target, use **Tools → Calibration** to move it to 520.5 cm⁻¹.

## Sample Preparation

- Powders finely ground beforehand (mortar & pestle).
- Take a small amount of sample (**< 5 mg**), add a few drops of **ethanol** to make a slurry.
- Let dry **~5 min** on a glass plate, then load into the Raman.

## Operating Parameters — "BioNa Standard Procedure"

| Parameter | Value |
|---|---|
| Laser | Green, **532 nm** |
| Laser power | **5 %** (`LP5`) |
| Accumulation time | **60 s** (`60s`) |
| Number of accumulations | **4** (`4Ac`) |
| Cosmic-ray removal | ON |
| Mode | Static, peaks centred ~1400 cm⁻¹ (D/G envelope) |

Filename tag legend: `60s` = accumulation time · `4Ac` = number of accumulations · `LP5` = laser power 5 %.

## Provenance

- Acquisition performed by **Siddharth Jain** (s242569); context with Nihat Ege Şahin (negsa)
  and Peter Curran (pcurran). Data measured Tue **2026-06-16/17**, delivered by email
  **2026-06-19**. (Source: "Raman Data" email thread — captured here so the PDF can be retired.)

## Data Files → Samples

Raw spectra (tab-separated `#Wave  #Intensity`, ~1015 pts, ~790–1936 cm⁻¹) in
`Experimental_Data/Raman/` (OneDrive-managed, gitignored).

| File | Sample | Pyrolysis | Notes |
|---|---|---|---|
| `MMB1A_base-biochar_60s-4Ac-LP5.txt` | MMB1A (base biochar) | untreated | |
| `MMB1_6A_60s-3Ac-LP5.txt` | MMB1_6A | 600 °C, 3 °C/min | **3 accumulations** (off-standard) |
| `MMB1_6A_15s-4Ac-LP5.txt` | MMB1_6A | 600 °C, 3 °C/min | **15 s** acquisition (off-standard) |
| `MMB1_8A_60s-4Ac-LP5.txt` | MMB1_8A | 800 °C, 3 °C/min | standard |
| `MMB1_10A_69s-4Ac-LP5.txt` | MMB1_10A | 1000 °C, 3 °C/min | filename token reads `69s` (likely typo for 60 s — verify) |
| `MMB1_12A_60s-4Ac-LP5.txt` | MMB1_12A | 1200 °C, 3 °C/min (standard ramp) | |
| `MMB1_12A_1Crm_60s-4Ac-LP5.txt` | MMB1_12A_1Crm | 1200 °C, 1 °C/min | slow-ramp variant |

> `MMB1_12A_10Crm` (1200 °C, 10 °C/min): Raman pending — pyrolysis not yet run.
