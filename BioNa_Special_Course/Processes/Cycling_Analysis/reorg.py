"""Dismantle ToProcessWClaude/ into the repo's normal layout.

DRY RUN by default. Pass --go to actually move/delete.
Only deletes what is provably redundant; everything else is moved, never dropped.
"""
import os, shutil, sys, hashlib

REPO = r"C:\Users\joaos\Desktop\DTU_ENT\BioNa\BioNa_Special_Course"
SRC = os.path.join(REPO, "ToProcessWClaude")
GO = "--go" in sys.argv

ED = os.path.join(REPO, "Experimental_Data")
DEST_BL = os.path.join(ED, "Cycling", "BioLogic_CC19-CC33")
DEST_NW = os.path.join(ED, "Cycling", "Neware_CC34-CC41")
DEST_XL = os.path.join(ED, "Cycling", "_supervisor_crosscheck")
DEST_TG = os.path.join(ED, "TGA_DSC")
PROC = os.path.join(REPO, "Processes")

moves, deletes = [], []

# --- Bio-Logic raw: everything except the redundant text exports ---
d = os.path.join(SRC, "BNa_Joao_2026")
for f in sorted(os.listdir(d)):
    p = os.path.join(d, f)
    if os.path.isdir(p):
        continue
    if f.startswith("~$"):
        deletes.append((p, "Excel lock file"))
    elif f.lower().endswith(".xlsx"):
        moves.append((p, os.path.join(DEST_XL, f)))
    else:
        moves.append((p, os.path.join(DEST_BL, f)))

# --- the 98 text exports: PROVEN redundant vs the .mpr (verified this session) ---
td = os.path.join(d, "BNa_CC19-33_J_textExports")
mpr_stems = {os.path.splitext(f)[0] for f in os.listdir(d) if f.endswith(".mpr")}
for f in sorted(os.listdir(td)):
    stem = os.path.splitext(f)[0]
    if stem in mpr_stems:
        deletes.append((os.path.join(td, f), "redundant text export; .mpr verified"))
    else:                                   # safety net: never delete an orphan
        moves.append((os.path.join(td, f), os.path.join(DEST_BL, "_textExports_orphan", f)))

# --- Neware ---
for sub in ["BNa_Joao_Neware", os.path.join("BioNa Jaoa", "Missing_Newara_Ongoing")]:
    d2 = os.path.join(SRC, sub)
    if not os.path.isdir(d2):
        continue
    for f in sorted(os.listdir(d2)):
        p = os.path.join(d2, f)
        if os.path.isfile(p):
            moves.append((p, os.path.join(DEST_NW, f)))

# --- TGA/DSC ---
d3 = os.path.join(SRC, "BioNa Jaoa")
for f in sorted(os.listdir(d3)):
    p = os.path.join(d3, f)
    if os.path.isfile(p):
        moves.append((p, os.path.join(DEST_TG, f)))

# --- top-level ---
for f in sorted(os.listdir(SRC)):
    p = os.path.join(SRC, f)
    if not os.path.isfile(p):
        continue
    if f.startswith("~$"):
        deletes.append((p, "Excel lock file"))
    elif f == "MANIFEST.md":
        moves.append((p, os.path.join(PROC, "Raw_Data_Manifest_2026-07-21.md")))
    elif f == "Notes_21_7_26.md":
        moves.append((p, os.path.join(PROC, "Raw_Data_Triage_Notes_2026-07-21.md")))
    elif f.lower().endswith(".xlsx"):
        moves.append((p, os.path.join(DEST_XL, f)))
    else:
        moves.append((p, os.path.join(DEST_XL, f)))

msz = sum(os.path.getsize(a) for a, _ in moves)
dsz = sum(os.path.getsize(a) for a, _ in deletes)
print(f"MOVE   {len(moves):4d} files  {msz/1048576:9.1f} MB")
print(f"DELETE {len(deletes):4d} files  {dsz/1048576:9.1f} MB")
print()
bydest = {}
for a, b in moves:
    bydest.setdefault(os.path.dirname(b), []).append(a)
for k, v in sorted(bydest.items()):
    print(f"  -> {os.path.relpath(k, REPO)}  ({len(v)} files, "
          f"{sum(os.path.getsize(x) for x in v)/1048576:.1f} MB)")
print()
byreason = {}
for a, r in deletes:
    byreason.setdefault(r, []).append(a)
for k, v in byreason.items():
    print(f"  X  {k}: {len(v)} files, {sum(os.path.getsize(x) for x in v)/1048576:.1f} MB")

if not GO:
    print("\nDRY RUN — nothing changed. Re-run with --go to apply.")
    sys.exit()

for a, b in moves:
    os.makedirs(os.path.dirname(b), exist_ok=True)
    if os.path.exists(b):
        print("SKIP (exists):", b)
        continue
    shutil.move(a, b)
for a, _ in deletes:
    os.remove(a)
# drop the now-empty tree
for root, dirs, files in os.walk(SRC, topdown=False):
    if not os.listdir(root):
        os.rmdir(root)
print("\nDONE. ToProcessWClaude exists:", os.path.exists(SRC))
