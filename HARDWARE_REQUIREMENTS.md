# Hardware Requirements

## Overview

This document lists the hardware needed for the autonomous citrus tree inspection project focused on Perante orange. The system focuses on outdoor citrus orchards, drone-based scanning, fruit counting, harvest-readiness estimation, tree-height estimation, orchard mapping, and Gazebo simulation.

The hardware is separated into four main areas:

1. Field validation tools
2. Drone inspection system
3. GPS and basic safety equipment
4. Backend and development equipment

The physical prototype should start with a small number of citrus trees, specifically Perante orange trees, and supervised drone flights. The larger orchard scenario should be tested first in Gazebo simulation.

## Field Validation Tools

| Device | Link | Price | Quantity |
| --- | --- | ---: | ---: |
| Citrus tree labels or waterproof tags | TBD | PHP 50-300 estimate | TBD |
| Measuring tape or laser distance meter | TBD | PHP 100-1,500 estimate | 1 |
| Notebook or digital field form device | TBD | PHP 0-500 estimate | 1 |
| Field validation subtotal | TBD | PHP 150-2,300 estimate | TBD |

## Drone Hardware and Electronics

| Device | Link | Price | Quantity |
| --- | --- | ---: | ---: |
| GPS-enabled outdoor drone with camera and return-to-home | TBD | TBD | 1 |
| Extra drone battery | TBD | TBD | 1+ recommended |
| Battery charger | Included with drone / TBD | TBD | 1 |
| Spare propellers | TBD | TBD | 1 set |
| Optional camera gimbal, if not built in | TBD | TBD | Optional |
| Optional companion computer for advanced autonomy | TBD | TBD | Optional |
| Drone hardware subtotal | TBD | TBD | TBD |

## GPS and Basic Safety Hardware

| Device | Link | Price | Quantity |
| --- | --- | ---: | ---: |
| GPS-enabled drone or GPS module | TBD | TBD | 1 |
| Manual control link / return-to-home support | Included with drone / TBD | TBD | 1 |
| Landing pad or marked launch area | TBD | PHP 200-1,000 estimate | 1 |
| LiPo-safe charging bag or battery safety box | TBD | PHP 200-800 estimate | 1 |
| GPS and safety subtotal | TBD | TBD | TBD |

## Development and Backend Equipment

| Device | Link | Price | Quantity |
| --- | --- | ---: | ---: |
| Laptop or desktop for development | Existing / TBD | TBD | 1 |
| Local server or cloud backend | TBD | TBD | 1 |
| External storage for image dataset backup | TBD | PHP 500-3,000 estimate | Optional |
| Internet connection for dashboard and dataset sync | Existing / TBD | TBD | 1 |
| Development equipment subtotal | TBD | TBD | TBD |

## 1. Field Validation and Tree Identification Tools

This section is not a separate farm system. These are only the simple tools needed to label trees and validate whether the drone's estimates are correct.

Required components:

- Access to citrus trees, specifically Perante orange trees, in a farm or controlled outdoor test area
- Tree labels or waterproof tags
- Tree ID list
- Measuring tape or laser distance meter for manual height reference
- Field notes for tree variety, fruit maturity, and farmer observations

Optional components:

- GPS phone or handheld GPS for rough tree coordinates
- Color reference card for fruit maturity image calibration, if available

Purpose:

- Assign each citrus tree a stable identity
- Help compare drone-estimated height with manual measurement
- Help validate fruit count and harvest-readiness estimates
- Support dashboard tree registration and map placement

Why this is needed:

The drone can estimate fruit count, height, and readiness, but the research still needs ground truth. For example, if the drone says a tree has 120 visible fruits and is 65% ready to harvest, the team needs some manual records or farmer observations to check whether the result is reasonable.

## 2. Drone Inspection Hardware

The drone inspection system captures tree images, circles around the target tree, supports autonomous navigation, and contributes to map creation or map updates.

### 2.1 Drone Platform

Recommended direction:

- Use a GPS-enabled outdoor drone with a camera.
- Prefer a drone that already supports return-to-home, flight logs, manual override, and stable outdoor hover.
- A ready-to-fly drone is the best first prototype direction because it reduces custom hardware risk.

Important note:

Citrus tree inspection in a Perante orange orchard is an outdoor task with wind, terrain, larger distances, and tree branches. The main physical prototype should use a safe outdoor-capable drone rather than a small indoor-style drone.

Required platform capabilities:

- Stable outdoor hover
- Manual control and emergency override
- Integrated camera or secure camera mount
- GPS support
- Return-to-home support
- Enough battery life for tree approach, circular scan, and return
- Safe operation near trees
- Flight log or last-known-location support

Optional platform capabilities:

- Gimbal stabilization
- Obstacle avoidance sensors
- Waypoint mission support
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

Heavy fruit detection and model training can run on the laptop or backend during early development. The drone does not need to run the full AI model onboard in the first prototype, so a companion computer is optional.

### 2.4 GPS, Navigation, and Recovery

Recommended minimum:

- GPS-enabled drone or GPS module for outdoor waypoint navigation
- Return-to-home behavior
- Flight log or last-known-location recording
- Camera-based capture for visual inspection
- Manual control link for safety

Why GPS is the best minimum choice:

- It helps the drone navigate to registered tree locations.
- It allows return-to-home when signal or battery problems happen.
- It records the drone's last known location, which helps find the drone if something goes wrong.
- It is simpler and more realistic for the first prototype than LiDAR, RTK GPS, or full SLAM.

Not required for the first prototype:

- RTK GPS
- LiDAR
- Depth camera
- Telemetry radio
- Full SLAM mapping

These can be added later if the project needs more precise autonomy, but they are not required to prove the main research idea.

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

- Access to one or more citrus trees, specifically Perante orange trees
- Tree ID labels or waterproof tags
- Measuring tape or laser distance meter
- Outdoor-capable drone with camera
- GPS support or built-in GPS return-to-home
- Manual RC control link and emergency override
- Battery and charger
- Laptop for backend, dashboard, model training, and image processing
- Gazebo simulation setup for orchard terrain and multi-tree navigation

Recommended improved prototype:

- Waypoint-capable drone
- Optional companion computer
- Stronger GPS or RTK GPS
- Optional obstacle avoidance sensor
- Optional gimbal
- Extra batteries
- Dataset backup storage

## 5. Recommended First Purchase or Build Priority

Suggested order:

1. Confirm access to a citrus farm growing Perante orange or similar test trees.
2. Define tree registration fields for the website.
3. Collect raw citrus fruit images from Perante orange trees manually using a phone or camera.
4. Label fruit bounding boxes and harvest-readiness classes.
5. Train a baseline citrus fruit detection model for Perante orange.
6. Build the web dashboard and database schema.
7. Start with manual-assisted drone image capture.
8. Add circular scan planning around a tree.
9. Add autonomous navigation to selected tree locations.
10. Build Gazebo simulation for orchard terrain, trees, obstacles, and repeated map updates.
11. Integrate drone capture, AI results, map, and dashboard.

## 6. Current Estimated Cost Summary

The cost table is intentionally marked as TBD because the final drone platform has not yet been selected.

| Category | Estimated Total |
| --- | ---: |
| Field validation tools | PHP 150-2,300 estimate |
| Drone platform and camera | TBD |
| GPS and basic safety hardware | TBD |
| Development and backend equipment | TBD |
| Current project total | TBD |

Notes:

- Final cost depends mainly on the selected drone platform, camera, GPS support, and whether a gimbal will be included.
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
