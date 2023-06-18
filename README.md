# Poly-Shield-Detector

Poly-Shield-Detector is an image processing tool that combines YOLOv8 and Pyside6. Detect objects in images, define polygons, and filter objects inside polygons. Perfect for interactive annotation and object recognition tasks. Efficient and user-friendly.

## Contents
- [Features](#features)
- [Requirements](#requirements)
- [Preparation](#preparation)
- [Installation](#installation)
- [Usage](#usage)
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
cd Poly-Shield-Detector
```

2. Install the required dependencies:

```shell
pip install -r requirements.txt
```

## Usage

1. Run the `app.py` file:

```shell
python app.py
```

2. Select an image file using the "Upload Image" button.
3. Define polygons by clicking on the image.
4. Click the "Predict" button to perform object detection.
5. View the detected objects in the list on the right-hand side.
6. To clear the polygons and start over, click the "Clear Lists" button.

## Configuration

- The `records` folder stores the detected objects and polygon information.
- The `output` folder stores the processed images.

## License

This project is licensed under the [AGPL-3.0](https://github.com/yihong1120/YOLOv8-PostProcessing-PRCurve/blob/main/LICENSE).
