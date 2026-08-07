# Project Plan

## Project Direction

The project focuses on **visible fruit counting for Perante orange trees** using a drone-mounted camera, computer vision, orchard mapping, Gazebo simulation, and a web dashboard. 

The project is restructured into two main phases to accommodate both software foundations and hardware integration: **Thesis 1 (Foundations & Simulation)** and **Thesis 2 (Integration & Deployment)**.

---

## Thesis 1 (Foundations & Simulation)

Thesis 1 establishes the core software systems, manual dataset collection, basic hardware assembly (manual flight only), and simulated autonomous capabilities.

### 1. Databox Dataset and Annotation Tool

Before training the fruit detection model, the project will use **Databox**, a separate reusable dataset and annotation tool built by the researcher. Databox gives the researchers control over image quality, labels, review status, and export format, and can be made open source so other researchers can use it to create YOLO-ready datasets.

**Main Idea:**
Create dataset -> upload or capture image -> video-to-frame extraction -> choose label class -> draw bounding boxes around fruits or citrus canopy -> save coordinates and metadata -> mark image as reviewed -> export labels for machine learning.

**Recommended Perante orange classes:**
```text
0 = citrus_fruit
1 = citrus_canopy
```

**Bounding Box Rules:**
- Both fruits and canopy regions use bounding boxes (YOLO object detection learns from rectangular boxes).
- A fruit box should tightly surround each visible fruit.
- A canopy box should surround the visible leafy or fruit-bearing area of the target tree, avoiding unnecessary trunk, ground, sky, and background areas as much as possible. This helps the model learn the region where fruit counting should happen.

**Suggested Database Fields (Databox):**
```text
datasets
- id
- name
- description
- project_type
- created_at

images
- id
- dataset_id
- filename
- file_path
- width
- height
- source
- capture_date
- tree_id
- status
- notes
- created_at

classes
- id
- dataset_id
- name
- class_index

annotations
- id
- image_id
- class_id
- annotation_type
- x_min
- y_min
- x_max
- y_max
- created_by
- created_at
```

**Bounding Box Math & YOLO Export Format:**
The platform stores boxes as pixel coordinates first:
```text
x_min, y_min, x_max, y_max
```
Then it converts them to YOLO's normalized format during export (`class_id center_x center_y width height`):
```text
center_x = ((x_min + x_max) / 2) / image_width
center_y = ((y_min + y_max) / 2) / image_height
width = (x_max - x_min) / image_width
height = (y_max - y_min) / image_height
```

### 2. Manual Dataset Collection
- Collect initial ground-level images and videos of Perante orange trees manually using handheld cameras/phones.
- Capture from multiple sides, distances, and lighting conditions. Include easy, medium, and difficult cases (occluded fruits).
- Use Databox to annotate this initial dataset for early machine learning development.

### 3. Physical Hardware Milestone (Manual Flight)
- Focus strictly on assembling a manual micro-drone for initial hardware validation.
- **Hardware Profile:** SpeedyBee F405 Mini flight controller running ArduPilot/Betaflight, motors, ESCs, frame, RC transmitter/receiver.
- **Scope Restriction:** The physical drone in Thesis 1 will ONLY perform manual RC flight, hovering, and landing. Do NOT include the Raspberry Pi Zero or onboard AI processing on the physical drone during Thesis 1.

### 4. Farmer Web Dashboard
Build a Next.js + Supabase dashboard as the central system where farms, trees, drones, scan requests, images, and AI results will eventually connect.

**Core Workflow:**
Farmer account -> farm registration -> crop registration -> tree registration -> interactive map location -> simulated drone scan UI -> scan records.

**Features & Map (Leaflet):**
- Farm registration and crop/tree details.
- Interactive map using Leaflet with OpenStreetMap tiles to place tree markers on a farm map.
- Simulated drone mission states (`QUEUED`, `PROCESSING`, `COMPLETED`), showing simulated battery and GPS status while the drone is not yet fully autonomous.

**Suggested Database Fields (Dashboard):**
```text
users
- id
- name
- email
- role
- created_at

farms
- id
- user_id
- name
- location_name
- map_center_lat
- map_center_lng
- notes

crops
- id
- farm_id
- name
- variety
- notes

trees
- id
- farm_id
- crop_id
- tree_code
- tree_name
- latitude
- longitude
- local_x
- local_y
- approximate_height
- notes
- status

drones
- id
- farm_id
- drone_name
- camera_type
- gps_supported
- status
- battery_percent
- gps_status
- camera_status
- last_seen_at

scan_missions
- id
- farm_id
- tree_id
- drone_id
- status
- requested_by
- requested_at
- started_at
- completed_at
- notes
```

### 5. Gazebo Simulation Engine
Use Gazebo Sim with ArduPilot SITL to test autonomous capabilities entirely in software before risking the physical drone.

**Simulation Tasks:**
- Build a Gazebo orchard environment with virtual trees, terrain, and obstacles.
- Spawn a simulated drone model.
- Test autonomous navigation from launch point to a selected tree.
- Simulate a circular scan path around the tree canopy.
- Test obstacle avoidance around trunks, branches, and nearby trees in software.

---

## Thesis 2 (Integration & Deployment)

Thesis 2 focuses on upgrading the physical hardware, refining the computer vision, integrating the pipeline end-to-end, and conducting real-world outdoor tests.

### 1. Hardware Upgrade
- **Companion Computer:** Mount a Raspberry Pi Zero 2 W + Raspberry Pi Camera V2 onto the physical drone.
- **Flight Controller Integration:** Connect the Pi to the SpeedyBee F405 flight controller.
- Enable MAVLink image triggering for synchronized aerial capture during autonomous flights.

### 2. Computer Vision Engine
- Train YOLOv8 on the Databox-exported dataset containing `citrus_fruit` and `citrus_canopy` classes.
- **Duplicate-Count Reduction:** Add ByteTrack / multi-frame association to track detections between nearby frames and avoid counting the same fruit repeatedly while the drone moves.

### 3. Pipeline Integration
Connect the entire workflow end-to-end:
```text
Aerial capture (RPi Camera) 
-> Offboard processing engine (Ground Laptop for MVP / Cloud GPU for Production) 
-> Supabase DB 
-> Real-time Dashboard updates
```
- The drone captures images and sends them to the processing engine.
- YOLOv8 and ByteTrack process the images, generating visible fruit count estimates.
- Results are saved to Supabase and immediately reflected on the Farmer Dashboard.

### 4. Field Validation
Conduct outdoor supervised flight tests on physical Perante orange trees in Nueva Vizcaya.

**Evaluation Metrics:**
- **Computer Vision:** Precision, recall, F1-score, mAP, and counting error per tree.
- **Drone Navigation:** Navigation success rate, obstacle avoidance success rate, and average scan time per tree.
- **Dashboard:** Reliable telemetry display and scan result storage.

---

## Scope Boundaries

**Included:**
- Databox reusable image dataset and annotation tool
- YOLO-ready annotation export
- Citrus canopy labeling and Perante orange fruit detection
- Visible fruit counting with duplicate-count reduction
- Drone image/video capture workflow
- Gazebo simulation for route planning and circular scans
- Orchard map and web dashboard

**Not included in the main scope:**
- Harvest readiness estimation or ripeness classification
- Disease and pest detection
- Exact 3D coordinate mapping of every individual fruit
- Fully autonomous large-scale farm deployment

## Recommended Thesis Claim

The project should claim:

> The system estimates the visible fruit count of registered Perante orange trees using drone-captured images or video, machine learning-based fruit detection, duplicate-count reduction, and orchard mapping.

The project should avoid claiming:

> The system counts every fruit on the tree perfectly.

This is important because some fruits may be hidden by leaves, branches, or other fruits.
