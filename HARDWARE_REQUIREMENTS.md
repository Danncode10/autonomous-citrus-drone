# Hardware Requirements

## Overview

This document focuses only on the drone inspection hardware needed for the modified CogniFly-inspired drone. Hydroponic tower components, growing supplies, and related non-drone items are intentionally excluded.

## Drone Hardware and Electronics

| Device | Link | Price | Quantity |
| --- | --- | ---: | ---: |
| CogniFly-based 3D-printable drone frame STL files | <https://github.com/thecognifly/CogniFly-STL> | TBD | 1 |
| SpeedyBee F405 Mini Stack, FC + BLS 35A 4-in-1 ESC | [Shopee, choose option "Stack"](https://shopee.ph/product/709543365/25756157647?gads_t_sig=gqRjZGVrxHCFomtpsTE0MjUxOnRzc19zZGtfa2V5omt20QABpGFsZ2_SAAAAZKNkZWvAomN0xEAAAAAMHJtu46N4YL1ETOwWAbpdPCpoOnQDXHQJ5OvtcN0M_eDbRA41r_846ydnLzTRf_samdRHEh2GSlumtjiKqmNpcGhlcnRleHTEbgAAAAw8-UEATWkahzAjSTPjL3YTk89P96JpeyADKv9kpXsKLDIuOsN7QnyVuzBF07NUqKrX7yBNGbBHa3YFB3__8U178RSXZV9-K4ZgQ25TximiGqVyhasgJPSPiDdVL0toBxqEK89MpmU4AUuB&gad_source=1&gad_campaignid=23303611172&gbraid=0AAAAADPpU9BKk0LBc6FmkMD8t9HzhJLcU&gclid=EAIaIQobChMIx-SH2ZKHlgMVKhx7Bx1VxhrhEAQYASABEgKlXfD_BwE) | PHP 5,342 | 1 |
| CADDXFPV 1303 6000KV 2-4S brushless motors | [Banggood, 4pcs already](https://ph.banggood.com/1-or-4PCS-CADDXFPV-1303-6000KV-2-4S-Brushless-Motors-1_5mm-Shaft-for-Gofilm-20-2-Inch-Brushless-Whoop-RC-FPV-Racing-Drone-p-2017084.html?rmmds=search&act_poa=POA10879739&cur_warehouse=CN&tags=searchListProductcard&bid=84561&forced_jump=1&xpath=0000000DL&page_id=bgm_search-list&uet=1785854062946&is_wap=1&user_id=1563232186965&sess_id=1563232186965&site=ph-m.banggood.com&position_type=2&ID=6291971529815) | PHP 3,609.07 | 4 |
| Gemfan Hurricane 3018 3x1.8 3-inch 2-blade propellers, 1.5mm hole T-mount | [Banggood](https://ph.banggood.com/4-Pairs-or-20-Pairs-Gemfan-Hurricane-3018-3x1_8-3-Inch-2-Blade-Propeller-1_5mm-Hole-T-Mount-for-RC-Drone-FPV-Racing-p-1576078.html?cur_warehouse=CN&ID=5173886313661&rmmds=search) | PHP 168.15 | 4 pairs |
| Raspberry Pi Zero 2 W (~~Raspberry Pi Zero W~~ not allowed) | Always out of Stock: Get Notified Here [Cytron](https://www.cytron.io/p-raspberry-pi-zero-2-w?currency=PHP&src=raspberrypi), [Element 14](https://ph.element14.com/raspberry-pi/rpi-zero-w-v2/raspberry-pi-kit-64bit-arm-cortex/dp/3838499?rd=raspberry+pi+zero+2+w&ost=Raspberry+Pi+Zero+2+W), [pishop](https://www.pishop.ca/product/raspberry-pi-zero-2-w-with-header/) | PHP 2,000 estimate | 1 |
| Raspberry Pi Camera Module V2 | [Markerlab](https://makerlab.ph/products/raspberry-pi-camera-module-v2-8-megapixels?variant=42288085401791&country=PH&currency=PHP&utm_medium=product_sync&utm_source=google&utm_content=sag_organic&utm_campaign=sag_organic&gad_source=1&gad_campaignid=23272569557&gbraid=0AAAAADiCHt1xiQslFpC1l-f3CRMHsFRci&gclid=EAIaIQobChMI6vr93buIlgMVFcFMAh03UylvEAQYASABEgKPBvD_BwE) | PHP 2,299 | 1 |
| Raspberry Pi Zero camera ribbon cable | TBD | PHP 80-200 estimate | 1 |
| HGLRC M100-5883 GPS + Compass Module | [Shopee](https://shopee.ph/product/779642846/29163602209?gads_t_sig=gqRjZGVrxHCFomtpsTE0MjUxOnRzc19zZGtfa2V5omt20QABpGFsZ2_SAAAAZKNkZWvAomN0xEAAAAAMHJtu46N4YL1ETOwWAbpdPCpoOnQDXHQJ5OvtcN0M_eDbRA41r_846ydnLzTRf_samdRHEh2GSlumtjiKqmNpcGhlcnRleHTEbgAAAAzDnclO7-bMvX3rynRr0XNyi6EqPr_u0c6t2cJ3FOANFzVs0_vNFl8pkFIOBgI4so46sTu_VmOcjIW0CptTtBBRrOsH90Aqof5m34qISUQtbB8u82P0DD0wKIVX9KOlhEsYPANCTI83SeKj&gad_source=1&gad_campaignid=23914051368&gbraid=0AAAAADPpU9BqsdEdCGNu0Tf1Xt_d5j_21&gclid=EAIaIQobChMI35btz5KOlgMVusRMAh3yvBsAEAQYAiABEgIUnPD_BwE) | PHP 1050  | 1 (required for outdoor deployment) |
| 4G LTE Cellular HAT module (e.g., Waveshare SIM7600) | TBD | ~PHP 2,000 estimate | Optional (required for commercial Cloud GPU offloading) |
| Front Time-of-Flight distance sensor | TBD | PHP 150-600 estimate | Optional |
| LiPo battery, 3S 11.1V 650mAh 75C, XT30 | [AliExpress](https://www.aliexpress.com/item/1005007414258002.html?spm=a2g0o.productlist.main.1.31ffuVZxuVZxao&algo_pvid=3d3c94d0-354a-4514-b863-ad752640e064&algo_exp_id=3d3c94d0-354a-4514-b863-ad752640e064-0&pdp_ext_f=%7B%22order%22%3A%2214%22%2C%22eval%22%3A%221%22%2C%22fromPage%22%3A%22search%22%7D&pdp_npi=6%40dis%21PHP%211004.19%211004.19%21%21%2115.99%2115.99%21%400bafc98f17859036007364756e10c2%2112000040653925601%21sea%21PH%210%21ABX%211%210%21n_tag%3A-29910%3Bd%3Affa3ea66%3Bm03_new_user%3A-29895&curPageLogUid=D1YWUTrVIgkd&utparam-url=scene%3Asearch%7Cquery_from%3A%7Cx_object_id%3A1005007414258002%7C_p_origin_prod%3A) | PHP 1005 | 3 (minimum for field testing) |
| LiPo battery charger | [Shopee](https://shopee.ph/product/933050849/22523275057?gads_t_sig=gqRjZGVrxHCFomtpsTE0MjUxOnRzc19zZGtfa2V5omt20QABpGFsZ2_SAAAAZKNkZWvAomN0xEAAAAAMHJtu46N4YL1ETOwWAbpdPCpoOnQDXHQJ5OvtcN0M_eDbRA41r_846ydnLzTRf_samdRHEh2GSlumtjiKqmNpcGhlcnRleHTEbgAAAAzt6xHLEel2tixnsm8WgqWDeM7uDzf7iAlc3cFMeLMQOeQxMxoKHdcQobCjOBjOE9j1ExFvvjWLVuSmA0A-0vwQ9jNbPR2T3ok58rVVUGKHb20lh3gm9hZQs1Px3G2UuFdKQAHxjK04aArg&gad_source=1&gad_campaignid=23303611172&gbraid=0AAAAADPpU9AlH-1_7NH_qcuCnpfVm2Vzb&gclid=EAIaIQobChMI24rG3tGIlgMVRF8PAh2YoDaJEAQYASABEgJjtfD_BwE) | PHP 625 | 1 |
| 5V voltage regulator / BEC for Raspberry Pi | [Amazon](https://www.amazon.com/Module-Quadcopter-Airplane-Servo-Model/dp/B0D97FH1JS/ref=sr_1_1?crid=1S0FWBEGH4I1E&dib=eyJ2IjoiMSJ9.B69bMzHFave2f719qjB8FAEhxFicLXnzucNs-w1iQCgA6KtGndpZjc0mhZ83iFxqTWKB5S_3ZQqmX1EUFbWE9Kr-0mpG1SjWIfHZjpRbpyfofe86-vaTpx7CIb2heEYjQwIuCRgiOcv_HgVy9K189U8H7SJgYeHIvcStgLXGL7hBPkBX7mcIvvRIz0GdfeAXx4BOmEhSvyMBwuf7fHbcMQdbRwrW3P2dlUt01VUxTp0.bo7M3DXeiUGe7qUBevqWMpXpODW3kXBb_PpKJFPX6S0&dib_tag=se&keywords=5V+5A+BEC+2S+6S+drone&qid=1785904092&sprefix=5v+5a+bec+2s+6s%2Caps%2C788&sr=8-1) | PHP 609 | 1 |
| RC transmitter and receiver / control link — replace bundled FS-iA6B receiver with FlySky FS-A8S or FS-X6B (smaller, lighter, micro-stack compatible) | [Shopee, choose "mode2 i6X with A8S" or "mode2 i6X with X6B"](https://shopee.ph/Flysky-FS-i6X-10CH-2.4GHz-AFHDS-2A-RC-Transmitter-With-FS-iA6B-FS-iA10B-FS-X6B-FS-A8S-Receiver-For-Rc-Airplane-i.779642846.21405448162) | PHP 3850 estimate | 1 |
| TPU 95A filament for protective frame | TBD | PHP 700-1,200 estimate | 1 kg spool |
| PLA or ABS filament for rigid plates | TBD | PHP 600-1,000 estimate | 1 kg spool |
| 3mm carbon fiber rods or bamboo skewers for frame struts | TBD | PHP 100-600 estimate | TBD |
| M2 screws, nuts, standoffs, and rubber rings | TBD | PHP 150-500 estimate | TBD |
| Propeller guards / protective frame | TBD | TBD | Optional / custom printed |
| XT30 connector, battery strap, and zip ties | TBD | PHP 150-400 estimate | 1 set |
| Drone hardware selected/required subtotal, excluding optional front ToF and propeller guards | TBD | PHP 22,556.22-25,326.22 estimate | TBD |

## Drone Inspection Hardware

The drone inspection system is the part of the project being prioritized. The focus here is on the modified CogniFly-based 3D-printable drone platform, its onboard electronics, and the hardware needed for field deployment.

Reference repositories:

- CogniFly project page: <https://thecognifly.github.io/>
- CogniFly STL files: <https://github.com/thecognifly/CogniFly-STL>
- CogniFly Python control: <https://github.com/thecognifly/cognifly-python>

### Drone Frame and Mechanical Parts

Required components:

- 3D-printed drone frame
- 3D-printed protective frame or bumper
- Custom 3D-printed motor mounts for CADDXFPV 1303 motors
- Battery holder
- Flight controller mount
- Raspberry Pi mount
- Camera mount
- Landing gear or landing supports
- TPU 95A filament for flexible/protective parts
- PLA or ABS filament for rigid plates
- 3mm rods or spars for frame structure
- Screws, nuts, standoffs, and fasteners

Optional components:

- 3D-printed prop guards
- 3D-printed sensor mounts
- 3D-printed cable guides
- Rubber vibration dampers
- Foam padding for protection
- Modular payload bay

### Flight Hardware

Required components:

- SpeedyBee F405 Mini flight controller from the SpeedyBee F405 Mini Stack
- ArduPilot/ArduCopter firmware on the SpeedyBee F405 Mini
- 4x CADDXFPV 1303 6000KV 2-4S brushless motors
- Gemfan Hurricane 3018 3x1.8 3-inch 2-blade propellers, 1.5mm hole T-mount
- Included BLS 35A 4-in-1 ESC from the SpeedyBee F405 Mini Stack
- Power distribution wiring or board
- Battery connector
- RC receiver or control link

Optional components:

- Spare propellers
- Spare motors
- Spare ESCs
- Propeller guards
- Telemetry module
- Buzzer or lost-drone beeper
- Status LEDs

### Onboard Computer

Required board:

- Raspberry Pi Zero 2 W (~~Raspberry Pi Zero W~~ - single-core ARMv6 is insufficient)

Why this board:

- Quad-core ARM Cortex-A53 provides required processing power to prevent severe frame drops and lag when streaming live camera frames to the backend while simultaneously handling MSP serial communication
- Small and lightweight
- Has Wi-Fi
- Supports Raspberry Pi Camera
- Can run Python and OpenCV
- Suitable for marker detection and image capture

### Camera

Recommended camera:

- Raspberry Pi Camera Module V2

Optional alternatives:

- Raspberry Pi Camera Module 3 with autofocus
- USB webcam
- Arducam autofocus camera
- Small FPV camera

### Navigation and Obstacle Sensors

Recommended for indoor and low-light environments:

- Matek Optical Flow & Lidar Sensor 3901-L0X (indoor only — the VL53L0X ToF rangefinder is saturated by ambient sunlight, reducing usable range from ~2m indoors to under 0.5m in bright daylight)

Required for outdoor and farm deployment:

- HGLRC M100-5883 GPS + Compass Module (~PHP 1,050) — provides stable outdoor altitude hold, position hold, and Return-To-Home capability

Additional recommended sensor:

- Front Time-of-Flight or LiDAR distance sensor (for obstacle avoidance)

### Battery and Power

Required components:

- LiPo battery, 3S 11.1V 650mAh or 850mAh 75C, XT30 — minimum 3 batteries recommended for field operations; a single battery provides approximately 3–4 minutes of flight time; the 850mAh option adds ~15g but extends flight time to approximately 5–6 minutes per charge
- Battery charger
- XT30 battery connector or adapter
- 5V voltage regulator or BEC for Raspberry Pi

### Communication

Required components:

- Wi-Fi connection from Raspberry Pi to laptop/backend
- Control link for drone operation, safety override, and setup

Optional components:

- 4G LTE Cellular HAT module (e.g., Waveshare SIM7600 series) for commercial scaling and cloud GPU offloading
- RC transmitter and receiver
- Telemetry radio
- Bluetooth module
- Ground station laptop

### Safety Hardware

Required or strongly recommended:

- Propeller guards or protective frame
- Emergency stop method
- Manual override control
- Designated safe operating area
- Spare propellers

## Known Constraints and Deployment Caveats

### Outdoor Sensor Limitation

The Matek 3901-L0X uses a VL53L0X Time-of-Flight (ToF) rangefinder that operates on 940nm infrared light. This sensor is designed for indoor environments only. In direct sunlight, ambient infrared light saturates the sensor and its usable range drops from approximately 2 meters indoors to under 0.5 meters outdoors.

**Impact for citrus farm deployment:** Flying over uneven citrus tree canopies, the drone will lose its height reference and drift or crash without a GPS module providing position hold.

**Required fix for outdoor deployment:** Add an HGLRC M100-5883 GPS + Compass Module (~PHP 1,050). The 3901-L0X remains valid for indoor and low-light environments only.

### Software and Firmware Architecture Decision

The source-of-truth firmware path for this project is **ArduPilot/ArduCopter on the SpeedyBee F405 Mini**.

This choice matches the RRL and project overview because ArduPilot provides MAVLink telemetry, autonomous mission support, companion-computer integration, rangefinder/GPS support, Lua scripting, and a direct Gazebo SITL workflow through `ardupilot_gz`. These features are required for the thesis architecture: registered-tree missions, circular scan behavior, synchronized camera/telemetry capture, simulation validation, and dashboard mission states.

**Current ArduPilot path:**

- Flash **ArduPilot/ArduCopter** onto the SpeedyBee F405 Mini
- Use MAVLink telemetry between the flight controller, Raspberry Pi Zero 2 W, ground laptop, and/or backend
- Use the Raspberry Pi Zero 2 W for image capture, timestamping, lightweight telemetry handling, and data upload
- Offload ROS 2, YOLO, duplicate-count reduction, and heavy post-processing to a ground laptop for the thesis MVP
- Use Gazebo Sim with ArduPilot SITL and `ardupilot_gz` for autonomous mission testing before real-world flights

**Optional early validation only:**

- Manual RC hover and safety tests may be performed under ArduPilot/ArduCopter before full autonomous integration

**Not the current plan:**

- PX4 is not selected for the present hardware path because it would likely require an H7-class flight controller swap and additional integration cost
- Full ROS 2 and YOLO inference will not run onboard the Raspberry Pi Zero 2 W because its 512MB RAM and thermal envelope are too limited for reliable sustained processing

### RC Receiver Size Constraint

The FlySky FS-iA6B bundled with the standard i6X kit is designed for 5-inch freestyle quads and RC aircraft. At approximately 15g and 40×25×15mm, it is too large and heavy for the CogniFly 20×20mm micro-stack.

**Recommended replacement:** FlySky FS-A8S or FlySky FS-X6B — significantly smaller and lighter while remaining fully compatible with the FlySky i6X transmitter over IBUS or SBUS. Alternatively, ExpressLRS 2.4GHz (e.g., RadioMaster RP1) offers superior link reliability in dense foliage environments.

### All-Up Weight and Estimated Flight Time

| Component | Estimated Weight |
| --- | ---: |
| CogniFly TPU frame | ~90g |
| SpeedyBee F405 Mini Stack | ~14g |
| 4x CADDXFPV 1303 motors | ~26g |
| Raspberry Pi Zero 2 W + Camera | ~15g |
| 3S 650mAh LiPo battery | ~60g |
| BEC, wiring, and hardware | ~20g |
| **Estimated All-Up Weight (AUW)** | **~225g–240g** |

Motor thrust estimate: 1303 6000KV motors with 3018 props on 3S produce approximately 120g–140g max thrust per motor, approximately 500g total maximum thrust.

Estimated thrust-to-weight ratio: approximately **2.1:1** — flyable but with limited safety margin.

**Estimated flight time per battery: 3–4 minutes.** A minimum of 3 batteries is strongly recommended for field operations. Using 850mAh batteries adds approximately 15g but extends flight time to approximately 5–6 minutes per charge.

## Minimum Hardware Build

Minimum realistic physical prototype:

- Modified CogniFly-based 3D-printable drone frame
- SpeedyBee F405 Mini flight controller from the SpeedyBee F405 Mini Stack
- ArduPilot/ArduCopter firmware
- 4x CADDXFPV 1303 6000KV 2-4S brushless motors
- Included BLS 35A 4-in-1 ESC from the SpeedyBee F405 Mini Stack
- Raspberry Pi Zero 2 W (~~Raspberry Pi Zero W~~ - single-core ARMv6 is insufficient)
- Raspberry Pi Camera Module V2
- Raspberry Pi Zero camera ribbon cable
- Matek Optical Flow & Lidar Sensor 3901-L0X (indoor use only)
- HGLRC M100-5883 GPS + Compass Module (required for outdoor deployment)
- Gemfan Hurricane 3018 3x1.8 propellers
- LiPo battery, 3S 11.1V 650mAh or 850mAh 75C, XT30 (minimum 3 batteries for field operations)
- Battery and charger
- 5V voltage regulator or BEC for Raspberry Pi
- RC transmitter and receiver or equivalent control link
- TPU 95A filament, PLA/ABS filament, 3mm rods, and fasteners for the drone frame
- Computer/laptop for backend and field operation

## Estimated Cost Summary

| Category | Estimated Total |
| --- | ---: |
| Drone hardware selected/required subtotal (base) | PHP 22,556.22–25,326.22 |
| HGLRC M100-5883 GPS + Compass (required for outdoor deployment) | ~PHP 1,050 |
| Extra LiPo batteries — 2 additional units for field testing | ~PHP 2,008–2,400 |
| Optional front Time-of-Flight distance sensor | PHP 150–600 |
| Propeller guards / protective frame | TBD |
| **Outdoor-ready revised estimate** | **~PHP 25,914–29,526** |

Notes:

- The base drone subtotal includes the selected flight stack, motors, propellers, Raspberry Pi, camera, Pi Zero camera cable, Matek 3901-L0X, 3S LiPo battery, charger, 5V BEC, RC transmitter/receiver, filament estimates, rods/skewers, fasteners, XT30 connector, battery strap, and zip ties. The outdoor-ready revised estimate additionally includes the HGLRC M100-5883 GPS + Compass Module and 2 extra LiPo batteries for field operations.
- Shipping fees, vouchers, replacement parts, and price changes are not included.
