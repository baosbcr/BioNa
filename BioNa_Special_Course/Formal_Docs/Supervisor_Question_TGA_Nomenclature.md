QUESTION TO NIHAT - TGA/DTA sample nomenclature + missing metadata

Date drafted: 2026-07-22
Addressed to: Nihat Ege Sahin (operator on all four runs)
STATUS: SENT 2026-07-22 - awaiting reply. Until it arrives, the four TGA runs stay unattributed
and must not be plotted against pyrolysis temperature.

Context: Four NETZSCH STA 409 PC/PG runs (16-21 July 2026) are in Experimental_Data/TGA_DSC/.
The sample codes do not follow Samples/Sample_Nomenclature.md, so the data cannot be attributed
to a pyrolysis condition. Instrument details recovered from the file headers are in
Instruments/Instruments.md.

Everything between the two ===== lines is plain text - copy it straight into the email body.

=====================================================================

Subject: TGA runs 16-21 July - missing info

Hi Nihat,

Can you please complete the missing info on the four TGA runs? I got the instrument
parameters out of the file headers; these are the things the files don't tell me.

  1. BNa-MMB1Ag_Air         16 Jul, 09:58    8.27 mg
  2. BNa-MMB1Ag_N2          21 Jul, 10:50    6.02 mg
  3. BNa-MMB2Am_Air         16 Jul, 21:24    8.71 mg
  4. NS.51B_MMB2A-13-1Cww   17 Jul, 09:50    7.24 mg

1. What material is each one? The codes don't map to our sample IDs (MMB1_6A, MMB1_8A,
MMB1_10A, MMB1_12A, MMB1_12A_1Crm, MMB1_12A_2Crm). Is MMB1Ag the base MMB1A biochar, and
what is the "g"? What is the "m" in MMB2Am? For NS.51B_MMB2A-13-1Cww - should I read it as
MMB2A at 1300 C, 1 C/min, and what is "ww"?

2. Are there runs on the pyrolysed series? None of the six study samples appears here. If
these four are all that exist, is TGA on 6A/8A/10A/12A worth booking?

3. Atmosphere: the header only says "gas 1" / "gas 2" at 50 mL/min. I've assumed gas 1 = air,
gas 2 = N2 from the file names - correct? And which gas grade?

4. Temperature: the CSVs end at about 820 C at t = 233 min, but 30 to 900 C at 5 K/min plus
the 60 min hold should be at 900 C. Thermocouple offset, run stopped early, or an export
artefact?

5. Small items:
- No raw .ngb-dsv for NS.51B_MMB2A-13-1Cww - can you send it?
- Each run has a plain .tif plus _ns / _nss versions - which is the final evaluation?
- Is the DTA signal usable quantitatively, or should I treat these as TG only?

Thanks,
Joao

=====================================================================

WHAT WE ALREADY HAVE (no need to ask)

Recovered from the export headers - see Instruments/Instruments.md for the full entry:
instrument model, crucible type/mass, reference setup, temperature programme, ramp, hold,
purge flow, sample masses, baseline-correction and calibration files, operator, NETZSCH
project number (117134), run dates, and final mass-% for each run
(air: 9.67 % / 5.88 % / 2.87 %; N2: 70.30 %).

OPEN ITEMS THIS QUESTION IS MEANT TO CLOSE

- Map MMB1Ag, MMB2Am, NS.51B_MMB2A-13-1Cww to Samples/Sample_Nomenclature.md
  (open checkbox, section 9 of Processes/Raw_Data_Triage_Notes_2026-07-21.md)
- Confirm gas 1 = air / gas 2 = N2, and gas grade
- Resolve the ~820 C-at-233-min discrepancy
- Obtain the missing .ngb-dsv for NS.51B_MMB2A-13-1Cww
- Identify the authoritative .tif / evaluation
- Decide whether TGA on the six study samples is in scope
