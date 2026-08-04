# Hardware Requirements

## Overview

This document lists the hardware needed for the automated hydroponic tower health check project. The hardware is separated into two main systems:

1. Hydroponic tower system
2. Drone inspection system

The physical prototype will use one real hydroponic tower and one 3D-printable CogniFly-based drone. The larger multi-tower farm scenario will be tested in Gazebo simulation.

## 1. Hydroponic Tower Hardware

The hydroponic tower is the physical crop-growing system. It will hold lettuce plants and provide the real images and sensor readings used by the drone and web dashboard.

### 1.1 Tower Structure

Required components:

- Vertical tower body or PVC pipe
- Plant holes or plant ports
- Net cups
- Tower base or support stand
- Reservoir lid or tower mounting plate
- Tubing from pump to tower top
- Return path for water back to reservoir

Optional components:

- 3D-printed plant cup holders
- 3D-printed tower brackets
- Modular tower sections
- Waterproof inspection labels
- Cable clips or wire guides

### 1.2 Growing Components

Required components:

- Lettuce seeds or seedlings
- Growing medium
- Hydroponic nutrient solution
- Clean water supply
- Net cups matched to the plant holes

Possible growing media:

- Rockwool cubes
- Coco peat
- Clay pebbles
- Perlite
- Sponge starter plugs

### 1.3 Water Circulation System

Required components:

- Reservoir tank
- Submersible water pump
- Water tubing
- Pump outlet fitting
- Water return path
- Pump power supply

Optional components:

- Pump timer
- Flow control valve
- Water filter
- Backup pump
- Check valve

### 1.4 Tower Sensors

The tower can work without sensors if the first prototype focuses only on computer vision. However, sensors are recommended because they make the system stronger and allow the dashboard to show nutrient and water status.

Recommended sensors:

- pH sensor
- EC/TDS sensor
- Water temperature sensor
- Water level sensor

Optional sensors:

- Air temperature sensor
- Humidity sensor
- Light intensity sensor
- Flow sensor
- Dissolved oxygen sensor
- Reservoir leak sensor

### 1.5 Tower Microcontroller

Recommended board:

- ESP32 development board

Why ESP32:

- Built-in Wi-Fi
- Low cost
- Good for sensor readings
- Can send data to the backend or website
- Easy to program using Arduino IDE, PlatformIO, or MicroPython

ESP32 responsibilities:

- Read pH value
- Read EC/TDS value
- Read water temperature
- Detect low water level
- Send sensor data to backend/database
- Optionally control pump schedule

Optional alternatives:

- Arduino Uno with Wi-Fi module
- Raspberry Pi Pico W
- ESP8266
- Raspberry Pi

### 1.6 Tower Identification and Mapping

Required components:

- QR code or ArUco marker for tower identification
- Printed tower ID label
- Waterproof marker covering or lamination

Purpose:

- Allows the drone to identify which tower it is inspecting
- Helps the drone determine tower orientation
- Helps map captured images to the correct tower and plant slot

Optional components:

- Marker per tower face
- Marker per inspection side
- Slot labels
- Color-coded plant slot markers

### 1.7 Lighting

Required if indoor lighting is weak:

- LED grow lights or white LED inspection lights
- Light power supply
- Light mounting bracket

Optional components:

- Timer-controlled grow lights
- Dimmable LED lights
- Diffusers to reduce harsh shadows
- Ring light or inspection light mounted near the camera

### 1.8 Power and Safety

Required components:

- Pump power supply
- Safe cable routing
- Waterproof or splash-resistant wire protection
- Power strip or outlet with protection

Recommended safety components:

- Drip loop for cables
- Fuse or breaker
- Waterproof connectors
- Reservoir cover
- Non-slip base
- Emergency power switch

## 2. Drone Inspection Hardware

The drone inspection system captures images of lettuce plants, identifies tower markers, and supports basic navigation around the hydroponic tower.

The preferred direction is a **CogniFly-based 3D-printable drone**, adapted for hydroponic tower inspection.

Reference repositories:

- CogniFly project page: <https://thecognifly.github.io/>
- CogniFly STL files: <https://github.com/thecognifly/CogniFly-STL>
- CogniFly Python control: <https://github.com/thecognifly/cognifly-python>

### 2.1 Drone Frame and Mechanical Parts

Required components:

- 3D-printed drone frame
- 3D-printed protective frame or bumper
- Motor mounts
- Battery holder
- Flight controller mount
- Raspberry Pi mount
- Camera mount
- Landing gear or landing supports
- Screws, nuts, standoffs, and fasteners

Optional components:

- 3D-printed prop guards
- 3D-printed sensor mounts
- 3D-printed cable guides
- Rubber vibration dampers
- Foam padding for protection
- Modular payload bay

### 2.2 Flight Hardware

Required components:

- Flight controller compatible with the selected CogniFly setup
- 4 brushless or brushed motors, depending on chosen design
- 4 propellers
- ESCs if using brushless motors
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

### 2.3 Drone Onboard Computer

Recommended board:

- Raspberry Pi Zero 2 W

Why Raspberry Pi Zero 2 W:

- Small and lightweight
- More powerful than Raspberry Pi Zero W
- Has Wi-Fi
- Supports Raspberry Pi Camera
- Can run Python and OpenCV
- Suitable for QR/ArUco detection and image capture

Drone onboard computer responsibilities:

- Capture camera images
- Detect QR/ArUco markers
- Identify tower ID and orientation
- Send images to backend/server
- Communicate with drone control software
- Run simple inspection logic

Optional alternatives:

- Raspberry Pi Zero W
- Raspberry Pi 4
- Raspberry Pi 5
- Jetson Nano
- Jetson Orin Nano

Important note: Raspberry Pi 4, Raspberry Pi 5, and Jetson boards are more powerful, but they are heavier and use more power. For a small 3D-printable drone, weight is a major design constraint.

### 2.4 Camera

Recommended camera:

- Raspberry Pi Camera Module

Preferred options:

- Raspberry Pi Camera Module V2
- Raspberry Pi Camera Module 3 with autofocus

Camera responsibilities:

- Capture lettuce plant images
- Read QR/ArUco tower markers
- Support tower alignment and inspection workflow

Recommended camera requirements:

- Clear image at close range
- Stable mounting
- Good enough resolution for plant health classification
- Adjustable angle toward plant slots

Optional alternatives:

- USB webcam
- Arducam autofocus camera
- Small FPV camera
- Depth camera, if payload allows

### 2.5 Navigation and Obstacle Sensors

Recommended minimum sensors:

- Downward optical flow sensor
- Downward Time-of-Flight or range sensor
- Front Time-of-Flight or LiDAR distance sensor

Purpose:

- Improve indoor position holding
- Help maintain distance from the tower
- Detect obstacles in front of the drone
- Reduce collision risk near towers

Optional sensors:

- Side distance sensors
- Rear distance sensor
- Depth camera
- 360-degree LiDAR
- IMU expansion sensor
- Barometer

### 2.6 Battery and Power

Required components:

- LiPo battery compatible with the selected drone design
- Battery charger
- Battery connector
- Voltage regulator or power module for electronics

Recommended considerations:

- Keep the battery light enough for the drone to lift safely
- Use a battery with enough current output for motors
- Separate clean power for camera/computer if needed
- Monitor battery voltage during flight

Optional components:

- Extra batteries
- Battery voltage alarm
- Fire-resistant LiPo charging bag
- Power switch
- Battery strap

### 2.7 Communication

Required components:

- Wi-Fi connection from Raspberry Pi to laptop/backend
- Control link for drone operation

Optional components:

- RC transmitter and receiver
- Telemetry radio
- Bluetooth module
- Ground station laptop

Communication tasks:

- Send captured images to backend
- Send inspection status
- Receive control commands
- Monitor drone status during testing

### 2.8 Safety Hardware

Required or strongly recommended:

- Propeller guards or protective frame
- Emergency stop method
- Manual override control
- Safe test area
- Spare propellers

Optional components:

- Soft landing gear
- Protective net around test area
- Low-battery alarm
- Buzzer
- LED status indicators

## 3. Backend and Cloud Hardware Context

The cloud/backend is not a physical hardware category like the tower or drone, but it affects hardware decisions.

Recommended first setup:

- Laptop or desktop for development
- Local server or cloud backend
- Database
- Image storage

Suggested processing split:

- Drone Raspberry Pi captures images and detects tower markers.
- Backend or laptop runs heavier lettuce health AI model.
- ESP32 sends tower sensor readings to backend.
- Website displays plant health, tower status, and inspection history.

This avoids forcing the small drone computer to run heavy AI models during early development.

## 4. Minimum Hardware Build

Minimum realistic physical prototype:

- One hydroponic tower
- Lettuce plants
- Reservoir
- Pump
- Net cups
- Nutrient solution
- ESP32
- pH sensor
- EC/TDS sensor
- Water level sensor
- CogniFly-based 3D-printable drone frame
- Raspberry Pi Zero 2 W
- Raspberry Pi Camera Module
- Optical flow or range sensor
- Battery and charger
- Computer/laptop for backend, model training, and dashboard development

## 5. Recommended First Purchase or Build Priority

Suggested order:

1. Build the hydroponic tower.
2. Start growing lettuce.
3. Set up ESP32 sensors for water/nutrient monitoring.
4. Collect plant images using a phone or fixed camera.
5. Start training the computer vision model.
6. Build or adapt the CogniFly-based drone.
7. Add camera and marker detection.
8. Add basic distance sensing.
9. Integrate drone image capture with the backend.
10. Build Gazebo simulation for multi-tower navigation testing.
