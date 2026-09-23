# Hardware Requirements

## Overview

This document focuses on the drone inspection hardware needed for the modified CogniFly-inspired drone, as well as the structural frame required for testing. Functional hydroponic plumbing and growing supplies are intentionally excluded.

## Structural Frame Setup (Physical Target)

The project requires a physical target for the drone to scan. Since functional hydroponics are not required for the computer vision validation, a simplified physical setup is used:
- **Hydroponic Tower Frame:** A downloadable 3D-printable or DIY structural frame.
- **Purpose:** Serves strictly as a physical structure to hold the lettuce and empty pots, acting as a visual target for the drone to detect slots and plants in an open space.
- **Features:** Does not require water pumps or plumbing. The tower will have its GPS coordinates recorded in the dashboard.

## Drone Hardware and Electronics

| Device | Link | Price | Quantity |
| --- | --- | ---: | ---: |
| CogniFly-based 3D-printable drone frame STL files | <https://github.com/thecognifly/CogniFly-STL> | TBD | 1 |
| SpeedyBee F405 Mini Stack, FC + BLS 35A 4-in-1 ESC | [Shopee](https://shopee.ph) | PHP 5,342 | 1 |
| CADDXFPV 1303 6000KV 2-4S brushless motors | [Banggood](https://ph.banggood.com) | PHP 3,609.07 | 4 |
| Gemfan Hurricane 3018 3x1.8 3-inch 2-blade propellers, 1.5mm hole T-mount | [Banggood](https://ph.banggood.com) | PHP 168.15 | 4 pairs |
| Raspberry Pi Zero 2 W | [Cytron](https://www.cytron.io) | PHP 2,000 estimate | 1 |
| Raspberry Pi Camera Module V2 | [Markerlab](https://makerlab.ph) | PHP 2,299 | 1 |
| Raspberry Pi Zero camera ribbon cable | TBD | PHP 80-200 estimate | 1 |
| HGLRC M100-5883 GPS + Compass Module | [Shopee](https://shopee.ph) | PHP 1050  | 1 (required for GPS tower alignment) |
| 4G LTE Cellular HAT module (e.g., Waveshare SIM7600) | TBD | ~PHP 2,000 estimate | Optional (for Cloud GPU offloading) |
| LiPo battery, 3S 11.1V 650mAh 75C, XT30 | [AliExpress](https://www.aliexpress.com) | PHP 1005 | 3 (minimum for field testing) |
| LiPo battery charger | [Shopee](https://shopee.ph) | PHP 625 | 1 |
| 5V voltage regulator / BEC for Raspberry Pi | [Amazon](https://www.amazon.com) | PHP 609 | 1 |
| RC transmitter and receiver / control link | [Shopee](https://shopee.ph) | PHP 3850 estimate | 1 |
| TPU 95A filament for protective frame | TBD | PHP 700-1,200 estimate | 1 kg spool |
| PLA or ABS filament for rigid plates | TBD | PHP 600-1,000 estimate | 1 kg spool |
| M2 screws, nuts, standoffs, and rubber rings | TBD | PHP 150-500 estimate | TBD |

*(Note: Obstacle avoidance sensors like Front Time-of-Flight or LiDAR have been explicitly removed from the hardware list, as the drone will operate in an open, obstacle-free space.)*

## Drone Inspection Hardware

The focus here is on the modified CogniFly-based 3D-printable drone platform, its onboard electronics, and the hardware needed for field deployment.

Reference repositories:
- CogniFly project page: <https://thecognifly.github.io/>
- CogniFly STL files: <https://github.com/thecognifly/CogniFly-STL>

### Onboard Computer
Required board:
- Raspberry Pi Zero 2 W
Why this board:
- Quad-core ARM Cortex-A53 provides required processing power to prevent severe frame drops and lag when streaming live camera frames to the backend while simultaneously handling MSP serial communication.

### Camera
Recommended camera:
- Raspberry Pi Camera Module V2

### Navigation Sensors
Required for outdoor open-space deployment:
- **HGLRC M100-5883 GPS + Compass Module** (~PHP 1,050) — provides stable outdoor altitude hold, position hold, and precise navigation to the hydroponic tower's GPS coordinates.

### Battery and Power
Required components:
- LiPo battery, 3S 11.1V 650mAh or 850mAh 75C, XT30
- Battery charger
- XT30 battery connector or adapter
- 5V voltage regulator or BEC for Raspberry Pi

## Known Constraints and Deployment Caveats

### Software and Firmware Architecture Decision
The source-of-truth firmware path for this project is **ArduPilot/ArduCopter on the SpeedyBee F405 Mini**.

This choice matches the project overview because ArduPilot provides MAVLink telemetry, autonomous mission support, companion-computer integration, and GPS support. These features are required for the simplified thesis architecture: GPS target approach paths, vertical tower scanning behavior, synchronized camera/telemetry capture, and dashboard mission states.

**Current ArduPilot path:**
- Flash **ArduPilot/ArduCopter** onto the SpeedyBee F405 Mini.
- Use MAVLink telemetry between the flight controller, Raspberry Pi Zero 2 W, ground laptop, and/or backend.
- Use the Raspberry Pi Zero 2 W for image capture, timestamping, lightweight telemetry handling, and data upload.
- Offload YOLOv8 and heavy post-processing to a ground laptop for the thesis MVP.
- Program autonomous GPS waypoints for the drone to align with the hydroponic tower and perform a vertical scan.

## Minimum Hardware Build

Minimum realistic physical prototype:
- Modified CogniFly-based 3D-printable drone frame
- SpeedyBee F405 Mini flight controller
- ArduPilot/ArduCopter firmware
- 4x CADDXFPV 1303 6000KV 2-4S brushless motors
- BLS 35A 4-in-1 ESC
- Raspberry Pi Zero 2 W
- Raspberry Pi Camera Module V2
- HGLRC M100-5883 GPS + Compass Module
- Gemfan Hurricane 3018 3x1.8 propellers
- LiPo battery, 3S 11.1V 650mAh (minimum 3 batteries)
- Battery and charger
- 5V voltage regulator or BEC for Raspberry Pi
- RC transmitter and receiver
- Computer/laptop for backend and field operation
- **Hydroponic Tower Structural Frame** (Physical testing target)

## Estimated Cost Summary

| Category | Estimated Total |
| --- | ---: |
| Drone hardware selected/required subtotal (base) | PHP 22,556.22–25,326.22 |
| HGLRC M100-5883 GPS + Compass (required for tower alignment) | ~PHP 1,050 |
| Extra LiPo batteries — 2 additional units for field testing | ~PHP 2,008–2,400 |
| **Revised estimate** | **~PHP 25,614–28,776** |

Notes:
- The estimate excludes the cost of the structural tower frame and lettuce/pots, which can be acquired or built separately.
