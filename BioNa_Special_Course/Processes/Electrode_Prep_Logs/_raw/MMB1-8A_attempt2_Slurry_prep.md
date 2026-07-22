### BioNa Experiment 58
### Planned: 2026-07-22 (slurry + coating).
### 2026-07-21 attempt STOOD DOWN: both drying furnaces booked, so the run was stopped
### before the hard carbon was added. MMB1_8A hard carbon NOT used - full amount still available.
### The water/CMC/C45 premix from 21/07 was DISCARDED - start completely fresh on 22/07.
### Numbers entered on 21/07 have been cleared; this sheet is blank and ready to run.
###
### MMB1_8A SLURRY #2 (redo). Batch #1 was anomalous -> see MMB1-8A_Slurry_prep.md /
### MMB1_8A_Electrode_Prep.md. Known issues in batch #1 to avoid here:
###   - CMC would not dissolve -> 2 restarts + 7 min extra mixing (SPRINKLE the CMC, don't dump)
###   - SBR dosed as "5 drops" (0.1228 g, too low) -> +1 drop added -> composition off. USE 200 uL PIPETTE.
###   - Resulting coating was implausibly thin/smooth (~5-20 um) - suspected SBR excess and/or HC loss.
### Fill in the blanks as you go; aim values are stated in brackets.

4.9ml water (aim 4.9g / 4.9mL, pipete) | 5.0199g (initial/peak reading; note drift - evaporation, not subtracted)
  [reading was decreasing = evaporation. +0.12g / +2.4% over aim; solvent only, does not enter dry composition]
0.09986g CMC added to thinky container (aim 0.100g)  [SPRINKLE across water surface, don't dump -> avoids persistent agglomerates]
thinky at std settings (2000rpm, 10min)
agglomerates after CMC mix? yes - barely noticeable, much better than batch #1 (sprinkling worked).
  Proceeded to C45 addition WITHOUT extra mixing (extra mix time: 0 min @ 2000rpm).
  Rationale: 3 further 10-min mix cycles still to come; expected to break down. FLAG for coating inspection.
0.16650g C45 added (aim 0.167g)  [weighed out in advance, added after CMC mix]
thinky at std settings (2000rpm, 10min)
2.5ml water added with pipete (aim 2.5g / 2.5mL) | NOT MEASURED (pipette volume only, no balance reading)
thinky at std settings (2000rpm, 10min)
3.23379g MMB1_8A hard carbon (aim 3.64g)  [ADD BEFORE SBR! confirm powder actually transferred - check boat + container]
  [SHORT: 3.23379g was ALL the MMB1_8A remaining - not a dosing choice, a stock limit. 0.888x the 3.64g aim.
   Reading drifted UP to 3.23424g (+0.00045g, +0.014%) = moisture pickup by the HC, opposite sign to the
   water evaporation drift. Negligible; initial reading 3.23379g taken as the value.
   DECISION: did NOT restart. CMC + C45 were already in the pot and cannot be scaled back, so the only
   available lever was SBR -> scaled to 0.888x (200uL -> 178uL) to keep total binder near target.
   Resulting dry composition vs target (HC/C45/CMC/SBR wt%):
     target        88.7 / 4.07 / 2.44 / 4.75   (total binder 7.19%)
     this batch    88.0 / 4.53 / 2.72 / 4.72   (total binder 7.44%)
   Rejected 200uL-as-written: would have given SBR 5.28%, total binder 7.98% (+11% rel) - i.e. exactly the
   SBR-excess failure mode batch #1 is suspected of. Rejected full restart: 0.7pp active-mass deviation is
   smaller than the unquantified boat-retention bias, all masses are known to 0.1mg so loading and
   gravimetric capacity remain exactly computable, and a restart risked the drying-furnace slot again.
   BOAT: shaken + flicked to transfer as much HC as possible, but the boat was NOT reweighed - it was
   discarded straight after, so the retained mass is unrecoverable. 3.23379g is therefore an UPPER BOUND on
   the HC actually delivered; true active mass is slightly lower and the HC wt% slightly below the 88.0%
   quoted above. Direction of the bias is known, magnitude is not.
   NOT FIXABLE: this is the LAST slurry of the campaign (JCR, 22/07/2026) - no further batches will be
   made, so boat retention CANNOT be quantified retrospectively. It stays an unquantified bias for every
   sample in the study and must be carried into the report as a stated limitation, not a TODO.
   Argument for why it largely cancels (JCR): retention is a ~constant FRACTION of the powder, so it is a
   ~constant wt% offset applied to all samples alike, and cross-sample comparison is preserved.
   Caveat on that argument: retention is governed by particle size and static, both of which plausibly
   track pyrolysis temperature (higher-temp chars are harder and grind differently - see the grind/
   calendering note in Slurry_Preparation_Standard.md). If retention is temperature-dependent, the bias
   correlates with the study's independent variable and would distort the trend rather than offset it.
   Scale: ~1% retention -> active fraction 88.0% -> 87.1% -> ~1% underestimate of mAh/g. Negligible if flat
   across temperature; only matters if it is markedly steeper for 6A/8A than 12A. Unresolved either way.
   WATCH: solids content drops 35.7% -> 33.3% (water already added, cannot be removed). Expect a THINNER
   wet film than 6A/10A/12A at the same 100um gap. Do not confuse this with batch #1's thin-coating anomaly.]
thinky at std settings (2000rpm, 10min)
178 microliters SBR added with pipete (REVISED aim ~0.173g / 178uL - scaled 0.888x for the short HC, see above)
  | ADDED 22/07/2026 - single 178uL dose, bottle shaken, no top-ups. Mass: NOT MEASURED (volume only).
  [SBR mass is therefore INFERRED, not measured: 0.195g x (178/200) = ~0.173g, assuming the SOP's
   0.195g/200uL reference and pipette linearity. That reference has been weighed exactly ONCE and has no
   known spread - and no further slurries will be made, so it can never be improved. Every SBR wt% quoted
   for this batch (4.72%) rests on that single unreplicated calibration. State as a limitation.]
  [SHAKE SBR bottle before dispensing. No "drops" this time - pipette only, single dose, no top-ups.]
  [WEIGH THIS DOSE: the SOP's 0.195g/200uL reference has been weighed only ONCE (open TODO in
   Slurry_Preparation_Standard.md). A second point at a different volume is nearly free here.]
thinky at std settings (2000rpm, 10min)
coating: 1 sheet, 100 micrometer doctor blade, tape? YES (est +35um -> effective gap ~135um)
  [COATING SUCCESSFUL - no blade catching / kinks / tearing this time, unlike 6A, 10A and 8A batch #1.]
  [TAPE + COMPARABILITY: tape partly offsets this batch's low solids content (33.3% vs 35.7%).
   Rough dry-thickness scaling vs a standard untaped coat: 1.35 (tape) x 0.933 (solids) = ~1.26x.
   Tape usage across the campaign is SPLIT and this matters for cross-sample thickness comparison:
     NO tape  - MMB1_6A, MMB1_8A batch #1, MMB1_10A
     TAPE     - MMB1_12A_1C, _2C, _3C, and now MMB1_8A batch #2 (this run)
   So 8A#2 should land THICKER than 6A/10A and slightly THINNER (~0.93x) than the taped 12A series.
   Do not read an 8A-vs-6A/10A loading difference as a material effect - it is a coating-protocol
   difference. Normalise by measured disk mass, not by assumed thickness.]
drying: 30C for 12 h + 80C for 2 h  (sheet said std 6h+2h, but 6A/8A#1/10A all actually ran 12h+2h and
  were flagged "to rectify times" - 12h+2h is the de facto standard and is what was used here)
  [SPLIT RUN: 12h at 30C started 22/07/2026 by JCR; the 2h at 80C hold will be completed by NIHAT on
   23/07/2026. Then BUCHI (vacuum) oven. Handover noted in case the timing needs reconstructing later.]

Thickness (micrometer, mm) after drying — top to bottom:
  sheet 1: ______ ______ ______ ______
  sheet 2: ______ ______ ______ ______
  bare foil reference: ______

Visual and other notes:
- Coating LOOKED NORMAL overall - no kinks caught, no tearing, no blade relocation (contrast 6A / 10A /
  8A batch #1, which all had blade-catching or tearing).
- BUT: slurry crept round to the SIDES of the doctor blade and dragged PROGRESSIVELY MORE as the coat
  advanced. JCR's prediction at the time of coating: the BOTTOM of the sheet should be THICKER than the top.
- Likely mechanism: this batch is the lowest-solids slurry of the campaign (33.3% vs 35.7% - the HC was
  stock-short at 3.23379g but the water was already in and could not be removed). Lower solids -> lower
  viscosity -> more creep past the blade edges, accumulating along the pass. Compare MMB1-10A_Slurry_prep.md,
  which describes slurry attaching to the BACKSIDE of the blade with "viscosity dependent release" - probably
  the same phenomenon, and it supports viscosity as the driver rather than blade geometry alone.
- TESTABLE: the thickness rows above are ordered TOP TO BOTTOM, so a monotonic increase down the sheet
  would confirm the prediction; a flat profile would refute it and point at blade geometry instead.
  NOTE: this only gets answered if Nihat measures the sheet on 23/07 - JCR decided NOT to request it,
  so the prediction may simply go untested. Recorded here so it stays falsifiable either way.
- CAUTION for disk selection: if the gradient is real, disks punched from the bottom of the sheet carry
  more mass than disks from the top. Record WHERE on the sheet each disk came from, and always normalise
  capacity by that disk's own measured mass rather than a sheet-average loading.
