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

## Furnace (Drying)

| Parameter | Value |
|---|---|
| Model | TBD |
| Atmosphere | Air |
| Used for | Electrode drying (30 °C / 6 h → 80 °C / 2 h) |

> Not to be confused with the pyrolysis furnace — separate instrument, separate atmosphere.

---

## Calendering Roller

| Parameter | Value |
|---|---|
| Model | TBD |
| Roller temperature | 60 °C |
| Gap (current) | 0.04 mm |
| Used for | Electrode densification |

> Standard compression target (fixed ratio vs fixed final thickness) still to be decided —
> see `Biona_Academy/Open_Questions.md`.

---

## Coating Table / Film Applicator

| Parameter | Value |
|---|---|
| Model | TBD |
| Blade speed | TBD (observed critical — to standardise) |
| Used for | Doctor-blade coating of slurry onto foil |

> See `Biona_Academy/Open_Questions.md` (doctor blade / coating table TODOs).

---

## Doctor Blade

| Parameter | Value |
|---|---|
| Model | TBD |
| Gap used | 100 µm |
| Tape | None (tape vs no-tape to be tested) |
| Used for | Defining wet coating thickness |

---

## Table-Top Micrometer

| Parameter | Value |
|---|---|
| Model | TBD |
| Used for | Coating / foil thickness measurement |
| Substrate baseline | Carbon-coated Al foil ≈ 0.016–0.017 mm |
| Uncertainty | TBD |

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

## Pyrolysis Furnace

| Parameter | Value |
|---|---|
| Model | TBD (located in Furnace Lab) |
| Atmosphere | N2 (50%) |
| Standard ramp | 180 °C/h (3 °C/min) |
| Hold time | 2 h |
| Temperature range used | 600–1300 °C |
| Used for | Hard carbon pyrolysis |
