# Data Processing — Szymon Web App

Web application (built by Szymon) for processing spectroscopy data. Used for this project's
**Raman** and **XRD** data.

## What it does

- Background/baseline removal.
- Automatic calculation of key metrics.
- Handles Raman, XRD, and other data types.

## Input format

- The app expects **`.mbr`** files — **not** the raw `.txt` / xy spectra.
- **TODO:** confirm how `.mbr` is produced/exported (from WiRE?) for the existing Raman data in
  `Experimental_Data/Raman/` (currently stored as tab-separated `.txt`).

## Access

- Hosted at **biona.energy** / **charts.biona.energy** (client-certificate authenticated).
- Certificates and password are stored locally in **`SzymonWebApp/`** (repo root):
  - `Archive/Joao_Maria_De_Sacadura_Botte_Corte-Real.pfx` — personal client certificate.
  - `Archive/biona.energy.crt`, `Archive/charts.biona.energy.crt` — server certs.
  - `password.md` — certificate password.

> 🔒 **Do not commit `SzymonWebApp/` to git.** It holds a personal certificate and password and the
> repo pushes to GitHub. It is excluded via `.gitignore` — keep it that way.

## Workflow (to document)

- **TODO:** record the step-by-step — convert/export spectra to `.mbr`, load into the app, and note
  where processed outputs / metrics are saved.
- Relevant raw data: `Experimental_Data/Raman/` (`.txt`; see `Processes/RamanSesh.md`).
