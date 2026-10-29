**THESIS PROPOSAL DEFENSE (v2)**
**Presentation Content and Flow**

Source: *Chapter 1 v2.docx* (Introduction, Review of Related Literature, Objectives, Conceptual Framework, Paradigm, Scope, Significance, Methodology, References). Follows the school template, `PROPOSAL/THESIS-PROPOSAL-DEFENSE-Template.docx.md`. Items in `[brackets]` are still open in the chapter and must be filled in before the defense.

---

## Presentation Flow

Target length: **about 19 minutes** of presentation, then open forum. Slides keep the template numbers 1–17; where one template slide needs more room, it is split into lettered slides (2a, 2b, 3a–3d …), as in v1. A section slide opens each of the five parts.

| # | Slide | Part | Time | Presenter | Key message (one sentence) |
| ----- | ----- | ----- | ----- | ----- | ----- |
| 1 | Title | Opening | 0:35 | Lopez | Who we are and what we propose. |
| 2a | Introduction / Background of the Study | **Problem** | 1:15 | Lopez | More towers, taller towers, but pot checks are still manual and sensors can't see empty pots. |
| 2b | Introduction · Key Concepts | **Problem** | 1:00 | Lopez | QR registration, GPS + ArUco alignment, YOLOv8, offline-first dashboard; one drone for the whole farm. |
| 3a–3c | Review of Related Literature and Studies | **Problem** | 2:30 | Marvilla | 38 sources: what we adopt, what they leave out. |
| 3d | Research Gap | **Problem** | 0:40 | Marvilla | Each piece exists; no study combines them. |
| 4a | Conceptual Framework · IPO Model | **Solution** | 0:45 | Marvilla | Inputs → RAD process → working inspection system, with feedback. |
| 4b | Conceptual Framework · System Flow (Figure 1) | **Solution** | 0:55 | Marvilla | Fly and scan offline; internet only for records. |
| 5 | Research Objectives | **Solution** | 1:00 | Valentino | One general objective, five specific objectives. |
| 6 | Significance of the Study | **Solution** | 0:45 | Valentino | Practical, academic, technical and community contributions. |
| 7 | Scope and Delimitation | **Solution** | 0:55 | Valentino | What we build, and the limits we fly within. |
| 8a | Research Methodology · Research Design | **Method** | 0:55 | Fernandez | Developmental, mixed-method, RAD with simulation first. |
| 8b | Research Methodology · Dataset | **Method** | 0:45 | Fernandez | About 2,000 labeled images, split 70/20/10. |
| 9 | Locale and Participants | **Method** | 0:35 | Fernandez | Busilac and Savara Lettuce Farm; 4 respondents by total enumeration. |
| 10 | Research Instruments | **Method** | 0:45 | Fernandez | Survey, interview guide, observation checklist, system evaluation tool. |
| 11 | Data Gathering Procedure | **Method** | 0:35 | Fernandez | Approval → validation → collection → processing → analysis. |
| 12 | Statistical Treatment of Data | **Method** | 0:45 | Fernandez | Precision, recall, mAP@50, counting error; weighted mean and SD. |
| 13a | Proposed System Architecture | **System** | 0:55 | Lopez | Five parts; only the cloud needs internet. |
| 13b | Proposed System Architecture · Scan Sequence | **System** | 0:55 | Lopez | How one scan runs, and the failsafes. |
| 13c | Proposed System Architecture · Technical Design | **System** | 0:35 | Lopez | Power, flight control, companion computer, ground link. |
| 13d | Proposed System Architecture · Key Features | **System** | 0:35 | Lopez | Architecture layers and dashboard features. |
| 14 | Project Timeline (Gantt Chart) | **Plan** | 0:25 | Lopez | Proposed six-month schedule along the RAD phases (not set in Chapter 1 v2). |
| 15 | Expected Output | **Plan** | 0:35 | Lopez | Anticipated benefits and deliverables. |
| 16 | Budget Requirements | **Plan** | 0:30 | Lopez | About ₱25,600 to ₱28,500 in hardware. |
| 17 | Thank You / Open Forum | Closing | 0:10 | All | Invite questions. |
|  | Backup slides A–C | Q&A | — | As asked | Show only when a panelist asks. |

> Presenter assignment is a suggestion. Rebalance it so that each member speaks on the part they built or wrote.

---

**Slide 1: Title Slide**
**Thesis Proposal Defense**

* **Computer Vision and Autonomous Drone Inspection for Hydroponic Towers with Web Dashboard Integration**
* Lester Dann G. Lopez (Leader) · Rhoan Joy M. Marvilla · Prince Daniel A. Valentino · Joshua Jing A. Fernandez
* Bachelor of Science in Computer Science (BSCS 4B)
* College of Information Technology Education
* Adviser: Bernadeth B. Liggayu, MIT
* Nueva Vizcaya State University
* November 3, 2026

*Visual:* NVSU logo over the blueprint-to-real Google Flow photo.

---

**Slide 2a: Introduction / Background of the Study**
**Overview of the Study**

* **Context of the problem:** Vertical farms use less land and water, but success depends on efficient management (van Delden et al., 2021; Saad et al., 2021).
* **Current situation:** Monitoring is still manual (Domingo, 2022; Bunga, 2026). IoT tracks temperature, humidity, pH and nutrients, not whether each pot holds a plant (Dhanaraju et al., 2022; Santiago et al., 2025).
* **Scale:** a farm has many towers, and stackable towers grow taller module by module, so checking by hand takes longer as the farm grows (Significance of the Study).
* **Importance of the study:** Slot availability (empty pots vs. total slots) for every tower on the farm tells farmers where to replant and when to harvest.
* **SDGs:** 2, 9, 11, 12.

*Visual:* drawn tower with empty pots ringed in red, a row of towers behind it ("…and every other tower on the farm"), and an IoT readout showing "Empty pots: ?".

**Slide 2b: Introduction · Key Concepts**

* **QR code registration:** the farmer scans a printed QR sign; the phone saves its GPS as the tower location.
* **GPS + ArUco markers:** GPS brings the drone near; the Raspberry Pi aligns on the markers.
* **YOLOv8 computer vision:** every face, bottom to top; live preview on the laptop; final count from the onboard recording.
* **Offline-first dashboard:** saved offline first, uploaded when there is internet.
* **Whole farm, not one tower:** each tower has its own QR code and location, so one drone inspects every tower in turn; adding a tower costs only a printed sign.

*Visual:* Figure 5 (Conceptual Illustration). Each step points to its callout numbers.

---

**Slide 3a: Review of Related Literature and Studies**
**Related Literature: Farm and Monitoring**

| Author | Key Findings | Relevance |
| ----- | ----- | ----- |
| van Delden et al. (2021); Saad et al. (2021); Siregar et al. (2022) | Vertical farms use less land and water, but success depends on efficient management; automation and AI crop monitoring are key prospects. | **Evidence:** towers only pay off when well managed. **Gap:** focus on environment, not which slots are in use. |
| DOST-PCAARRD (n.d.); Bendanillo (2023) | UPLB's SIGLA vertical farm trialed lettuce; PVC pipe-and-pot gardens split each structure into discrete slots. | **Evidence:** local towers are slot-based. |
| Domingo (2022); Bunga (2026); Petropoulou et al. (2023) | Iloilo farm logged data by hand with inconsistent results; Bohol systems rely on manual checks; plant-position data guides space use. | **Evidence:** monitoring is still manual; slot data helps planning. |
| Dhanaraju et al. (2022); Santiago et al. (2025) | IoT tracks temperature, humidity, pH and nutrients; automates fertilizer for lettuce. | **Gap:** none reports whether each slot holds a plant. |
| Qian et al. (2021); GPS.gov (n.d.) | QR readability depends on distance, size and curvature; phone GPS ≈ **4.9 m** under open sky. | **Adopted:** printed QR sign + phone GPS; GPS only brings the drone near. |

**Slide 3b: Review of Related Literature and Studies**
**Related Literature: Detection and Flight**

| Author | Key Findings | Relevance |
| ----- | ----- | ----- |
| Terven et al. (2023); Ultralytics (n.d.) | YOLO is a central real-time detector judged by precision, recall and mAP; YOLOv8 is anchor-free. | **Adopted:** YOLOv8 with precision, recall, mAP@50. |
| Wang, Wu & Shen (2024) | YOLOv8n: **~99%** precision and recall on hydroponic lettuce, 2,240 frames. | **Adopted:** YOLOv8, ~2,000-image dataset. **Gap:** no empty-pot class; stable camera. |
| Zhang et al. (2022); Villacrés et al. (2023) | ByteTrack keeps low-score boxes; DeepSORT + YOLOv5 averaged **20.07%** counting error. | **Adopted:** ByteTrack; counting error vs. manual counts. |
| Aslan et al. (2022); de Azambuja et al. (2022); Aliane (2024) | Almost no UAV work in greenhouses; CogniFly (**<250 g**) survived 7 m/s collisions; ArduPilot supports companion computers and SITL. | **Adopted:** CogniFly-style frame, ArduPilot + Pi, Gazebo SITL. **Gap:** no single-tower inspection. |
| Kalaitzakis et al. (2021); OpenCV (n.d.); Andrzejewski et al. (2026) | Markers make localization accurate and robust; pose from four corners; Pi + ArduPilot marker landing. | **Adopted:** ArUco + solvePnP on the Pi. **Gap:** landing pads only. |

**Slide 3c: Review of Related Literature and Studies**
**Related Literature: Processing, Data and Method**

| Author | Key Findings | Relevance |
| ----- | ----- | ----- |
| Shalash et al. (2026); Zhu & Chen (2026) | YOLOv8–v12 on Pi 4/5 mostly **<3 fps**; Wi-Fi offloading 15–45 ms, fails when the link weakens. | **Adopted:** YOLOv8 on the laptop; steering stays on the Pi. |
| Mirandilla-Santos (2021); Serafica et al. (2023); Mayta et al. (2026) | **92%** of barangays have cell signal, rural areas lag; offline-first app kept 100% sync. | **Evidence:** internet can't be assumed. **Adopted:** offline cache + Sync Center. |
| Schulze Schwering et al. (2022); Supabase (n.d.) | FMIS useful but underused; Supabase Realtime pushes changes live. | **Adopted:** Supabase + Next.js dashboard. |
| Meier et al. (2022); ArduPilot Dev Team (n.d.); CAAP (2026) | Wind estimation from flight data; battery failsafe RTL; Part 11 open category (≤25 kg, VLOS, <120 m, daylight, **30 m** from others). | **Adopted:** fair-weather flights, RTL failsafes, open-category rules. |
| Fauzi et al. (2023); Hajesmaeel-Gohari et al. (2022) | RAD has the shortest completion time among SDLC models; USE questionnaire: 30 items in four sections (usefulness, ease of use, ease of learning, satisfaction), 7-point. | **Adopted:** RAD; USE adapted to 5 points. |

**Slide 3d: Research Gap**

* IoT studies monitor growing conditions, **not pot occupancy**.
* Lettuce detection studies detect plants from stable viewpoints, **not empty pots or slot positions**.
* Agricultural UAV studies cover fields and orchards, **not single vertical towers**.
* Marker-based UAV studies cover **precision landing**, not alignment with the faces of a tower.
* **No reviewed study combines** a low-cost micro-drone, QR registration with the farmer's phone GPS, layered GPS → onboard ArUco navigation, a face-by-face scan that maps every pot to its slot, a live preview with final counts from the onboard recording, and an offline-first dashboard.

*Visual:* coverage matrix (study groups × capabilities); only "This study" fills every column.

---

**Slide 4a: Conceptual Framework**
**Input–Process–Output (IPO) Model**

| INPUT | PROCESS (Rapid Application Development) | OUTPUT |
| ----- | ----- | ----- |
| **Problem input:** interviews with hydroponic farmers | **Requirements Planning:** farmer needs, components, scope, evaluation criteria | **Computer Vision and Autonomous Drone Inspection for Hydroponic Towers with Web Dashboard Integration** |
| **Knowledge input:** related literature | **User Design** ⇄ **Rapid Construction** (repeated until each part works) | Reports **lettuce count, empty pot count and slot availability** per tower |
| **Technical inputs:** SpeedyBee F405 Mini, HGLRC GPS, Pi Zero 2 W, Pi Camera V2, **printed tower sign**, ArUco markers, ground laptop, YOLOv8, ArduPilot, Supabase, web dashboard | **Cutover:** end-to-end tests; precision, recall, mAP@50, counting error, alignment and scan success; weighted mean | |

**Feedback loop:** flight tests, detection tests and user evaluations refine the next iteration. (Redrawn from Figure 2 with the printed tower sign in place of the old tower unit.)

**Slide 4b: Conceptual Framework · System Flow**

* Figure 1 with the steps grouped by zone.
* **At the tower (local Wi-Fi):** 1 scan QR + save GPS · 3 mission · 4 approach, align, scan · 5a live preview · 5b full recording after landing.
* **Records (internet):** 2 upload registration · 6 sync · 7 dashboard.

---

**Slide 5: Research Objectives**
**General Objective**
To design and develop an autonomous drone-based monitoring system that registers vertical hydroponic towers through a printed QR code and the location of the farmer's phone, navigates to each tower using GPS, aligns itself using computer vision and visual markers, scans every face of the tower in an open space, detects lettuce plants and empty planting pots using computer vision, and displays tower-level records on a web-based dashboard.

**Specific Objectives**

1. To identify the existing tools, process, and challenges in monitoring vertical hydroponic farming to establish the system's baseline requirements.
2. To design and develop a web dashboard for QR-based tower registration using the location of the farmer's phone, scan requests, and inspection records that works even when the farm has no internet connection.
3. To develop an autonomous navigation and alignment method that combines GPS waypoints with onboard QR code and ArUco marker positioning to scan every face of a tower.
4. To develop a YOLOv8 model that detects lettuce heads and empty pots, shown as a live preview during flight and finalized from the onboard recording after landing, matches each detection to its exact pot, and is integrated with the drone telemetry, offline cache, and web dashboard.
5. To evaluate the system in terms of detection and counting accuracy, alignment and scan success, and its usefulness, ease of use, and user satisfaction.

---

**Slide 6: Significance of the Study**

* **Hydroponic Farmers (practical):** less time checking pots, especially upper levels; counts guide replanting and harvesting.
* **Farm Managers and Workers (practical):** per-tower occupancy and inspection history, fewer counting errors.
* **Students and Researchers (academic):** a reference and a labeled dataset for health, pest or harvest studies.
* **Academic Community (academic):** adds to smart farming, robotics and applied computer vision.
* **Local Community and Agricultural Offices (community):** guides affordable urban and vertical farming.
* **Technical contribution:** extends marker alignment from landing pads to the vertical faces of a tower and maps each detection to its exact pot.

---

**Slide 7: Scope and Delimitation**
**Scope** (inclusions and coverage)

* QR registration with the phone's GPS; a printed sign, no electronics.
* GPS approach + onboard QR/ArUco alignment; every face, bottom to top.
* YOLOv8 lettuce and empty pots: live preview, final count, matched to each pot.
* SQLite offline cache, upload to Supabase, Next.js dashboard.
* One 1.5 m tower built and tested; method meant to scale to taller and more towers.

**Delimitations** (exclusions and limits of coverage)

* Exclusions: watering or nutrient system; crops other than lettuce; disease, pests, growth, weight; obstacle avoidance; indoor or GPS-denied flight; LiDAR and 3D; cellular or cloud GPU; commercial deployment.
* Limits: ≤ 1.8 m (6 ft) above ground; ≤ 20 m from launch; 3–5 min per battery, one tower per flight; daylight and fair weather; wind ≤ `[maximum wind speed, km/h]` checked with an anemometer; open area with GPS; local Wi-Fi only.

---

**Slide 8a: Research Methodology**
**Research Design**

* **Developmental research design**, **mixed-method** (interviews + tests and ratings), **RAD** (Fauzi et al., 2023).
* **Phase 1 – Requirements Planning:** interviews, including how often and how long checks take; site observation; components rated on availability, cost, weight, compatibility; SWOT.
* **Phase 2 – User Design:** architecture, sign and marker layout, mission and slot matching, Supabase schema, dashboard shown to users, Gazebo + SITL (full scan, lost markers, lost Wi-Fi).
* **Phase 3 – Rapid Construction:** drone build, thrust test, AutoTune; 1.5 m tower, sign, markers; ~2,000 labeled images → YOLOv8; streaming, alignment, cache, dashboards. Stage 1, then Stage 2.
* **Phase 4 – Cutover:** model, flight, streaming and sync tests; end to end; USE evaluation; documentation.

**Slide 8b: Research Methodology · Dataset**

* About **2,000 labeled images**: ≥ 1,500 with lettuce, ≥ 1,500 with empty pots, 5–10% background.
* Basis: Wang et al. (2024) used 2,240 frames; meets the Ultralytics guideline of at least 1,500 images per class.
* Capture from every side, distance and lighting → one frame per ~1 s → label in Supabox (YOLO format) → train YOLOv8.
* Split 70/20/10 (~1,400 / ~400 / ~200); each recording session stays in one set.

---

**Slide 9: Locale and Participants**
**Research Locale**

* Flight tests: Purok 2, Busilac, Bayombong, Nueva Vizcaya. Open, obstacle-free, with GPS signal.
* Needs-assessment interviews: Savara Lettuce Farm, Purok 5, Brgy. Masoc, Bayombong. The only hydroponic farm in Bayombong.

**Participants/Respondents**

* **Population size:** 1 hydroponic farmer + 3 IT experts (CITE, NVSU) = 4.
* **Sampling technique:** total enumeration.
* **Sample size:** 4 of 4 (100%).

---

**Slide 10: Research Instruments**
**Instruments to Use**

* **Survey Questionnaire:** adapted USE questionnaire (Hajesmaeel-Gohari et al., 2022), 7-point → 5-point with "Moderately Agree" in place of neutral; usefulness, ease of use, satisfaction.
* **Interview Guide:** interview questionnaire for farmers, six parts, ~15 min.
* **Observation Checklist:** site observation sheet (tower height and levels, open space, obstacles, lighting and wind, GPS and network signal).
* **System Evaluation Tool:** test logs (precision, recall, mAP@50; counting error, slot matching; alignment, scan success; stream delay, frame loss; flight time, Pi temperature, marker fps).

**Validation**

* **Expert Validation:** adviser review and approval of the interview questionnaire.
* **Pilot Testing:** `[not yet in Chapter 1 v2]`
* **Reliability Testing:** `[not yet in Chapter 1 v2]`

---

**Slide 11: Data Gathering Procedure**
**Steps**

1. **Secure Approval:** letter of request; approval from school authorities and the farm owner.
2. **Validation of Instruments:** interview questionnaire reviewed and approved by the adviser.
3. **Data Collection:** ~15-min interviews with informed consent; observation checklist; tower photos into the Supabox dataset; test flights; then the survey questionnaire.
4. **Data Processing:** data organized and categorized; interview responses coded; flight and detection test results recorded.
5. **Data Analysis:** themes update the SWOT; performance metrics; weighted mean and SD.

*Ethics:* voluntary; RA 10173; consent for audio and photos, towers not people; AI use disclosed.

---

**Slide 12: Statistical Treatment of Data**

* **Precision** = TP / (TP + FP) · **Recall** = TP / (TP + FN) · **mAP@50**.
* **Counting error per tower:** system counts compared with manual counts of lettuce and empty pots · **Slot matching accuracy:** status assigned to each slot compared with the actual pot.
* **Flight tests:** alignment success rate, mean alignment error (cm), full-tower scan completion, stream delay and frame loss, flight time per tower.
* **Weighted mean** x̄ = Σfx / n and **standard deviation** per category.
* **Thematic analysis** of interviews → SWOT.

| Scale | Range | Descriptor | Interpretation |
| :---: | ----- | ----- | ----- |
| 5 | 4.21 – 5.00 | Strongly Agree | Highly Acceptable |
| 4 | 3.41 – 4.20 | Agree | Acceptable |
| 3 | 2.61 – 3.40 | Moderately Agree | Moderately Acceptable |
| 2 | 1.81 – 2.60 | Disagree | Not Acceptable |
| 1 | 1.00 – 1.80 | Strongly Disagree | Highly Not Acceptable |

---

**Slide 13a: Proposed System / Project Architecture**

* **System Architecture:** Figure 6, five parts: (1) tower and sign, (2) drone, (3) farmer and RC, (4) ground station, (5) cloud. Only the cloud needs internet.
* Design decisions: (1) the laptop runs YOLOv8, and the Pi only reads markers (~640×480, ~10 fps; Shalash et al., 2026); (2) only the Pi steers; (3) no internet needed to scan.

**Slide 13b: Proposed System Architecture · Scan Sequence**

* GPS waypoint → search for the 15 × 15 cm approach marker → align on 6 × 6 cm face markers (solvePnP, MAVLink corrections) → climb face A bottom to top → next face → land and finalize from the 1080p recording.
* Failsafes: Wi-Fi lost → keep scanning · markers lost → hold ~10 s, then RTL · RC or battery lost → ArduPilot RTL · wind over limit → operator cancels. The RC transmitter stays with a trained researcher.

**Slide 13c: Proposed System Architecture · Technical Design**

* Figure 7: power (separate 5 V BEC for the Pi), flight control, companion + camera, ground link.
* ~200–240 g; 3S 650 mAh; 3–5 min.
* Bench checks: weigh, thrust test (1404 motors if over ~half throttle), AutoTune, camera calibration, marker fps.

**Slide 13d: Proposed System Architecture · Key Features**

* Architecture layers, matching the template's Users → Web/Application → Database → Dashboard:
  * Web front end (Next.js, qr-scanner, Leaflet)
  * Cloud back end (Supabase)
  * Ground processing (ROS 2, Python/OpenCV, YOLOv8, ByteTrack, SQLite)
  * Drone companion (Picamera2, GStreamer, pymavlink, OpenCV)
  * Flight control (ArduPilot, `[ground control station]`)
  * Build and test (Supabox, Gazebo + SITL)
* **Key Features:**
  * Register towers by QR, even offline
  * Tower map
  * Request scans
  * Inspection history
  * Per-pot results
  * Exportable datasets
  * Local Live Scan view
  * Sync Center with no duplicates

---

**Slide 14: Project Timeline (Gantt Chart)**

| Activities | Month 1 | Month 2 | Month 3 | Month 4 | Month 5 | Month 6 |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| Proposal Defense (Nov 3, 2026) | ◆ |  |  |  |  |  |
| Requirements Planning (interviews, site observation, SWOT) | ■ | ■ |  |  |  |  |
| Validation of Instruments | ■ | ■ |  |  |  |  |
| User Design (architecture, UI, Gazebo + SITL) |  | ■ | ■ |  |  |  |
| Rapid Construction – Stage 1 (dashboard, sign, ~2,000-image dataset, manual flight) |  | ■ | ■ | ■ |  |  |
| Rapid Construction – Stage 2 (Pi + camera + GPS, alignment, full pipeline) |  |  | ■ | ■ | ■ |  |
| Cutover Testing (model, flight, streaming, sync, end to end) |  |  |  | ■ | ■ |  |
| User Evaluation and Data Analysis |  |  |  |  | ■ | ■ |
| Documentation and Final Defense |  |  |  |  |  | ■ |

`[Proposed schedule. Chapter 1 v2 sets no dates; replace Month 1–6 with actual months.]`

---

**Slide 15: Expected Output**

* **Deliverables**
  * Working prototype drone (ArduPilot, Pi Zero 2 W, Pi Camera V2) that scans a full tower on its own.
  * 1.5 m tower frame, printed QR sign, 20 laminated ArUco markers.
  * YOLOv8 model + ~2,000 labeled images (lettuce, empty pot).
  * Local dashboard (Live Scan, Sync Center, SQLite cache) and Next.js + Supabase web dashboard.
  * Test results and the final manuscript.
* **Anticipated Benefits**
  * Per-tower lettuce count, empty pot count and slot availability without walking every tower.
  * Replanting and harvest planned from slot availability.
  * A reusable dataset and method for future research.

*Visual:* illustrative per-tower dashboard mock-up, labeled as an example, not results.

---

**Slide 16: Budget Requirements (Optional)**

| Item | Cost |
| ----- | ----- |
| Flight hardware (frame, F405 stack, 4 motors, props, GPS) | ₱10,969 – ₱11,369 |
| Power and control (3 LiPo, charger, 5 V regulator, RC set) | ₱6,089 |
| Pi and camera (Pi Zero 2 W, Camera V2, cable, microSD) | ₱4,729 – ₱4,849 |
| Tower and markers (frame, sign, 20 markers, net pots, lettuce) | ₱1,900 – ₱2,660 |
| Fabrication (TPU, PLA/ABS filament, screws) | ₱1,450 – ₱2,700 |
| Field tools (anemometer; Wi-Fi via laptop hotspot) | ₱500 – ₱800 |
| Printing | ₱`[to be estimated]` |
| Internet | ₱`[to be estimated]` |
| Transportation | ₱`[to be estimated]` |
| Miscellaneous | ₱`[to be estimated]` |

**Total Budget:** ₱25,637 – ₱28,467 (hardware, Table 5 of Chapter 1 v2)

*Note on the slide:* excludes the ground laptop. Add ₱3,000–4,000 only if 1404 motors are needed, and ₱1,000–1,500 only if a travel router is needed.

---

**Slide 17: Thank You / Open Forum**

**Questions, Comments, and Suggestions**

---

## Backup Slides (show only when asked)

| Slide | Content | Likely panel question |
| ----- | ----- | ----- |
| **A** (`slide-A1`) | SWOT Analysis (Figure 4, v2) | "What are the weaknesses and risks?" |
| **B** (`slide-A2`) | CAAP Part 11 open-category checklist; on-flight and respondent safety | "Is it safe? Is it legal to fly?" |
| **C** (`slide-A3`) | Hardware components (Table 1) | "Why these components?" |

**Still to prepare** (suggested in the template, not yet in Chapter 1 v2): Database Design (ERD), Use Case Diagram, and prototype screenshots once available.

---

**Presentation Guidelines**

* Maximum 6 bullet points per slide
* Use visual diagrams instead of lengthy paragraphs
* Maintain consistent colors and layouts
* Allocate 15–20 minutes for the proposal presentation
