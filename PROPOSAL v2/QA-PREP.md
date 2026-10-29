# Q&A Prep

Short answers for likely panel questions. These aren't part of the script.

**Why not just add more sensors?**
Sensors measure the air and the water. Only a camera can see whether a pot has a plant.

**Why not a weight sensor under each pot?**
That means one device, with its own wiring and power, for every pot on every tower, and the cost grows with each pot added. Our towers need only a printed sign, and one drone covers the whole farm. A weight sensor also gives just a number. Our scans save pictures of every pot. In this study we use them only for counting, but the same pictures can later be used for plant health or harvest readiness, and for future research (Significance of the Study; SWOT, Opportunities).

**Why a printed sign instead of an electronic device on the tower?**
A sign costs about ₱150 and needs no battery or wiring. The phone already has GPS, so adding towers stays cheap.

**Why YOLOv8 and not a newer version?**
YOLOv8 has published results on hydroponic lettuce (Wang et al., 2024), so we have a baseline to compare against.

**Why not run the AI on the drone?**
The Raspberry Pi is too slow and can overheat (Shalash et al., 2026). The laptop runs the AI, and the Pi only reads the markers.

**Why not train an AI model to find the tower after GPS, instead of using markers?**
GPS gets the drone within about 4.9 m. From there, the drone has to steer itself, and its small computer can't run AI fast enough to steer; YOLO runs under 3 frames per second even on bigger Raspberry Pis (Shalash et al., 2026). Running the AI on the laptop doesn't work either, because Wi-Fi lag makes remote steering unsafe near the tower (Zhu & Chen, 2026). An AI model would also only find *a* tower, and it can't tell identical towers apart. Our approach is different: the QR code on the tower sign says *which* tower and face A, and the ArUco markers, at known positions on each face, run fast on the drone and give its exact distance and angle (OpenCV; Kalaitzakis et al., 2021). So AI does what it's best at, counting lettuce and empty pots, and markers do what they're best at, precise positioning.

**What if the Wi-Fi drops mid-scan?**
The drone keeps scanning, because it steers itself. The final count comes from the full video saved on the drone.

**How do you know which pot a detection belongs to?**
The markers are at known positions on each side of the tower. Their position in the video tells us the side, level and spot of each pot.

**Is 2,000 images enough?**
It's close to the 2,240 images Wang et al. (2024) used for lettuce, and meets the Ultralytics guideline of at least 1,500 images per class.

**Why only four respondents?**
Savara is the only hydroponic farm in Bayombong, and three IT experts are available, so we include everyone. The main results come from the system tests, which use many images and flights.

**Why only one tower?**
One tower fits the budget. Every tower is scanned the same way, so the method applies to the whole farm.

**Why RAD?**
The drone, the AI model and the dashboard each need several build-and-test rounds. RAD is built for that, and it's fast (Fauzi et al., 2023).

**Is it safe and legal to fly?**
Yes. It falls under the open category of CAAP Part 11: under 25 kg, within sight, below 120 m, in daylight, and at least 30 m from people not involved. A team member always holds the remote control.

**What if it's windy?**
We check the wind before every flight and fly only below our limit. If the wind picks up, we cancel the scan and the drone returns home.
