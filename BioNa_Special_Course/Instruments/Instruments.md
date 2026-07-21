# Instruments

## Thinky Mixer ARE-250

| Parameter | Value |
|---|---|
| Model | ARE-250 |
| Type | Planetary centrifugal mixer |
| Standard recipe speed | 2000 rpm |
| Standard recipe time | 10 min per step |
| Used for | Slurry preparation |

---

## Analytical Balance

| Parameter | Value |
|---|---|
| Model | Mettler Toledo **AX205** (semi-micro analytical balance) |
| Readability (d) | **0.01 mg** (fine range) / **0.1 mg** (full range) — printed on the instrument |
| Repeatability (typ.) | ~0.015 mg fine range *(manufacturer typical — confirm from datasheet)* |
| Used for | Slurry component weighing; electrode-disk mass; foil tare |

> Disk masses were recorded to 0.01 mg (fine range).
> **Foil tare MEASURED 2026-07-21: 5.5255 mg** (mean of 11 blanks cut with the standard 12.7 mm die,
> SD 0.057 mg) — supersedes the earlier assumed 5.50 / 5.55 mg values.
> Full record: `Processes/Foil_Tare_Measurement.md`.
> Uncertainty used in `Processes/Electrode_Prep_Logs/disk_loading.py`.

---

## Pipettes

| Parameter | Value |
|---|---|
| Model | Eppendorf **Research plus** (all pipettes) |
| Used for | Slurry water/binder dosing; **SBR standard = 200 µL** (see `Processes/Slurry_Preparation_Standard.md`) |

> Manufacturer accuracy/precision specs are volume-dependent — pull the per-channel figures if slurry
> composition uncertainty is ever needed.

---

## Coin-Cell Electrode Disk Cutter (stamper)

| Parameter | Value |
|---|---|
| Model | CES coin-cell electrode disk cutter |
| Die used | **12.7 mm Ø** (½″) → area **1.2668 cm²** |
| Die tolerance | **UNKNOWN** — no manufacturer spec found. Currently *assumed* ±0.05 mm |
| Used for | Punching electrode disks for coin-cell assembly |

> ⚠️ The die-diameter tolerance is the **dominant** term in areal mass-loading uncertainty
> (see `Processes/Electrode_Prep_Logs/MMB1_6A_CoinCell_Disks.md`). Getting the real value matters most.

---

## Furnace (Drying)

| Parameter | Value |
|---|---|
| Model | Memmert **UF55plus** (universal forced-air oven) |
| Atmosphere | Air (forced convection) |
| Used for | Electrode drying (30 °C / 6 h → 80 °C / 2 h) |

> Not to be confused with the pyrolysis furnace — separate instrument, separate atmosphere.
> Also distinct from the **Büchi vacuum oven inside the glovebox** (see below, TBD).

---

## Calendering Roller

| Parameter | Value |
|---|---|
| Model | CES **JS100** |
| Roller temperature | 60 °C |
| Gap (current) | 0.04 mm |
| Used for | Electrode densification |

> Standard compression target (fixed ratio vs fixed final thickness) still to be decided —
> see `Biona_Academy/Open_Questions.md`.

---

## Coating Table / Film Applicator

| Parameter | Value |
|---|---|
| Model | **K101 Control Coater** (RK Print Coat Instruments Ltd) |
| Blade speed | TBD (observed critical — to standardise) |
| Used for | Doctor-blade coating of slurry onto foil |

> See `Biona_Academy/Open_Questions.md` (doctor blade / coating table TODOs).

---

## Doctor Blade

| Parameter | Value |
|---|---|
| Model | TQC Sheen / Industrial Physics **Baker applicator, 60 mm** (part **VF2147-376**) |
| Available gaps | 50 / 100 / 150 / 200 µm *(the "20" on the label is an abbreviation for 200 µm — there is no 20 µm option)* |
| Gap used | 100 µm |
| Tape | None (tape vs no-tape to be tested) |
| Used for | Defining wet coating thickness |

---

## Table-Top Micrometer (thickness gauge)

| Parameter | Value |
|---|---|
| Indicator | Mahr **MarCator 1075 R Digital Indicator** (LCD readout, not analog dial — order no. **4336030** variant) |
| Stand / base | Mahr **820 NG/FG** measuring stand; reference surface **DIN 876 grade 0** |
| Resolution | 0.001 mm (1 µm) — matches recorded thickness data; identifies the 4336030 order-no. variant |
| Uncertainty | Manufacturer-specified **span of error G = ±0.005 mm (5 µm)**, "in any zero point" (Mahr datasheet, not a DIN 878 figure — supersedes prior ±1–2 µm estimate) |
| Used for | Coating / foil thickness measurement |
| Substrate baseline | Carbon-coated Al foil ≈ 0.016–0.017 mm |

> All reported coating thicknesses are **total** (coating + substrate). See
> `Biona_Academy/Open_Questions.md`.

---

## Szymon Web App (data processing)

| Parameter | Value |
|---|---|
| Host | biona.energy / charts.biona.energy (client-cert auth) |
| Input format | `.mbr` (not raw `.txt`/xy) |
| Used for | Raman / XRD background removal + auto key metrics |

> See `Processes/Data_Processing_SzymonWebApp.md`. Credentials in `SzymonWebApp/` (git-ignored).

---

## Raman Spectrometer

| Parameter | Value |
|---|---|
| System | Renishaw (WiRE **4.4** control software) — *exact model TBD (inVia?)* |
| Laser | Green, **532 nm** |
| Standard acquisition | 5 % power, 60 s × 4 accumulations, static mode, cosmic-ray removal ON |
| Calibration | Si reference @ **520.5 cm⁻¹** |
| Used for | D/G band analysis of hard carbon (~1350 / 1580 cm⁻¹) |

> Full SOP and file-naming in `Processes/RamanSesh.md`.

---

## XRD

| Parameter | Value |
|---|---|
| Model | Malvern Panalytical **Aeris** (benchtop) |
| Specs | TBD (exact configuration / source to be supplied by João) |
| Used for | Crystallographic characterisation of hard carbon |

> Some XRD/Raman data supplied by supervisor (see `CLAUDE.md` note on MMB1_12A_2Crm).

---

## Pyrolysis Furnace

| Parameter | Value |
|---|---|
| Model | TBD (located in Furnace Lab) |
| Atmosphere | N2 (50%) |
| Standard ramp | 180 °C/h (3 °C/min) |
| Hold time | 2 h |
| Temperature range used | 600–1300 °C |
| Used for | Hard carbon pyrolysis |

> **Tube furnace model still TBD** (located in Furnace Lab).

---

## Glovebox — *TBD (info pending)*

| Parameter | Value |
|---|---|
| Model | TBD (info to come from João) |
| Atmosphere | TBD (Ar assumed for Na-ion work) |
| Used for | Coin-cell assembly (Na metal handling) |

---

## Büchi Vacuum Oven (inside glovebox) — *TBD (info pending)*

| Parameter | Value |
|---|---|
| Model | TBD (info to come from João) |
| Used for | Final electrode / disk drying under vacuum before cell assembly |

---

## Coin-Cell Crimper / Press — *TBD (not yet documented)*

| Parameter | Value |
|---|---|
| Model | TBD |
| Used for | Sealing (crimping) coin cells after stacking |

---

## Battery Cyclers / Potentiostats — **Bio-Logic VMP3 + MPG-2**

Two **Bio-Logic SAS** (Made in France) multichannel instruments, both driven from the **same PC and the
same EC-Lab session** — they appear together in the EC-Lab *Devices* list.
Documented 2026-07-21 from the instrument labels and the software screen
(`images/Cycling/`).

| Parameter | Instrument 1 | Instrument 2 |
|---|---|---|
| Manufacturer | Bio-Logic SAS (France) | Bio-Logic SAS (France) |
| Model | **VMP3** | **MPG-2** |
| Serial number | **0509** | **0124** |
| EC-Lab device ID | `VMP3-USB-509` | `MPG-2-USB-124` |
| Connection | USB | USB |
| Mains | 110–240 Vac, 50/60 Hz | 110–240 Vac, 50/60 Hz |
| Fuses | 6.3 AF | 6.3 AF |
| Max power | 600 W | 600 W |
| Used for | Galvanostatic cycling / electrochemical testing of the Na half-cells | same |

**Software:** **EC-Lab V11.62** (Bio-Logic), single install controlling both instruments.
Techniques available/used include OCV, PEIS and GCPL — see `Biona_Academy/Open_Questions.md` for the
protocol details still to be recorded.

**Photos:** `images/Cycling/Biologic_VMP3_sn0509_Label.jpg`,
`images/Cycling/Biologic_MPG2_sn0124_Label.jpg`, `images/Cycling/ECLab_V11.62_DeviceList.jpg`.

> ⚠️ **Not yet recorded: which cells ran on which instrument.** All cells to date (CC19–CC41) are logged
> without an instrument/channel assignment. VMP3 and MPG-2 are different hardware (the MPG-2 is a
> battery-cycling-oriented unit; the VMP3 is the general-purpose modular potentiostat), so any
> instrument-dependent artefact would be invisible in the current logs. **Record instrument + channel
> per cell from here on.**
>
> ⚠️ **EC-Lab version** read off a photographed screen — **V11.62** is legible but worth confirming in
> *Help → About* before quoting it in a report.
>
> ⚠️ The second cycler was previously noted as sounding like *"Kuwara"/"Kuwahara"* — that does **not**
> match either unit here. Either it was a mishearing of MPG-2, or a **third instrument** exists that is
> not on this PC. Confirm.
