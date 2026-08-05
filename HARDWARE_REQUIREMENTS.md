# Hardware Requirements

## Overview

This document lists the hardware needed for the updated autonomous citrus tree inspection project. The previous hydroponic tower hardware is no longer part of the research scope. The system now focuses on outdoor citrus orchards, drone-based scanning, fruit counting, harvest-readiness estimation, tree-height estimation, orchard mapping, and Gazebo simulation.

The hardware is separated into four main areas:

1. Citrus farm data collection
2. Drone inspection system
3. Mapping, navigation, and safety equipment
4. Backend and development equipment

The physical prototype should start with a small number of citrus trees and supervised drone flights. The larger orchard scenario should be tested first in Gazebo simulation.

## Citrus Farm Data Collection

| Device | Link | Price | Quantity |
| --- | --- | ---: | ---: |
| Citrus farm access / test trees | TBD | TBD | 1 farm or test area |
| Citrus tree labels or waterproof tags | TBD | PHP 50-300 estimate | TBD |
| Measuring tape or laser distance meter | TBD | PHP 100-1,500 estimate | 1 |
| Ground control markers / visual reference markers | TBD | PHP 100-500 estimate | TBD |
| Notebook or digital field form device | TBD | PHP 0-500 estimate | 1 |
| Data collection subtotal | TBD | PHP 250-2,800 estimate | TBD |

## Drone Hardware and Electronics

| Device | Link | Price | Quantity |
| --- | --- | ---: | ---: |
| Outdoor-capable drone platform | TBD | TBD | 1 |
| Flight controller compatible with PX4 or ArduPilot | TBD | TBD | 1 |
| ESC and motor set suitable for outdoor flight | TBD | TBD | 1 set |
| Propellers plus spare propellers | TBD | TBD | TBD |
| Drone battery packs | TBD | TBD | 2+ recommended |
| Battery charger | TBD | TBD | 1 |
| RC transmitter and receiver / manual override link | TBD | TBD | 1 |
| RGB camera or drone camera | TBD | TBD | 1 |
| Optional camera gimbal | TBD | TBD | Optional |
| Companion computer, such as Raspberry Pi, Jetson, or similar | TBD | TBD | Optional / recommended |
| 5V voltage regulator / BEC for companion computer | TBD | TBD | 1 if needed |
| Drone hardware subtotal | TBD | TBD | TBD |

## Mapping, Navigation, and Safety Hardware

| Device | Link | Price | Quantity |
| --- | --- | ---: | ---: |
| GPS module | TBD | TBD | 1 |
| RTK GPS module and base station | TBD | TBD | Optional |
| Depth camera or LiDAR sensor | TBD | TBD | Optional / recommended |
| Front obstacle distance sensor | TBD | TBD | Optional |
| Telemetry radio | TBD | TBD | Optional |
| Landing pad or marked launch area | TBD | PHP 200-1,000 estimate | 1 |
| Propeller guards or protective frame | TBD | TBD | Optional |
| Safety cones / test boundary markers | TBD | PHP 100-500 estimate | TBD |
| LiPo-safe charging bag or battery safety box | TBD | PHP 200-800 estimate | 1 |
| Mapping and safety subtotal | TBD | TBD | TBD |

## Development and Backend Equipment

| Device | Link | Price | Quantity |
| --- | --- | ---: | ---: |
| Laptop or desktop for development | Existing / TBD | TBD | 1 |
| Local server or cloud backend | TBD | TBD | 1 |
| External storage for image dataset backup | TBD | PHP 500-3,000 estimate | Optional |
| Internet connection for dashboard and dataset sync | Existing / TBD | TBD | 1 |
| Development equipment subtotal | TBD | TBD | TBD |

## 1. Citrus Farm and Tree Identification Hardware

The field setup provides the real-world citrus trees, labels, and reference measurements needed for training and validating the system.

Required components:

- Access to citrus trees in a farm or controlled outdoor test area
- Tree labels or waterproof tags
- Tree ID list
- Measuring tape or laser distance meter for manual height reference
- Ground reference markers or visual markers for controlled tests
- Field notes for tree variety, fruit maturity, and farmer observations

Optional components:

- GPS phone or handheld GPS for rough tree coordinates
- RTK reference points for accurate mapping
- Calibration board for camera testing
- Color reference card for fruit maturity image calibration

Purpose:

- Assign each citrus tree a stable identity
- Help compare drone-estimated height with manual measurement
- Help validate fruit count and harvest-readiness estimates
- Support dashboard tree registration and map placement

## 2. Drone Inspection Hardware

The drone inspection system captures tree images, circles around the target tree, supports autonomous navigation, and contributes to map creation or map updates.

### 2.1 Drone Platform

Recommended direction:

- Use an outdoor-capable quadcopter or similar drone platform.
- Prefer a platform that supports autonomous missions, GPS waypoints, manual override, and camera mounting.
- For research flexibility, a PX4-compatible or ArduPilot-compatible platform is preferred.

Important note:

The previous CogniFly-inspired drone direction was better suited for indoor, close-range tower inspection. Citrus tree inspection is an outdoor task with wind, terrain, larger distances, and tree branches. A small indoor drone may still be useful for simulation concepts or controlled tests, but the main physical prototype should use a safer outdoor-capable drone.

Required platform capabilities:

- Stable outdoor hover
- Manual control and emergency override
- Camera mount or integrated camera
- Enough battery life for tree approach, circular scan, and return
- Safe operation near trees
- Support for waypoint missions or companion-computer control

Optional platform capabilities:

- Obstacle avoidance sensors
- Gimbal stabilization
- RTK GPS support
- Telemetry radio
- Payload bay for companion computer or extra sensors

### 2.2 Camera

Recommended camera requirements:

- RGB image capture
- Clear view of citrus fruits at tree-canopy distance
- Stable mounting or gimbal support
- Good resolution for fruit detection
- Ability to capture still images or video

Camera responsibilities:

- Capture fruits from multiple sides of the tree
- Capture images while circling the tree
- Support fruit counting and harvest-readiness estimation
- Support visual mapping or localization if used

Optional alternatives:

- Integrated drone camera
- Raspberry Pi Camera Module
- USB camera
- Arducam autofocus camera
- Depth camera, if payload allows

### 2.3 Companion Computer

Recommended options:

- Raspberry Pi 4 or Raspberry Pi 5
- Jetson Nano or Jetson Orin Nano
- Raspberry Pi Zero 2 W for lighter capture-only setups
- Laptop/backend processing for early prototypes

Possible responsibilities:

- Capture or receive camera images
- Run basic image processing
- Detect visual markers or tree target areas
- Communicate with the flight controller through MAVLink
- Upload images to the backend
- Store mission logs

Important note:

Heavy fruit detection and model training can run on the laptop or backend during early development. The drone does not need to run the full AI model onboard in the first prototype.

### 2.4 Navigation and Mapping Sensors

Recommended minimum:

- GPS module for outdoor waypoint navigation
- Camera-based capture for visual inspection
- Manual control link for safety

Stronger navigation setup:

- RTK GPS for more accurate tree approach
- Depth camera or LiDAR for obstacle detection
- Visual SLAM or visual-inertial odometry support
- Telemetry radio for monitoring

Purpose:

- Navigate to registered tree positions
- Maintain distance from tree canopies
- Avoid branches, trunks, posts, and other obstacles
- Update the orchard map after repeated missions
- Support autonomous or semi-autonomous operation in unfamiliar environments

### 2.5 Battery and Power

Required components:

- Drone battery packs
- Battery charger
- Power cables and connectors
- Voltage regulator or BEC if powering a companion computer

Recommended considerations:

- Use at least two batteries for field testing.
- Monitor voltage during flight.
- Keep enough reserve power for return-to-home.
- Verify payload weight before adding sensors.
- Use a LiPo-safe charging bag or battery safety box.

## 3. Website, Backend, and Storage Context

The backend is not a physical farm component, but it affects the hardware and data collection workflow.

Recommended first setup:

- Laptop or desktop for development
- Local server or cloud backend
- Database
- Image storage
- Dataset backup drive

Suggested processing split:

- Drone captures images and mission logs.
- Backend or laptop runs fruit detection and harvest-readiness estimation.
- Website stores tree registration and inspection results.
- Dashboard displays map, fruit count, readiness percentage, height, images, and history.

## 4. Minimum Hardware Build

Minimum realistic physical prototype:

- Access to one or more citrus trees
- Tree ID labels or waterproof tags
- Measuring tape or laser distance meter
- Outdoor-capable drone with camera
- Manual RC control link and emergency override
- Battery and charger
- Laptop for backend, dashboard, model training, and image processing
- Ground markers for controlled navigation tests
- Gazebo simulation setup for orchard terrain and multi-tree navigation

Recommended improved prototype:

- PX4-compatible or ArduPilot-compatible drone
- Companion computer
- GPS module
- Optional RTK GPS
- Optional depth camera or LiDAR
- Optional gimbal
- Telemetry radio
- Extra batteries
- Dataset backup storage

## 5. Recommended First Purchase or Build Priority

Suggested order:

1. Confirm access to a citrus farm or test trees.
2. Define tree registration fields for the website.
3. Collect raw citrus fruit images manually using a phone or camera.
4. Label fruit bounding boxes and harvest-readiness classes.
5. Train a baseline citrus fruit detection model.
6. Build the web dashboard and database schema.
7. Start with manual-assisted drone image capture.
8. Add circular scan planning around a tree.
9. Add autonomous navigation to selected tree locations.
10. Build Gazebo simulation for orchard terrain, trees, obstacles, and repeated map updates.
11. Integrate drone capture, AI results, map, and dashboard.

## 6. Current Estimated Cost Summary

The cost table is now intentionally marked as TBD because the hydroponic tower parts have been removed and the final drone platform has not yet been selected.

| Category | Estimated Total |
| --- | ---: |
| Citrus farm data collection tools | PHP 250-2,800 estimate |
| Drone platform and camera | TBD |
| Mapping, navigation, and safety hardware | TBD |
| Development and backend equipment | TBD |
| Current project total | TBD |

Notes:

- The previous hydroponic tower subtotal is no longer applicable.
- The old CogniFly-inspired bill of materials should not be treated as final for outdoor citrus orchard work.
- Final cost depends mainly on the selected drone platform, camera, GPS accuracy requirements, and whether LiDAR, RTK GPS, or a gimbal will be included.
- Shipping fees, replacement parts, batteries, and safety equipment should be included before final procurement.

## 7. Safety Notes

Outdoor drone testing near citrus trees requires careful safety planning.

Required or strongly recommended:

- Manual override control
- Emergency stop or return-to-home behavior
- Safe launch and landing area
- Clear testing boundary
- Visual observer during field tests
- Flight testing away from people and animals
- Weather and wind checks before flight
- Battery safety procedures
- Permission from farm owner or site manager

Operational cautions:

- Do not fly too close to branches during early tests.
- Start with manual-assisted capture before full autonomy.
- Test circular scan paths in simulation first.
- Use slow movement near trees.
- Keep altitude and distance limits conservative.
- Document failed scans and low-confidence results.
