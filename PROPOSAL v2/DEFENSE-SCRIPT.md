# Defense Script

Each heading is the exact image file name in the `slides/` folder, in the same order.

Target: about 12 minutes. The slides already show the details. The script explains what the slides can't, which is the why and the how. Don't read the slide aloud.

---

## slide-01.png · Title (Dann)

Good morning to our panel, to our adviser, Bernadeth B. Liggayu, and to everyone here. I am Lester Dann Lopez, and with me are Rhoan Joy Marvilla, Prince Daniel Valentino and Joshua Jing Fernandez. Our study is titled "Computer Vision and Autonomous Drone Inspection for Hydroponic Towers with Web Dashboard Integration."

---

## slide-02-0-section-problem.png · Section: Part One: The Problem

(No lines.)

---

## slide-02a.png · Introduction / Background of the Study (Dann)

Vertical farms grow plants in towers to save land and water. But a tower only pays off when its pots are being used.

Today, the only way to find empty pots is to walk up and look. The upper pots are the hardest to see. Farms do use sensors, but those measure the water, not the pots. None of them can tell if a pot has a plant.

That missing number is what we call slot availability. It tells farmers where to replant and when to harvest.

---

## slide-02b.png · Introduction · Key Concepts (Dann)

Our idea is one small drone that checks every pot on every tower.

First, the farmer scans the QR sign on the tower, and the phone saves the tower's location.

Next, the drone flies there by GPS. But phone GPS can be off by about five meters, which is too far when flying near plants. So for the last few meters, the drone uses ArUco markers. These are printed black-and-white squares. When the camera sees one, it knows exactly how far away the tower is and at what angle.

Then the drone scans each side from bottom to top, and YOLOv8 counts the lettuce and the empty pots. Finally, the dashboard shows the counts and the photos of each pot. So the farmer can see the crops without walking to the tower.

RJ will now present the related studies.

---

## slide-03a.png · Review of Related Literature · Farm and Monitoring (RJ)

Thank you. We reviewed thirty-eight sources in three groups. The first group is about the farm. Towers grow more plants on less land. But farms in the Philippines still check them by hand. Their sensors watch the water, not the pots. And as Dann mentioned, phone GPS alone is too rough to fly beside a tower.

---

## slide-03b.png · Review of Related Literature · Detection and Flight (RJ)

The second group is about detection and flight. Wang and colleagues used YOLOv8 on lettuce with about ninety-nine percent accuracy. But nobody trained it to find empty pots.

Video also shows the same plant in many frames. So we use a tracker called ByteTrack, which makes sure each plant is counted only once.

Finally, markers have guided drones only when landing, never beside a tower.

---

## slide-03c.png · Review of Related Literature · Processing, Data and Method (RJ)

The third group follows the data from the drone to the phone. A Raspberry Pi is too slow to run AI during flight. Wi-Fi adds delay and can drop. Rural internet is unreliable. And farm dashboards go unused when they are hard to use. These findings shaped how we split the work, which we will explain later.

---

## slide-03d.png · Research Gap (RJ)

So every piece already exists, but only separately. Some studies detect lettuce. Some fly drones on farms, and some use markers. Each one covers only part of the problem. Our study puts these pieces together in one system that checks every pot on a tower.

---

## slide-04-0-section-solution.png · Section: Part Two: The Solution

(No lines.)

---

## slide-04a.png · Conceptual Framework · Input–Process–Output (IPO) Model (RJ)

Our framework follows the Input, Process and Output model. The inputs are the farmers' needs, the literature and the tools we chose. The process is Rapid Application Development, which Prince will explain later. The output is a system that reports the lettuce, the empty pots and the slot availability of every tower.

---

## slide-04b.png · Conceptual Framework · System Flow (RJ)

This figure shows the system on a normal day. Everything on the left happens at the farm. The drone scans the tower, and the laptop shows a live preview. After landing, the laptop processes the full recording. All of this needs only local Wi-Fi.

The right side needs internet, but it only uploads and displays the results. So a weak connection never stops a scan.

Prince will now present our objectives.

---

## slide-05a.png · Research Objectives · General Objective (Prince)

Thank you. This study aims to design and develop an autonomous drone-based monitoring system that registers vertical hydroponic towers through a printed QR code and the location of the farmer's phone, navigates to each tower using GPS, aligns itself using computer vision and visual markers, scans every face of the tower in an open space, detects lettuce plants and empty planting pots using computer vision, and displays tower-level records on a web-based dashboard.

---

## slide-05b.png · Research Objectives · Specific Objectives (Prince)

We have five specific objectives. The first is to learn how farmers monitor their towers today. The second is to build a dashboard that works even without internet. The third is to make the drone fly and align on its own. The fourth is to train YOLOv8 to find lettuce and empty pots and link each one to its exact pot. The last is to test how accurate and useful the system is.

---

## slide-06.png · Significance of the Study (Prince)

Our main contribution is how we use markers. Other drones use them only to land. We use them to hold the drone beside a tower and to link each detection to its exact pot.

This mainly helps farmers, who can check the upper pots without climbing. It also gives future researchers a dataset they can reuse.

---

## slide-07.png · Scope and Delimitation (Prince)

Our scope is what this study covers. It covers the whole system, from scanning the QR sign to seeing the results on the dashboard. The drone checks every face of the tower, from the bottom level to the top. The AI looks for two things only, lettuce and empty pots, and it links each one to its exact pot. We will build and test the system on one tower that is one and a half meters tall.

Our delimitations are what we leave out and the limits we fly within. Each flight limit has a reason. The drone stays below one point eight meters, just above the tower. It stays within twenty meters so the Wi-Fi can reach it. We fly only in daylight and calm weather because the drone is very light. And we need open sky because the drone relies on GPS. Plant health, other crops and indoor flight are not covered.

---

## slide-08-0-section-method.png · Section: Part Three: The Method

(No lines.)

---

## slide-08a.png · Research Methodology · Research Design (Prince)

This is developmental research that uses both interviews and measurements. We follow Rapid Application Development because we build in short cycles and test each part early.

We start by planning with the farmers. Then we design the system and test the whole scan in a simulation first. Design and building repeat until each part works. Last, we test the full system with real users.

---

## slide-08b.png · Research Methodology · Dataset (Prince)

Our model learns from about two thousand labeled images. This is close to the number Wang and colleagues used. The makers of YOLO also suggest at least one thousand five hundred images for each class. So we aim for that many lettuce images and that many empty pot images. A few images show neither. These teach the model not to see a plant where there is none.

The first step is to record videos of every side of the tower. We record from the drone and by hand in different light. Next we take one frame per second. This skips frames that look almost the same. Then we draw a box around each lettuce and each empty pot. Finally we train YOLOv8 and test it on images it has never seen.

Seventy percent of the images are for training. Twenty percent are for validation and ten percent are for the final test. Frames from the same video look alike. So each video stays in only one set. That keeps the test images truly new to the model.

Joshua will now present our locale and participants.

---

## slide-09a.png · Locale and Participants (Joshua)

Thank you. We will fly in Purok 2, Busilac, an open area with good GPS. Our interviews are at Savara Lettuce Farm in Masoc, the only hydroponic farm in Bayombong. Our four respondents are the Savara farmer and three IT experts from CITE. Since there is only one farm, we include everyone. This is called total enumeration.

---

## slide-09b.png · Locale and Participants · Preliminary Interview (Joshua)

We already interviewed the owner of Savara on October 11. She checks her plants every day just by looking, and she keeps no records. Her strongest answer was that the upper levels are hard to reach. But she also said she rarely miscounts. So for her, our real value is reach and record keeping, not just counting.

Her farm uses horizontal pipes inside a net house. But she is willing to add vertical towers alongside them.

---

## slide-10.png · Research Instruments (Joshua)

We use three instruments and the system's own test logs. The first is a survey. Farmers and IT experts answer it after using the system. It measures how useful and easy the system is and how satisfied they are. The second is the interview guide. It shows how farmers monitor their towers today. The third is an observation checklist. We use it on site to check the tower and the flying area. Finally the test logs record how accurate each flight and each count is.

Our adviser reviewed and approved the interview guide. [Pilot and reliability testing: fill in.]

---

## slide-11.png · Data Gathering Procedure (Joshua)

First, we get approval from the school and the farm. Then our adviser checks our instruments. After that, we collect the data, organize it and analyze it.

Joining is voluntary, and we follow the Data Privacy Act. We photograph only the towers, never the people.

Dann will now explain how we measure the results.

---

## slide-12.png · Statistical Treatment of Data (Dann)

Thank you. To evaluate the AI we use precision, recall and mAP at fifty. In our system precision shows how often the AI is right when it marks a lettuce or an empty pot. Recall shows how many of the real lettuce and empty pots it finds. mAP at fifty combines both into one score for the two classes.

We target at least ninety percent for each. Wang and colleagues reached about ninety-nine percent with a still camera. We set ours a little lower because our camera is on a moving drone. We also compare the system's count with a hand count of each tower. We target a counting error of ten percent or less. For the survey a weighted mean of 4.21 and above means highly acceptable.

Prince will now show our system.

---

## slide-13-0-section-system.png · Section: Part Four: The System

(No lines.)

---

## slide-13a.png · Proposed System Architecture (Prince)

Thank you. This figure shows the five parts of our system. The first is the tower with its sign and markers. The second is the drone. It flies the scan and records the video. The third is the farmer who starts the scan from the dashboard. The fourth is the ground station. This is a laptop that runs the AI and keeps the results offline. The last is the cloud. It holds the database and the web dashboard.

Each computer does what it does best. The Pi on the drone steers because it can react instantly. The laptop runs the AI because it is much faster. The laptop never steers. A Wi-Fi delay near the tower could cause a crash. Only the cloud needs internet. So the farmer can scan with no signal and upload the results later.

Dann will now explain how one scan works.

---

## slide-13b.png · Proposed System Architecture · Scan Sequence (Dann)

Thank you. This is how one scan works, and it is the heart of our study.

First, the drone flies by GPS to a point near the tower. It turns slowly until it finds the large marker on the sign. Now it knows exactly where the tower is.

Next, it climbs the first side from bottom to top. Each side has small markers at known heights, and every marker has its own ID. So when the camera sees a marker, the system knows which side and which level it is on. That is how each detection becomes a specific pot, like side A, level two. Then the drone moves to the next side.

You may ask why there is both a live preview and a final count. The Wi-Fi video is smaller and can drop frames, so it is only a preview. The drone also saves a full-quality recording. After landing, that recording gives the final count.

If the Wi-Fi drops, the drone keeps scanning. If it loses the markers or runs low on battery, it flies back to launch. A researcher always holds the remote as a backup.

---

## slide-13c.png · Proposed System Architecture · Technical Design (Dann)

This is what is inside the drone. A three-cell LiPo battery powers the motors and the flight controller. The Pi has its own five-volt line so motor surges can't make it restart. The flight controller is a SpeedyBee F405 running ArduPilot. It keeps the drone stable using the GPS and compass. The Pi Zero 2 W reads the QR code and the markers. It sends steering corrections to the flight controller through MAVLink. Its camera saves a full recording to the memory card. It also streams a live preview to the laptop over Wi-Fi.

The drone weighs about two hundred to two hundred forty grams. With our height and daylight limits this keeps us in the open category of the CAAP rules. One battery lasts three to five minutes which is enough for one tower. Before flying we weigh the drone and test the motors. We also tune the flight controller and calibrate the camera.

RJ will now present our software.

---

## slide-13d.png · Proposed System Architecture · Key Features (RJ)

Thank you. This slide shows our software from the drone up to the farmer. ArduPilot flies the drone. The Pi uses OpenCV to read the markers and GStreamer to send the video. The laptop runs YOLOv8 and ByteTrack and saves the results in SQLite. When there is internet the results go to Supabase. The farmer sees them on a Next.js dashboard. Before flying we label images in Supabox and test the scan in a Gazebo simulation.

The web dashboard works on a phone. The farmer registers towers by QR even offline. They can request scans and see each pot on every tower. The dashboard also keeps the photos from every scan. So the farmer sees the actual plants and not just the counts. We do not analyze these photos yet. But future researchers can use them to study plant health. The local dashboard on the laptop shows the scan live. It uploads the results later without duplicates. All our tools are free and open source. This keeps costs low for small farms.

Dann will now present our plan.

---

## slide-14-0-section-plan.png · Section: Part Five: The Plan

(No lines.)

---

## slide-14.png · Project Timeline (Gantt Chart) (Dann)

Thank you. This is our plan from October to March. We already started. We interviewed Savara Lettuce Farm on October 11 and found the problem. Today is our proposal defense.

We build the computer vision first and the drone last. There are three reasons. First the AI and the markers are the core of our study. If they work by hand they will work on the drone. Second a drone is expensive and easy to crash. We should not fly it before the camera and the AI are ready. Third our budget comes in two parts. We have ten thousand pesos this semester and twenty thousand next semester.

So after this defense we buy the Raspberry Pi and its camera. These are the same parts that go on the drone later. The first step is to stream the camera to the laptop and send the results to the dashboard. Next we test the QR code. The phone saves the tower's GPS location to the dashboard. Then we build the tower frame and add the markers and lettuce. We carry the camera up the tower by hand to check that each marker leads to the right pot. After that we capture and label two thousand images in Supabox and train YOLOv8. We also practice the flight in a simulation.

Next semester we buy the drone parts and build it with ArduPilot. Then we teach it to fly to the tower and scan each side from bottom to top and fly back. In March we test the full system and let farmers and IT experts evaluate it. We finalize the paper and finish by March 30.

Joshua will now present our expected output.

---

## slide-15.png · Expected Output (Joshua)

Thank you. This is a sample screen with example numbers only. This tower has twelve lettuce and four empty pots. The farmer sees exactly which pots are empty. So they know where to replant without walking over. By March 30 we will hand over the items on the right. These are the drone and the tower with its markers. They also include the trained model and its images. Last are both dashboards and the final paper with our results.

---

## slide-16.png · Budget Requirements (Joshua)

Our hardware budget is about twenty-five thousand six hundred to twenty-eight thousand five hundred pesos. We split it across two semesters like our timeline. This semester we only buy the Pi with its camera and the tower parts. That fits our ten thousand pesos. Next semester our twenty thousand goes to the drone parts. The software is free. Each extra tower only needs a printed sign and markers. [Printing, internet, transportation and miscellaneous: fill in.]

Dann will now close our presentation.

---

## slide-17.png · Thank You / Open Forum (Dann, then all for questions)

That is our proposal. We start with the computer vision this semester and finish the drone by March. One small drone checks every pot on every tower. So farmers know where to replant without climbing. Thank you. We welcome your questions and suggestions.

---

## slide-A1.png, slide-A2.png, slide-A3.png · Backup slides

(No lines. Show only if the panel asks.)
