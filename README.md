# Real-Time Traffic Sign Recognition with IoT-Based Driver Assistance

A real-time computer vision and deep learning system for recognizing traffic signs and providing driver-assistance feedback through visual, voice, and Arduino-based alerts.

## Overview

Traffic sign recognition is an important component of intelligent transportation and driver-assistance systems. This project explores how a Convolutional Neural Network (CNN) can be combined with computer vision and embedded hardware to recognize traffic signs from a live camera feed.

The system is trained on the German Traffic Sign Recognition Benchmark (GTSRB) dataset and supports classification across 43 traffic sign categories.

During real-time operation, the webcam captures frames, identifies potential traffic-sign regions, preprocesses the detected region, and passes it to the trained CNN model. Predictions are filtered using a confidence threshold and stabilized across multiple frames to reduce unreliable alerts.

The recognized sign can then be presented through the application interface, announced using text-to-speech, and communicated to an Arduino-based alert system.

---

## Key Features

- 43-class traffic sign classification
- CNN-based image recognition using TensorFlow/Keras
- Real-time webcam processing with OpenCV
- Region-of-interest based sign detection
- Confidence-based prediction filtering
- Multi-frame prediction stabilization
- Voice alerts using `pyttsx3`
- Arduino serial communication
- LED and buzzer based driver alerts
- Traffic recognition event logging
- Fallback simulation mode when Arduino is unavailable

---

## System Architecture

```text
                    LIVE WEBCAM
                         │
                         ▼
                ┌─────────────────┐
                │ OpenCV Processing│
                │                 │
                │ Frame Capture   │
                │ ROI Detection   │
                │ Preprocessing   │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │   CNN MODEL     │
                │                 │
                │ Traffic Sign    │
                │ Classification  │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Prediction &    │
                │ Confidence      │
                └───────┬─┬───────┘
                        │ │
             ┌──────────┘ └──────────┐
             ▼                       ▼
       VOICE ALERT               ARDUINO
        pyttsx3              LED / BUZZER
             │                       │
             └───────────┬───────────┘
                         ▼
                  EVENT LOGGING
Machine Learning Model

The recognition model is a custom Convolutional Neural Network implemented using TensorFlow and Keras.

CNN Architecture
Input: 32 × 32 × 3
        │
        ▼
Conv2D — 32 Filters
        │
MaxPooling
        │
        ▼
Conv2D — 64 Filters
        │
MaxPooling
        │
        ▼
Conv2D — 128 Filters
        │
MaxPooling
        │
        ▼
Flatten
        │
        ▼
Dense — 256 Units
        │
Dropout — 0.5
        │
        ▼
Dense — 43 Units
        │
        ▼
Softmax
Training Configuration
Parameter	Configuration
Input Size	32 × 32 × 3
Classes	43
Optimizer	Adam
Loss Function	Categorical Cross-Entropy
Epochs	15
Train/Test Split	80/20
Data Augmentation	Rotation, Zoom, Width/Height Shifts
Framework	TensorFlow / Keras
Real-Time Recognition Pipeline

The webcam application follows a multi-stage recognition process:

Capture live video from the webcam.
Convert and preprocess the camera frame.
Detect potential traffic-sign regions.
Filter unsuitable candidate regions.
Resize the selected region to 32 × 32.
Normalize the image.
Run CNN inference.
Apply the confidence threshold.
Stabilize predictions using multiple consecutive frames.
Display the recognized sign and confidence.
Trigger voice and hardware feedback.
Record the recognition event in the log.

This approach helps reduce unstable predictions and unnecessary alerts during live operation.

Driver Assistance Feedback
Visual Feedback

The application displays:

Detected traffic sign
Prediction confidence
Detection bounding box
System status
FPS information
Voice Feedback

The system uses pyttsx3 to provide audible notifications for recognized traffic signs.

Arduino Feedback

The application can communicate with an Arduino through serial communication.

The Arduino interface can be used to demonstrate:

LED indicators
Warning buzzer
Sign-specific alert responses
Driver warning signals

Arduino connectivity is optional. The software can also operate using its fallback simulation behavior.

Dataset

The model uses the German Traffic Sign Recognition Benchmark (GTSRB) dataset.

The dataset contains 43 traffic sign categories and is used for training and evaluating the classification model.

The complete dataset is not included in this repository to keep the repository lightweight. Users should obtain the dataset separately and configure the dataset location before training.

Project Files

The current repository contains the following core files:

.
├── README.md
├── Train_model.py
├── webcam_test.py
├── class_mapping.json
└── traffic_sign_model.h5
File Description
File	Purpose
Train_model.py	CNN model training and model generation
webcam_test.py	Real-time webcam recognition and driver alerts
class_mapping.json	Mapping of model classes to traffic-sign categories
traffic_sign_model.h5	Trained CNN model
README.md	Project documentation

The GTSRB dataset is intentionally excluded from the repository.

Technology Stack
Technology	Purpose
Python	Core development
TensorFlow	Deep learning framework
Keras	CNN implementation
OpenCV	Computer vision and webcam processing
NumPy	Numerical computation
Pandas	Data processing and logging
Matplotlib	Visualization
pyttsx3	Text-to-speech alerts
Arduino	Hardware feedback
Serial Communication	PC-to-Arduino communication
GTSRB	Traffic sign dataset
Installation
1. Clone or Download the Repository

Download this repository from GitHub and open it in your development environment.

2. Create a Virtual Environment
python -m venv .venv

Activate it on Windows:

.venv\Scripts\activate
3. Install Required Libraries

Install the dependencies required by the Python scripts:

pip install tensorflow opencv-python numpy pandas matplotlib pyttsx3 pyserial
Dataset Configuration

Before training the model:

Download the GTSRB dataset.
Place the dataset on your local system.
Ensure the dataset contains the required training images and CSV files.
Update the dataset path in Train_model.py according to your local directory.

The dataset itself should not be uploaded to this GitHub repository.

Model Training

Run the training script:

python Train_model.py

The training workflow includes:

Dataset Loading
      ↓
Image Preprocessing
      ↓
Normalization
      ↓
Label Encoding
      ↓
Train/Test Split
      ↓
Data Augmentation
      ↓
CNN Training
      ↓
Model Evaluation
      ↓
Model Saving

After training, the model is saved as:

traffic_sign_model.h5
Real-Time Detection

After the trained model is available, start the webcam application:

python webcam_test.py

The application uses the webcam to detect and classify traffic signs in real time.

The system can display the prediction, confidence score, bounding box, and system status while also providing voice and Arduino-based feedback.

Arduino Setup

Arduino integration is optional.

If an Arduino is connected:

Connect the Arduino to the computer.
Identify the assigned serial/COM port.
Configure the port in webcam_test.py.
Upload the corresponding Arduino program.
Start the webcam recognition application.

The hardware interface can be used to demonstrate warning signals through LEDs and a buzzer.

Detection Logging

Recognition events can be recorded for later analysis.

The log contains information such as:

Time
Detected Sign
Confidence

This allows recognition activity during testing to be reviewed after a session.

Applications

The project demonstrates concepts relevant to:

Advanced Driver Assistance Systems (ADAS)
Intelligent Transportation Systems
Smart Mobility
Computer Vision
Deep Learning
Real-Time AI Applications
Embedded AI Systems
Autonomous Driving Research
Limitations

This implementation is an academic and research prototype. Real-world performance may vary depending on environmental and camera conditions.

Potential factors include:

Lighting conditions
Camera quality
Sign distance
Viewing angle
Background complexity
Motion blur
Occlusion
Real-world environmental conditions

The system is intended to demonstrate an AI-based driver-assistance workflow and is not designed as a production automotive safety system.

Future Development

Possible future improvements include:

YOLO-based traffic-sign detection
More robust object localization
Multi-sign detection
Temporal object tracking
Improved low-light performance
Real-world traffic datasets
Model optimization for edge devices
Raspberry Pi deployment
NVIDIA Jetson deployment
GPU-accelerated inference
GPS-based contextual alerts
Advanced ADAS integration

Academic Project
Degree: B.Tech – Artificial Intelligence & Machine Learning
Institution: COER University, Roorkee
Project Type: Academic Project
Application Area: Intelligent Transportation / Driver Assistance

Project Team
Muhammad Affan
Keshav Dixit
Mohd Zaid
License

This project is licensed under the MIT License.

Disclaimer

This project is intended for educational and research purposes only.

It is not a certified automotive safety system and should not be used as a replacement for professional driver-assistance or vehicle safety technologies.
