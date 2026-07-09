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
U_FOIL = 0.00003   # g, foil-tare uncertainty. Tare recorded to 0.1 mg -> resolution 0.1/sqrt(12)=0.029 mg.
                   # NOTE: real foil disk-to-disk mass variation may exceed this.
D_MM   = 12.70     # cutting-die diameter, mm (nominal 1/2", CES disk cutter)
U_D_MM = 0.05      # mm, ASSUMED die-diameter tolerance — CES spec UNKNOWN. Dominant term; confirm.

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
    analyse("MMB1_6A coin-cell disks", MMB1_6A_disks, foil_g=0.0055, comp=comp_6A)

    MMB1_8A_disks = [
        0.00611,0.00608,0.00604,0.00612,0.00611,0.00609,0.00612,0.00608,0.00608,0.00611,
        0.00612,0.00612,0.00608,0.00614,0.00614,0.00613,0.00615,0.00609,0.00610,0.00612,
        0.00611,
    ]
    # dried slurry solids as weighed for MMB1_8A (see MMB1_8A_Electrode_Prep.md).
    # SBR UNCERTAIN: 0.1228 g measured + 1 unmeasured drop -> best estimate ~0.148 g.
    comp_8A = dict(hard_carbon=3.6400, cmc=0.1002, c45=0.1665, sbr=0.148)
    analyse("MMB1_8A coin-cell disks", MMB1_8A_disks, foil_g=0.0055, comp=comp_8A)

    MMB1_10A_disks = [
        0.02023,0.02082,0.02005,0.02035,0.02014,0.02006,0.02037,0.02029,0.01996,0.02044,
        0.01976,0.02053,0.02036,0.01983,0.01953,0.01994,0.02005,0.02005,0.02066,0.01995,
    ]
    # dried slurry solids as weighed for MMB1_10A (see MMB1_10A_Electrode_Prep.md).
    # SBR NOT weighed ("0.g"); 200 uL calibrated pipette -> best estimate ~0.195 g (standard value).
    comp_10A = dict(hard_carbon=3.6715, cmc=0.1002, c45=0.1673, sbr=0.195)
    analyse("MMB1_10A coin-cell disks", MMB1_10A_disks, foil_g=0.0055, comp=comp_10A)

    # MMB1_12A_1C: 20 punched, 3 discarded as light outliers (0.01952, 0.01976, 0.01942 g) -> 17 kept.
    MMB1_12A_1C_disks = [
        0.02082,0.02064,0.02019,0.02211,0.02116,0.02121,0.02024,0.02069,0.02062,0.02059,
        0.02090,0.02024,0.02046,0.02104,0.02087,0.02141,0.02128,
    ]
    # dried slurry solids as weighed for MMB1_12A_1C (see MMB1_12A_1C_Electrode_Prep.md).
    # SBR NOT weighed; 200 uL calibrated pipette -> best estimate ~0.195 g. Taped-blade run is
    # irrelevant to mass loading (only affects thickness comparison).
    comp_12A_1C = dict(hard_carbon=3.6398, cmc=0.1000, c45=0.1673, sbr=0.195)
    analyse("MMB1_12A_1C coin-cell disks", MMB1_12A_1C_disks, foil_g=0.0055, comp=comp_12A_1C)
