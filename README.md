# Poly-Shield-Detector

Poly-Shield-Detector is an image processing tool that combines YOLOv8 and Pyside6. Detect objects in images, define polygons, and filter objects inside polygons. Perfect for interactive annotation and object recognition tasks. Efficient and user-friendly.

![User Interface](https://github.com/yihong1120/Poly-Shield-Detector/blob/main/images/User_Interface.png)

## Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [Select Image](#select-image)
  - [Draw Polygons](#draw-polygons)
  - [Perform Object Detection](#perform-object-detection)
  - [Clear Polygons](#clear-polygons)
- [Results](#results)
- [Configuration](#configuration)
- [License](#license)

## Features

- Object detection using YOLOv8 model
- Polygon definition for filtering objects inside polygons
- Interactive annotation for precise object identification
- User-friendly graphical user interface (GUI) using Pyside6
- Efficient and accurate object recognition

## Requirements

Before using Poly-Shield-Detector, make sure you have the following:

- Python 3.7 or higher
- Pyside6
- torch
- ultralytics
- shapely

## Preparation

Before running Poly-Shield-Detector, make sure to perform the following preparation steps:

- Place the YOLOv8 model file in the `models` folder.
- Create the `records` folder to store the detected objects and polygon information.
- Create the `output` folder to store the processed images.

## Installation

1. Clone the repository:

```shell
git clone https://github.com/yihong1120/Poly-Shield-Detector.git
```

2. Navigate to the project directory:

```shell
cd Poly-Shield-Detector
```

3. Install the required dependencies:

```shell
pip install -r requirements.txt
```

4. Download the pre-trained YOLOv8 model:

```shell
mkdir models
cd models
wget https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8x.pt
cd ..
```

## Usage

1. Run the `app.py` file:

```shell
python app.py
```

The application window will appear, providing the following options:

* **Upload Image**: Click this button to select an image for object detection.

* **Predict**: Click this button to perform object detection on the selected image.

* **Clear Lists**: Click this button to clear the polygons and reset the scene.

### Select Image

1. Click the **Upload Image** button.

2. Select an image file (PNG, JPG, or BMP) from the file dialog and click **Open**.

### Draw Polygons
1. After selecting an image, you can draw polygons on the image by clicking the desired points on the image.

2. To create a closed polygon, click on the starting point again or click on the **Close Polygon** button that appears.

3. To draw multiple polygons, repeat the process.

### Perform Object Detection

1. After drawing polygons or if no polygons are drawn, click the **Predict** button.

2. The application will perform object detection on the selected image and display the detected objects in the list on the right.

### Clear Polygons

To clear the drawn polygons and reset the scene, click the **Clear Lists** button.

![Flowchart](https://github.com/yihong1120/Poly-Shield-Detector/blob/main/images/flowchart.png)

## Results

The detected objects and their frequencies will be displayed in the list on the right side of the application window. The list will show the class names of the objects and the number of times each class appears in the detection results.

Additionally, the application will save the detection results as a JSON file in the '**records**' folder. The JSON file will include the filename, predictions, and the base64 encoded original image.

## Configuration

- The `records` folder stores the detected objects and polygon information.
- The `output` folder stores the processed images.

## License

This project is licensed under the [AGPL-3.0](https://github.com/yihong1120/YOLOv8-PostProcessing-PRCurve/blob/main/LICENSE).
