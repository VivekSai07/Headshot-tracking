# Headshot Tracking with OpenCV and dlib

## Overview

This repository contains a Python script that uses OpenCV and dlib to perform headshot tracking. The script captures video from your default camera, detects a face, and then tracks the 28th facial landmark (located between the eyebrows) with a red dot. It also draws a red circle, black lines, and displays coordinates, creating a "headshot tracking" effect. The red dot is always on top of the black lines.

## Prerequisites

Before running the code, ensure you have the following installed:

- Python 3
- OpenCV
- dlib
- NumPy

You can install the required libraries using pip:
```bash
pip install opencv-python-headless
pip install dlib
```

## How to Run

1. Clone this repository to your local machine.

```bash
git clone https://github.com/VivekSai07/Headshot-tracking.git
```


2. Change into the project directory:
```bash
cd headshot-tracking
```

3. Run the Python script:
```bash
python Headshot Tracking.py
```

- The application will open a window displaying the camera feed with the headshot tracking effect.
- Press the 'Esc' key to exit the application.

## Configuration
You can customize the behavior of the code by adjusting parameters in the headshot_tracking.py file. For example, you can change the color of the red dot, circle, or lines, or modify the landmark position.


## Acknowledgments
This code is built upon the foundations of OpenCV and dlib and was created for educational purposes.
If you find this code useful or have any suggestions, feel free to contribute or provide feedback.
