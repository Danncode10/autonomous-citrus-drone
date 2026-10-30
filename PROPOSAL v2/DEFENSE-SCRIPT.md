# Defense Script

Each heading is the exact image file name in the `slides/` folder, in the same order.

Target: about 12 minutes. The slides already show the details. The script explains what the slides can't, which is the why and the how. Don't read the slide aloud.

[click] marks a build step on slides 03a to 03d. Each one reveals the next panel (see `slides/steps/`).

---

## slide-01.png · Title (Lopez)

Good [morning / afternoon] to our panel, to our adviser, Bernadeth B. Liggayu, and to everyone here. I am Lester Dann Lopez, and with me are Rhoan Joy Marvilla, Prince Daniel Valentino and Joshua Jing Fernandez. Our study is titled "Computer Vision and Autonomous Drone Inspection for Hydroponic Towers with Web Dashboard Integration."

---

## slide-02-0-section-problem.png · Section: Part One: The Problem

(No lines.)

---

## slide-02a.png · Introduction / Background of the Study (Lopez)

Vertical farms grow plants in towers to save land and water. But a tower only pays off when its pots are being used.

Today, the only way to find empty pots is to walk up and look. The upper pots are the hardest to see. Farms do use sensors, but those measure the water, not the pots. None of them can tell if a pot has a plant.

That missing number is what we call slot availability. It tells farmers where to replant and when to harvest.

---

## slide-02b.png · Introduction · Key Concepts (Lopez)

Our idea is one small drone that checks every pot on every tower.

First, the farmer scans the QR sign on the tower, and the phone saves the tower's location.

Next, the drone flies there by GPS. But phone GPS can be off by about five meters, which is too far when flying near plants. So for the last few meters, the drone uses ArUco markers. These are printed black-and-white squares. When the camera sees one, it knows exactly how far away the tower is and at what angle.

Then the drone scans each side from bottom to top, and YOLOv8 counts the lettuce and the empty pots. Finally, the results appear on the farmer's dashboard.

Rhoan will now present the related studies.

---

## slide-03a.png · Review of Related Literature · Farm and Monitoring (Marvilla)

Thank you. We reviewed thirty-eight sources in three groups. The first group is about the farm. Towers grow more plants on less land. [click] But farms in the Philippines still check them by hand. [click] Their sensors watch the water, not the pots. [click] And as Lester mentioned, phone GPS alone is too rough to fly beside a tower.

---

## slide-03b.png · Review of Related Literature · Detection and Flight (Marvilla)

The second group is about detection and flight. Wang and colleagues used YOLOv8 on lettuce with about ninety-nine percent accuracy. But nobody trained it to find empty pots.

[click] Video also shows the same plant in many frames. So we use a tracker called ByteTrack, which makes sure each plant is counted only once.

[click] Finally, markers have guided drones only when landing, never beside a tower.

---

## slide-03c.png · Review of Related Literature · Processing, Data and Method (Marvilla)

The third group follows the data from the drone to the phone. A Raspberry Pi is too slow to run AI during flight. [click] Wi-Fi adds delay and can drop. [click] Rural internet is unreliable. [click] And farm dashboards go unused when they are hard to use. These findings shaped how we split the work, which Lester will explain later.

---

## slide-03d.png · Research Gap (Marvilla)

So every piece already exists, but only separately. Some studies detect lettuce. Some fly drones on farms, and some use markers. Each one covers only part of the problem. [click] No study puts them together to check every pot on a tower. Ours does.

---

## slide-04-0-section-solution.png · Section: Part Two: The Solution

(No lines.)

---

## slide-04a.png · Conceptual Framework · Input–Process–Output (IPO) Model (Marvilla)

Our framework follows the Input, Process and Output model. The inputs are the farmers' needs, the literature and the tools we chose. The process is Rapid Application Development, which Joshua will explain later. The output is a system that reports the lettuce, the empty pots and the slot availability of every tower.

---

## slide-04b.png · Conceptual Framework · System Flow (Marvilla)

This figure shows the system on a normal day. Everything on the left happens at the farm. The drone scans the tower, and the laptop shows a live preview. After landing, the laptop processes the full recording. All of this needs only local Wi-Fi.

The right side needs internet, but it only uploads and displays the results. So a weak connection never stops a scan.

Prince will now present our objectives.

---

## slide-05a.png · Research Objectives · General Objective (Valentino)

Thank you. This study aims to design and develop an autonomous drone-based monitoring system that registers vertical hydroponic towers through a printed QR code and the location of the farmer's phone, navigates to each tower using GPS, aligns itself using computer vision and visual markers, scans every face of the tower in an open space, detects lettuce plants and empty planting pots using computer vision, and displays tower-level records on a web-based dashboard.

---

## slide-05b.png · Research Objectives · Specific Objectives (Valentino)

We have five specific objectives. The first is to learn how farmers monitor their towers today. The second is to build a dashboard that works even without internet. The third is to make the drone fly and align on its own. The fourth is to train YOLOv8 to find lettuce and empty pots and link each one to its exact pot. The last is to test how accurate and useful the system is.

---

## slide-06.png · Significance of the Study (Valentino)

Our main contribution is how we use markers. Other drones use them only to land. We use them to hold the drone beside a tower and to link each detection to its exact pot.

This mainly helps farmers, who can check the upper pots without climbing. It also gives future researchers a dataset they can reuse.

---

## slide-07.png · Scope and Delimitation (Valentino)

We will build and test the system on one tower that is one and a half meters tall.

Each flight limit has a reason. The drone stays below one point eight meters, just above the tower. It stays within twenty meters so the Wi-Fi can reach it. We fly only in daylight and calm weather because the drone is very light. And we need open sky because the drone relies on GPS. Plant health, other crops and indoor flight are not covered.

Joshua will now explain our method.

---

## slide-08-0-section-method.png · Section: Part Three: The Method

(No lines.)

---

## slide-08a.png · Research Methodology · Research Design (Fernandez)

Thank you. This is developmental research that uses both interviews and measurements. We follow Rapid Application Development because we build in short cycles and test each part early.

We start by planning with the farmers. Then we design the system and test the whole scan in a simulation first. Design and building repeat until each part works. Last, we test the full system with real users.

---

## slide-08b.png · Research Methodology · Dataset (Fernandez)

Our model learns from about two thousand labeled images of lettuce and empty pots. This is close to what Wang and colleagues used.

We take one frame per second from videos of the tower. Frames from the same video look almost the same. So each video stays in only one set. That keeps the test images truly new to the model.

---

## slide-09a.png · Locale and Participants (Fernandez)

We will fly in Busilac, an open area with good GPS. Our interviews are at Savara Lettuce Farm, the only hydroponic farm in Bayombong. Our four respondents are the Savara farmer and three IT experts from CITE. Since there is only one farm, we include everyone. This is called total enumeration.

---

## slide-09b.png · Locale and Participants · Preliminary Interview (Fernandez)

We already interviewed the owner of Savara on October 11. She checks her plants every day just by looking, and she keeps no records. Her strongest answer was that the upper levels are hard to reach. But she also said she rarely miscounts. So for her, our real value is reach and record keeping, not just counting.

Her farm uses pipe systems inside a net house, where a GPS drone can't fly safely yet. That is why we test on our own tower outdoors. The bottom of the slide shows how we answered her concerns.

---

## slide-10.png · Research Instruments (Fernandez)

We use three instruments. The first is a survey based on the USE questionnaire. We replaced its neutral option with "moderately agree," so every answer leans one way. The second is the interview guide, and the third is a site checklist. The system also logs every flight.

Our adviser reviewed and approved the interview guide. [Pilot and reliability testing: fill in.]

---

## slide-11.png · Data Gathering Procedure (Fernandez)

First, we get approval from the school and the farm. Then our adviser checks our instruments. After that, we collect the data, organize it and analyze it.

Joining is voluntary, and we follow the Data Privacy Act. We photograph only the towers, never the people.

---

## slide-12.png · Statistical Treatment of Data (Fernandez)

Precision asks how many of the model's detections were correct. Recall asks how many of the real plants and empty pots it found. mAP at fifty combines both into one score. We also compare the system's count with a count done by hand. For the survey, a weighted mean of four point two one and above means highly acceptable.

Lester will now show the system.

---

## slide-13-0-section-system.png · Section: Part Four: The System

(No lines.)

---

## slide-13a.png · Proposed System Architecture (Lopez)

Thank you. This figure shows the five parts of our system. Each computer does what it does best. The Pi on the drone steers because it can react instantly. The laptop runs the AI because it is much faster. The laptop never steers, since a Wi-Fi delay near the tower could cause a crash.

---

## slide-13b.png · Proposed System Architecture · Scan Sequence (Lopez)

This is how one scan works, and it is the heart of our study.

First, the drone flies by GPS to a point near the tower. It turns slowly until it finds the large marker on the sign. Now it knows exactly where the tower is.

Next, it climbs the first side from bottom to top. Each side has small markers at known heights, and every marker has its own ID. So when the camera sees a marker, the system knows which side and which level it is on. That is how each detection becomes a specific pot, like side A, level two. Then the drone moves to the next side.

You may ask why there is both a live preview and a final count. The Wi-Fi video is smaller and can drop frames, so it is only a preview. The drone also saves a full-quality recording. After landing, that recording gives the final count.

If the Wi-Fi drops, the drone keeps scanning. If it loses the markers or runs low on battery, it flies back to launch. A researcher always holds the remote as a backup.

---

## slide-13c.png · Proposed System Architecture · Technical Design (Lopez)

The drone weighs about two hundred to two hundred forty grams. Together with our height and daylight limits, this keeps us in the open category of the CAAP rules. The Pi has its own power line, so motor surges can't make it restart. Before flying, we weigh the drone, test the motors and calibrate the camera.

---

## slide-13d.png · Proposed System Architecture · Key Features (Lopez)

All our tools are free and open source, which keeps costs low for small farms. The farmer uses the web dashboard on a phone to register towers and see each pot. The local dashboard on the laptop shows the scan live and uploads the results later.

---

## slide-14-0-section-plan.png · Section: Part Five: The Plan

(No lines.)

---

## slide-14.png · Project Timeline (Gantt Chart) (Lopez)

This is our six-month plan, colored by RAD phase. It starts with the interviews after this defense on November 3. It ends with testing and the final defense.

---

## slide-15.png · Expected Output (Lopez)

This is a sample screen with example numbers only. This tower has twelve lettuce and four empty pots. So the farmer knows where to replant without walking over. Our deliverables are listed on the right.

---

## slide-16.png · Budget Requirements (Lopez)

Our hardware budget is about twenty-five thousand six hundred to twenty-eight thousand five hundred pesos, mostly for the drone. The software is free. Each extra tower only needs a printed sign and markers. [Printing, internet, transportation and miscellaneous: fill in.]

---

## slide-17.png · Thank You / Open Forum (All)

That is our proposal. One small drone checks every pot on every tower, so farmers know where to replant without climbing. Thank you, and we welcome your questions and suggestions.

---

## slide-A1.png, slide-A2.png, slide-A3.png · Backup slides

(No lines. Show only if the panel asks.)
