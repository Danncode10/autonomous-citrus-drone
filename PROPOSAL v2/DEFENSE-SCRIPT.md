# Defense Script

Each heading is the exact image file name in the `slides/` folder, in the same order.

---

## slide-01.png · Title (Lopez)

Good [morning / afternoon] to our panel, to our adviser, Bernadeth B. Liggayu, and to everyone here. I am Lester Dann Lopez, with Rhoan Joy Marvilla, Prince Daniel Valentino, and Joshua Jing Fernandez, from BSCS 4B. Today we present "Computer Vision and Autonomous Drone Inspection for Hydroponic Towers with Web Dashboard Integration."

---

## slide-02-0-section-problem.png · Section: Part One: The Problem

(No lines.)

---

## slide-02a.png · Introduction / Background of the Study (Lopez)

Vertical farms save land, but only if they are managed well, according to van Delden and Saad. Today, monitoring is still manual, as Domingo and Bunga show for farms in Iloilo and Bohol. And sensors can't see an empty pot. IoT, in studies by Dhanaraju and Santiago, measures pH and nutrients, and a weight sensor per pot needs its own wiring and shows no picture.

So on every tower, and every other tower on the farm, someone still walks up and checks by hand. Knowing the slot availability tells farmers where to replant and when to harvest.

---

## slide-02b.png · Introduction · Key Concepts (Lopez)

Our key concept: one drone checks every pot on every tower, in four steps.

Step 1, register: the farmer scans the tower's QR sign, and the phone saves its GPS. Step 2, fly and align: GPS gets the drone near, and the ArUco markers hold its position. Step 3, scan and detect: the drone scans every face, and YOLOv8 counts lettuce and empty pots. Step 4, upload and view: results are saved offline, then uploaded to the dashboard.

---

## slide-03a.png · Review of Related Literature · Farm and Monitoring (Marvilla)

Thank you. We reviewed 38 sources.

Van Delden, Saad and Siregar found vertical farms save land and water, but only if they are managed well. They don't track which slots are being used.

DOST-PCAARRD and Bendanillo show local towers are built in separate slots, the same layout our drone scans.

Domingo and Bunga found farms in Iloilo and Bohol still check by hand, and Petropoulou showed that knowing where the plants are helps plan the space.

Dhanaraju and Santiago's sensor systems track pH and nutrients, but never check if a slot has a plant.

Qian found phones read QR codes reliably, and GPS.gov says phone GPS can be off by about 4.9 meters. So we use the QR code and phone GPS to register towers, and the marker on the sign for the final alignment.

---

## slide-03b.png · Review of Related Literature · Detection and Flight (Marvilla)

Terven and Ultralytics describe YOLO as a fast AI that finds objects in video. Wang, Wu and Shen used YOLOv8 on lettuce and scored about 99 percent. So we use YOLOv8, but they never taught it to find empty pots.

Zhang's ByteTrack makes sure each plant is counted only once. Still, Villacrés found video counts can be off by about 20 percent, so we compare ours with a count done by hand.

Aslan found drones are rarely flown close to plants. De Azambuja's CogniFly, under 250 grams, showed a light drone is safer, and Aliane shows ArduPilot lets us test in simulation first.

Kalaitzakis, OpenCV and Andrzejewski show printed markers help a drone position itself exactly, but only for landing, never beside a tower.

---

## slide-03c.png · Review of Related Literature · Processing, Data and Method (Marvilla)

Shalash found AI runs too slowly on a Raspberry Pi, and Zhu and Chen found Wi-Fi can lag. So the laptop runs the AI, and the drone steers itself.

Mirandilla-Santos and Serafica show rural internet is unreliable, and Mayta's farm app worked offline and synced later. Ours does the same.

Schulze Schwering and Supabase shaped our dashboard; Meier, ArduPilot and CAAP, our safety rules; and Fauzi and Hajesmaeel-Gohari, our RAD method and survey.

---

## slide-03d.png · Research Gap (Marvilla)

Each piece exists, but no study puts them together. Dhanaraju, Domingo and Santiago don't look at the pots. Wang and Petropoulou find plants, not empty pots. Aslan and de Azambuja fly over fields, not beside a tower. Andrzejewski uses markers only to land. Mayta's app works offline, but does nothing more. No study we reviewed does all of this. Ours does.

---

## slide-04-0-section-solution.png · Section: Part Two: The Solution

(No lines.)

---

## slide-04a.png · Conceptual Framework · Input–Process–Output (IPO) Model (Marvilla)

Our framework follows the Input–Process–Output model, from farmer needs to a working inspection system.

The input has three parts. The problem input comes from interviews with farmers on how they monitor towers today. The knowledge input comes from the literature on vertical farming, computer vision, drones and markers. The technical inputs are our hardware and software: the SpeedyBee flight controller, GPS, Raspberry Pi and camera, the printed tower sign, ArUco markers, the ground laptop, YOLOv8, ArduPilot, Supabase and the web dashboard.

The process follows RAD in four phases. Phase 1, Requirements Planning: we gather farmer needs and choose the components, scope and evaluation criteria. Phase 2, User Design: we design the system, database, dashboard and drone mission, and test it in a Gazebo simulation first. Phase 3, Rapid Construction: we build the drone, tower, sign, dataset, YOLOv8 model, streaming and dashboard. Phases 2 and 3 repeat until each part works. Phase 4, Cutover: we test the whole system outdoors, then run the user evaluation.

We measure it with precision, recall and mAP@50, counting error, alignment and scan success, and the weighted mean of the USE survey.

The output is our system, which reports the lettuce count, empty pot count and slot availability for every tower. And feedback from the tests and evaluations goes back into the next cycle.

---

## slide-04b.png · Conceptual Framework · System Flow (Marvilla)

At the tower, everything runs on local Wi-Fi: scan the QR, send the mission, scan the tower, preview live, and process the full recording after landing. The internet is used only for the records: uploading, syncing, and showing the counts on the dashboard.

---

## slide-05a.png · Research Objectives · General Objective (Valentino)

Thank you. This study aims to design and develop an autonomous drone-based monitoring system that registers vertical hydroponic towers through a printed QR code and the location of the farmer's phone, navigates to each tower using GPS, aligns itself using computer vision and visual markers, scans every face of the tower in an open space, detects lettuce plants and empty planting pots using computer vision, and displays tower-level records on a web-based dashboard.

---

## slide-05b.png · Research Objectives · Specific Objectives (Valentino)

The specific objectives of the study are:

1. To identify the existing tools, process, and challenges in monitoring vertical hydroponic farming to establish the system's baseline requirements.
2. To design and develop a web dashboard for QR-based tower registration using the location of the farmer's phone, scan requests, and inspection records that works even when the farm has no internet connection.
3. To develop an autonomous navigation and alignment method that combines GPS waypoints with onboard QR code and ArUco marker positioning to scan every face of a tower.
4. To develop a YOLOv8 computer vision model that detects lettuce heads and empty planting pots from the aerial video, shown as a live preview during flight and finalized from the full onboard recording after landing, and matches each detection to its exact pot on the tower, and to integrate it with the drone telemetry, offline cache, and web dashboard into a unified crop tracking system.
5. To evaluate the system in terms of detection and counting accuracy, alignment and scan success, and its usefulness, ease of use, and user satisfaction.

---

## slide-06.png · Significance of the Study (Valentino)

Our technical contribution: we use markers to align a drone beside a tower, not just for landing, and match every detection to its pot. The benefits reach farmers, farm managers and workers, students and researchers, the academic community, and local agricultural offices.

---

## slide-07.png · Scope and Delimitation (Valentino)

Our scope: QR registration, autonomous scanning of every face, lettuce and empty pot detection, and offline and online dashboards, tested on one 1.5-meter tower. Our limits: fair weather and daylight, an open area with GPS, below 1.8 meters, within 20 meters, and one tower per battery. We exclude plant health, other crops, obstacle avoidance and indoor flight.

---

## slide-08-0-section-method.png · Section: Part Three: The Method

(No lines.)

---

## slide-08a.png · Research Methodology · Research Design (Fernandez)

Thank you. This is developmental research with a mixed-method approach, using RAD, following Fauzi and colleagues. Phase 1, we interview farmers and choose components. Phase 2, we design the system and simulate the scan in Gazebo. Phase 3, we build the drone, tower and software, repeating with design. Phase 4, we test everything and run the user evaluation.

---

## slide-08b.png · Research Methodology · Dataset (Fernandez)

The model learns from about 2,000 labeled images, at least 1,500 each for lettuce and empty pots. This is close to the 2,240 frames Wang and colleagues used, and meets the Ultralytics guideline. We capture, sample, label in Supabox, and train YOLOv8, split 70, 20 and 10 percent, so the test images are unseen.

---

## slide-09.png · Locale and Participants (Fernandez)

Flight tests will be in Busilac, Bayombong, and interviews at Savara Lettuce Farm, the only hydroponic farm in Bayombong. Our respondents are one farmer and three IT experts, four in total, by total enumeration.

---

## slide-10.png · Research Instruments (Fernandez)

We use three instruments, plus test logs: a survey questionnaire adapted from the USE questionnaire described by Hajesmaeel-Gohari, an interview guide, an observation checklist, and the system evaluation tool. Our adviser validates the interview questionnaire. [Pilot and reliability testing: fill in.]

---

## slide-11.png · Data Gathering Procedure (Fernandez)

Five steps: secure approval, validate the instruments, collect the data, process it, and analyze it. Participation is voluntary, and we follow the Data Privacy Act.

---

## slide-12.png · Statistical Treatment of Data (Fernandez)

For the model, we use precision, recall and mAP@50. Counts and slot matches are compared with manual checks, and flight tests measure alignment and scan success. Survey ratings use the weighted mean and standard deviation, read on this five-point scale.

---

## slide-13-0-section-system.png · Section: Part Four: The System

(No lines.)

---

## slide-13a.png · Proposed System Architecture (Lopez)

Our system has five parts, and only the cloud needs internet. Three decisions: the laptop runs the AI, because the Pi is too slow, as Shalash found; only the Pi steers, because Wi-Fi lag is unsafe near the tower; and scanning works without internet.

---

## slide-13b.png · Proposed System Architecture · Scan Sequence (Lopez)

The drone flies by GPS, finds the approach marker, aligns, and climbs each face bottom to top, then lands for the final count. If Wi-Fi drops, it keeps scanning. If markers are lost or the battery is low, it returns home. A researcher always holds the remote.

---

## slide-13c.png · Proposed System Architecture · Technical Design (Lopez)

The drone weighs about 200 to 240 grams and flies 3 to 5 minutes per battery. It has four parts: power, flight control, the Pi with its camera, and the Wi-Fi link to the laptop. We test it on the bench before flying.

---

## slide-13d.png · Proposed System Architecture · Key Features (Lopez)

These are our software layers, all free and open source. On the dashboard, farmers can register towers by QR even offline, view a map, request scans, and see results per pot. On the laptop, they can watch a scan live and sync later.

---

## slide-14-0-section-plan.png · Section: Part Five: The Plan

(No lines.)

---

## slide-14.png · Project Timeline (Gantt Chart) (Lopez)

This is our proposed six-month schedule, following the RAD phases, from requirements to the final defense.

---

## slide-15.png · Expected Output (Lopez)

The farmer gets per-tower counts and slot availability, shown here as a sample. We will deliver the drone, the tower and markers, the YOLOv8 model with 2,000 labeled images, the dashboards, and our manuscript.

---

## slide-16.png · Budget Requirements (Lopez)

Our hardware budget is ₱25,637 to ₱28,467, mostly for the drone. The laptop is not included, and each extra tower needs only a printed sign.

---

## slide-17.png · Thank You / Open Forum (All)

Thank you. We welcome your questions, comments and suggestions.

---

## slide-A1.png, slide-A2.png, slide-A3.png · Backup slides

(No lines. Show only if asked.)
