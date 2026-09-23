# Project Plan

## Project Direction

The project focuses on **visual inspection of hydroponic towers for lettuce and empty pots** using a drone-mounted camera, computer vision, GPS alignment, and a web dashboard. 

The project is restructured into two main phases to accommodate both software foundations and hardware integration: **Thesis 1 (Foundations & Simulation)** and **Thesis 2 (Integration & Deployment)**.

---

## Thesis 1 (Foundations & Simulation)

Thesis 1 establishes the core software systems, manual dataset collection, basic hardware assembly (manual flight only), and simulated capabilities.

### 1. Databox Dataset and Annotation Tool

Before training the detection model, the project will use **Databox**, a researcher-customized web dataset and annotation tool. Databox gives the researchers control over image quality, labels, review status, and export format, and can be used to create YOLO-ready datasets.

**Main Idea:**
Create dataset -> upload or capture image -> video-to-frame extraction -> choose label class -> draw bounding boxes around lettuce, empty pots, and the frame -> save coordinates and metadata -> mark image as reviewed -> export labels for machine learning.

**Recommended classes:**
```text
0 = lettuce
1 = empty_pot
2 = tower_frame
```

**Bounding Box Rules:**
- A box should tightly surround each visible lettuce head or empty pot.
- The tower frame can be labeled to help the drone identify the overall structure.

### 2. Manual Dataset Collection
- Assemble a physical structural frame (downloaded/3D printed or DIY) to serve as the hydroponic tower.
- Place lettuce and empty pots in the frame.
- Collect initial ground-level images and videos manually using handheld cameras/phones.
- Capture from multiple sides, distances, and lighting conditions.
- Use Databox to annotate this initial dataset for early machine learning development.

### 3. Physical Hardware Milestone (Manual Flight)
- Focus strictly on assembling a manual micro-drone for initial hardware validation.
- **Hardware Profile:** CogniFly-based frame, SpeedyBee F405 Mini flight controller running ArduPilot/ArduCopter, motors, ESCs, RC transmitter/receiver.
- **Scope Restriction:** The physical drone in Thesis 1 will ONLY perform manual RC flight, hovering, and landing under ArduPilot-stabilized control. Do NOT include the Raspberry Pi Zero or onboard AI processing on the physical drone during Thesis 1.

### 4. Farmer Web Dashboard
Build a Next.js + Supabase dashboard as the central system where farms, towers, drones, scan requests, images, and AI results will eventually connect.

**Core Workflow:**
Farmer account -> farm registration -> tower registration (with GPS coordinates) -> interactive map location -> simulated drone scan UI -> scan records.

**Features & Map (Leaflet):**
- Farm and tower registration.
- Interactive map using Leaflet with OpenStreetMap tiles to place tower markers based on their GPS coordinates.
- Simulated drone mission states (`QUEUED`, `PROCESSING`, `COMPLETED`).

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
- notes

towers
- id
- farm_id
- tower_code
- latitude
- longitude
- total_slots
- notes
- status

drones
- id
- farm_id
- drone_name
- status
- gps_status
- camera_status
- last_seen_at

scan_missions
- id
- farm_id
- tower_id
- drone_id
- status
- requested_by
- requested_at
- completed_at
- lettuce_count
- empty_pot_count
```

### 5. Gazebo Simulation (Development Tool)
While not a primary objective, Gazebo Sim with ArduPilot SITL can be used to safely test vertical camera scanning logic in software before risking the physical drone.
- Test autonomous GPS navigation from launch point to a selected tower's GPS coordinate.
- Simulate an up/down vertical scan path along the tower frame.

---

## Thesis 2 (Integration & Deployment)

Thesis 2 focuses on upgrading the physical hardware, refining the computer vision, integrating the pipeline end-to-end, and conducting real-world outdoor tests.

### 1. Hardware Upgrade
- **Companion Computer:** Mount a Raspberry Pi Zero 2 W + Raspberry Pi Camera V2 onto the physical drone.
- **Flight Controller Integration:** Connect the Pi to the SpeedyBee F405 flight controller. Add the GPS module.
- Enable MAVLink image triggering for synchronized capture during autonomous vertical flights.

### 2. Computer Vision Engine
- Train YOLOv8 on the Databox-exported dataset containing `lettuce`, `empty_pot`, and `tower_frame` classes.

### 3. Pipeline Integration
Connect the entire workflow end-to-end:
```text
Aerial capture (RPi Camera) 
-> Offboard processing engine (Ground Laptop for MVP) 
-> Supabase DB 
-> Real-time Dashboard updates
```
- The drone captures images during the vertical scan and sends them to the processing engine.
- YOLOv8 processes the images, generating lettuce and empty pot counts.
- Results are saved to Supabase and immediately reflected on the Farmer Dashboard.

### 4. Field Validation
Conduct outdoor supervised flight tests on the physical structural frame in an open, obstacle-free space.

**Evaluation Metrics:**
- **Computer Vision:** Precision, recall, and counting error per tower for lettuce and empty pots.
- **Drone Navigation:** GPS alignment accuracy and successful vertical scanning.
- **Dashboard:** Reliable telemetry display and scan result storage.

---

## Scope Boundaries

**Included:**
- Databox reusable image dataset and annotation tool
- YOLO-ready annotation export
- Detection of lettuce and empty pots
- GPS-based navigation to a hydroponic tower in an open space
- Vertical drone image/video capture workflow
- Web dashboard with tower registration and GPS mapping

**Not included in the main scope:**
- Complex obstacle avoidance or navigation in cluttered environments
- Large-scale spatial orchard mapping
- Functional hydroponic watering systems (a structural frame is sufficient for testing detection)
- Disease and pest detection

## Recommended Thesis Claim

The project should claim:

> The system automates the visual inspection of hydroponic towers in an open space using drone-captured images to detect lettuce and empty pots, aligned via GPS, and displayed on a web dashboard.

The project should avoid claiming:

> The drone can navigate complex cluttered environments or avoid unpredictable obstacles.

This is important because the project has been explicitly simplified to focus on GPS alignment and vertical scanning in an open, controlled space.
