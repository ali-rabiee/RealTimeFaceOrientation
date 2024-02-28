# RealTimeFaceOrientation

RealTimeFaceOrientation is a cutting-edge, real-time video processing application that detects human faces and determines the orientation of the head (neutral, left bend, or right bend) using advanced computer vision techniques.

## Features

- Real-time face detection in video streams.
- Accurate head orientation detection (neutral, left bend, right bend).
- Utilizes Histogram of Oriented Gradients (HOG) for face detection.
- Implementation of facial landmark detection for precise orientation analysis.

## Prerequisites

Before you begin, ensure you have met the following requirements:
- Python 3.6+
- Dlib
- OpenCV
- A pre-trained model file `shape_predictor_68_face_landmarks.dat` for facial landmark detection.

## Installation

To install and run RealTimeFaceOrientation, follow these steps:

Linux, macOS, and Windows:

```bash
git clone https://github.com/ali-rabiee/RealTimeFaceOrientation.git
cd RealTimeFaceOrientation
pip install -r requirements.txt
python main.py

