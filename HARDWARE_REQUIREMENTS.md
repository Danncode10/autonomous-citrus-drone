# Hardware Requirements

## Overview

This document lists the hardware needed for the autonomous citrus tree inspection project focused on Perante orange. The system focuses on outdoor citrus orchards, drone-based scanning, visible fruit counting, tree-height estimation, orchard mapping, and Gazebo simulation.

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
| CogniFly-based 3D-printable drone frame STL files | [GitHub](https://github.com/thecognifly/CogniFly-STL) | TBD | 1 |
| SpeedyBee F405 Mini Stack, FC + BLS 35A 4-in-1 ESC | [Shopee](https://shopee.ph/product/709543365/25756157647?gads_t_sig=gqRjZGVrxHCFomtpsTE0MjUxOnRzc19zZGtfa2V5omt20QABpGFsZ2_SAAAAZKNkZWvAomN0xEAAAAAMHJtu46N4YL1ETOwWAbpdPCpoOnQDXHQJ5OvtcN0M_eDbRA41r_846ydnLzTRf_samdRHEh2GSlumtjiKqmNpcGhlcnRleHTEbgAAAAw8-UEATWkahzAjSTPjL3YTk89P96JpeyADKv9kpXsKLDIuOsN7QnyVuzBF07NUqKrX7yBNGbBHa3YFB3__8U178RSXZV9-K4ZgQ25TximiGqVyhasgJPSPiDdVL0toBxqEK89MpmU4AUuB&gad_source=1&gad_campaignid=23303611172&gbraid=0AAAAADPpU9BKk0LBc6FmkMD8t9NzhJLcU&gclid=EAIaIQobChMIx-SH2ZKHlgMVKhx7Bx1VxhrhEAQYASABEgKlXfD_BwE) | PHP 5,342 | 1 |
| CADDXFPV 1303 6000KV 2-4S brushless motors | [Banggood](https://ph.banggood.com/1-or-4PCS-CADDXFPV-1303-6000KV-2-4S-Brushless-Motors-1_5mm-Shaft-for-Gofilm-20-2-Inch-Brushless-Whoop-RC-FPV-Racing-Drone-p-2017084.html?rmmds=search&act_poa=POA10879739&cur_warehouse=CN&tags=searchListProductcard&bid=84561&forced_jump=1&xpath=0000000DL&page_id=bgm_search-list&uet=1785854062946&is_wap=1&user_id=1563232186965&sess_id=1563232186965&site=ph-m.banggood.com&position_type=2&ID=6291971529815) | PHP 3,609.07 | 4 |
| Gemfan Hurricane 3018 3x1.8 3-inch 2-blade propellers, 1.5mm hole T-mount | [Banggood](https://ph.banggood.com/4-Pairs-or-20-Pairs-Gemfan-Hurricane-3018-3x1_8-3-Inch-2-Blade-Propeller-1_5mm-Hole-T-Mount-for-RC-Drone-FPV-Racing-p-1576078.html?cur_warehouse=CN&ID=5173886313661&rmmds=search) | PHP 168.15 | 4 pairs |
| Raspberry Pi Zero W or Raspberry Pi Zero 2 W | [Cytron](https://www.cytron.io/p-raspberry-pi-zero-2-w?currency=PHP&src=raspberrypi), [Element 14](https://ph.element14.com/raspberry-pi/rpi-zero-w-v2/raspberry-pi-kit-64bit-arm-cortex/dp/3838499?rd=raspberry+pi+zero+2+w&ost=Raspberry+Pi+Zero+2+W), [pishop](https://www.pishop.ca/product/raspberry-pi-zero-2-w-with-header/) | PHP 2,000 estimate | 1 |
| Raspberry Pi Camera Module V2 | [Makerlab](https://makerlab.ph/products/raspberry-pi-camera-module-v2-8-megapixels?variant=42288085401791&country=PH&currency=PHP&utm_medium=product_sync&utm_source=google&utm_content=sag_organic&utm_campaign=sag_organic&gad_source=1&gad_campaignid=23272569557&gbraid=0AAAAADiCHt1xiQslFpC1l-f3CRMHsFRci&gclid=EAIaIQobChMI6vr93buIlgMVFcFMAh03UylvEAQYASABEgKPBvD_BwE) | PHP 2,299 | 1 |
| Raspberry Pi Zero camera ribbon cable | TBD | PHP 80-200 estimate | 1 |
| Matek Optical Flow & Lidar Sensor 3901-L0X | [Shopee](https://shopee.ph/product/779642846/23727761329) | PHP 1,920 | 1 |
| Front Time-of-Flight distance sensor | TBD | PHP 150-600 estimate | Optional |
| LiPo battery, 3S 11.1V 650mAh 75C, XT30 | [AliExpress](https://www.aliexpress.com/item/1005007414258002.html?spm=a2g0o.productlist.main.1.31ffuVZxuVZxao&algo_pvid=3d3c94d0-354a-4514-b863-ad752640e064&algo_exp_id=3d3c94d0-354a-4514-b863-ad752640e064-0&pdp_ext_f=%7B%22order%22%3A%2214%22%2C%22eval%22%3A%221%22%2C%22fromPage%22%3A%22search%22%7D&pdp_npi=6%40dis%21PHP%211004.19%211004.19%21%21%2115.99%2115.99%21%400bafc98f17859036007364756e10c2%2112000040653925601%21sea%21PH%21%210%21ABX%211%210%21n_tag%3A-29910%3Bd%3Affa3ea66%3Bm03_new_user%3A-29895&curPageLogUid=D1YWUTrVIgkd&utparam-url=scene%3Asearch%7Cquery_from%3A%7Cx_object_id%3A1005007414258002%7C_p_origin_prod%3A) | PHP 1,004 | 1+ |
| LiPo battery charger | [Shopee](https://shopee.ph/product/933050849/22523275057?gads_t_sig=gqRjZGVrxHCFomtpsTE0MjUxOnRzc19zZGtfa2V5omt20QABpGFsZ2_SAAAAZKNkZWvAomN0xEAAAAAMHJtu46N4YL1ETOwWAbpdPCpoOnQDXHQJ5OvtcN0M_eDbRA41r_846ydnLzTRf_samdRHEh2GSlumtjiKqmNpcGhlcnRleHTEbgAAAAzt6xHLEel2tixnsm8WgqWDeM7uDzf7iAlc3cFMeLMQOeQxMxoKHdcQobCjOBjOE9j1ExFvvjWLVuSmA0A-0vwQ9jNbPR2T3ok58rVVUGKHb20lh3gm9hZQs1Px3G2UuFdKQAHxjK04aArg&gad_source=1&gad_campaignid=23303611172&gbraid=0AAAAADPpU9AlH-1_7NH_qcuCnpfVm2Vzb&gclid=EAIaIQobChMI24rG3tGIlgMVRF8PAh2YoDaJEAQYASABEgJjtfD_BwE) | PHP 625 | 1 |
| 5V voltage regulator / BEC for Raspberry Pi | [Amazon](https://www.amazon.com/Module-Quadcopter-Airplane-Servo-Model/dp/B0D97FH1JS/ref=sr_1_1?crid=1S0FWBEGH4I1E&dib=eyJ2IjoiMSJ9.B69bMzHFave2f719qjB8FAEhxFicLXnzucNs-w1iQCgA6KtGndpZjc0mhZ83iFxqTWKB5S_3ZQqmX1EUFbWE9Kr-0mpG1SjWIfHZjpRbpyfofe86-vaTpx7CIb2heEYjQwIuCRgiOcv_HgVy9K189U8H7SJgYeHIvcStgLXGL7hBPkBX7mcIvvRIz0GdfeAXx4BOmEhSvyMBwuf7fHbcMQdbRwrW3P2dlUt01VUxTp0.bo7M3DXeiUGe7qUBevqWMpXpODW3kXBb_PpKJFPX6S0&dib_tag=se&keywords=5V+5A+BEC+2S+6S+drone&qid=1785904092&sprefix=5v+5a+bec+2s+6s%2Caps%2C788&sr=8-1) | PHP 609 | 1 |
| RC transmitter and receiver / control link | [Shopee](https://shopee.ph/Flysky-FS-i6X-10CH-2.4GHz-AFHDS-2A-RC-Transmitter-With-FS-iA6B-FS-iA10B-FS-X6B-FS-A8S-Receiver-For-Rc-Airplane-i.779642846.21405448162) | PHP 3,200-3,850 estimate | 1 |
| TPU 95A filament for protective frame | TBD | PHP 700-1,200 estimate | 1 kg spool |
| PLA or ABS filament for rigid plates | TBD | PHP 600-1,000 estimate | 1 kg spool |
| 3mm carbon fiber rods or bamboo skewers for frame struts | TBD | PHP 100-600 estimate | TBD |
| M2 screws, nuts, standoffs, and rubber rings | TBD | PHP 150-500 estimate | TBD |
| Propeller guards / protective frame | TBD | TBD | Optional / custom printed |
| XT30 connector, battery strap, and zip ties | TBD | PHP 150-400 estimate | 1 set |
| Drone hardware subtotal | TBD | PHP 22,556.22-25,326.22 estimate | TBD |

## GPS and Basic Safety Hardware

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
- Field notes for tree variety, manual fruit count references, and farmer observations

Optional components:

- GPS phone or handheld GPS for rough tree coordinates
- Color reference card for consistent image capture, if available

Purpose:

- Assign each citrus tree a stable identity
- Help compare drone-estimated height with manual measurement
- Help validate visible fruit count estimates
- Support dashboard tree registration and map placement

Why this is needed:

The drone can estimate visible fruit count and height, but the research still needs ground truth. For example, if the drone says a tree has 120 visible fruits, the team needs manual records or farmer observations to check whether the result is reasonable.

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
- Support fruit counting
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
- Backend or laptop runs fruit detection and visible fruit counting.
- Website stores tree registration and inspection results.
- Dashboard displays map, fruit count, height, images, and history.

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
4. Label fruit bounding boxes.
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
