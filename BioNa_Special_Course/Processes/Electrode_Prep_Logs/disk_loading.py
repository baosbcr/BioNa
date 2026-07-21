"""
Coin-cell disk mass-loading + uncertainty analysis.

Given punched electrode disks (measured total mass each), a foil-tare mass, a cutting-die
diameter and the slurry solids composition, computes per-disk:
  - coating (dried-solids) mass
  - coating areal loading  [mg/cm^2]
  - hard-carbon (active) areal loading  [mg/cm^2]
with measurement-uncertainty propagation, and population statistics.

>>> DEVICE UNCERTAINTIES BELOW ARE PLACEHOLDERS <<<
Instruments.md currently lists no analytical balance, no die tolerance, and micrometer
uncertainty = TBD. Update U_BAL, U_FOIL, U_D once the real specs are known.

Run:  python disk_loading.py
"""
import numpy as np

# ---- device uncertainties (1 sigma) ----
# Balance: Mettler Toledo AX205, d = 0.01 mg (fine) / 0.1 mg (full); repeatability ~0.015 mg fine range.
U_BAL  = 0.000015  # g, per disk weighing (fine range, 0.01 mg readability; AX205 repeatability).
U_FOIL = 0.0000566 # g, foil-tare uncertainty = MEASURED disk-to-disk SD of the blanks (0.057 mg, 1.0%).
                   # Supersedes the old 0.029 mg resolution-based placeholder, which understated it.
                   # WEAK ESTIMATE: only 2 of the 11 blanks were resolved individually -> 1 dof.
                   # Weigh the 11 blanks one at a time to firm this up (cheap, and 8A depends on it).
D_MM   = 12.70     # cutting-die diameter, mm (nominal 1/2", CES disk cutter)
U_D_MM = 0.05      # mm, ASSUMED die-diameter tolerance — CES spec UNKNOWN. Dominant term; confirm.

# ---- foil tare: MEASURED 2026-07-21, no longer assumed ----
# 5.5255 mg = mean of 11 carbon-coated foil blanks cut with the SAME 12.7 mm die as every
# electrode disk in this project, weighed cumulatively (see Biona_Academy/Open_Questions.md).
# Supersedes both the old 5.50 mg (-0.46%) and the supervisor's 5.55 mg (+0.44%) — it sits
# almost exactly between them, and both were within 0.5% of the truth.
# Changing this constant changes EVERY published loading; re-run and regenerate the .md tables.
FOIL_TARE_G = 0.0055255

def analyse(name, weights_g, foil_g, comp):
    w = np.array(weights_g, float)
    n = len(w)
    # area from die
    d_cm, ud_cm = D_MM/10.0, U_D_MM/10.0
    A = np.pi*d_cm**2/4.0
    relA = 2*ud_cm/d_cm                     # u(A)/A = 2 u(d)/d
    # active (hard carbon) mass fraction of dried solids
    tot = sum(comp.values())
    f = comp['hard_carbon']/tot
    # coating mass + per-disk measurement uncertainty
    coat = w - foil_g
    u_coat = np.sqrt(U_BAL**2 + U_FOIL**2)         # g, same for every disk
    # areal loadings
    load  = coat*1000.0/A                            # mg/cm^2 (coating)
    hload = load*f                                    # mg/cm^2 (hard carbon)
    # relative measurement uncertainty per disk (mass + area)
    relL  = np.sqrt((u_coat/coat)**2 + relA**2)
    uL    = load*relL                                # mg/cm^2, per disk (meas.)
    # which term dominates the per-disk measurement uncertainty (mass/tare vs die)?
    dom = "mass/tare-dominated" if (u_coat/coat).mean() > relA else "die-dominated"
    # population stats (physical disk-to-disk spread)
    def stats(x):
        return dict(mean=x.mean(), sd=x.std(ddof=1), sem=x.std(ddof=1)/np.sqrt(n),
                    cv=100*x.std(ddof=1)/x.mean(), mn=x.min(), mx=x.max())
    print(f"\n===== {name}  (n={n}) =====")
    print(f"die d = {D_MM} +/- {U_D_MM} mm   area A = {A:.4f} cm^2  (u(A)/A = {100*relA:.2f}%)")
    print(f"foil tare = {foil_g*1000:.3f} mg   active(hard-carbon) fraction f = {f:.4f}")
    print(f"per-disk measurement uncertainty: u(coat) = {u_coat*1000:.3f} mg  "
          f"-> u(load) ~ {uL.mean():.3f} mg/cm^2 ({100*relL.mean():.2f}%, {dom})")
    for key, x, lab in [('coat', coat*1000, 'coating mass (mg)'),
                        ('load', load, 'coating load (mg/cm^2)'),
                        ('hc',   hload, 'hard-carbon load (mg/cm^2)')]:
        s = stats(x)
        print(f"  {lab:28s} mean {s['mean']:.3f}  SD {s['sd']:.3f} ({s['cv']:.1f}%)  "
              f"SEM {s['sem']:.3f}  min {s['mn']:.3f}  max {s['mx']:.3f}")
    print("\n idx  wt(mg)  coat(mg)   load+/-u (mg/cm^2)   HCload (mg/cm^2)")
    for i,(wi,ci,li,ui,hi) in enumerate(zip(w,coat,load,uL,hload),1):
        print(f" {i:2d}  {wi*1000:6.2f}  {ci*1000:7.3f}    {li:5.3f} +/- {ui:.3f}      {hi:6.3f}")
    return dict(load=load, hload=hload, uL=uL)

if __name__ == "__main__":
    MMB1_6A_disks = [
        0.01672,0.01610,0.01651,0.01662,0.01581,0.01576,0.01598,0.01586,0.01589,0.01649,
        0.01645,0.01583,0.01660,0.01683,0.01689,0.01617,0.01561,0.01608,0.01632,0.01642,
    ]
    # dried slurry solids as weighed for MMB1_6A (see MMB1_6A_Electrode_Prep.md)
    comp_6A = dict(hard_carbon=3.6399, cmc=0.0999, c45=0.166, sbr=0.194)
    analyse("MMB1_6A coin-cell disks", MMB1_6A_disks, foil_g=FOIL_TARE_G, comp=comp_6A)

    MMB1_8A_disks = [
        0.00611,0.00608,0.00604,0.00612,0.00611,0.00609,0.00612,0.00608,0.00608,0.00611,
        0.00612,0.00612,0.00608,0.00614,0.00614,0.00613,0.00615,0.00609,0.00610,0.00612,
        0.00611,
    ]
    # dried slurry solids as weighed for MMB1_8A (see MMB1_8A_Electrode_Prep.md).
    # SBR UNCERTAIN: 0.1228 g measured + 1 unmeasured drop -> best estimate ~0.148 g.
    comp_8A = dict(hard_carbon=3.6400, cmc=0.1002, c45=0.1665, sbr=0.148)
    analyse("MMB1_8A coin-cell disks", MMB1_8A_disks, foil_g=FOIL_TARE_G, comp=comp_8A)

    MMB1_10A_disks = [
        0.02023,0.02082,0.02005,0.02035,0.02014,0.02006,0.02037,0.02029,0.01996,0.02044,
        0.01976,0.02053,0.02036,0.01983,0.01953,0.01994,0.02005,0.02005,0.02066,0.01995,
    ]
    # dried slurry solids as weighed for MMB1_10A (see MMB1_10A_Electrode_Prep.md).
    # SBR NOT weighed ("0.g"); 200 uL calibrated pipette -> best estimate ~0.195 g (standard value).
    comp_10A = dict(hard_carbon=3.6715, cmc=0.1002, c45=0.1673, sbr=0.195)
    analyse("MMB1_10A coin-cell disks", MMB1_10A_disks, foil_g=FOIL_TARE_G, comp=comp_10A)

    # MMB1_12A_1C: 20 punched, 3 discarded as light outliers (0.01952, 0.01976, 0.01942 g) -> 17 kept.
    MMB1_12A_1C_disks = [
        0.02082,0.02064,0.02019,0.02211,0.02116,0.02121,0.02024,0.02069,0.02062,0.02059,
        0.02090,0.02024,0.02046,0.02104,0.02087,0.02141,0.02128,
    ]
    # dried slurry solids as weighed for MMB1_12A_1C (see MMB1_12A_1C_Electrode_Prep.md).
    # SBR NOT weighed; 200 uL calibrated pipette -> best estimate ~0.195 g. Taped-blade run is
    # irrelevant to mass loading (only affects thickness comparison).
    comp_12A_1C = dict(hard_carbon=3.6398, cmc=0.1000, c45=0.1673, sbr=0.195)
    analyse("MMB1_12A_1C coin-cell disks", MMB1_12A_1C_disks, foil_g=FOIL_TARE_G, comp=comp_12A_1C)

    # ---- MMB1_12A_2C: two sheets punched and weighed as independent populations ----
    MMB1_12A_2C_sheet1 = [
        0.02207,0.02508,0.02561,0.02223,0.02166,0.02193,0.02375,0.02543,0.02164,0.02326,
        0.02330,0.02400,0.02340,0.02358,0.02501,0.02494,0.02347,0.02240,0.02145,
    ]
    MMB1_12A_2C_sheet2 = [
        0.02513,0.02243,0.02267,0.02244,0.02575,0.02187,0.02351,0.02149,0.02295,0.02209,
        0.02335,0.02253,0.02135,0.02390,0.02183,0.02364,0.02075,0.02383,0.02161,
    ]
    comp_12A_2C = dict(hard_carbon=3.64361, cmc=0.10019, c45=0.16707, sbr=0.195)
    analyse("MMB1_12A_2C sheet 1 (gap 0.23 mm)", MMB1_12A_2C_sheet1, foil_g=FOIL_TARE_G, comp=comp_12A_2C)
    analyse("MMB1_12A_2C sheet 2 (gap 0.28 mm)", MMB1_12A_2C_sheet2, foil_g=FOIL_TARE_G, comp=comp_12A_2C)

    # ---- MMB1_12A_3C: 19 punched, sorted at punching into 13 standard + 6 thick ----
    MMB1_12A_3C_standard = [
        0.02828,0.02943,0.03037,0.02845,0.03046,0.03082,0.02982,0.03004,0.03082,0.02982,
        0.02772,0.02952,0.03002,
    ]
    MMB1_12A_3C_thick = [0.03753,0.03396,0.03193,0.03465,0.03646,0.03304]
    comp_12A_3C = dict(hard_carbon=3.64020, cmc=0.10003, c45=0.16745, sbr=0.195)
    analyse("MMB1_12A_3C standard set", MMB1_12A_3C_standard, foil_g=FOIL_TARE_G, comp=comp_12A_3C)
    analyse("MMB1_12A_3C thick set", MMB1_12A_3C_thick, foil_g=FOIL_TARE_G, comp=comp_12A_3C)

    # ---- Kuranode commercial HC: OFF-STANDARD mix (SBR before HC + extra drop) ----
    Kuranode_disks = [
        0.01436,0.01431,0.01425,0.01421,0.01415,0.01421,0.01434,0.01431,0.01415,0.01438,
        0.01453,0.01410,0.01648,0.01439,0.01596,0.01442,0.01421,0.01418,
    ]
    comp_Kuranode = dict(hard_carbon=3.64010, cmc=0.10083, c45=0.16690, sbr=0.22)
    analyse("Kuranode commercial HC disks", Kuranode_disks, foil_g=FOIL_TARE_G, comp=comp_Kuranode)

