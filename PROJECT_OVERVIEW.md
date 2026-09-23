# COMPUTER VISION AND AUTONOMOUS DRONE INSPECTION FOR HYDROPONIC TOWERS WITH WEB DASHBOARD INTEGRATION

## Project Team

**LEADER:** LESTER DANN G. LOPEZ  
**MEMBERS:** RHOAN JOY M. MARVILLA, PRINCE DANIEL A. VALENTINO, JOSHUA JING A. FERNANDEZ  
**THESIS ADVISER:** BERNADETH B. LIGGAYU  

## Project Summary

This project introduces an autonomous drone-based inspection system that utilizes computer vision to monitor vertical hydroponic towers and transmits the captured data to a web dashboard for remote farmer monitoring. The system operates by deploying a drone that autonomously navigates the agricultural environment, using an onboard camera and computer vision algorithms to accurately detect and position itself relative to the specific frames of the hydroponic towers. 

Once aligned with the target plant slots, the drone captures images and automatically uploads this visual telemetry and inspection data to a centralized web platform. Through this web dashboard, farmers can seamlessly track inspection history and visually monitor their crops (specifically lettuce) and identify available empty pots without manual intervention.

To simplify the hardware and focus on the core inspection mechanics, the drone will operate in an open, obstacle-free space, eliminating the need for complex obstacle avoidance algorithms. For the physical testing phase, the project will utilize a structural frame for the hydroponic tower (which can be downloaded and 3D printed or assembled). This frame serves strictly as a physical target for the drone to detect slots and plants, meaning it does not need a functional hydroponic watering system to validate the drone's scanning capabilities. Both the drone and the tower frames will utilize GPS coordinates to ensure accurate open-space alignment.

## Problem Statement

Vertical hydroponic farms require regular monitoring to track plant growth, identify empty slots, and support farm planning. Manual inspection can be slow and inconsistent, especially for taller towers. 

A drone-based inspection system can help farmers collect tower-level data more efficiently. By combining autonomous GPS navigation, image capture, computer vision, and a web dashboard, the system can record plant status, detect empty pots, and maintain inspection history for each registered hydroponic tower.

## Main Objective

To design and develop an autonomous drone-based monitoring system that uses GPS to align with registered hydroponic towers in an open space, vertically scans the structure, detects lettuce and empty pots using computer vision, and displays tower-level records through a web-based dashboard.

## Specific Objectives

1. Build a hydroponic tower monitoring model where each tower has an ID, GPS location, inspection history, and slot attributes.
2. Create a web dashboard where a farmer can register hydroponic towers and request or view drone inspection results.
3. Use a drone-mounted camera to capture images or video while vertically scanning a registered hydroponic tower.
4. Train or fine-tune a computer vision model to detect lettuce and empty pots on the tower.
5. Estimate tower-level information such as available planting slots and occupied slots.
6. Store inspection results in a database with tower ID, images, timestamps, slot counts, and confidence values.
7. Implement autonomous GPS navigation for the drone to align itself with a target tower in an open, obstacle-free space.

*(Note: Gazebo simulation will be utilized during development to safely test the vertical scanning sequence in software before real-world flights, but it is not a primary objective of the final deployed system.)*

## Target Crop and Physical Setup

The target crop is **Lettuce**. Additionally, the system is designed to detect **Empty Pots** to notify the farmer of available slots.

The physical testing environment will consist of:
- An open, obstacle-free outdoor or controlled space where GPS is available.
- A physical structural frame serving as the hydroponic tower. This frame can be built from downloadable internet plans or 3D-printed. It does not require functional hydroponic plumbing; it only needs to hold the lettuce and empty pots so the drone has a visual target to detect and scan.

## System Concept

The farmer registers a hydroponic tower in the web dashboard, logging its GPS coordinates. The drone uses this GPS location to navigate toward the tower in the open space. Once aligned, it performs a vertical scan, captures images of the slots, and updates the system with lettuce and empty pot counts.

```text
Web Dashboard Tower Registration (with GPS)
        |
        v
Drone Mission Planning
        |
        v
Autonomous GPS Navigation to Tower
        |
        v
Vertical Scan of Tower Slots
        |
        v
Image Capture
        |
        v
Computer Vision Detection (Lettuce / Empty Pot)
        |
        v
Slot Availability Estimate
        |
        v
Database
        |
        v
Dashboard Records and History
```

## Major System Components

### 1. Hydroponic Tower Model

Each registered tower is represented digitally in the system.

Example data:
- Tower ID
- Farm section
- GPS coordinate
- Total slots
- Occupied slots (Lettuce)
- Empty slots (Empty Pot)
- Latest inspection date
- Inspection history

### 2. Web Dashboard

The web dashboard is the farmer-facing control and reporting system.

Expected dashboard features:
- Register towers and input their GPS coordinates.
- Select a tower for inspection.
- View tower-level records and inspection history.
- Display latest tower image captures.
- Display counts for lettuce and empty pots.

### 3. Drone Inspection Module

The drone travels to a target tower, scans it vertically, and sends captured data. Obstacle avoidance is intentionally excluded, as the drone operates in an open space.

Recommended scan behavior:
1. Take off from a safe launch area.
2. Navigate to the target tower's GPS coordinate.
3. Align with the tower face.
4. Ascend or descend vertically to scan the slots.
5. Capture images at planned intervals.
6. Return to the launch area.
7. Upload images and inspection results.

### 4. Computer Vision Module

The computer vision module analyzes images of the tower to detect the contents of each slot.

Possible AI tasks:
- Detect `lettuce`.
- Detect `empty_pot`.
- Count occupied vs. available slots.

### 5. Dataset and Training Plan

The project will use **Databox**, a customized web dataset annotation tool, to organize and label images of the structural frame, lettuce, and empty pots.

1. Assemble the structural frame and place lettuce and empty pots in it.
2. Capture images from the drone or a handheld camera.
3. Import images into Databox.
4. Label `lettuce`, `empty_pot`, and `tower_frame`.
5. Export the labeled dataset in YOLO format.
6. Train a baseline object detection model (e.g., YOLOv8).

### 6. Database Module

Stores tower data, drone missions, images, and detections.

Possible tables:
- Users
- Farms
- Towers
- Drone missions
- Captured images
- Detections

### 7. Gazebo Simulation (Development Tool)

While not a core specific objective, Gazebo will be used as a development tool. It provides a software environment to simulate the drone taking off, navigating to a GPS waypoint, and executing a vertical camera scan of a virtual tower model. This allows for safe testing of the camera alignment code before physical flight.

## Minimum Viable Prototype (Thesis Proof of Concept)

1. Web dashboard for registering towers with GPS coordinates.
2. A physical structural frame to serve as the hydroponic tower target.
3. Drone-mounted camera with GPS navigation capabilities.
4. Vertical scan workflow.
5. Computer vision model that detects lettuce and empty pots.
6. Database and dashboard for storing and displaying results.

## System Technology Stack

### 1. Thesis MVP Technology Stack (Academic Defense Setup)
* **Physical Flight Controller:** SpeedyBee F405 Mini running ArduPilot (ArduCopter) on a CogniFly-based drone frame.
* **Drone GPS:** HGLRC M100-5883 GPS + Compass Module.
* **Companion Computer:** Raspberry Pi Zero 2 W + Raspberry Pi Camera V2.
* **Local Telemetry & Video Link:** Local Wi-Fi network stream from Pi Zero 2 W to Ground Laptop.
* **Ground Offboard Processing:** Ground Laptop running Ubuntu 22.04 LTS, ROS 2, OpenCV, YOLOv8.
* **Simulation (Optional/Dev):** Gazebo Sim integrated with ArduPilot SITL.
* **Database & Web Dashboard:** Supabase (PostgreSQL + Realtime) + Next.js.

### 2. Commercial Scaling Technology Stack (Production Roadmap)
* **Physical Hardware:** Same ~$150 Micro-Drone + Waveshare SIM7600 4G LTE Cellular HAT.
* **Backend Ingestion API:** FastAPI (Python) hosted on Cloud VPS.
* **Cloud AI Inference Engine:** Serverless GPU workers (RunPod / AWS EC2) running YOLOv8 asynchronously.

## Proposed Development Phases

### Phase 1: Research and Setup
- Assemble the physical hydroponic tower structural frame.
- Build the CogniFly-based drone with GPS module.

### Phase 2: Data Collection
- Capture images of lettuce and empty pots on the frame.
- Label bounding boxes in Databox.

### Phase 3: Computer Vision Model
- Train and fine-tune a YOLOv8 detection model.
- Test detection accuracy on unseen tower images.

### Phase 4: Web Dashboard and Database
- Create database schema for towers and slots.
- Build tower registration workflow (including GPS coordinates).
- Build scan result views.

### Phase 5: Drone Inspection Flight
- Program the GPS waypoint navigation.
- Implement the vertical scanning maneuver.
- Test the flight in an open, obstacle-free space.

### Phase 6: Integration and Testing
- Connect drone capture, AI model, database, and dashboard.
- Test end-to-end tower inspection workflow.
- Measure detection and counting performance.
- Document limitations.
