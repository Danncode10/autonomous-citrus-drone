# Thesis Proposal Defense: Speaker Script (v2)

**Computer Vision and Autonomous Drone Inspection for Hydroponic Towers with Web Dashboard Integration**
November 3, 2026 · Nueva Vizcaya State University · College of Information Technology Education

Source: **Chapter 1 v2.docx**, which now includes the Review of Related Literature. Slides follow the school template (`PROPOSAL/THESIS-PROPOSAL-DEFENSE-Template.docx.md`). Each slide is numbered by its template slide, and a template slide that needs more than one gets letters, as in v1 (03a, 03b…).

**How to read this script**
- Times assume about 130 words per minute. Sentences marked ✂ can be cut if you run long.
- **`<next>`** means click to the next slide. The arrow names the image that should appear. Whoever is speaking clicks.
- Section slides (`…-0-section-…`) have no lines; just click through.
- *If asked* notes are short answers taken from Chapter 1 v2, in case a panelist interrupts.

## Timing and speakers

Target: **about 19 minutes**, then open forum. Presenter assignment carries over from v1; rebalance it so each member presents what they built or wrote.

| Template | Slide | Speaker | Time |
| ----- | ----- | ----- | ----- |
| 1 | slide-01 · Title | Lester Dann G. Lopez | 0:35 |
| | slide-02-0 · Section: The Problem | Lopez | 0:02 |
| 2 | slide-02a · Introduction / Background of the Study | Lopez | 1:15 |
| 2 | slide-02b · Introduction · Key Concepts (Figure 5) | Lopez | 1:00 |
| 3 | slide-03a · RRL · Farm and Monitoring | Rhoan Joy M. Marvilla | 0:55 |
| 3 | slide-03b · RRL · Detection and Flight | Marvilla | 0:55 |
| 3 | slide-03c · RRL · Processing, Data and Method | Marvilla | 0:40 |
| 3 | slide-03d · Research Gap | Marvilla | 0:40 |
| | slide-04-0 · Section: The Solution | Marvilla | 0:02 |
| 4 | slide-04a · Conceptual Framework · IPO Model | Marvilla | 0:45 |
| 4 | slide-04b · Conceptual Framework · System Flow (Figure 1) | Marvilla | 0:55 |
| 5 | slide-05 · Research Objectives | Prince Daniel A. Valentino | 1:00 |
| 6 | slide-06 · Significance of the Study | Valentino | 0:45 |
| 7 | slide-07 · Scope and Delimitation | Valentino | 0:55 |
| | slide-08-0 · Section: The Method | Valentino | 0:02 |
| 8 | slide-08a · Research Methodology · Research Design | Joshua Jing A. Fernandez | 0:55 |
| 8 | slide-08b · Research Methodology · Dataset (2,000 images) | Fernandez | 0:45 |
| 9 | slide-09 · Locale and Participants | Fernandez | 0:35 |
| 10 | slide-10 · Research Instruments | Fernandez | 0:45 |
| 11 | slide-11 · Data Gathering Procedure | Fernandez | 0:35 |
| 12 | slide-12 · Statistical Treatment of Data | Fernandez | 0:45 |
| | slide-13-0 · Section: The System | Fernandez | 0:02 |
| 13 | slide-13a · Proposed System Architecture (Figure 6) | Lopez | 0:55 |
| 13 | slide-13b · Scan Sequence and Failsafes | Lopez | 0:55 |
| 13 | slide-13c · Technical Design (Figure 7) | Lopez | 0:35 |
| 13 | slide-13d · Architecture Layers and Key Features | Lopez | 0:35 |
| | slide-14-0 · Section: The Plan | Lopez | 0:02 |
| 14 | slide-14 · Project Timeline (Gantt Chart) | Lopez | 0:25 |
| 15 | slide-15 · Expected Output | Lopez | 0:35 |
| 16 | slide-16 · Budget Requirements | Lopez | 0:30 |
| 17 | slide-17 · Thank You / Open Forum | All | 0:10 |
| | | **Total** | **≈ 19:00** |

Backup slides A–C (SWOT, safety and regulation, hardware) come after slide-17. Show them only when asked.

---

## slide-01 · Title
**Speaker:** Lopez · **Time:** 0:35

Good [morning / afternoon] to our honorable panel members, to our thesis adviser, Bernadeth B. Liggayu, and to everyone present.

We are Lester Dann Lopez, Rhoan Joy Marvilla, Prince Daniel Valentino, and Joshua Jing Fernandez, from BS Computer Science 4B.

Today we present **"Computer Vision and Autonomous Drone Inspection for Hydroponic Towers with Web Dashboard Integration."** In one line: a small drone scans a hydroponic tower and tells the farmer which pots have lettuce and which are empty.

**`<next>`** → slide-02-0-section-problem
**`<next>`** → slide-02a · Introduction / Background of the Study

---

## slide-02a · Introduction / Background of the Study
**Speaker:** Lopez · **Time:** 1:15

First, the context. Vertical farms stack crops in tiers. Van Delden and colleagues found that this saves land and water, but only if the farm is managed well.

The current situation: managing it is still done by hand. A lettuce farm in Iloilo logged its data manually, with inconsistent results, and in Bohol, Bunga reported that hydroponic systems still rely on manual monitoring.

Most farm technology today is IoT: sensors for temperature, humidity, pH and nutrients. Look at the readout on the left. It knows the pH. It does not know **which pots are empty**. Someone still has to walk up, look, and write it down.

And it is never just one tower. **A farm has many towers**, and stackable towers grow taller module by module, so checking every pot by hand takes longer as the farm grows.

That is why this study matters: **slot availability**, empty pots against total slots, for every tower on the farm, tells farmers where to replant and when to harvest. ✂ This work supports SDGs 2, 9, 11 and 12.

**`<next>`** → slide-02b · Key Concepts

> **If asked: "Why not just add more sensors?"**
> Sensors measure the air and the nutrient solution. Whether a pot holds a plant needs a visual record of the tower itself (Chapter 1 v2, IoT and Smart Farming).

---

## slide-02b · Introduction · Key Concepts
**Speaker:** Lopez · **Time:** 1:00

So our system does the looking. Four key concepts, in four steps; the numbers on the right match Figure 5.

**One, QR registration:** the farmer scans a printed QR sign on the tower, and the phone saves its own GPS as the tower's location. **Two, GPS and ArUco markers:** the drone flies there by GPS, then the Raspberry Pi finds the markers and holds its distance, height and face. **Three, YOLOv8 computer vision:** the drone scans every face, bottom to top, while a ground laptop shows a live preview; the final count comes from the full recording after landing. **Four, an offline-first dashboard:** results are saved offline, and the farmer uploads them when there is internet.

And this is built for **the whole farm, not one tower**. Each tower is registered with its own QR code and location, so the same drone inspects every tower, one after another. Adding a tower costs only a printed sign, no electronics.

**`<next>`** → slide-03a · Related Literature: Farm and Monitoring

> **If asked: "Why a printed sign and not an electronic tower unit?"**
> A sign costs about ₱150 and needs no battery or wiring. The phone already has GPS, so the tower does not need its own. That keeps the cost of adding towers low (Table 5).

---

## slide-03a · Review of Related Literature · Farm and Monitoring
**Speaker:** Marvilla · **Time:** 0:55

Thank you. We reviewed 38 sources, shown in three tables: author, key findings, and relevance. The tags say whether we **adopted** it, whether it leaves a **gap**, or whether it is **evidence** for the problem.

Van Delden, Saad and Siregar show vertical farms only pay off when managed well, but they focus on the environment, not on which slots are in use. Locally, SIGLA at UPLB and Bendanillo's PVC gardens confirm that towers are made of discrete slots. Domingo and Bunga show monitoring is still manual. IoT studies like Dhanaraju and Santiago track the air and water, but none reports whether a slot holds a plant.

And from Qian and GPS.gov: a QR code reads reliably at the right size, and phone GPS is accurate to about **4.9 meters**. So we use a printed QR sign with the phone's GPS, and GPS only gets the drone near.

**`<next>`** → slide-03b · Related Literature: Detection and Flight

---

## slide-03b · Review of Related Literature · Detection and Flight
**Speaker:** Marvilla · **Time:** 0:55

For detection, Terven and Ultralytics support YOLOv8 and its metrics. Wang and colleagues reached about **99 percent** precision on hydroponic lettuce with 2,240 frames, so we adopt YOLOv8 with about 2,000 images. But their model had **no empty-pot class**, and their camera was stable.

ByteTrack, from Zhang, counts each pot once. Villacrés found a **20 percent** counting error even with good trackers, so we check against manual counts.

For flight, Aslan found almost no drone work in greenhouses, and CogniFly, **under 250 grams**, gave us our frame concept. Kalaitzakis and Andrzejewski show a Pi with ArduPilot can align on markers, but **only for landing on flat pads**, not beside a vertical face.

**`<next>`** → slide-03c · Related Literature: Processing, Data and Method

> **If asked: "Why YOLOv8 and not a newer version?"**
> YOLOv8 has published results on hydroponic lettuce (Wang et al., 2024) and a documented evaluation method (Terven et al., 2023), which gives us a baseline to compare against.

---

## slide-03c · Review of Related Literature · Processing, Data and Method
**Speaker:** Marvilla · **Time:** 0:40

Shalash found YOLO on a Raspberry Pi runs **under 3 frames per second**, and Zhu and Chen showed that Wi-Fi offloading fails when the link weakens. So YOLOv8 runs on the laptop, and steering stays on the Pi.

Rural connectivity is uneven, and an offline-first farm app kept full sync, so we cache offline and sync later. ✂ Schulze Schwering and Supabase shape the dashboard; Meier, ArduPilot and CAAP shape our safety rules; and Fauzi and Hajesmaeel-Gohari support RAD and the USE questionnaire.

**`<next>`** → slide-03d · Research Gap

---

## slide-03d · Research Gap
**Speaker:** Marvilla · **Time:** 0:40

Read this table across. IoT studies cover none of these columns. Lettuce detection sees plants, but not empty pots. Agricultural drones fly over fields, not beside one tower. Marker-based drones align, but only for landing. Offline-first apps work offline, but do none of the rest.

**No study we reviewed combines all of it.** That is our gap: one low-cost system, tested on lettuce towers in an open outdoor area, in the Philippine setting.

**`<next>`** → slide-04-0-section-solution
**`<next>`** → slide-04a · Conceptual Framework · IPO Model

---

## slide-04a · Conceptual Framework · Input–Process–Output (IPO) Model
**Speaker:** Marvilla · **Time:** 0:45

We framed the study as Input–Process–Output. **Inputs**: farmer interviews, the literature, and the hardware and software, including the printed tower sign. **Process**: the four RAD phases, with User Design and Rapid Construction repeating until each part works, measured by precision, recall, mAP@50, counting error, scan success, and the weighted mean of user ratings. **Output**: a system that reports lettuce count, empty pot count and slot availability for every tower. Test results feed back into the next iteration.

**`<next>`** → slide-04b · Conceptual Framework · System Flow

> **If asked: "Why RAD and not Waterfall or Agile?"**
> RAD favors quick prototypes and repeated user feedback over a long, fixed plan, and has the shortest completion time among SDLC models (Fauzi et al., 2023). The drone, the model and the dashboard each need several build-and-test rounds before they work together.

---

## slide-04b · Conceptual Framework · System Flow (Figure 1)
**Speaker:** Marvilla · **Time:** 0:55

Figure 1 shows how that output works in the field, in two zones.

At the tower, on local Wi-Fi only: the farmer scans the QR and saves the phone's GPS, **step 1**. The laptop sends the mission, **3**. The drone approaches, aligns and scans each face, **4**. Video streams to the laptop for a live preview, **5a**. After landing, the full recording is processed for the final count, **5b**.

The internet is used only for records: uploading the registration, **2**; syncing, **6**; and showing the counts on the dashboard, **7**.

**`<next>`** → slide-05 · Research Objectives

---

## slide-05 · Research Objectives
**Speaker:** Valentino · **Time:** 1:00

Thank you. Our general objective, in short: register towers with a printed QR code and the phone's location, fly there by GPS, align with markers, scan every face, detect lettuce and empty pots, and show the records on a web dashboard.

Five specific objectives. **One**, set the baseline: how farmers monitor towers today, including how often and how long they check. **Two**, an offline-ready dashboard for QR registration, scan requests and records. **Three**, navigation and alignment with GPS plus onboard QR and ArUco markers. **Four**, the YOLOv8 model: live preview in flight, final count from the recording, each detection matched to its pot. **Five**, evaluation.

Each card shows the evidence we will collect and the RAD phase. ✂ Objective five is measured with the tools on slide 12.

**`<next>`** → slide-06 · Significance of the Study

---

## slide-06 · Significance of the Study
**Speaker:** Valentino · **Time:** 0:45

At the center is the idea of the whole study: **one drone for every tower on the farm**. The benefits spread outward from there. **Farmers** spend less time checking pots, especially the upper levels. **Managers and workers** get a per-tower history with fewer counting errors. **Students and researchers** get a reference and a labeled dataset. The **academic community** gains work on smart farming and computer vision. And **local agricultural offices** get guidance on affordable vertical farming.

Our **technical contribution**: we extend marker alignment from landing pads to the vertical faces of a tower, and map every detection to its exact pot.

**`<next>`** → slide-07 · Scope and Delimitation

---

## slide-07 · Scope and Delimitation
**Speaker:** Valentino · **Time:** 0:55

Our **scope**, on the right: QR registration, GPS approach with onboard alignment, YOLOv8 detection matched to each pot, the offline cache and dashboards. We build and test **one 1.5-meter tower** to fit the budget, but the system is designed for the whole farm: every registered tower is scanned the same way.

Our **delimitations**. On the left are the limits we fly within: the drone stays **no higher than 1.8 meters** and **within 20 meters** of launch; one tower per battery, three to five minutes; daylight and fair weather, with wind checked on an anemometer; an open area with GPS; local Wi-Fi only. And we exclude watering systems, other crops, plant health, obstacle avoidance, indoor flight, LiDAR, and commercial deployment.

**`<next>`** → slide-08-0-section-method
**`<next>`** → slide-08a · Research Methodology · Research Design

> **If asked: "Why only one tower?"**
> Each stackable module adds printing and material cost, so one 5 ft tower fits the budget. Because the drone scans face by face using markers at known positions, the method is meant to extend to taller towers and many towers.

> **Fill in before the defense:** the maximum wind speed (km/h) is still blank in Chapter 1 v2.

---

## slide-08a · Research Methodology · Research Design
**Speaker:** Fernandez · **Time:** 0:55

Thank you. This is a **developmental** study with a **mixed-method** approach: interviews for qualitative data, and system tests and user ratings for quantitative data. It follows **Rapid Application Development**.

**Phase 1**, Requirements Planning: farmer interviews, site observation, choosing components, and SWOT. **Phases 2 and 3** repeat as a loop: we design, including a full scan in **Gazebo simulation** with lost-marker and lost-Wi-Fi tests, then build the drone with a thrust test, the tower and markers, the dataset, and the software. **Phase 4**, Cutover: end-to-end tests and user evaluation.

Construction runs in two stages: first the dashboard, sign, dataset and manual flight; then the Pi, camera and GPS on the drone and the full pipeline.

**`<next>`** → slide-08b · Research Methodology · Dataset

---

## slide-08b · Research Methodology · Dataset
**Speaker:** Fernandez · **Time:** 0:45

The model learns from about **2,000 labeled images**. That is close to the 2,240 frames Wang and colleagues used, and above the Ultralytics guideline of 1,500 images per class.

At least **1,500 images contain lettuce**, at least **1,500 contain empty pots**, and 5 to 10 percent are background images with neither, to reduce false detections.

We capture video from every side, distance and lighting; take one frame about every second; label in Supabox; and train YOLOv8. The split is **70, 20, 10**, and every image from one recording session stays in one set, so the test images are truly unseen.

**`<next>`** → slide-09 · Locale and Participants

> **If asked: "Is 2,000 images enough?"**
> It matches the published lettuce study (Wang et al., 2024) and the 1,500-per-class guideline (Ultralytics). The 10,000-objects-per-class guideline is treated as a goal for best results, not a minimum.

---

## slide-09 · Locale and Participants
**Speaker:** Fernandez · **Time:** 0:35

Our research locale: flight tests at **Purok 2, Busilac, Bayombong**, an open, obstacle-free area with GPS, and interviews at **Savara Lettuce Farm** in Masoc, Bayombong, the only hydroponic farm in town.

The population is **one hydroponic farmer and three IT experts** from CITE, four in total. Our sampling technique is **total enumeration**, so the sample size is all four.

**`<next>`** → slide-10 · Research Instruments

> **If asked: "Isn't four respondents too few?"**
> Total enumeration covers the whole population: Savara is the only hydroponic farm in Bayombong, and three IT experts are available. The main claims of the study rest on system performance tests (detection, counting, alignment), which are measured on many images and flights, not on the four ratings.

---

## slide-10 · Research Instruments
**Speaker:** Fernandez · **Time:** 0:45

Four instruments. A **survey questionnaire**, adapted from the USE questionnaire: we shortened it from seven points to five, with "Moderately Agree" in place of neutral, covering usefulness, ease of use and satisfaction. An **interview guide** for farmers, in six parts, about 15 minutes. An **observation checklist** for tower size, open space, obstacles, wind and signal. And a **system evaluation tool**: the test logs.

For validation, our adviser reviews and approves the questionnaire before any data gathering.

**`<next>`** → slide-11 · Data Gathering Procedure

> **If asked about pilot or reliability testing:**
> Chapter 1 v2 covers expert (adviser) validation only, and the slide shows the other two as blanks. Decide your answer and fill them in before the defense; see `README.md`, open items.

---

## slide-11 · Data Gathering Procedure
**Speaker:** Fernandez · **Time:** 0:35

Five steps. **Secure approval** from the school and the farm owner. **Validation of instruments** with our adviser. **Data collection**: interviews with consent, the observation checklist, tower photos for the dataset, test flights, then the survey. **Data processing**, per tower and per flight. And **data analysis**.

Participation is voluntary, we follow the Data Privacy Act, photos show towers and not people, and we disclose our use of AI tools.

**`<next>`** → slide-12 · Statistical Treatment of Data

---

## slide-12 · Statistical Treatment of Data
**Speaker:** Fernandez · **Time:** 0:45

For the model: **precision**, **recall** and **mAP at 50**, on unseen images. For counting: the **counting error per tower** against a manual count, and **slot matching accuracy**. For flights: alignment success and error in centimeters, full-scan completion, stream delay and frame loss, and flight time.

For the survey: the **weighted mean and standard deviation** per category, read with this scale, from Highly Acceptable at 4.21 and up, down to Highly Not Acceptable. Interviews go through thematic analysis and update the SWOT.

**`<next>`** → slide-13-0-section-system
**`<next>`** → slide-13a · Proposed System Architecture

---

## slide-13a · Proposed System Architecture (Figure 6)
**Speaker:** Lopez · **Time:** 0:55

Figure 6 shows five parts: the tower and sign, the drone, the farmer, the ground station, and the cloud. **Only the cloud needs internet.**

Three design decisions. **First**, the laptop does the AI. A Pi Zero 2 W running YOLOv8 would be slow and could overheat; the Pi only reads markers at about 640 by 480, ten frames a second. **Second**, only the Pi steers. The laptop never sends flight commands, because Wi-Fi delay varies and a late correction near the tower could cause a collision. **Third**, no internet is needed to scan. The farmer decides when to upload.

**`<next>`** → slide-13b · Scan Sequence and Failsafes

---

## slide-13b · Scan Sequence and Failsafes
**Speaker:** Lopez · **Time:** 0:55

Here is one scan. The drone flies by GPS to an approach point. The Pi turns it slowly until it sees the **15-centimeter approach marker** on the sign. Then the **6-centimeter markers** on each face give its pose through solvePnP, and the Pi sends small corrections. It climbs face A **bottom to top**, moves to the next face, and repeats. After landing, the 1080p recording goes to the laptop for the final count.

If Wi-Fi drops, it **keeps scanning**. If markers are lost, it **holds about ten seconds**, then returns to launch. If the RC link or battery fails, ArduPilot returns it home. And a trained researcher always holds the RC transmitter.

**`<next>`** → slide-13c · Technical Design

---

## slide-13c · Technical Design (Figure 7)
**Speaker:** Lopez · **Time:** 0:35

Inside the drone: the LiPo powers the flight stack, and a **separate 5-volt BEC** powers the Pi so motor surges cannot restart it. The SpeedyBee runs ArduPilot with GPS and compass. The Pi talks to it over MAVLink and records 1080p video. The drone weighs an estimated 200 to 240 grams.

Before flying, we weigh it, run a thrust test, and switch to 1404 motors if it needs more than half throttle to hover, then run AutoTune.

**`<next>`** → slide-13d · Architecture Layers and Key Features

---

## slide-13d · Architecture Layers and Key Features
**Speaker:** Lopez · **Time:** 0:35

The architecture, layer by layer: the web front end on Next.js; Supabase in the cloud; YOLOv8, ByteTrack and SQLite on the laptop; Picamera2, GStreamer, MAVLink and OpenCV on the Pi; and ArduPilot flying the drone.

Key features: farmers register towers by QR even offline, see them on a map, request scans, and review history and per-pot results. At the farm, the local dashboard shows the **live scan** and has the **Sync Center**.

**`<next>`** → slide-14-0-section-plan
**`<next>`** → slide-14 · Project Timeline

---

## slide-14 · Project Timeline (Gantt Chart)
**Speaker:** Lopez · **Time:** 0:25

We plan six months, following the RAD phases: planning first, then design and construction overlapping as a loop, then cutover testing, evaluation, and the final defense.

**`<next>`** → slide-15 · Expected Output

---

## slide-15 · Expected Output
**Speaker:** Lopez · **Time:** 0:35

Anticipated benefits: a per-pot view of each tower, with lettuce, empty pots and slot availability, so farmers can plan replanting and harvest without walking every tower. This is a mock-up, not a result.

Our deliverables: the working drone; the tower, sign and markers; the YOLOv8 model with the **2,000-image dataset**; the local and web dashboards; and the test results and manuscript.

**`<next>`** → slide-16 · Budget Requirements

---

## slide-16 · Budget Requirements
**Speaker:** Lopez · **Time:** 0:30

The hardware costs about **₱25,600 to ₱28,500**. The biggest share is the flight hardware. This excludes the laptop we already own; the 1404 motors and a travel router are bought only if tests show we need them. Each extra tower needs only a printed sign and markers. ✂ Printing, internet, transportation and miscellaneous costs are [to be estimated].

**`<next>`** → slide-17 · Thank You

---

## slide-17 · Thank You / Open Forum
**Speaker:** All · **Time:** 0:10

Thank you. We welcome your questions, comments and suggestions.

---

## More *If asked* answers

> **"What if the drone drifts in the wind?"**
> ArduPilot stabilization and GPS position hold, tuned with AutoTune, plus marker corrections from the Pi. Flights happen only below the wind limit, checked with an anemometer; above it, the operator cancels and the drone returns to launch. → Backup B.

> **"Is it legal to fly?"**
> Yes, in the CAAP Part 11 open category: under 25 kg, within sight, below 120 m, in daylight, and at least 30 m from anyone not involved. → Backup B.

> **"How do you know which pot a detection belongs to?"**
> ArUco markers sit at known positions on each face. Their positions in the frame give each detection its face, level and position. The final status of a slot is decided from every frame it appeared in.

> **"What if a pot has no marker beside it?"**
> It is matched with lower confidence, which is listed as a weakness in the SWOT. → Backup A.

> **"Why not a 3D or LiDAR sensor?"**
> The task is only occupied or empty. 2D RGB is enough for that (Wang et al., 2024), and LiDAR adds weight and power to a drone of about 200–240 g.

> **"Why these specific parts?"** → Backup C.

---

## Rehearsal checklist

- [ ] Each speaker has read their part aloud at least three times with a timer.
- [ ] Every speaker can answer the *If asked* notes on their slides without reading.
- [ ] Decide who says "Good morning" or "Good afternoon".
- [ ] Fill in the blanks shown in yellow on the slides (wind limit on 07; pilot and reliability testing on 10; other budget items on 16; ground control station on 13d) and re-render.
- [ ] Click through the whole deck once and check that every `<next>` lands on the named image.
