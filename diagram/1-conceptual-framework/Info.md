
FIGURE 1: CONCEPTUAL FRAMEWORK:
Create a simple conceptual framework diagram (not a detailed architecture; that is Figure 5). Landscape, white background, black and one gray accent only, serif font (Cambria), rounded boxes with short labels, numbered arrows that match the order of the explanation in the text below the figure.
BLOCKS (left to right, top to bottom):
1. HYDROPONIC TOWER + TOWER UNIT: tower frame with lettuce, empty pots, and ArUco markers; tower unit = ESP32 + GPS module + e-paper QR display + Generate button.
2. FARMER + WEB APPLICATION: farmer's smartphone scans the QR code (tower ID, GPS coordinates, checksum) to register the tower and request a scan.
3. DATABASE (SUPABASE): stores towers, locations, scan missions, and results.
4. DRONE: flight controller (SpeedyBee F405 Mini, ArduPilot) + GPS/compass; Raspberry Pi Zero 2 W + Pi Camera V2 (records backup, streams video, visual alignment with QR + ArUco).
5. GROUND LAPTOP: live YOLOv8 detection (tower frame, lettuce, empty pot) -> slot matching by face, level, position -> slot availability; local offline cache.
6. WEB DASHBOARD: tower map, per-pot results, scan history, upload (Sync Center).
ARROWS (label each):
① Farmer -> Tower Unit: "press Generate" -> "QR with tower ID + location".
② Phone -> Web Application -> Database: "register tower / request scan".
③ Ground Laptop -> Drone: "mission (tower GPS, face A first)".
④ Drone -> Tower: "GPS approach -> YOLO tower detection -> QR/ArUco alignment -> full-tower scan, face by face, bottom to top".
⑤ Drone -> Ground Laptop: "live video + telemetry over local Wi-Fi"; dashed: "backup recording after landing (gap filling)".
⑥ Ground Laptop -> Database: dashed, "upload when internet is available".
⑦ Database -> Web Dashboard -> Farmer: "updated lettuce and empty pot counts per tower".
GROUPING:
• Draw a light dotted boundary labeled "Offline (local Wi-Fi)" around blocks 1, 4, and 5, and one labeled "Online (internet)" around blocks 3 and 6. Block 2 sits on the border.
OUTPUT FILE:
• SVG and 300 dpi PNG, about 16 cm wide. Do not draw the caption inside the image; the document caption is: Figure 1. Conceptual Framework of the Autonomous Hydroponic Tower Monitoring System.
