# Project Plan

## Project Direction

The project will focus on **visible fruit counting for Perante orange trees** using a drone-mounted camera, computer vision, orchard mapping, Gazebo simulation, and a web dashboard.

The main research scope is:

```text
Farmer creates an account
-> farmer registers farm, crop, trees, and drone profile
-> dashboard shows farm map and tree locations
-> farmer can prepare a drone scan mission from the UI
-> researcher uses reusable image dataset platform
-> researcher uploads or captures images
-> researcher draws bounding boxes around target objects
-> system saves annotation coordinates and metadata
-> system exports a YOLO-ready dataset
-> machine learning model detects visible citrus fruits
-> counting logic estimates visible fruit count
-> dashboard stores and displays tree-level results
```

The project will not focus on harvest readiness or ripeness estimation. That topic is broader and would require another set of labels, criteria, and validation methods.

## Main Goal

To first build the farmer-facing software platform, including account access, farm mapping, tree registration, drone registration, and scan mission UI, then build the reusable image dataset and annotation platform that will support training a computer vision model for visible Perante orange fruit counting.

## Core Components

### 1. Farmer Dashboard and Farm Mapping Platform

The first software priority should be the dashboard that farmers and researchers can actually use before the physical drone is completed. This dashboard becomes the central system where farms, trees, drones, scan requests, images, and AI results will eventually connect.

Main idea:

```text
Farmer account
-> farm registration
-> crop or fruit registration
-> tree registration
-> map location for each tree
-> drone registration
-> drone health and scan mission UI
-> scan records and fruit count results
```

Important note:

Some drone-related features can start as UI-only or simulated states while the drone is not yet built. For example, the dashboard can already show a "Start Drone Scan" button, drone battery status, GPS status, camera status, and mission status, even if those values are manually entered, mocked, or connected later.

Suggested farmer-facing pages:

- Sign in and account setup
- Farm profile
- Crop or fruit type management
- Orchard block management
- Tree registration
- Farm map view
- Drone registration
- Drone health panel
- Start drone scan screen
- Scan history
- Fruit count result view
- Alerts and failed scan view

Core dashboard features:

- Farmer can create an account.
- Farmer can register one or more farms.
- Farmer can register fruit or crop type, with Perante orange as the main target crop.
- Farmer can register individual trees with ID, name, variety, notes, and location.
- Farmer can place tree markers on a farm map.
- Farmer can register the drone profile, such as drone name, camera type, GPS support, and status.
- Farmer can open a drone health UI showing battery, GPS, camera, connection, storage, and mission readiness.
- Farmer can click a "Start Scan" or "Prepare Scan" button for a selected tree.
- System can show scan status such as pending, preparing, scanning, completed, failed, or needs rescan.
- System can display captured images and visible fruit count after processing.

Farm map options:

- Google Maps or Google Earth-style satellite map for a familiar farm view
- Leaflet with OpenStreetMap tiles for a free/open-source map option
- Mapbox for a polished custom map UI
- Manual farm sketch or local coordinate grid if GPS/map services are not available

Possible map features:

- Add tree marker
- Move tree marker
- Show selected tree details
- Show drone launch point
- Show planned route to tree
- Show circular scan path around the tree
- Show latest scan status per tree
- Use marker colors for not scanned, scanned, low confidence, or navigation blocked

Suggested database fields:

```text
users
- id
- name
- email
- role
- created_at

farms
- id
- user_id
- name
- location_name
- map_center_lat
- map_center_lng
- notes

crops
- id
- farm_id
- name
- variety
- notes

trees
- id
- farm_id
- crop_id
- tree_code
- tree_name
- latitude
- longitude
- local_x
- local_y
- approximate_height
- notes
- status

drones
- id
- farm_id
- drone_name
- camera_type
- gps_supported
- status
- battery_percent
- gps_status
- camera_status
- last_seen_at

scan_missions
- id
- farm_id
- tree_id
- drone_id
- status
- requested_by
- requested_at
- started_at
- completed_at
- notes
```

### 2. Reusable Dataset and Annotation Platform

Before training the fruit detection model, the project should first build a platform for collecting, organizing, labeling, reviewing, and exporting image datasets. This platform will be used for the Perante orange project, but it should be designed so it can also support future object-detection research.

Main idea:

```text
Upload or capture image
-> draw bounding boxes around objects
-> save box coordinates and image metadata
-> mark image as done or reviewed
-> export labels for machine learning training
```

Why this should come first:

- Machine learning needs labeled data before the model can be trained.
- Public datasets may not match local Perante orange trees.
- A custom annotation system gives the researchers control over image quality, labels, review status, and export format.
- The same platform can be reused later for other crops, objects, or robotics/computer vision projects.

Suggested pages:

- Dataset list
- Image upload
- Image annotation
- Annotation review
- Class or label management
- YOLO export
- Dataset split management

Essential features:

- Upload images
- Store image width, height, filename, source, and notes
- Draw bounding boxes by dragging over an image
- Move, resize, edit, or delete boxes
- Assign a class label to each box
- Mark images as unlabeled, in progress, done, or reviewed
- Save annotation coordinates
- Export images and labels in YOLO format

Suggested database fields:

```text
datasets
- id
- name
- description
- project_type
- created_at

images
- id
- dataset_id
- filename
- file_path
- width
- height
- source
- capture_date
- tree_id
- status
- notes
- created_at

classes
- id
- dataset_id
- name
- class_index

annotations
- id
- image_id
- class_id
- x_min
- y_min
- x_max
- y_max
- created_by
- created_at
```

YOLO export format:

```text
class_id center_x center_y width height
```

The platform can store boxes as pixel coordinates first:

```text
x_min, y_min, x_max, y_max
```

Then it can convert them to YOLO's normalized format during export:

```text
center_x = ((x_min + x_max) / 2) / image_width
center_y = ((y_min + y_max) / 2) / image_height
width = (x_max - x_min) / image_width
height = (y_max - y_min) / image_height
```

Recommended technology:

- Next.js for the web platform
- Database such as PostgreSQL, SQLite, or Supabase
- Local or cloud image storage
- Canvas-based annotation interface
- Export function for YOLO datasets

### 3. Dataset Collection

The team must collect local images of Perante orange trees because public fruit datasets may not match local tree structure, fruit appearance, lighting, camera angle, and orchard background.

Tasks:

1. Visit or coordinate with a citrus farm growing Perante orange.
2. Capture images from multiple tree sides.
3. Capture images from different distances and heights.
4. Capture images under different lighting conditions.
5. Include easy, medium, and difficult cases, such as occluded fruits and clustered fruits.
6. Store images with tree ID, date, location or orchard section, and capture notes.

Target dataset size:

- Prototype: 100-300 labeled images
- Stronger thesis dataset: 500-1,000+ labeled images

### 4. Image Annotation

Each visible Perante orange in the image should be labeled with a bounding box.

Initial class:

```text
citrus_fruit
```

Optional label:

```text
unclear_or_occluded_fruit
```

The preferred approach is to use the project's own annotation platform. Existing annotation tools can still be used as references or backup options:

- Roboflow
- CVAT
- LabelImg
- makesense.ai

### 5. Machine Learning Fruit Detection

The project should build an actual machine learning fruit detector by training or fine-tuning an object detection model.

Recommended model:

```text
YOLOv8, YOLOv11, or a similar YOLO object detection model
```

Model input:

```text
Image of a Perante orange tree
```

Model output:

```text
Bounding boxes around visible citrus fruits
Confidence score per detection
Fruit count per image
```

Training steps:

1. Split labeled images into training, validation, and test sets.
2. Train a baseline YOLO model.
3. Evaluate detection using precision, recall, F1-score, and mAP.
4. Fine-tune using more local Perante orange images.
5. Test on unseen tree images and drone-captured images.

### 6. Fruit Counting Logic

For a single image, the first fruit count can be the number of detected fruit bounding boxes.

For multiple images or video, the system must reduce duplicate counting because the same fruit may appear in several frames while the drone moves around the tree.

Basic counting:

```text
fruit count per image = number of valid detected fruit boxes
```

Improved tree-level counting:

```text
detect fruits across multiple frames
-> track or associate detections between nearby frames
-> avoid counting the same fruit repeatedly
-> estimate visible unique fruit count per tree
```

Possible methods:

- Keyframe selection from video
- Intersection-over-Union matching between nearby frames
- ByteTrack or DeepSORT for object tracking
- Kalman filter and Hungarian algorithm for frame-to-frame association
- Camera pose-based association for more advanced testing

### 7. Autonomous Drone Build and Image Capture Workflow

The project does not assume that the drone already exists. The drone platform should be built or assembled as part of the system, then tested gradually. However, image collection for the AI model should not wait until the drone is fully autonomous. The team can collect initial images manually first, while the drone hardware, camera mounting, navigation, and safety workflow are being developed.

Stage 1:

```text
Manual phone/camera images
```

Purpose:

- Build the first dataset
- Train the first detection model
- Test whether Perante oranges can be detected clearly
- Allow AI development to start before the drone build is complete

Stage 2:

```text
Drone platform build or assembly
```

Purpose:

- Select or assemble an outdoor-capable drone frame
- Add flight controller, GPS, camera, battery, and manual RC control
- Add return-to-home or recovery support when available
- Verify stable hover, safe takeoff, landing, and emergency manual override
- Prepare a secure camera mount or gimbal for tree-facing image capture

Stage 3:

```text
Manual-assisted drone images or video
```

Purpose:

- Collect realistic aerial/drone viewpoints
- Test blur, distance, lighting, and angle issues
- Compare drone images against manually captured images
- Validate that the built drone can safely capture useful citrus tree images

Stage 4:

```text
Controlled circular tree scan
```

Purpose:

- Capture images from multiple sides of one registered tree
- Test duplicate-count reduction
- Estimate visible fruit count per tree
- Keep manual override active for safety during early tests

Recommended scan pattern:

```text
Front -> front-right -> right -> back-right -> back -> back-left -> left -> front-left
```

Stage 5:

```text
Autonomous or semi-autonomous tree inspection
```

Purpose:

- Navigate to a selected registered tree using GPS waypoints, map position, or assisted mission planning
- Circle the tree at a safe distance while keeping the camera pointed toward the canopy
- Capture images or video at planned intervals
- Upload captured images, mission logs, and scan metadata to the backend
- Compare real-world scan behavior with Gazebo simulation results

### 8. Gazebo Simulation

Gazebo or a similar robotics simulator should be used to test drone navigation before real-world autonomous testing.

Simulation tasks:

1. Create a simple citrus orchard environment.
2. Add multiple virtual trees, terrain, and obstacles.
3. Spawn a simulated drone model.
4. Plan a route from launch point to selected tree.
5. Simulate a circular scan path around the tree.
6. Test obstacle avoidance around trunks, branches, and nearby trees.
7. Record simulated flight paths and mission results.

Purpose:

- Reduce risk before real drone flights
- Test repeated missions
- Demonstrate autonomous navigation logic
- Support the mapping part of the research

### 9. Scan Results Dashboard and Database

This part connects the farmer dashboard to actual scan records, captured images, fruit detections, and fruit count results.

Main dashboard features:

- View latest captured images
- View estimated visible fruit count
- View confidence score
- View scan history
- Show alerts for low-confidence scans or failed navigation

Possible database tables:

- Users
- Farms
- Orchard blocks
- Citrus trees
- Drone missions
- Tree scans
- Captured images
- Fruit detections
- Map versions
- Obstacles
- Alerts

### 10. Evaluation

The project should be evaluated using both computer vision metrics and system-level metrics.

Computer vision metrics:

- Precision
- Recall
- F1-score
- mAP
- Counting error per image
- Counting error per tree

Drone and simulation metrics:

- Scan completion rate
- Navigation success rate
- Obstacle avoidance success rate
- Simulated collision rate
- Average scan time per tree

Dashboard metrics:

- Correct storage of scan results
- Correct display of tree records
- Dashboard response time
- Farmer or user feedback

## Development Phases

### Phase 1: Research and Scope Finalization

- Finalize title and objectives.
- Review fruit detection, fruit counting, UAV navigation, and Gazebo simulation studies.
- Confirm that harvest readiness is outside the main scope.
- Finalize the system architecture for the dataset platform, AI model, drone workflow, simulation, and dashboard.

### Phase 2: Farmer Dashboard and Farm Mapping Platform

- Build the Next.js farmer dashboard.
- Add farmer account access.
- Add farm registration.
- Add crop or fruit registration.
- Add tree registration.
- Add farm map view using Google Maps, Google Earth-style satellite view, Leaflet, Mapbox, or a local coordinate map.
- Add tree markers on the map.
- Add drone registration.
- Add drone health UI for battery, GPS, camera, connection, storage, and mission readiness.
- Add UI-only or simulated states for drone health while the drone is not yet built.
- Add "Prepare Scan" or "Start Drone Scan" UI for a selected tree.
- Add scan status UI such as pending, preparing, scanning, completed, failed, or needs rescan.

### Phase 3: Dataset Platform Development

- Build the reusable image dataset platform.
- Add image upload and storage.
- Add dataset and class management.
- Build the bounding box annotation interface.
- Save annotation coordinates and image metadata.
- Add image statuses such as unlabeled, in progress, done, and reviewed.
- Add export to YOLO format.
- Test the platform using sample images before field data collection.

### Phase 4: Dataset Collection and Annotation

- Collect Perante orange tree images.
- Organize images by tree, date, and capture condition.
- Use the annotation platform to label fruit bounding boxes.
- Review labels for missed, incorrect, or duplicated boxes.
- Split dataset into training, validation, and test sets.

### Phase 5: Fruit Detection Model

- Train baseline YOLO model.
- Evaluate detection accuracy.
- Improve dataset and labels if detection is weak.
- Fine-tune model using drone-captured images.

### Phase 6: Counting and Duplicate Reduction

- Count fruits per image.
- Add keyframe extraction for videos.
- Add tracking or association between frames.
- Compare simple counting versus duplicate-reduced counting.

### Phase 7: Autonomous Drone Build, Capture, and Simulation

- Select or assemble the drone frame, flight controller, GPS, camera, battery, and manual RC control.
- Verify safe takeoff, landing, hover, return/recovery behavior, and emergency manual override.
- Mount and test the RGB camera for stable tree-facing image capture.
- Test manual-assisted drone image capture before autonomous flight.
- Define circular scan positions.
- Build Gazebo orchard simulation.
- Test simulated navigation to a selected tree.
- Test simulated circular scan path.
- Compare simulated circular scan behavior with controlled real-world tests.

### Phase 8: Scan Results Dashboard and Database

- Build scan-result storage.
- Display images, visible fruit count, confidence, and history.
- Connect scan results to the already-built tree records and map view.

### Phase 9: Integration and Testing

- Connect image capture, AI model, database, map, and dashboard.
- Run end-to-end tests using real or sample tree images.
- Evaluate detection, counting, duplicate reduction, navigation, and dashboard output.
- Document results, limitations, and future improvements.

## Minimum Viable Prototype

The first complete prototype should include:

1. Farmer account access.
2. Farm, crop, tree, and drone registration.
3. Farm map with tree markers and selected-tree details.
4. Drone health UI with battery, GPS, camera, connection, storage, and mission readiness states.
5. "Prepare Scan" or "Start Drone Scan" UI for a selected tree.
6. Reusable Next.js dataset and annotation platform.
7. Image upload and storage.
8. Bounding box drawing for object detection labels.
9. Saved annotation coordinates and metadata.
10. YOLO dataset export.
11. A small Perante orange image dataset.
12. Labeled citrus fruit bounding boxes.
13. A trained or fine-tuned YOLO fruit detection model.
14. Fruit count per image.
15. Tree-level visible fruit count from multiple images.
16. Basic duplicate-count reduction.
17. A built or assembled drone platform with RGB camera, GPS support, manual override, and safe supervised flight testing.
18. Scan result database.
19. Dashboard showing tree records, images, map position, scan status, and fruit count.
20. Gazebo simulation showing route planning and circular scan behavior.

## Scope Boundaries

Included:

- Reusable image dataset and annotation platform
- YOLO-ready annotation export
- Perante orange fruit detection
- Visible fruit counting
- Duplicate-count reduction
- Drone image/video capture workflow
- Gazebo simulation
- Orchard map or tree-location view
- Web dashboard

Not included in the main scope:

- Harvest readiness estimation
- Ripeness classification
- Disease detection
- Pest detection
- Exact 3D coordinate of every individual fruit
- Fully autonomous large-scale farm deployment

## Recommended Thesis Claim

The project should claim:

> The system estimates the visible fruit count of registered Perante orange trees using drone-captured images or video, machine learning-based fruit detection, duplicate-count reduction, and orchard mapping.

The project should avoid claiming:

> The system counts every fruit on the tree perfectly.

This is important because some fruits may be hidden by leaves, branches, or other fruits.
