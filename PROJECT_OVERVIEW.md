# Autonomous Drone-Based Citrus Fruit Counting and Orchard Mapping for Perante Orange

## Project Summary

This project is a drone-based computer vision and mapping system for citrus orchards, focused on Perante orange farms in Nueva Vizcaya. Instead of manually checking each citrus tree, the farmer registers Perante orange trees in a web dashboard, and the drone autonomously navigates to a selected tree, circles around it, captures images or video, counts visible citrus fruits, and updates the dashboard with tree-level records.

The target environment has two parts: a real-world citrus orchard planted with Perante orange trees and a Gazebo citrus-orchard simulation. The real-world environment provides actual tree images, fruit-counting data, and supervised prototype testing. The simulation environment provides a safer place to test autonomous navigation, orchard layouts, terrain, obstacle avoidance, circular tree scanning, and repeated inspection missions before real-world drone testing.

The physical prototype will focus on scanning selected citrus trees, specifically Perante orange trees, in a real farm or controlled outdoor test area. The Gazebo simulation will represent a larger citrus orchard with multiple virtual trees, terrain, obstacles, and drone routes so the system can be tested beyond the limited number of trees available for physical testing.

## Working Thesis Title

**Autonomous Drone-Based Computer Vision and Mapping System for Citrus Fruit Counting in Perante Orange Trees**

## Problem Statement

Citrus farms require regular monitoring to estimate fruit quantity and support farm planning. For Perante orange trees, manual fruit counting can be slow, inconsistent, and difficult across many trees, especially when fruits are hidden behind leaves or distributed around different sides of the canopy.

A drone-based citrus inspection system can help farmers collect tree-level data more efficiently. By combining autonomous navigation, image capture, computer vision, and a web dashboard, the system can record visible fruit count, tree height, inspection history, and orchard map information for each registered Perante orange tree.

## Main Objective

To design and develop an autonomous drone-based citrus monitoring system that scans registered Perante orange trees, counts visible citrus fruits, creates or updates an orchard map, and displays tree-level records through a web-based dashboard.

## Specific Objectives

1. Build a citrus orchard monitoring model where each Perante orange tree has an ID, location, map position, inspection history, and tree attributes.
2. Create a web dashboard where a farmer can register citrus trees, with Perante orange as the specific target crop, and request or view drone inspection results.
3. Use a drone-mounted camera to capture images or video while circling a registered citrus tree.
4. Train or fine-tune a computer vision model to detect citrus fruits from Perante orange trees.
5. Estimate tree-level information such as visible fruit count and approximate tree height.
6. Store inspection results in a database with tree ID, images, timestamps, fruit count, map data, and confidence values.
7. Add autonomous navigation and obstacle avoidance for safe movement around trees and uneven terrain.
8. Develop a Gazebo simulation environment to test orchard navigation, terrain traversal from the air, tree scanning paths, and map updating before real-world drone testing.

## Target Crop

The target crop is **Perante orange**, a citrus crop under sweet orange.

Citrus, specifically Perante orange, is selected because:

- Nueva Vizcaya is strongly associated with citrus farming.
- Fruit quantity is important for farm monitoring, yield estimation, and planning.
- Fruits are visually detectable from images when lighting and angle are suitable.
- Tree-level monitoring is useful for orchard management.
- The project has local relevance and can use real images gathered from local citrus farms growing Perante orange.

## System Concept

The farmer registers a citrus tree in the website. For this project, the registered crop is Perante orange. The tree record may include a tree ID, tree name or label, farm section, approximate GPS or map location, variety, and notes. The drone uses this information to navigate toward the tree, scan around the canopy, capture images, and update the system with fruit count estimates.

The drone should ideally maintain or improve a map of the orchard over time. If the area has already been scanned, the drone can use previous map information to plan safer routes. If the environment is unfamiliar, the drone should still be able to explore carefully, detect obstacles, and update the map after each mission. This makes the mapping module a continuing system memory rather than a one-time map.

```text
Web Dashboard Tree Registration
        |
        v
Drone Mission Planning
        |
        v
Autonomous Navigation to Citrus Tree
        |
        v
Circle Scan Around Tree Canopy
        |
        v
Image Capture + Mapping Data
        |
        v
Computer Vision Fruit Detection
        |
        v
Visible Fruit Count Estimate
        |
        v
Database
        |
        v
Dashboard Map, Tree Records, and History
```

## Major System Components

### 1. Citrus Tree Model

Each registered citrus tree should be represented digitally in the system. The prototype focuses on Perante orange trees.

Example data:

- Tree ID
- Tree name or label
- Farm or orchard section
- GPS coordinate or local map coordinate
- Variety
- Approximate height
- Latest fruit count
- Latest inspection date
- Inspection history
- Notes or farmer observations

Example:

```text
Tree CT-001
- Location: Orchard Block A, Row 2
- Variety: Perante orange
- Approximate height: 2.4 m
- Latest fruit count: 186 visible fruits
- Last inspected: 2026-08-05 10:30 AM
```

### 2. Web Dashboard

The web dashboard is the farmer-facing control and reporting system.

Expected dashboard features:

- Register Perante orange trees
- View orchard map
- Select a tree for inspection
- View tree-level records
- Show drone-created or drone-updated map data
- Display latest tree image captures
- Display fruit count
- Display approximate tree height
- Show inspection history
- Show alerts for failed scans, low confidence, or blocked navigation

Possible tree-level statuses:

- Not yet inspected
- Scanned successfully
- Needs rescan
- High fruit count
- Low confidence result
- Navigation blocked

### 3. Drone Inspection Module

The drone is responsible for traveling to a target Perante orange tree, scanning the canopy, and sending captured data for processing.

Possible drone tasks:

- Navigate to a registered tree
- Avoid obstacles in an orchard environment
- Maintain a safe distance from tree branches
- Circle around the tree canopy
- Capture images or video from multiple angles
- Estimate or assist in estimating tree height
- Save camera pose, timestamp, and map data
- Send images and mission data to the processing system

Recommended scan behavior:

1. Take off from a safe launch area.
2. Navigate toward the target tree using map, GPS, visual markers, or manual-assisted initialization.
3. Slow down near the tree.
4. Detect the tree canopy or registered target area.
5. Circle around the tree at a safe distance.
6. Capture images from multiple angles and heights.
7. Avoid branches and nearby obstacles.
8. Return to the launch area or move to the next registered tree.
9. Upload images, map updates, and inspection results.

### 4. Mapping and Localization Module

The system should support orchard mapping because Perante orange orchards can have irregular tree spacing, terrain changes, and natural obstacles.

Possible mapping tasks:

- Create an orchard map from drone flight data
- Store known tree locations
- Update the map after each flight
- Record obstacles and safe flight corridors
- Support navigation in a previously mapped area
- Support careful exploration in unfamiliar areas
- Display map output in the web dashboard

Possible mapping technologies:

- GPS waypoint mapping & QMC5883L compass (Physical Drone)
- Visual pose association & image camera metadata (Physical Drone)
- Depth camera and 2D LiDAR simulation (Gazebo Simulation Only)

Important scope note: full reliable autonomous mapping in an unfamiliar outdoor orchard can become a large research problem by itself. A realistic thesis scope can combine manual tree registration, GPS/map waypoints, controlled autonomous scan paths, and incremental map updates.

### 5. Computer Vision Module

The computer vision module analyzes citrus tree images from Perante orange orchards and predicts visible fruit count.

Possible AI tasks:

- Detect the visible citrus canopy or fruit-bearing tree region
- Detect citrus fruits in images
- Count visible fruits from multiple angles
- Avoid double-counting the same fruit across frames where possible
- Estimate tree canopy area or approximate height
- Flag low-confidence results for human review

Recommended first model outputs:

- Citrus canopy bounding box, if canopy labeling is included
- Citrus fruit bounding boxes
- Fruit count per image
- Estimated unique fruit count per tree
- Confidence score

Important note: the system should avoid claiming perfect total fruit count because occlusion from leaves and branches can hide fruits. A safer and more realistic claim is that the system estimates visible fruit count from drone-captured images.

### 6. Dataset and Training Plan

The project will gather raw images from a citrus farm growing Perante orange. These images are important because real farm images will match the actual camera angles, lighting, fruit color, foliage density, and terrain conditions better than generic datasets. The images will be organized and labeled using **Databox**, a separate reusable dataset annotation tool built by the researcher for computer vision datasets.

Suggested dataset process:

1. Visit a citrus farm growing Perante orange and capture raw images from different trees.
2. Capture fruits from multiple angles, distances, heights, and lighting conditions.
3. Import or upload images into Databox.
4. Label visible citrus fruits with bounding boxes in Databox.
5. Label the visible citrus canopy or fruit-bearing leafy region with a larger bounding box when useful.
6. Export the labeled dataset from Databox in YOLO format.
7. Split the dataset into training, validation, and test sets.
8. Train a baseline object detection model.
9. Fine-tune the model using locally captured Perante orange farm images.
10. Evaluate fruit detection and counting accuracy.

Recommended initial labels:

- Citrus fruit
- Citrus canopy
- Unclear or occluded fruit

For canopy labeling, the box should focus on the visible leafy or fruit-bearing part of the target tree. It should avoid unnecessary trunk, ground, sky, and background areas where fruits are not expected to appear.

### 7. Gazebo Simulation Module

Gazebo will be used to simulate the drone and orchard environment before real-world testing.

Possible simulation tasks:

- Create virtual citrus trees modeled after Perante orange trees
- Create an orchard layout with multiple trees
- Add uneven terrain and slopes
- Add obstacles such as trunks, branches, fences, posts, irrigation pipes, and farm paths
- Simulate drone navigation to a target tree
- Simulate a circular tree scan path
- Test obstacle avoidance around tree canopies
- Test map update behavior across repeated missions
- Compare simulated route success with real-world testing

The planned simulated drone behavior is:

1. Take off from a start position.
2. Navigate to a registered tree.
3. Detect the tree or its assigned waypoint.
4. Approach at a safe distance.
5. Circle around the tree while keeping the camera pointed toward the canopy.
6. Capture images at planned intervals.
7. Update the map with path and obstacle information.
8. Return to start or continue to another tree.

### 8. Database Module

The database stores orchard, tree, drone mission, image, fruit detection, counting, and mapping data.

Possible tables:

- Users
- Farms
- Orchard blocks
- Citrus trees
- Drone missions
- Drone flight paths
- Tree scans
- Captured images
- Fruit detections
- Map versions
- Obstacles
- Alerts

Example inspection record:

```text
Scan ID: SCAN-001
Tree ID: CT-001
Mission ID: MIS-001
Images: ct_001_scan_2026_08_05/*.jpg
Visible fruit count: 186
Approximate height: 2.4 m
Confidence: 84%
Timestamp: 2026-08-05 10:30 AM
```

## Open-Source Datasets and Libraries

The project can use open citrus datasets and pre-trained models to reduce training time, but the strongest dataset should come from local Perante orange farm images.

### Possible Datasets

- Orange or citrus fruit detection datasets from Roboflow, Kaggle, or GitHub
- Fruit detection and counting datasets
- Agricultural drone imagery datasets
- Custom Perante orange farm image dataset from Nueva Vizcaya or nearby farms

Limitations:

- Public datasets may not match local Perante oranges.
- Public datasets may not match drone camera angle.
- Fruits may be occluded by leaves and branches.
- Public datasets may use different varieties, tree structures, and field conditions.

### Possible AI Libraries and Models

- YOLOv8, YOLOv11, or later YOLO models for object detection
- Detectron2 or Mask R-CNN for detection and segmentation
- OpenCV for image processing and camera calibration
- PyTorch or TensorFlow for training
- DeepSORT, ByteTrack, or similar tracking methods to reduce double counting across video frames

## Recommended AI Strategy

The recommended approach is **object detection plus counting aggregation**.

The first version should detect citrus fruits from Perante orange trees and estimate visible fruit count. A later version can reduce double-counting by tracking fruit detections across video frames or associating detections with camera poses from the drone scan.

Suggested steps:

1. Collect citrus images from Perante orange trees manually using a phone or camera.
2. Label fruit bounding boxes.
3. Train a baseline YOLO object detection model.
4. Test counting accuracy on unseen tree images.
5. Capture drone images from one or more citrus trees in the Perante orange orchard.
6. Fine-tune the model using drone-captured images.
7. Add tree-level aggregation to estimate total visible fruit count while reducing repeated counts across frames.

## Drone Navigation Scope

Autonomous orchard navigation should be included, but it should be scoped carefully. Outdoor autonomy, terrain awareness, obstacle avoidance, and mapping can become a separate thesis if the scope is too broad.

Recommended prototype scope:

- The farmer registers trees in the web dashboard.
- The system stores tree coordinates or map positions.
- The drone follows a controlled route to a selected tree.
- The drone performs a planned circular scan around the tree.
- The drone captures images from multiple angles.
- The system updates a map or mission path after each run.
- Gazebo is used to test larger orchard layouts, terrain, and obstacle avoidance.
- Real-world testing focuses on a limited number of Perante orange trees under supervised conditions.

Possible navigation methods:

- GPS waypoints
- RTK GPS, if available
- Visual markers for controlled tests
- Visual SLAM or VIO
- Depth camera or LiDAR for obstacle detection
- ROS 2 with ArduPilot (ArduCopter)
- Manual-assisted flight with automated image capture for early dataset collection

## Minimum Viable Prototype (Thesis Proof of Concept)

The first complete version should focus on proving the main concept.

MVP features:

1. Web dashboard for registering citrus trees.
2. One or more real citrus trees, specifically Perante orange trees, for data collection and testing.
3. Drone-mounted camera or manually controlled drone capture workflow.
4. Circular scan workflow around a selected tree.
5. Computer vision model that detects citrus fruits.
6. Estimated visible fruit count per tree.
7. Database for storing tree records and scan results.
8. Dashboard map showing registered trees, drone scan history, and results.
9. Gazebo simulation with orchard terrain, multiple trees, and obstacles.

## MVP vs. Commercial Product Strategy

Offloading AI inference from the physical drone to a cloud GPU server is the industry standard for commercial agricultural robotics, keeping hardware replacement costs under $200 while scaling computing power indefinitely.

| Dimension | Thesis MVP (Proof of Concept) | Commercial Product (Scale) |
| --- | --- | --- |
| **Primary Goal** | Validate autonomous navigation and vision algorithms for academic defense. | Scalable, low-cost hardware with simple "one-click" farmer UX. |
| **Drone Hardware** | ~$150 (SpeedyBee F405 Mini + Pi Zero 2 W + Pi Camera V2). | ~$180–$220 (Same drone + 4G LTE Cellular HAT module). |
| **Processing Engine** | Local Ground Laptop (runs ROS 2, YOLOv8, ByteTrack). | Cloud GPU Server (FastAPI / Celery worker with YOLOv8 on AWS or RunPod). |
| **Data Transmission** | Local Wi-Fi video stream from Pi to Laptop. | 4G/LTE cellular or automated Wi-Fi sync upon returning to base. |
| **UI Updates** | Local dashboard / post-flight analytics. | Real-time WebSocket updates via Supabase Realtime. |
| **Hardware Crash Risk** | Minimal financial impact; processing laptop stays safe on the ground. | Minimal financial impact; cheap ~$150 drone is easily replaced without losing software IP. |

## Step-by-Step Commercial Implementation Architecture

To achieve a system where a farmer clicks **"Scan My Farm"**, the drone flies autonomously, and the web UI shows progress updates (e.g., *Scanning*, *Processing*, *Completed*), the end-to-end pipeline operates through four core layers:

```text
 [ Farmer UI ] ──(1. Start Mission)──> [ Cloud API ] ──(2. MAVLink)──> [ 4G Drone ]
       ▲                                                                      │
       │                                                                (3. Upload Image
 (6. Realtime UI Update)                                                   + GPS Metadata)
       │                                                                      │
       └───── [ Supabase DB ] <─── (5. Save Counts) ─── [ Cloud AI Worker ] <──┘
```

#### 1. Drone Hardware Layer (Low Cost)

* **Flight Controller:** SpeedyBee F405 Mini running ArduPilot.
* **Companion Computer:** Raspberry Pi Zero 2 W.
* **Connectivity Module:** A 4G LTE HAT (e.g., Waveshare SIM7600 series) connected via USB/UART to the Pi.
* **Execution:** When hovering over a target tree, the Pi captures a high-resolution snapshot, tags it with the tree ID and GPS coordinates, and sends an HTTP `POST` request with the compressed JPEG to your Cloud API endpoint over 4G LTE.

#### 2. Cloud Ingestion & Async Processing Queue

* When the Cloud API (FastAPI / Node.js) receives an image:
  1. It immediately saves the raw image to **Supabase Storage**.
  2. It creates an entry in the `scans` table with status set to `'PROCESSING'`.
  3. It pushes an event to an asynchronous background task queue (e.g., Redis + Celery or a Cloud GPU Worker).

* *Why asynchronous?* The drone does not need to wait for the AI to respond before moving to the next tree. It uploads and immediately flies to the next waypoint.

#### 3. Cloud AI Execution Engine

* A lightweight, auto-scaling GPU instance (e.g., RunPod Serverless or AWS EC2) pulls the image from the queue.
* It executes your YOLOv8 fruit detection model.
* It calculates total count, confidence scores, and bounding box annotations.
* It updates the Supabase database row status to `'COMPLETED'` along with the final fruit count and annotated image URL.

#### 4. Real-Time Farmer Dashboard UX

* The web dashboard subscribes to database changes using **Supabase Realtime** (WebSockets).
* As soon as the Cloud AI worker updates a tree status from `'PROCESSING'` to `'COMPLETED'`, the UI automatically updates without refreshing.

### Farmer UI State Machine

```text
 ┌─────────────────────────────────────────────────────────────┐
 │                TREE INSPECTION QUEUE - BLOCK A              │
 ├──────────┬──────────────────────┬─────────────┬─────────────┤
 │ Tree ID  │ GPS Location         │ Status      │ Fruit Count │
 ├──────────┼──────────────────────┼─────────────┼─────────────┤
 │ CT-001   │ 10.3157 N, 123.8854 E│  COMPLETED  │  142 Fruits │
 │ CT-002   │ 10.3159 N, 123.8855 E│  COMPLETED  │  189 Fruits │
 │ CT-003   │ 10.3161 N, 123.8856 E│  PROCESSING │  [ Counting...]
 │ CT-004   │ 10.3163 N, 123.8857 E│  QUEUED     │  --         │
 │ CT-005   │ 10.3165 N, 123.8858 E│  QUEUED     │  --         │
 └──────────┴──────────────────────┴─────────────┴─────────────┘
```

## Possible Advanced Features

- Multi-tree autonomous inspection route
- Improved SLAM-based map creation
- RTK GPS integration
- 3D orchard map or point cloud view
- Fruit tracking across video frames to reduce double counting
- Tree canopy volume estimation
- Yield prediction
- Yield trend monitoring
- Disease or pest symptom detection
- Farmer notification system
- Mobile app support
- Automatic comparison of fruit count over time

## Research Questions

Main research question:

**Can an autonomous drone-mounted camera and computer vision model estimate visible citrus fruit count for Perante orange trees while using mapping and simulation to support navigation in an orchard environment?**

Supporting research questions:

1. How accurately can the model detect citrus fruits from drone-captured Perante orange tree images?
2. How accurately can the system estimate visible fruit count per tree?
3. Can tracking or multi-view association reduce repeated counting of the same fruit across multiple frames?
4. Can the drone follow a safe circular scan path around a registered Perante orange tree?
5. Can repeated drone missions improve or update an orchard map?
6. Can Gazebo simulation help validate orchard navigation, terrain handling, and obstacle avoidance before real-world testing?
7. Can a web dashboard help farmers view tree-level fruit count, height, map, and inspection history?

## Expected Outputs

The final project should produce:

- A working citrus tree inspection prototype focused on Perante orange
- A drone or drone-mounted camera workflow for tree scanning
- A Gazebo simulation environment with citrus trees, terrain, and obstacles
- A trained or fine-tuned citrus fruit detection model for Perante orange
- A database of citrus tree records and inspection results
- A web dashboard with tree registration, map view, fruit count, image records, and history
- Test results showing detection accuracy, counting accuracy, duplicate-count reduction, and navigation performance
- Thesis documentation explaining design, implementation, testing, and limitations

## Evaluation Metrics

Possible metrics for evaluating the project:

- Fruit detection precision, recall, and F1-score
- Counting error per image
- Counting error per tree
- Mean average precision for fruit detection
- Image capture success rate
- Correct tree identification rate
- Average scan time per tree
- Navigation success rate
- Obstacle avoidance success rate
- Simulated collision rate
- Map update consistency across repeated missions
- Dashboard response time
- Farmer usability feedback

## Risks and Limitations

### Computer Vision Limitations

- Fruits may be hidden by leaves, branches, or other fruits.
- Lighting changes may affect image quality.
- Fruit appearance can vary by variety, lighting, distance, and camera angle.
- Similar-looking fruits may be counted twice across multiple images.
- Public datasets may not match local Perante orange trees.
- More custom farm images may be needed for reliable accuracy.

### Drone Limitations

- Outdoor wind can affect stable scanning.
- Tree branches can be dangerous for close flight.
- GPS accuracy may not be enough for close tree scanning.
- Battery life limits the number of trees per mission.
- Manual override is still needed for safety.
- A small indoor-style drone may not be suitable for outdoor orchard conditions.

### Mapping and Navigation Limitations

- Autonomous mapping in unfamiliar terrain is difficult.
- Trees can look visually similar.
- Dense canopy may reduce visibility.
- Gazebo simulation may not perfectly match real orchard conditions.
- Navigation that works in simulation may still need tuning outdoors.

### Scope Limitations

- The system estimates visible fruit count, not guaranteed total fruit count.
- Full orchard-wide autonomous navigation may be too large for the initial thesis scope.

## Recommended Project Scope

The best thesis scope is:

**A drone-assisted computer vision and mapping system that estimates visible citrus fruit count for registered Perante orange trees, then displays tree-level inspection results on a web dashboard.**

This scope is locally relevant, research-worthy, and buildable. The system can include autonomous navigation and map updating, but the main contribution should be citrus fruit detection for Perante orange trees, tree-level counting, duplicate-count reduction, and dashboard reporting. Gazebo simulation can validate larger orchard navigation while real-world testing focuses on a limited number of trees.

## System Technology Stack

### 1. Thesis MVP Technology Stack (Academic Defense Setup)
* **Physical Flight Controller:** SpeedyBee F405 Mini running ArduPilot (ArduCopter).
* **Companion Computer:** Raspberry Pi Zero 2 W + Raspberry Pi Camera V2.
* **Local Telemetry & Video Link:** Local Wi-Fi network stream from Pi Zero 2 W to Ground Laptop.
* **Ground Offboard Processing:** Ground Laptop running Ubuntu 22.04 LTS, ROS 2, OpenCV, YOLOv8, and ByteTrack.
* **Simulation Engine:** Gazebo Sim integrated with ArduPilot SITL (`ardupilot_gz`).
* **Database & Web Dashboard:** Local or hosted Supabase (PostgreSQL + Realtime) + Next.js / React map interface.

### 2. Commercial Scaling Technology Stack (Production Roadmap)
* **Physical Hardware:** Same ~$150 Micro-Drone + Waveshare SIM7600 4G LTE Cellular HAT.
* **Communication Protocol:** MAVLink over 4G LTE / MQTT for snapshot uploads.
* **Backend Ingestion API:** FastAPI (Python) hosted on Cloud VPS.
* **Cloud AI Inference Engine:** Serverless GPU workers (RunPod / AWS EC2) running YOLOv8 asynchronously.
* **Database & Storage:** Supabase Cloud (PostgreSQL, Storage Buckets, Realtime WebSockets).
* **User Interface:** Responsive Web App / PWA (Next.js + Leaflet.js) with real-time job queues (`QUEUED`, `PROCESSING`, `COMPLETED`).
## Proposed Development Phases

### Phase 1: Research and Planning

- Review fruit detection and counting datasets.
- Review drone orchard navigation methods.
- Review Gazebo orchard simulation requirements.
- Finalize system architecture and scope.

### Phase 2: Data Collection

- Coordinate access to a citrus farm growing Perante orange.
- Capture raw citrus tree images from multiple angles.
- Capture images under different lighting conditions.
- Record tree notes and manual fruit count references when possible.
- Label fruit bounding boxes.

### Phase 3: Computer Vision Model

- Train a baseline fruit detection model.
- Fine-tune the model using local Perante orange farm images.
- Test detection and counting accuracy.
- Add counting aggregation and duplicate-count reduction.

### Phase 4: Web Dashboard and Database

- Create database schema.
- Build tree registration workflow.
- Build map view for registered trees.
- Build scan result views for fruit count, height, images, and history.

### Phase 5: Drone or Camera Inspection

- Set up the drone camera capture workflow.
- Add manual-assisted image capture for early testing.
- Define circular tree scan positions.
- Add autonomous mission planning for selected trees.
- Add obstacle detection and safety procedures.

### Phase 6: Gazebo Simulation

- Create virtual citrus tree models based on Perante orange trees.
- Create orchard terrain and multi-tree layouts.
- Add obstacles and safe flight paths.
- Simulate autonomous navigation to selected trees.
- Simulate circular scan behavior and map updates.

### Phase 7: Integration and Testing

- Connect drone capture, AI model, database, map, and dashboard.
- Test end-to-end tree inspection workflow.
- Test simulated orchard navigation.
- Measure detection, counting, duplicate-count reduction, mapping, and navigation performance.
- Document limitations and future improvements.

## Short Pitch

This project automates citrus tree inspection for Perante orange using a drone, computer vision, mapping, simulation, and a web dashboard. A farmer registers citrus trees in the website, then the drone navigates to a selected Perante orange tree, circles around it, captures images, counts visible fruits, updates the orchard map, and saves tree-level results so farmers can monitor fruit quantity and inspection history more efficiently.
