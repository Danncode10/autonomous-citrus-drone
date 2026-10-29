# Defense Script

Section title slides (Part One, Part Two, and so on) have no lines. Click past them.

---

## 01 · Title (Lopez)

Good [morning / afternoon] to our panel, to our thesis adviser, Bernadeth B. Liggayu, and to everyone here.

I am Lester Dann Lopez, Rhoan Joy Marvilla, Prince Daniel Valentino, and Joshua Jing Fernandez, from BS Computer Science 4B.

Our thesis is "Computer Vision and Autonomous Drone Inspection for Hydroponic Towers with Web Dashboard Integration." Simply put, a small drone flies around a hydroponic tower, and a computer counts which pots have lettuce and which are empty.

---

## 02a · Background of the Study (Lopez)

Vertical farms grow crops in stacked towers. They save land and water, but only if they are managed well. A big part of that is knowing which pots have plants and which are empty, so the farmer knows where to replant and what to harvest.

Today, this is still checked by hand. Studies from Iloilo and Bohol show that farms still monitor and record manually. Most farm technology uses IoT sensors, but these only measure things like temperature, pH and nutrients. A sensor cannot tell if a pot is empty.

And a farm has many towers, and towers can be made taller. So checking every pot by hand takes longer as the farm grows. That is the problem our study solves.

---

## 02b · Key Concepts (Lopez)

Our solution has four parts.

First, registration. Each tower has a printed sign with a QR code. The farmer scans it with a phone, and the phone saves the tower's GPS location.

Second, navigation. The drone flies to the tower using GPS. Since GPS is only accurate to a few meters, the drone then uses ArUco markers, printed black-and-white squares on the tower, to keep the right distance and height.

Third, detection. The drone flies up each side of the tower and records video. On a laptop, an AI model called YOLOv8 finds the lettuce and the empty pots and matches each one to its exact pot.

Fourth, the dashboard. Results are saved on the laptop first, so no internet is needed at the farm. They are uploaded to a web dashboard when internet is available.

Because every tower has its own QR code, one drone can check every tower on the farm.

---

## 03a · Related Literature: Farm and Monitoring (Marvilla)

Thank you. We reviewed 38 sources. For each one, the table shows what it found and how it relates to our study.

Studies on vertical farming, like van Delden and Saad, say towers work well only with good management. Local projects, like SIGLA at UPLB, use towers with separate planting slots, the same layout we scan. Domingo and Bunga show that local farms still monitor by hand. IoT studies like Dhanaraju and Santiago measure the air and water, but none of them checks if a pot is empty.

For registration, Qian shows phones read QR codes reliably, and phone GPS is accurate to about 4.9 meters. So we use a QR sign and the phone's GPS, but GPS only gets the drone close to the tower.

---

## 03b · Related Literature: Detection and Flight (Marvilla)

For detection, Wang and colleagues used YOLOv8 to find hydroponic lettuce with about 99 percent accuracy, so we use YOLOv8 too. But their model did not detect empty pots, and their camera did not move. Ours detects both, from a moving drone.

To avoid counting the same pot twice, we use a tracker called ByteTrack. Villacrés showed that counts can still be off by about 20 percent, so we will check our counts against manual counts.

For the drone, Aslan found almost no drone studies on farms like ours, and CogniFly, a drone under 250 grams, inspired our design. Other studies used markers to guide drones, but only for landing, not for flying beside a tower.

---

## 03c · Related Literature: Processing and Data (Marvilla)

Shalash found that AI models run slowly on a small Raspberry Pi, under 3 frames per second. So in our system, the AI runs on the laptop, while the drone's Raspberry Pi only reads the markers and steers. Zhu and Chen showed that Wi-Fi can lag, which is another reason the laptop never controls the drone.

Internet in rural areas is unreliable, so, like Mayta's offline-first app, we save results locally and upload them later.

The remaining studies guided our dashboard, our safety rules under CAAP, our development method, and our user survey.

---

## 03d · Research Gap (Marvilla)

To sum up: IoT studies cannot see empty pots. Lettuce detection studies do not detect empty pots. Farm drones fly over fields, not around a single tower. And marker-based drones use markers only for landing.

No study we found combines all of these into one low-cost system. That is our research gap, and that is what this study will build.

---

## 04a · Conceptual Framework (Marvilla)

Our study follows an Input–Process–Output model.

The input is what farmers tell us in interviews, what we learned from the literature, and our hardware and software.

The process is Rapid Application Development, or RAD. We plan, then design and build in repeated cycles, then test the whole system.

The output is our system, which reports the lettuce count, the empty pot count, and the available slots for each tower. Test results go back into the next cycle, so the system keeps improving.

---

## 04b · System Flow (Marvilla)

This figure shows how the system works, step by step.

The farmer scans the tower's QR code. The laptop sends the drone to that tower. The drone finds the tower, aligns using the markers, and scans each side from bottom to top. During the flight, the laptop shows a live preview. After landing, the full video is processed for the final count.

Everything at the farm works on local Wi-Fi, without internet. Internet is needed only to upload the results to the online dashboard.

---

## 05 · Research Objectives (Valentino)

Thank you. Our general objective is to build a drone system that registers towers by QR code, flies to them, scans every side, detects lettuce and empty pots, and shows the results on a web dashboard.

Specifically, we aim to:

1. Find out how farmers monitor their towers today and what problems they face.
2. Build a web dashboard for registering towers, requesting scans and viewing results, which works even without internet.
3. Develop the drone's navigation and alignment using GPS and markers.
4. Train a YOLOv8 model to detect lettuce and empty pots and match each one to its pot.
5. Evaluate the system's accuracy and how useful and easy to use it is.

---

## 06 · Significance of the Study (Valentino)

Farmers spend less time checking pots, especially on the upper levels, and can plan replanting and harvesting better. Farm managers and workers get a clear record of every tower. Students and researchers get a reference and a labeled image dataset they can reuse. The study adds to research on smart farming and computer vision, and it can help local agriculture offices promote affordable vertical farming.

Our technical contribution is using markers to keep a drone aligned beside a tower, not just for landing, and matching every detection to its exact pot.

---

## 07 · Scope and Delimitation (Valentino)

Our scope covers QR registration, flying to the tower on its own, scanning every side, detecting lettuce and empty pots, and the offline and online dashboards. We will build and test one tower, about 1.5 meters tall, to fit our budget, but the system is designed for a whole farm.

As for our delimitations, we cover only lettuce, and only whether a pot is full or empty, not plant health or growth. The tower has no watering system. We fly only outdoors, in an open area with GPS, in daylight and good weather, no higher than 1.8 meters and within 20 meters of where the drone takes off. One battery lasts about three to five minutes, enough for one tower.

---

## 08a · Research Design (Fernandez)

Thank you. This is a developmental study that uses both qualitative data, from interviews, and quantitative data, from system tests and user ratings. We follow Rapid Application Development, or RAD, in four phases.

In phase one, requirements planning, we interview farmers, observe the site, and choose our components. In phase two, design, we plan the system and test the full drone scan in a computer simulation before any real flight. In phase three, construction, we build the drone, the tower and the software. We repeat phases two and three until everything works. In phase four, cutover, we test the whole system outdoors and let users evaluate it.

---

## 08b · Dataset (Fernandez)

To train the AI model, we will prepare about 2,000 labeled images of the tower. At least 1,500 will contain lettuce, at least 1,500 will contain empty pots, and a few will contain neither, to reduce false detections. This is close to the 2,240 images Wang and colleagues used.

We record videos from every side, distance and lighting, take about one frame per second, label every lettuce and empty pot, and train YOLOv8. We use 70 percent of the images for training, 20 for validation and 10 for testing. The test images are ones the model has never seen.

---

## 09 · Locale and Participants (Fernandez)

Flight tests will be at Purok 2, Busilac, Bayombong, an open area with a clear GPS signal. Interviews will be at Savara Lettuce Farm in Masoc, Bayombong, the only hydroponic farm in town.

Our respondents are one hydroponic farmer and three IT experts from CITE, four in total. Since the group is small, we include all of them. This is called total enumeration.

---

## 10 · Research Instruments (Fernandez)

We use four instruments:
- A survey questionnaire, adapted from the USE questionnaire, to rate how useful, easy to use and satisfying the system is, on a five-point scale.
- An interview guide, to learn how farmers monitor their towers today.
- An observation checklist, for the tower and the flying area.
- A system evaluation tool, which is the test records from the drone and the model.

Our adviser reviews and approves the instruments before we collect any data.

---

## 11 · Data Gathering Procedure (Fernandez)

We gather data in five steps:
1. We get approval from the school and the farm owner.
2. Our adviser validates the instruments.
3. We collect data: interviews with consent, site observation, tower photos for the dataset, test flights, and the survey.
4. We organize the data per tower and per flight.
5. We analyze it.

Participation is voluntary, personal data is protected under the Data Privacy Act, and photos show only the towers, not people.

---

## 12 · Statistical Treatment of Data (Fernandez)

For the AI model, we measure three things:
- Precision: how many of its detections are correct.
- Recall: how many of the actual pots it found.
- mAP: a standard overall accuracy score.

For counting, we compare the system's count with a manual count for each tower, and check whether each pot was matched correctly. For the drone, we measure how well it aligns, how often it finishes a full scan, and how long each flight takes.

For the survey, we compute the weighted mean and standard deviation and interpret the results with this scale, from Highly Acceptable down to Highly Not Acceptable.

---

## 13a · System Architecture (Lopez)

Our system has five parts: the tower with its sign, the drone, the farmer, the laptop, and the cloud. Only the cloud needs internet.

We made three key decisions:
- The AI runs on the laptop, because the drone's small computer is too slow for it.
- Only the drone steers itself, because a Wi-Fi delay from the laptop could cause a crash near the tower.
- The scan works without internet, and the farmer uploads the results when ready.

---

## 13b · Scan Sequence and Failsafes (Lopez)

Here is how one scan works. The drone flies to the tower by GPS. It turns until it sees the large marker on the tower sign. Then it uses the smaller markers to stay at the right distance and height. It flies up one side, moves to the next side, and repeats until every side is scanned. Then it lands, and the full video is processed.

For safety:
- If the Wi-Fi drops, it keeps scanning.
- If it loses the markers, it waits ten seconds, then returns home.
- If the battery runs low or the remote signal is lost, it returns home.

A team member always holds the remote control.

---

## 13c · Technical Design (Lopez)

Inside the drone, the battery powers the flight controller, and a separate power supply runs the Raspberry Pi, so it does not restart during flight. The flight controller keeps the drone stable using GPS. The Raspberry Pi records the video and sends small corrections to the flight controller. The whole drone weighs about 200 to 240 grams.

---

## 13d · Key Features (Lopez)

On the web dashboard, farmers can:
- register towers by QR code, even offline;
- see their towers on a map;
- request scans;
- view the results and history for every pot.

On the laptop, they can watch a scan live and upload the results when they have internet. All the software we use is free and open source.

---

## 14 · Project Timeline (Lopez)

We plan to finish in six months, following the RAD phases: planning first, then designing and building in cycles, then testing, user evaluation, and the final defense.

---

## 15 · Expected Output (Lopez)

The farmer gets a view of each tower showing which pots have lettuce, which are empty, and how many slots are available, without checking by hand. This is a sample screen, not actual results.

We will deliver:
- the working drone;
- the tower with its sign and markers;
- the trained AI model and the 2,000-image dataset;
- the dashboards;
- our test results and manuscript.

---

## 16 · Budget Requirements (Lopez)

Our hardware budget is about 25,600 to 28,500 pesos. Most of it goes to the drone's flight parts. This does not include the laptop, which we already have. Adding another tower costs only a printed sign and markers.

---

## 17 · Thank You (All)

Thank you. We welcome your questions and suggestions.
