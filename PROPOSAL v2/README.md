# PROPOSAL v2

Proposal defense deck rebuilt from **Chapter 1 v2.docx**, which now holds the Review of Related Literature too. The old `PROPOSAL/` folder (built from Chapter 1 and Chapter 2) is left untouched.

| File | What it is |
| ----- | ----- |
| `slides/` | 34 rendered slides, 3840 × 2160 PNG. Insert each as a full-slide picture in a 16:9 PowerPoint. |
| `DEFENSE-SCRIPT.md` | What to say on each slide, and who says it. |
| `QA-PREP.md` | Short answers to likely panel questions. |
| `THESIS-PROPOSAL-DEFENSE.md` | Slide-by-slide content, mapped to the school template. |
| `figures/` | NVSU logo, the Google Flow photos from v1, and Figures 1, 3, 5, 6, 7 taken from Chapter 1 v2. |
| `slide-builder/` | HTML source of every slide and `build.py`, which renders them. |

## Slide order for PowerPoint (34 slides)

Slides follow the school template (`PROPOSAL/THESIS-PROPOSAL-DEFENSE-Template.docx.md`) the same way v1 did. Each slide keeps its template number, and a template slide that needs more room is split into lettered slides (02a, 02b, 03a…). Every element the template asks for is on its slide. The parts not yet in Chapter 1 v2 show as yellow `[ ]` blanks.

| # | Template slide | Image | Slide |
| ----- | ----- | ----- | ----- |
| 1 | 1 | slide-01.png | Title |
| 2 |  | slide-02-0-section-problem.png | Section: The Problem |
| 3 | 2 | slide-02a.png | Introduction / Background of the Study |
| 4 | 2 | slide-02b.png | Introduction · Key Concepts (Figure 5) |
| 5 | 3 | slide-03a.png | Review of Related Literature · Farm and Monitoring |
| 6 | 3 | slide-03b.png | Review of Related Literature · Detection and Flight |
| 7 | 3 | slide-03c.png | Review of Related Literature · Processing, Data and Method |
| 8 | 3 | slide-03d.png | Research Gap |
| 9 |  | slide-04-0-section-solution.png | Section: The Solution |
| 10 | 4 | slide-04a.png | Conceptual Framework · IPO Model |
| 11 | 4 | slide-04b.png | Conceptual Framework · System Flow (Figure 1) |
| 12 | 5 | slide-05.png | Research Objectives |
| 13 | 6 | slide-06.png | Significance of the Study |
| 14 | 7 | slide-07.png | Scope and Delimitation |
| 15 |  | slide-08-0-section-method.png | Section: The Method |
| 16 | 8 | slide-08a.png | Research Methodology · Research Design |
| 17 | 8 | slide-08b.png | Research Methodology · Dataset (2,000 labeled images) |
| 18 | 9 | slide-09.png | Locale and Participants |
| 19 | 10 | slide-10.png | Research Instruments |
| 20 | 11 | slide-11.png | Data Gathering Procedure |
| 21 | 12 | slide-12.png | Statistical Treatment of Data |
| 22 |  | slide-13-0-section-system.png | Section: The System |
| 23 | 13 | slide-13a.png | Proposed System Architecture (Figure 6) |
| 24 | 13 | slide-13b.png | Proposed System Architecture · Scan Sequence |
| 25 | 13 | slide-13c.png | Proposed System Architecture · Technical Design (Figure 7) |
| 26 | 13 | slide-13d.png | Proposed System Architecture · Key Features |
| 27 |  | slide-14-0-section-plan.png | Section: The Plan |
| 28 | 14 | slide-14.png | Project Timeline (Gantt Chart) |
| 29 | 15 | slide-15.png | Expected Output |
| 30 | 16 | slide-16.png | Budget Requirements |
| 31 | 17 | slide-17.png | Thank You / Open Forum |
| 32 |  | slide-A1.png | Backup A: SWOT |
| 33 |  | slide-A2.png | Backup B: Safety and regulation |
| 34 |  | slide-A3.png | Backup C: Hardware components |

## Rebuilding a slide

Edit the HTML in `slide-builder/src/`, then from `slide-builder/`:

```
python3 build.py            # every slide
python3 build.py 07 16      # only slides whose number starts with these
```

Needs Python Playwright and Google Chrome, plus internet for fonts and icons on the first run. The build warns about content spilling off the slide and about unknown icon names. Three warnings are expected and harmless: `slide-01` (hero photo offset), `slide-05` (outline numbers) and `slide-06` (ripple rings).

Shared pieces: `theme.css` (colors, fonts, light and dark slides), `frame.js` (top bar and footer), `tower.js` (the drawn tower on slide-02a), `rrl.css` (the literature tables), `section.css` / `section.js` (section dividers).

## What changed from v1

**Content, following Chapter 1 v2**
- **No more ESP32 tower unit.** Each tower carries a printed, laminated sign (QR code + 15 × 15 cm ArUco approach marker), and the farmer's phone saves the GPS location.
- **Navigation:** GPS → the Pi turns slowly to find the approach marker → 6 × 6 cm face markers + solvePnP. YOLOv8 is no longer used to find the tower, and the laptop never steers.
- **Detection:** live preview during flight; final counts come from the full onboard 1080p recording after landing. Classes are lettuce and empty pot only.
- **RRL:** rebuilt on the new sources (van Delden, Shalash, Mayta, Kalaitzakis, Fauzi, Hajesmaeel-Gohari, CAAP 2026 and others). v1 citations that v2 dropped (Despommier, Chowdhury, Stefas, Wubben, Benoit-Cattin, Kleppmann, Martin, Lund) are gone from the slides.
- **Locale and respondents** are now filled in: Busilac and Savara Lettuce Farm; 1 farmer + 3 IT experts by total enumeration (v1 had purposive sampling with blanks).
- **Table 6 scale:** 4.21–5.00 Highly Acceptable … with "Moderately Agree / Moderately Acceptable" in the middle.
- **Budget:** ₱25,637–28,467 (Table 5); the tower, lettuce and anemometer are now included.
- **New figures** from the document are used in the main deck: Figure 1 (slide-04b), Figure 5 (slide-02b), Figure 6 (slide-13a), Figure 7 (slide-13c).
- **Dataset** (~2,000 labeled images, ≥ 1,500 per class, 70/20/10) gets its own slide (slide-08b).
- **Script** now covers every slide (v1 stopped at slide-05).

**Design, to make it less monotonous**
- Dark and light slides alternate; v1 was almost all light cards.
- More visuals and fewer bullet cards:
  - RRL tables with highlighted numbers (03a–03c)
  - a coverage matrix (03d)
  - a ripple diagram (06)
  - a drawn flight envelope (07)
  - a dataset chart (08b)
  - a scan-path diagram (13b)
  - a layered stack (13d)
  - a Gantt chart (14)
  - a dashboard mock-up (15)
  - range bars for the budget (16)
- The Plan divider no longer shows the "Google Flow image goes here" placeholder; it has a drawn schedule instead.

## Open items in Chapter 1 v2 (fix before the defense)

These are in the document itself, not the slides. The panel may notice them.

1. **Figures still show the old tower unit.**
   - Figure 2 (the Paradigm, a Word drawing) still lists *"tower unit (ESP32 and e-paper QR display)"*. Slide-04a uses the corrected wording.
   - Figure 3 (RAD) says *"Build Drone and Tower Unit."* Slide-08a is redrawn instead of using it.
   - Figure 5 still draws a small electronic box with an antenna on the tower, near callout 3. That figure is shown on slide-02b.
2. **Drone weight doesn't add up.** The parts listed in Phase 3 sum to about **181–221 g**, but the text says **200–240 g**. Either list what makes up the difference (wiring, mounts, TPU guards) or change the estimate. Slides 13c and B use the chapter's 200–240 g.
3. **Blanks still in brackets:**
   - maximum wind speed (km/h), shown on slide-07
   - frame type and size; propeller size
   - tower frame material; number of faces × pots per face
   - ground control station (QGroundControl or Mission Planner), shown on slide-13d
   - Raspberry Pi OS Lite (still bracketed); microSD size
4. **"Chapter 2" references remain** (Introduction: *"the literature reviewed in Chapter 2"*; Phase 1: *"presented in Chapter 2"*), but the RRL is now in Chapter 1.
5. **Duplicate references:** van Delden, Villacrés, Wang and Zhang each appear twice. Ultralytics (n.d.) and (n.d.-a) are the same page. The Ultralytics entries also sit out of alphabetical order at the end.
6. **Validation is adviser-only.** The school template asks for expert validation, pilot testing and reliability testing. Slide-10 shows pilot and reliability testing as blanks. Add them to the chapter (e.g., a pilot run and Cronbach's alpha), or decide how you'll explain leaving them out with n = 4.
7. **No schedule dates.** The Gantt on slide-14 is a proposed Month 1–6 plan carried over from v1. Replace it with real months if the panel needs them.
8. **Budget template items.** The template's Printing, Internet, Transportation and Miscellaneous rows aren't in Table 5. Slide-16 shows them as blanks.
