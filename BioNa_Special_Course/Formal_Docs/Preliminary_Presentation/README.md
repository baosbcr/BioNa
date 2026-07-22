# Preliminary results presentation — CC19–CC41 cycling

~7 min supervisor update. DTU Beamer theme, 14 pages
(2 title frames + 9 content + 2 backup + references).

Source of every number: `Processes/Cycling_Data_Review_2026-07-21.md`.
Figures come from `Figures/` — no placeholders, all real.

| File | Edit this when |
|---|---|
| `main.tex` | title, author, colour, date, department |
| `body.tex` | **all slide content** |

The compiled PDF is gitignored (build artifact). Rebuild it as below.

## Slides

1. Why hard carbon, and why pyrolysis conditions
2. Samples, cells and test protocol
3. Not all 23 cells are usable — the five exclusions
4. **ICE rises with temperature** — the solid result
5. **Slower ramp gives higher capacity** — the project's question
6. A systemic fade affects every cell — including the control
7. The obvious explanation (rising impedance) was tested and rejected
8. Conclusions
9. Future outlook — new 8 A slurry + recommended new cells
10–11. Backup: temperature series, instrument cross-check, how to read a single cell
12. References — **still placeholders, `% TODO`**

Every frame has a `\note{}`. To show notes on a second screen, uncomment the two
`pgfpages` lines in `main.tex`.

## Building on Overleaf (normal route)

Upload to a project created from the
[DTU Beamer template](https://da.overleaf.com/latex/templates/dtu-beamer-template/pryyqtsrpmpb):

- `main.tex` and `body.tex` → project root
- `Figures/` → project root, **keeping the `cells/` subfolder** (slide 11 uses
  `Figures/cells/CC19.png`)

Set `main.tex` as root document and compile. No path fiddling needed.

## Building locally (MiKTeX on Windows)

The template is not vendored here. Fetch it once:

```bash
git clone --depth 1 https://gitlab.gbar.dtu.dk/latex/dtutemplates.git
cp -r dtutemplates/templates/Beamer/template .
```

Then, from a directory holding `main.tex`, `body.tex`, `template/` and `Figures/`:

```bash
export TEXINPUTS=".;./template//;"
latexmk -pdf -interaction=nonstopmode main.tex
```

> ⚠️ **The template's own `latexmkrc` does not work on Windows.** It sets
> `TEXINPUTS` with Unix `:` separators; MiKTeX needs `;`, so `\input{preamble.tex}`
> fails with *"File `preamble.tex' not found"*. Export `TEXINPUTS` manually as above.

## Layout traps in this deck (hit once already — don't undo the fixes)

- **`\AtBeginEnvironment{itemize}` in `main.tex` injects `\small` *after*
  `\begin{itemize}`.** A `\scriptsize` written *before* the list is silently
  overridden. Put the size command **inside**: `\begin{itemize}\scriptsize`.
- **Text can be clipped by the footer with no LaTeX warning.** Trailing lines just
  disappear under the red bar. Overfull-vbox warnings do *not* catch it —
  check rendered pages, not just the log.
- **Do not use `[plain]` on backup frames.** The DTU theme renders the frame title
  inside the headline, which `plain` removes, so the slide loses its title. Use
  `[noframenumbering]` alone.
- Figure sizing: `height` is the binding constraint for figures 01/03/06
  (aspect ≈ 1.3), `width` for figure 04 (aspect 1.98). Current settings —
  `height=0.70\textheight`, figure column `0.57\textwidth` — are tuned to fill the
  slide without overflowing.

## Open TODOs

- Fill the three placeholder references in the last frame.
- Confirm department (`DTU Energy`, inferred) and whether a course code belongs in
  the subtitle — none is recorded anywhere in the repo.
