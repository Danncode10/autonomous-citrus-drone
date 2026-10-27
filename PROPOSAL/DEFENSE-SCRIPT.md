# Thesis Proposal Defense: Speaker Script

**Computer Vision and Autonomous Drone Inspection for Hydroponic Towers with Web Dashboard Integration**
November 3, 2026 · Nueva Vizcaya State University · College of Information Technology Education

Covers slide-01 to slide-05 so far. slide-06 to slide-17 will be added later.

**Slide order in the PowerPoint (24 slides).** Insert the images from `slides/` in this order. The script names each slide by its image file.

| # | Image file | Slide |
| ----- | ----- | ----- |
| 1 | slide-01.png | Title |
| 2 | slide-02-0-section-problem.png | Section: The Problem |
| 3 | slide-02.png | Background of the Study |
| 4 | slide-03a.png | Related Literature: Monitoring and Detection |
| 5 | slide-03b.png | Related Literature: Navigation, Processing and Data |
| 6 | slide-03c.png | Research Gap |
| 7 | slide-04-0-section-solution.png | Section: The Solution |
| 8 | slide-04.png | Conceptual Framework (IPO) |
| 9 | slide-05.png | Research Objectives |
| 10 | slide-06.png | Significance of the Study |
| 11 | slide-07.png | Scope and Delimitation |
| 12 | slide-08-0-section-method.png | Section: The Method |
| 13 | slide-08.png | Research Methodology |
| 14 | slide-09.png | Locale and Participants |
| 15 | slide-10.png | Research Instruments |
| 16 | slide-11.png | Data Gathering Procedure |
| 17 | slide-12.png | Statistical Treatment of Data |
| 18 | slide-13-0-section-system.png | Section: The System |
| 19 | slide-13.png | Proposed System Architecture |
| 20 | slide-14-0-section-plan.png | Section: The Plan |
| 21 | slide-14.png | Project Timeline |
| 22 | slide-15.png | Expected Output |
| 23 | slide-16.png | Budget Requirements |
| 24 | slide-17.png | Thank You / Open Forum |

**How to read this script**
- Times assume about 130 words per minute. Sentences marked ✂ can be cut if you run long.
- **`<next>`** means click to the next slide. The arrow after it names the image that should appear. Whoever is speaking clicks.
- Section slides (slide-02-0-section-problem and slide-04-0-section-solution) have no lines.
- *If asked* notes are short answers taken from Chapters 1 and 2, in case a panelist interrupts.

| Slide | Speaker | Time |
| ----- | ----- | ----- |
| slide-01 · Title | Lester Dann G. Lopez | 0:40 |
| slide-02-0-section-problem · Section: The Problem | Lester Dann G. Lopez | 0:02 |
| slide-02 · Background of the Study | Lester Dann G. Lopez | 1:35 |
| slide-03a · Related Literature: Monitoring and Detection | Rhoan Joy M. Marvilla | 1:00 |
| slide-03b · Related Literature: Navigation, Processing and Data | Rhoan Joy M. Marvilla | 1:20 |
| slide-03c · Research Gap | Rhoan Joy M. Marvilla | 0:30 |
| slide-04-0-section-solution · Section: The Solution | Rhoan Joy M. Marvilla | 0:02 |
| slide-04 · Conceptual Framework (IPO) | Rhoan Joy M. Marvilla | 1:15 |
| slide-05 · Research Objectives | Prince Daniel A. Valentino | 1:15 |
| | **Total for slide-01 to slide-05** | **≈ 7:40** |

---

## slide-01 · Title
**Speaker:** Lester Dann G. Lopez · **Time:** 0:40

Good [morning / afternoon] to our honorable panel members, to our thesis adviser, Bernadeth B. Liggayu, and to everyone present.

We are Lester Dann Lopez, Rhoan Joy Marvilla, Prince Daniel Valentino, and Joshua Jing Fernandez, from BS Computer Science 4B.

Today we present our thesis proposal, **"Computer Vision and Autonomous Drone Inspection for Hydroponic Towers with Web Dashboard Integration."**

In short: a small drone scans a hydroponic tower and tells the farmer which pots have lettuce and which are empty.

**`<next>`** → slide-02-0-section-problem · Section: The Problem

---

## slide-02-0-section-problem · Section: The Problem
**Speaker:** Lester Dann G. Lopez · **Time:** 0:02

**`<next>`** → slide-02 · Background of the Study

---

## slide-02 · Background of the Study
**Speaker:** Lester Dann G. Lopez · **Time:** 1:35

Vertical hydroponic farms stack crops in tiers to grow more food on less land, an idea Despommier proposed in 2010. But every tier adds another row of pots that someone has to check.

That checking is still done by hand. Domingo reported in 2022 that a lettuce farm in Iloilo recorded its data manually, with inconsistent results.

Most hydroponic technology today uses IoT sensors for temperature, pH, and nutrients, like the system of Chowdhury and colleagues. But **a sensor cannot tell a planted pot from an empty one.** Someone still has to look.

So our system does the looking. It works in four steps.

First, the farmer registers each tower by scanning a QR code with its ID and GPS location. Second, the drone flies there by GPS and uses printed ArUco markers to hold its distance and height. Third, a ground laptop runs YOLOv8 on the live video and matches each lettuce and empty pot to its exact slot. Fourth, the results go to a dashboard that works offline and syncs when internet is available.

The result: slot availability for every tower, without manual walk-throughs. ✂ This supports Sustainable Development Goals 2, 9, 11, and 12.

**`<next>`** → slide-03a · Related Literature: Monitoring and Detection

> **If asked: "Why not just add more sensors?"**
> Environmental sensors measure the air and the nutrient solution. Checking whether a pot holds a plant needs a visual record of the tower itself, which is why we use computer vision (Chapter 2, IoT and Smart Farming).

> **If asked: "Why lettuce only?"**
> Lettuce is the crop in the local hydroponic studies we reviewed (Domingo, 2022; Santiago et al., 2025). Limiting the study to one crop keeps the dataset and the evaluation manageable. Other crops are excluded in our delimitations.

---

## slide-03a · Related Literature: Monitoring and Detection
**Speaker:** Rhoan Joy M. Marvilla · **Time:** 1:00

Thank you. Each study here is tagged: **Adopted** means we use it, **Gap** means what it leaves out, and **Evidence** supports the problem.

Chowdhury, Domingo, and Santiago built IoT systems that monitor growing conditions in hydroponics, but none checks whether a pot holds a plant.

Domingo also shows that local farms still record data by hand.

Wang, Wu, and Shen detected hydroponic lettuce with YOLOv8 at about 99 percent precision and recall, so we adopt YOLOv8. But their model had **no class for empty pots**, and their camera did not move like a drone.

And from Zhang and Villacrés, we adopt ByteTrack tracking so each pot is counted once, checked against manual counts.

**`<next>`** → slide-03b · Related Literature: Navigation, Processing and Data

> **If asked: "Why YOLOv8 and not a newer version?"**
> YOLOv8 has published results on hydroponic lettuce (Wang et al., 2024) and a documented evaluation method using precision, recall, and mAP (Terven et al., 2023). That gives us a baseline to compare against.

---

## slide-03b · Related Literature: Navigation, Processing and Data
**Speaker:** Rhoan Joy M. Marvilla · **Time:** 1:20

Agricultural drones, as Aslan and Stefas found, work mostly over open fields and orchards, and GPS is unreliable near the ground. None inspects a single tower.

GPS is accurate only to a few meters. Wubben and Andrzejewski fixed this with ArUco markers, a Raspberry Pi, and ArduPilot. We adopt that: GPS gets the drone near, markers align it. But they only used markers for **landing on flat pads**, not for staying beside a vertical face.

ArUco markers, from Garrido-Jurado, work even when partly hidden, and Lepetit's EPnP method gives the camera's exact position from a marker's four corners. That is how our drone knows its distance, height, and face.

Benoit-Cattin found that a Raspberry Pi can overheat running neural networks, and Zhu and Chen showed offloading depends on Wi-Fi. So YOLOv8 runs on the ground laptop, while quick corrections stay on the drone.

Lastly, rural internet in the Philippines is uneven, as Mirandilla-Santos reported, so we follow Kleppmann's local-first approach: save locally, upload later.

**`<next>`** → slide-03c · Research Gap

> **If asked: "Why not run YOLOv8 on the drone itself?"**
> Sustained neural network load on a small, passively cooled board is likely to cause thermal throttling (Benoit-Cattin et al., 2020). Keeping detection on the ground laptop keeps the drone light and avoids slowdowns in flight.

> **If asked: "What happens if Wi-Fi drops mid-scan?"**
> The drone continues the scan using its onboard marker alignment and saves a backup recording on its memory card. The missing parts are processed after landing.

---

## slide-03c · Research Gap
**Speaker:** Rhoan Joy M. Marvilla · **Time:** 0:30

Each area solves part of the problem: IoT misses pot occupancy, lettuce detection misses empty pots, farm drones miss single towers, and marker-based drones only land.

**No study we reviewed combines all four.** That is our gap, and our system brings them together, tested on lettuce towers in an open outdoor area here in the Philippines.

**`<next>`** → slide-04-0-section-solution · Section: The Solution

---

## slide-04-0-section-solution · Section: The Solution
**Speaker:** Rhoan Joy M. Marvilla · **Time:** 0:02

**`<next>`** → slide-04 · Conceptual Framework (IPO)

---

## slide-04 · Conceptual Framework (Input–Process–Output)
**Speaker:** Rhoan Joy M. Marvilla · **Time:** 1:15

We framed the study as Input–Process–Output. Our inputs are the problem, from interviews with hydroponic farmers; the knowledge from the literature; and the hardware and software listed here. ✂ These include the SpeedyBee flight controller, the Raspberry Pi with its camera, the ESP32 tower unit, YOLOv8, ArduPilot, Supabase, and Next.js.

The process follows Rapid Application Development, or RAD. **Requirements Planning** gathers farmer needs and finalizes components. **User Design** covers the architecture, database, and dashboard, and tests the full scan in a Gazebo simulation before any real flight. **Rapid Construction** builds the drone and tower unit, trains YOLOv8, and develops the software.

These two phases repeat until each part works.

**Cutover** tests everything outdoors, measuring detection accuracy, counting error, and scan success, then runs the user evaluation.

The output is our system, reporting lettuce count, empty pot count, and slot availability for every tower.

Test and evaluation results feed back into the next iteration.

**`<next>`** → slide-05 · Research Objectives

> **If asked: "Why RAD and not Waterfall or Agile?"**
> RAD focuses on quick prototypes and repeated user feedback instead of a long, fixed plan (Martin, 1991). Our drone, detection model, and dashboard each need several build-and-test rounds before they work together, which matches RAD's repeated design and construction cycle.

---

## slide-05 · Research Objectives
**Speaker:** Prince Daniel A. Valentino · **Time:** 1:15

Thank you. Our general objective is to develop an autonomous drone system that registers towers by QR code, flies to them by GPS, aligns using markers, scans every face, detects lettuce and empty pots, and shows the records on a web dashboard.

Specifically, we aim to:

**One,** identify how farmers monitor towers today, to set our baseline requirements.

**Two,** build the tower unit with its QR code, and the web dashboard.

**Three,** develop navigation and alignment using GPS, YOLOv8, and the QR and ArUco markers.

**Four,** develop the YOLOv8 model that maps lettuce and empty pots to their exact slots, and integrate it with the drone and dashboard.

**Five,** evaluate detection and counting accuracy, scan success, and the system's usefulness, ease of use, and user satisfaction.

The tags on the right show the RAD phase for each one. ✂ Objective five is measured with the tools on slide-12.

**`<next>`** → slide-06 · Significance of the Study

> **If asked: "How will you know Objective 5 is met?"**
> Detection is measured with precision, recall, and mAP@50. Counting is checked against manual counts per tower. Usefulness, ease of use, and satisfaction come from an adapted USE Questionnaire (Lund, 2001), interpreted with the weighted mean (Chapter 1, Data Treatment).

---

## Rehearsal checklist (slide-01 to slide-05)

- [ ] Each speaker has read their part aloud at least three times with a timer.
- [ ] Every speaker can answer the *If asked* notes on their slides without reading.
- [ ] Decide who says "Good morning" or "Good afternoon" based on the defense schedule.
- [ ] Total for slide-01 to slide-05 stays under 8 minutes, leaving about 10 minutes for slide-06 to slide-17.
- [ ] Click through the whole deck once and check that every `<next>` lands on the image named after the arrow.
