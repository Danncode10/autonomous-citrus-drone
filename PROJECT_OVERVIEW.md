# Autonomous Drone-Based Perante Orange Tree Fruit Counting and Harvest Readiness Mapping

## Project Summary

This project is a drone-based computer vision and mapping system for Perante orange orchards. The system is designed for Perante orange farms in Nueva Vizcaya, which is known for citrus production in the Philippines. Instead of manually checking each tree, the farmer registers Perante orange trees in a web dashboard, and the drone autonomously navigates to a selected tree, circles around it, captures images or video, counts visible fruits, estimates how many fruits are ready to harvest, and updates the dashboard with tree-level records.

The target environment has two parts: a real-world Perante orange orchard and a Gazebo simulation orchard. The real-world environment provides actual tree images, fruit-counting data, harvest-readiness observations, and supervised prototype testing. The simulation environment provides a safer place to test autonomous navigation, orchard layouts, terrain, obstacle avoidance, circular tree scanning, and repeated inspection missions before real-world drone testing.

The physical prototype will focus on scanning selected Perante orange trees in a real farm or controlled outdoor test area. The Gazebo simulation will represent a larger orchard with multiple virtual trees, terrain, obstacles, and drone routes so the system can be tested beyond the limited number of trees available for physical testing.

## Working Thesis Title

**Autonomous Drone-Based Computer Vision and Mapping System for Perante Orange Tree Fruit Counting and Harvest Readiness Estimation**

## Problem Statement

Perante orange farms require regular monitoring to estimate fruit quantity, identify harvest-ready trees, and plan labor and selling schedules. Manual fruit counting and harvest readiness checking can be slow, inconsistent, and difficult across many trees, especially when fruits are hidden behind leaves or distributed around the canopy.

A drone-based inspection system can help farmers collect tree-level data more efficiently. By combining autonomous navigation, image capture, computer vision, and a web dashboard, the system can record fruit count, estimated harvest readiness, tree height, inspection history, and orchard map information for each registered Perante orange tree.

## Main Objective

To design and develop an autonomous drone-based system that scans registered Perante orange trees, counts visible Perante oranges, estimates harvest readiness percentage, creates or updates an orchard map, and displays tree-level records through a web-based dashboard.

## Specific Objectives

1. Build a Perante orange orchard monitoring model where each tree has an ID, location, map position, inspection history, and tree attributes.
2. Create a web dashboard where a farmer can register Perante orange trees and request or view drone inspection results.
3. Use a drone-mounted camera to capture images or video while circling a Perante orange tree.
4. Train or fine-tune a computer vision model to detect Perante oranges and classify harvest readiness.
5. Estimate tree-level information such as fruit count, approximate tree height, and percentage of visible fruits ready to harvest.
6. Store inspection results in a database with tree ID, images, timestamps, fruit count, readiness estimate, map data, and confidence values.
7. Add autonomous navigation and obstacle avoidance for safe movement around trees and uneven terrain.
8. Develop a Gazebo simulation environment to test orchard navigation, terrain traversal from the air, tree scanning paths, and map updating before real-world drone testing.

## Target Crop

The target crop is **Perante orange**.

Perante orange is selected because:

- Nueva Vizcaya is strongly associated with Perante orange farming.
- Fruit quantity and harvest readiness are important for farm planning.
- Fruits are visually detectable from images when lighting and angle are suitable.
- Tree-level monitoring is useful for orchard management.
- The project has local relevance and can use real images gathered from Perante orange farms.

## System Concept

The farmer registers a Perante orange tree in the website. The tree record may include a tree ID, tree name or label, farm section, approximate GPS or map location, variety, and notes. The drone uses this information to navigate toward the tree, scan around the canopy, capture images, and update the system with fruit count and readiness estimates.

The drone should ideally maintain or improve a map of the orchard over time. If the area has already been scanned, the drone can use previous map information to plan safer routes. If the environment is unfamiliar, the drone should still be able to explore carefully, detect obstacles, and update the map after each mission. This makes the mapping module a continuing system memory rather than a one-time map.

```text
Web Dashboard Tree Registration
        |
        v
Drone Mission Planning
        |
        v
Autonomous Navigation to Perante Orange Tree
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
Fruit Count + Harvest Readiness Estimate
        |
        v
Database
        |
        v
Dashboard Map, Tree Records, and History
```

## Major System Components

### 1. Perante Orange Tree Model

Each Perante orange tree should be represented digitally in the system.

Example data:

- Tree ID
- Tree name or label
- Farm or orchard section
- GPS coordinate or local map coordinate
- Variety
- Approximate height
- Latest fruit count
- Latest harvest readiness percentage
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
- Ready to harvest: 62%
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
- Display harvest readiness percentage
- Display approximate tree height
- Show inspection history
- Show trees ready for harvest
- Show alerts for failed scans, low confidence, or blocked navigation

Possible tree-level statuses:

- Not yet inspected
- Scanned successfully
- Needs rescan
- High fruit count
- Ready for harvest
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

- GPS waypoint mapping
- Visual SLAM
- VIO, visual-inertial odometry
- RTK GPS for more accurate outdoor localization, if available
- Depth camera or LiDAR-based mapping
- Photogrammetry for orchard map generation
- ROS 2 mapping and navigation tools

Important scope note: full reliable autonomous mapping in an unfamiliar outdoor orchard can become a large research problem by itself. A realistic thesis scope can combine manual tree registration, GPS/map waypoints, controlled autonomous scan paths, and incremental map updates.

### 5. Computer Vision Module

The computer vision module analyzes Perante orange tree images and predicts fruit count and harvest readiness.

Possible AI tasks:

- Detect Perante oranges in images
- Count visible fruits from multiple angles
- Avoid double-counting the same fruit across frames where possible
- Classify fruit readiness based on color, size, and visual maturity
- Estimate tree canopy area or approximate height
- Flag low-confidence results for human review

Recommended first model outputs:

- Perante orange fruit bounding boxes
- Fruit count per image
- Estimated unique fruit count per tree
- Ready-to-harvest count
- Not-yet-ready count
- Harvest readiness percentage
- Confidence score

Important note: the system should avoid claiming perfect total fruit count because occlusion from leaves and branches can hide fruits. A safer and more realistic claim is that the system estimates visible fruit count and harvest readiness from drone-captured images.

### 6. Dataset and Training Plan

The project will gather raw images from a Perante orange farm. These images are important because real farm images will match the actual camera angles, lighting, fruit color, foliage density, and terrain conditions better than generic datasets.

Suggested dataset process:

1. Visit a Perante orange farm and capture raw images from different trees.
2. Capture fruits from multiple angles, distances, heights, and lighting conditions.
3. Label Perante oranges with bounding boxes.
4. Label harvest readiness classes, such as ready and not ready.
5. Split the dataset into training, validation, and test sets.
6. Train a baseline object detection model.
7. Fine-tune the model using locally captured Perante orange images.
8. Evaluate fruit counting accuracy and readiness classification accuracy.

Recommended initial labels:

- Perante orange fruit
- Ready-to-harvest Perante orange fruit
- Not-yet-ready Perante orange fruit
- Unclear or occluded fruit

### 7. Gazebo Simulation Module

Gazebo will be used to simulate the drone and orchard environment before real-world testing.

Possible simulation tasks:

- Create virtual Perante orange trees with different canopy sizes
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

The database stores orchard, tree, drone mission, image, prediction, and mapping data.

Possible tables:

- Users
- Farms
- Orchard blocks
- Perante orange trees
- Drone missions
- Drone flight paths
- Tree scans
- Captured images
- Fruit detections
- Harvest readiness predictions
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
Ready-to-harvest count: 116
Harvest readiness: 62%
Approximate height: 2.4 m
Confidence: 84%
Timestamp: 2026-08-05 10:30 AM
```

## Open-Source Datasets and Libraries

The project can use open datasets and pre-trained models to reduce training time, but the strongest dataset should come from local Perante orange farm images.

### Possible Datasets

- Orange or citrus fruit detection datasets from Roboflow, Kaggle, or GitHub
- Fruit detection and counting datasets
- Agricultural drone imagery datasets
- Custom Perante orange farm image dataset from Nueva Vizcaya or nearby farms

Limitations:

- Public datasets may not match local Perante oranges.
- Public datasets may not match drone camera angle.
- Fruits may be occluded by leaves and branches.
- Harvest readiness can depend on variety and local farmer judgment.

### Possible AI Libraries and Models

- YOLOv8, YOLOv11, or later YOLO models for object detection
- Detectron2 or Mask R-CNN for detection and segmentation
- OpenCV for image processing and camera calibration
- PyTorch or TensorFlow for training
- DeepSORT, ByteTrack, or similar tracking methods to reduce double counting across video frames
- MobileNet, EfficientNet, ResNet, or Vision Transformer models for readiness classification

## Recommended AI Strategy

The recommended approach is **object detection plus readiness classification**.

The first version should detect Perante oranges and estimate visible fruit count. A later version can reduce double-counting by tracking fruit detections across video frames or associating detections with camera poses from the drone scan.

Suggested steps:

1. Collect Perante orange images manually from the farm using a phone or camera.
2. Label fruit bounding boxes and readiness classes.
3. Train a baseline YOLO object detection model.
4. Test counting accuracy on unseen tree images.
5. Capture drone images from one or more Perante orange trees.
6. Fine-tune the model using drone-captured images.
7. Add tree-level aggregation to estimate total visible fruit count and harvest readiness percentage.

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
- ROS 2 with PX4 or ArduPilot
- Manual-assisted flight with automated image capture for early dataset collection

## Minimum Viable Prototype

The first complete version should focus on proving the main concept.

MVP features:

1. Web dashboard for registering Perante orange trees.
2. One or more real Perante orange trees for data collection and testing.
3. Drone-mounted camera or manually controlled drone capture workflow.
4. Circular scan workflow around a selected tree.
5. Computer vision model that detects Perante oranges.
6. Estimated visible fruit count per tree.
7. Estimated percentage of ready-to-harvest fruits.
8. Database for storing tree records and scan results.
9. Dashboard map showing registered trees, drone scan history, and results.
10. Gazebo simulation with orchard terrain, multiple trees, and obstacles.

## Possible Advanced Features

- Multi-tree autonomous inspection route
- Improved SLAM-based map creation
- RTK GPS integration
- 3D orchard map or point cloud view
- Fruit tracking across video frames to reduce double counting
- Tree canopy volume estimation
- Yield prediction
- Harvest scheduling
- Disease or pest symptom detection
- Farmer notification system
- Mobile app support
- Automatic comparison of fruit count over time

## Research Questions

Main research question:

**Can an autonomous drone-mounted camera and computer vision model estimate Perante orange fruit count and harvest readiness at the tree level while using mapping and simulation to support navigation in an orchard environment?**

Supporting research questions:

1. How accurately can the model detect Perante oranges from drone-captured tree images?
2. How accurately can the system estimate visible fruit count per tree?
3. Can the system classify or estimate harvest readiness from visual fruit features?
4. Can the drone follow a safe circular scan path around a registered Perante orange tree?
5. Can repeated drone missions improve or update an orchard map?
6. Can Gazebo simulation help validate orchard navigation, terrain handling, and obstacle avoidance before real-world testing?
7. Can a web dashboard help farmers view tree-level fruit count, readiness, height, map, and inspection history?

## Expected Outputs

The final project should produce:

- A working Perante orange tree inspection prototype
- A drone or drone-mounted camera workflow for tree scanning
- A Gazebo simulation environment with Perante orange trees, terrain, and obstacles
- A trained or fine-tuned Perante orange fruit detection model
- A harvest-readiness estimation workflow
- A database of Perante orange tree records and inspection results
- A web dashboard with tree registration, map view, fruit count, readiness percentage, and history
- Test results showing detection accuracy, counting accuracy, readiness estimation, and navigation performance
- Thesis documentation explaining design, implementation, testing, and limitations

## Evaluation Metrics

Possible metrics for evaluating the project:

- Fruit detection precision, recall, and F1-score
- Counting error per image
- Counting error per tree
- Harvest readiness classification accuracy
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
- Fruit color varies by variety and maturity stage.
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
- Harvest readiness is estimated from images and should be validated with farmer judgment.
- Full orchard-wide autonomous navigation may be too large for the initial thesis scope.

## Recommended Project Scope

The best thesis scope is:

**A drone-assisted computer vision and mapping system that estimates visible Perante orange fruit count and harvest readiness for registered Perante orange trees, then displays tree-level inspection results on a web dashboard.**

This scope is locally relevant, research-worthy, and buildable. The system can include autonomous navigation and map updating, but the main contribution should be Perante orange fruit detection, tree-level counting, harvest readiness estimation, and dashboard reporting. Gazebo simulation can validate larger orchard navigation while real-world testing focuses on a limited number of trees.

## Suggested Technology Stack

### Hardware

- Outdoor-capable drone platform
- RGB camera or drone camera
- Optional gimbal for stable tree-facing image capture
- Optional depth camera or LiDAR
- Optional RTK GPS module
- Ground laptop or backend server

### AI and Computer Vision

- Python
- OpenCV
- PyTorch or TensorFlow
- YOLO for fruit detection
- Optional segmentation model for occluded fruits
- Optional tracking model for video-based counting

### Drone and Robotics

- Gazebo simulation
- ROS 2 for simulation and robotics integration
- PX4 or ArduPilot
- MAVLink
- GPS or RTK GPS
- SLAM, VIO, depth sensing, or LiDAR for mapping

### Web System

- Frontend: React, Vue, or plain HTML/CSS/JavaScript
- Backend: Node.js, Python Flask, FastAPI, or Django
- Database: PostgreSQL, MySQL, SQLite, or Supabase
- Image storage: local storage, cloud storage, or object storage
- Map display: Leaflet, Mapbox, Cesium, or a custom map view

## Proposed Development Phases

### Phase 1: Research and Planning

- Study Perante orange harvest-readiness indicators.
- Review fruit detection and counting datasets.
- Review drone orchard navigation methods.
- Review Gazebo orchard simulation requirements.
- Finalize system architecture and scope.

### Phase 2: Data Collection

- Coordinate access to a Perante orange farm.
- Capture raw Perante orange tree images from multiple angles.
- Capture images under different lighting conditions.
- Record tree notes and farmer harvest-readiness judgment.
- Label fruit bounding boxes and readiness classes.

### Phase 3: Computer Vision Model

- Train a baseline fruit detection model.
- Fine-tune the model using local Perante orange farm images.
- Test detection and counting accuracy.
- Add harvest-readiness estimation.

### Phase 4: Web Dashboard and Database

- Create database schema.
- Build tree registration workflow.
- Build map view for registered trees.
- Build scan result views for fruit count, readiness percentage, height, images, and history.

### Phase 5: Drone or Camera Inspection

- Set up the drone camera capture workflow.
- Add manual-assisted image capture for early testing.
- Define circular tree scan positions.
- Add autonomous mission planning for selected trees.
- Add obstacle detection and safety procedures.

### Phase 6: Gazebo Simulation

- Create virtual Perante orange tree models.
- Create orchard terrain and multi-tree layouts.
- Add obstacles and safe flight paths.
- Simulate autonomous navigation to selected trees.
- Simulate circular scan behavior and map updates.

### Phase 7: Integration and Testing

- Connect drone capture, AI model, database, map, and dashboard.
- Test end-to-end tree inspection workflow.
- Test simulated orchard navigation.
- Measure detection, counting, readiness, mapping, and navigation performance.
- Document limitations and future improvements.

## Short Pitch

This project automates Perante orange tree inspection using a drone, computer vision, mapping, simulation, and a web dashboard. A farmer registers Perante orange trees in the website, then the drone navigates to a selected tree, circles around it, captures images, counts visible fruits, estimates harvest readiness, updates the orchard map, and saves tree-level results so farmers can monitor fruit quantity, harvest timing, and inspection history more efficiently.
