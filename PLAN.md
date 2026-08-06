# Project Plan

## Project Direction

The project will focus on **visible fruit counting for Perante orange trees** using a drone-mounted camera, computer vision, orchard mapping, Gazebo simulation, and a web dashboard.

The main research scope is:

```text
Registered Perante orange tree
-> drone or camera captures images/video around the tree
-> machine learning model detects visible citrus fruits
-> counting logic estimates visible fruit count
-> tracking or frame association reduces duplicate counts
-> dashboard stores and displays tree-level results
```

The project will not focus on harvest readiness or ripeness estimation. That topic is broader and would require another set of labels, criteria, and validation methods.

## Main Goal

To build an autonomous drone-based computer vision and mapping system that estimates the visible fruit count of registered Perante orange trees and displays the result in a web dashboard.

## Core Components

### 1. Dataset Collection

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

### 2. Image Annotation

Each visible Perante orange in the image should be labeled with a bounding box.

Initial class:

```text
citrus_fruit
```

Optional label:

```text
unclear_or_occluded_fruit
```

Recommended annotation tools:

- Roboflow
- CVAT
- LabelImg
- makesense.ai

### 3. Machine Learning Fruit Detection

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

### 4. Fruit Counting Logic

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

### 5. Drone Image Capture Workflow

The drone capture workflow should progress from simple to advanced.

Stage 1:

```text
Manual phone/camera images
```

Purpose:

- Build the first dataset
- Train the first detection model
- Test whether Perante oranges can be detected clearly

Stage 2:

```text
Manual-assisted drone images or video
```

Purpose:

- Collect realistic aerial/drone viewpoints
- Test blur, distance, lighting, and angle issues
- Compare drone images against manually captured images

Stage 3:

```text
Planned circular tree scan
```

Purpose:

- Capture images from multiple sides of one registered tree
- Test duplicate-count reduction
- Estimate visible fruit count per tree

Recommended scan pattern:

```text
Front -> front-right -> right -> back-right -> back -> back-left -> left -> front-left
```

### 6. Gazebo Simulation

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

### 7. Web Dashboard and Database

The dashboard is the farmer-facing system for registering trees and viewing inspection results.

Main dashboard features:

- Register Perante orange trees
- Store tree ID, location, variety, notes, and inspection history
- View orchard map
- Select a tree for inspection
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

### 8. Evaluation

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
- Finalize system architecture.

### Phase 2: Dataset Preparation

- Collect Perante orange tree images.
- Organize images by tree, date, and capture condition.
- Label fruit bounding boxes.
- Split dataset into training, validation, and test sets.

### Phase 3: Fruit Detection Model

- Train baseline YOLO model.
- Evaluate detection accuracy.
- Improve dataset and labels if detection is weak.
- Fine-tune model using drone-captured images.

### Phase 4: Counting and Duplicate Reduction

- Count fruits per image.
- Add keyframe extraction for videos.
- Add tracking or association between frames.
- Compare simple counting versus duplicate-reduced counting.

### Phase 5: Drone Capture and Simulation

- Test manual-assisted drone image capture.
- Define circular scan positions.
- Build Gazebo orchard simulation.
- Test simulated navigation to a selected tree.
- Test simulated circular scan path.

### Phase 6: Dashboard and Database

- Build tree registration.
- Build map view.
- Build scan-result storage.
- Display images, visible fruit count, confidence, and history.

### Phase 7: Integration and Testing

- Connect image capture, AI model, database, map, and dashboard.
- Run end-to-end tests using real or sample tree images.
- Evaluate detection, counting, duplicate reduction, navigation, and dashboard output.
- Document results, limitations, and future improvements.

## Minimum Viable Prototype

The first complete prototype should include:

1. A small Perante orange image dataset.
2. Labeled citrus fruit bounding boxes.
3. A trained or fine-tuned YOLO fruit detection model.
4. Fruit count per image.
5. Tree-level visible fruit count from multiple images.
6. Basic duplicate-count reduction.
7. Tree registration and scan result database.
8. Dashboard showing tree records, images, map position, and fruit count.
9. Gazebo simulation showing route planning and circular scan behavior.

## Scope Boundaries

Included:

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
