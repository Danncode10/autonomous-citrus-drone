# Automated Hydroponic Tower Health Check

## Project Summary

This project is a drone-based computer vision system for monitoring the health of lettuce plants grown in vertical hydroponic towers. The system is designed for farms with many hydroponic towers, where manually checking each plant slot is time-consuming and prone to missed issues.

The main idea is to use a drone with a camera to inspect each tower, capture images of individual lettuce plants, analyze plant condition using an AI/computer vision model, and save the results to a web dashboard where farmers can view the status of each tower and plant.

The physical prototype will focus on **one real hydroponic tower** with lettuce plants. To represent the larger farm scenario, the project will also include a **Gazebo simulation environment** with multiple virtual towers and obstacles. This allows the navigation and inspection workflow to be tested at farm scale before applying it to the real-world prototype.

## Working Thesis Title

**Drone-Based Computer Vision and Simulation System for Plant-Level Health Monitoring of Hydroponic Lettuce Towers**

## Problem Statement

Hydroponic tower farms can contain many towers, and each tower can contain multiple plant holes or slots. Farmers need to regularly check whether plants are healthy, missing, diseased, nutrient-deficient, or ready to harvest.

Manual inspection becomes difficult as the number of towers increases. It also depends heavily on human observation, which can lead to inconsistent monitoring. A drone-based inspection system can help automate this process and provide farmers with organized, plant-level health records.

## Main Objective

To design and develop an automated system that uses a drone-mounted camera and computer vision to inspect lettuce plants in hydroponic towers and report plant-level health status through a web-based dashboard.

## Specific Objectives

1. Build a hydroponic tower monitoring model where each tower has an ID, location, and multiple plant slots.
2. Use a drone-mounted camera to capture images or video of lettuce plants in each tower.
3. Train or fine-tune a computer vision model to classify lettuce plant status.
4. Store inspection results in a database with tower, slot, image, timestamp, and health status.
5. Create a web dashboard where farmers can view tower status, individual plant status, and alerts.
6. Add basic drone navigation and obstacle avoidance for safe movement around towers.
7. Develop a Gazebo simulation environment to test multi-tower navigation before real-world drone testing.

## Target Crop

The initial target crop is **lettuce**.

Lettuce is selected because:

- It is commonly grown in hydroponic systems.
- It grows relatively fast.
- Its health symptoms are often visible through leaf color, size, shape, and wilting.
- It is suitable for tower-based vertical farming.
- It makes the prototype easier to test within a thesis timeline.

## System Concept

The farm concept contains multiple hydroponic towers. Each tower has a known location and multiple plant holes or slots. The drone visits each tower, captures plant images, and sends the data to the system.

For the physical prototype, only one tower will be built. The multi-tower farm environment will be represented in Gazebo, where the drone can be tested in a virtual layout with several towers and obstacles.

The system then analyzes each plant image and produces a health status. Farmers can check the results through a website.

```text
Hydroponic Tower Farm or Gazebo Farm Simulation
        |
        v
Drone with Camera
        |
        v
Image Capture per Tower/Plant Slot
        |
        v
Computer Vision Model
        |
        v
Database
        |
        v
Web Dashboard for Farmers
```

## Major System Components

### 1. Hydroponic Tower Model

Each tower should be represented digitally in the system.

Example data:

- Tower ID
- Tower name or label
- Tower location
- Number of plant slots
- Slot position
- Plant assigned to each slot
- Latest inspection status

Example:

```text
Tower A
- Location: Row 1, Column 3
- Slots: 24
- Slot A01: healthy
- Slot A02: ready to harvest
- Slot A03: yellowing
- Slot A04: missing plant
```

### 2. Drone Inspection Module

The drone is responsible for moving near each tower and capturing images of the plants.

Possible drone tasks:

- Navigate to a tower
- Maintain safe distance from the tower
- Capture images of plant slots
- Avoid obstacles such as nearby towers, pipes, frames, or walls
- Send captured images to the processing system

For the prototype, the drone navigation can start with a controlled path instead of full autonomous navigation. The drone should move slowly, stop at each inspection point, capture a clear image, then continue to the next plant slot.

Possible navigation methods:

- Fixed waypoints
- QR codes or ArUco markers on towers
- Manual-assisted flight with automatic image capture
- Distance sensors for collision prevention
- Depth camera or LiDAR for obstacle detection
- ROS 2 with PX4 or ArduPilot for advanced autonomous navigation

### 3. Drone Platform Direction

The preferred physical drone direction is a **CogniFly-based custom drone**.

CogniFly is a useful reference because it is an open-source indoor drone concept with printable parts, a protected/collision-resilient frame, camera support, optical flow, Time-of-Flight sensing, and Python control. This matches the project goal of flying indoors near hydroponic towers and capturing plant images.

Reference repositories:

- CogniFly project page: <https://thecognifly.github.io/>
- CogniFly STL files: <https://github.com/thecognifly/CogniFly-STL>
- CogniFly Python control: <https://github.com/thecognifly/cognifly-python>

The project may adapt CogniFly instead of designing a drone completely from zero. Custom 3D-printed modifications may include:

- Camera mount for tower-facing plant inspection
- Distance sensor mount
- Battery holder
- Protective frame improvements
- Landing gear or tower-inspection positioning guides
- Mounting points for QR/ArUco marker detection hardware

Important note: the drone should be designed for **slow, stable, close-range inspection**, not speed, racing, or cinematic video.

### 4. Gazebo Simulation Module

Gazebo will be used to simulate the drone and farm environment before real-world testing.

The simulation is important because the physical prototype will only include one real hydroponic tower. The simulation can show how the system would behave in a larger farm with multiple towers, obstacles, and inspection targets.

Possible simulation tasks:

- Create a virtual hydroponic farm with multiple towers
- Add obstacles such as nearby towers, walls, pipes, and frames
- Add QR codes or ArUco markers to towers
- Simulate a drone approaching a target tower
- Use marker detection to identify tower ID and orientation
- Test inspection paths around a tower
- Test move-stop-capture movement between plant slots
- Test obstacle avoidance behavior before real-world flight

The planned drone behavior is:

1. Take off from a start position.
2. Navigate toward the target tower.
3. Detect the tower marker using the camera.
4. Identify tower ID and orientation.
5. Align with the tower start position.
6. Move to a plant slot inspection point.
7. Hold position and capture an image.
8. Continue to the next plant slot.
9. Upload or save results for dashboard viewing.

### 5. Computer Vision Module

The computer vision module analyzes lettuce plant images and predicts plant status.

Possible AI tasks:

- Detect whether a plant exists in a slot
- Classify plant health
- Detect yellowing leaves
- Detect wilting
- Estimate plant size
- Estimate harvest readiness
- Flag abnormal plants for human review

Recommended first classification categories:

- Healthy
- Yellowing / possible nutrient deficiency
- Wilted
- Undersized
- Missing plant
- Ready to harvest
- Possible disease / abnormal

Important note: the system should avoid claiming that it can perfectly diagnose exact fertilizer needs from images alone. A safer and more realistic claim is that the system detects visible symptoms that may indicate nutrient deficiency or poor growth.

### 6. Optional Sensor Module

To improve accuracy, the system can also collect sensor data from the hydroponic setup.

Possible sensors:

- pH sensor
- EC/TDS sensor
- Water temperature sensor
- Water level sensor
- Air temperature and humidity sensor
- Light intensity sensor

Sensor data can help explain plant symptoms. For example, yellowing leaves plus abnormal EC readings may suggest a nutrient issue.

### 7. Database Module

The database stores information about towers, plants, inspections, images, and AI results.

Possible tables:

- Users
- Farms
- Towers
- Plant slots
- Plants
- Drone inspections
- Plant images
- Health predictions
- Sensor readings
- Alerts

Example inspection record:

```text
Inspection ID: INS-001
Tower ID: TOWER-01
Slot ID: SLOT-08
Image: slot_08_2026_08_04.jpg
Prediction: Yellowing / possible nutrient deficiency
Confidence: 87%
Timestamp: 2026-08-04 12:54 PM
```

### 8. Web Dashboard

The web dashboard allows farmers to monitor the farm without manually checking every tower.

Expected dashboard features:

- Farm overview
- Tower list
- Tower map or layout
- Individual tower view
- Plant slot status view
- Latest captured plant images
- Health classification result
- Alerts and recommendations
- Harvest-ready list
- Inspection history

Possible tower-level statuses:

- All healthy
- Needs attention
- Has missing plants
- Has harvest-ready plants
- Requires nutrient check

Possible plant-level statuses:

- Healthy
- Needs observation
- Possible nutrient deficiency
- Possible disease
- Ready to harvest
- Missing or dead plant

## Open-Source Datasets and Libraries

The project can use open datasets and pre-trained models to reduce the amount of training required.

### Possible Datasets

- **PlantVillage Dataset**
  - Large open dataset for plant disease recognition.
  - Useful for transfer learning.
  - Limitation: mostly individual leaf images, not hydroponic tower images.

- **New Plant Diseases Dataset**
  - Large dataset based on healthy and diseased crop leaf images.
  - Useful for initial model experiments.
  - Limitation: may not match the real farm camera angle.

- **Lettuce disease datasets from Roboflow or GitHub**
  - More crop-specific.
  - Useful because the target crop is lettuce.
  - Limitation: often smaller and may need additional custom images.

### Possible AI Libraries and Models

- YOLOv8 or YOLOv11 for object detection
- Detectron2 for detection and segmentation
- TensorFlow or Keras for classification
- PyTorch for model training
- OpenCV for image processing
- MobileNet, EfficientNet, ResNet, or Vision Transformer models for transfer learning

## Recommended AI Strategy

The recommended approach is **transfer learning**.

Instead of training a model from zero, the system should start with a pre-trained computer vision model and fine-tune it using lettuce images from the actual hydroponic tower setup.

Suggested steps:

1. Collect initial lettuce images from open datasets.
2. Train a baseline classifier.
3. Capture real images from the hydroponic tower prototype.
4. Label the real images by plant status.
5. Fine-tune the model using the real images.
6. Compare model performance before and after fine-tuning.

This makes the thesis stronger because it can show that real farm images improve accuracy compared with using generic plant datasets only.

## Drone Navigation Scope

Drone navigation should be included, but it should be scoped carefully because full autonomous navigation can become a separate thesis. This project will use simulation to explore the larger autonomous navigation problem while keeping the physical build manageable.

Recommended prototype scope:

- The drone follows a controlled route around the hydroponic tower.
- The tower has visual markers such as QR codes or ArUco markers.
- The drone uses a camera and distance sensor to maintain safe positioning.
- The system includes basic obstacle avoidance to prevent collision with nearby towers.
- Gazebo is used to simulate multiple towers and obstacle layouts.
- Real-world testing focuses on one physical tower.

Possible obstacle avoidance technologies:

- Ultrasonic sensor
- Infrared distance sensor
- Depth camera
- LiDAR
- Optical flow camera
- ROS 2 navigation
- PX4 or ArduPilot autopilot

## Minimum Viable Prototype

The first complete version should focus on proving the main concept.

MVP features:

1. One hydroponic tower with lettuce plants.
2. A CogniFly-based or similar 3D-printable drone prototype.
3. Camera or drone-mounted camera that captures plant images.
4. Plant slot identification using tower layout or markers.
5. Computer vision model that classifies plant status.
6. Database for storing inspection results.
7. Web dashboard for viewing tower and plant status.
8. Basic obstacle avoidance or controlled navigation demonstration.
9. Gazebo simulation with multiple towers and obstacles.

## Possible Advanced Features

These can be added if time allows:

- Multiple tower support
- Farm map view
- More realistic Gazebo farm simulation
- ROS 2 integration
- Automated drone route planning
- Full autonomous navigation
- Sensor fusion with pH, EC/TDS, and water level readings
- Growth tracking over time
- Yield prediction
- Harvest scheduling
- Mobile app support
- Farmer notification system
- Disease localization using bounding boxes or segmentation

## Research Questions

Main research question:

**Can a drone-mounted camera and computer vision model accurately identify the health and harvest status of lettuce plants in a vertical hydroponic tower farm, while using simulation to validate navigation in a larger multi-tower environment?**

Supporting research questions:

1. How accurately can the model classify lettuce plant health from tower-captured images?
2. Does fine-tuning with real hydroponic tower images improve model accuracy?
3. Can the system correctly associate captured images with tower IDs and plant slots?
4. Can a web dashboard help farmers identify towers and plants that need attention?
5. Can basic drone navigation safely support plant inspection in a tower farm environment?
6. Can Gazebo simulation help validate multi-tower navigation and obstacle avoidance before real-world testing?

## Expected Outputs

The final project should produce:

- A working hydroponic tower inspection prototype
- A CogniFly-based or similar 3D-printable drone prototype
- A Gazebo simulation environment with multiple hydroponic towers
- A trained or fine-tuned lettuce health classification model
- A drone/camera image capture workflow
- A database of tower inspections
- A web dashboard for farmers
- Test results showing model accuracy and system performance
- Thesis documentation explaining design, implementation, testing, and limitations

## Evaluation Metrics

Possible metrics for evaluating the project:

- Classification accuracy
- Precision, recall, and F1-score per plant status category
- Image capture success rate
- Correct tower/slot identification rate
- Average inspection time per tower
- Obstacle detection success rate
- Simulation navigation success rate
- Simulated collision rate
- Dashboard usability feedback
- System response time from image capture to dashboard update

## Risks and Limitations

### Computer Vision Limitations

- Lighting changes may affect image quality.
- Leaves can overlap, making individual plant detection harder.
- Plant symptoms can look similar across different causes.
- Open datasets may not match real hydroponic tower images.
- More custom images may be needed for good accuracy.

### Drone Limitations

- Indoor drone flight can be difficult due to limited GPS.
- Airflow from the drone may disturb plants.
- Towers may be too close together for safe navigation.
- Obstacle avoidance may require additional sensors.
- Battery life limits inspection time.
- A fully 3D-printed or mostly 3D-printed drone may have vibration, weight, and durability issues.

### Simulation Limitations

- Gazebo simulation may not perfectly match real-world flight behavior.
- Simulated lighting, camera images, and plant appearances may be simpler than real farm conditions.
- Navigation that works in simulation may still need tuning during real-world testing.

### Scope Limitations

- Exact disease diagnosis may be difficult.
- Exact fertilizer recommendation may require sensor data.
- Full autonomous navigation may be too large for the initial thesis scope.

## Recommended Project Scope

The best thesis scope is:

**A drone-assisted computer vision system that detects visible lettuce plant health conditions in hydroponic towers and displays plant-level inspection results on a web dashboard.**

This scope is realistic, research-worthy, and buildable. The system can include basic navigation and obstacle avoidance, but the main contribution should be plant-level health monitoring and farm dashboard reporting. The physical system will validate inspection on one real tower, while Gazebo simulation will validate the navigation concept for multiple towers.

## Suggested Technology Stack

### Hardware

- Hydroponic tower prototype
- Lettuce plants
- CogniFly-based or similar 3D-printable drone prototype
- RGB camera
- Optional depth camera or distance sensor
- Optional pH and EC/TDS sensors

### AI and Computer Vision

- Python
- OpenCV
- PyTorch or TensorFlow
- YOLO for detection
- MobileNet, EfficientNet, or ResNet for classification

### Drone and Robotics

- CogniFly reference design
- 3D-printed drone frame
- Gazebo simulation
- ROS 2 for future simulation and robotics integration
- PX4 or ArduPilot for future advanced navigation, if needed
- MAVLink
- ArUco markers or QR codes
- Depth sensor or distance sensor for obstacle avoidance

### Web System

- Frontend: React, Vue, or plain HTML/CSS/JavaScript
- Backend: Node.js, Python Flask, FastAPI, or Django
- Database: PostgreSQL, MySQL, SQLite, or Supabase
- Image storage: local storage, cloud storage, or object storage

## Proposed Development Phases

### Phase 1: Research and Planning

- Study hydroponic lettuce growth symptoms.
- Review open plant disease datasets.
- Review drone navigation options.
- Review CogniFly hardware and software structure.
- Review Gazebo drone simulation requirements.
- Finalize system architecture.

### Phase 2: Prototype Tower and Data Collection

- Build or prepare a small hydroponic tower.
- Grow lettuce plants.
- Capture sample images under different lighting and growth conditions.
- Label images by plant status.

### Phase 3: Computer Vision Model

- Train a baseline model using open datasets.
- Fine-tune the model using real hydroponic tower images.
- Test accuracy and improve the dataset.

### Phase 4: Drone or Camera Inspection

- Build or adapt a CogniFly-based 3D-printable drone.
- Mount the camera on the drone.
- Define tower inspection positions.
- Capture plant slot images.
- Add basic obstacle detection.

### Phase 5: Gazebo Simulation

- Create a virtual hydroponic tower model.
- Create a multi-tower farm layout.
- Add obstacles and tower markers.
- Simulate drone navigation to a target tower.
- Simulate move-stop-capture inspection behavior.
- Compare simulation behavior with real-world prototype testing.

### Phase 6: Web Dashboard

- Create database schema.
- Build API for storing inspection results.
- Build dashboard views for farm, tower, and plant slot status.

### Phase 7: Integration and Testing

- Connect camera capture, AI model, database, and dashboard.
- Test end-to-end inspection workflow.
- Test simulated multi-tower navigation.
- Measure performance and accuracy.
- Document limitations and future improvements.

## Short Pitch

This project automates the inspection of hydroponic lettuce towers using a 3D-printable drone, camera, computer vision, and web dashboard. The physical prototype uses one real lettuce tower, while Gazebo simulation represents a larger farm with multiple towers and obstacles. The drone identifies a tower using visual markers, captures images of individual plant slots, and sends AI-generated plant health results to a dashboard so farmers can quickly identify healthy plants, problem areas, and harvest-ready lettuce.
