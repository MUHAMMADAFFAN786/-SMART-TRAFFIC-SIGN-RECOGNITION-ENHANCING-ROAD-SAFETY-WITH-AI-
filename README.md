# 🚦 SMART Traffic Sign Recognition: Enhancing Road Safety with AI

### 🧠 AI • Computer Vision • Deep Learning • IoT • Arduino

A real-time traffic sign recognition and driver-assistance system using
CNN, OpenCV, Voice Alerts and Arduino-based hardware feedback.

---

## 🌟 Overview

**SMART Traffic Sign Recognition: Enhancing Road Safety with AI** is an AI/ML-based academic project designed to recognize traffic signs from a live webcam feed and provide driver-assistance feedback.

The system combines:

- 🧠 **Convolutional Neural Network (CNN)**
- 👁️ **Computer Vision**
- 📷 **Real-Time Webcam Processing**
- 🔊 **Voice Assistance**
- 🔌 **Arduino Hardware**
- 💡 **LED & Buzzer Alerts**
- 📝 **Recognition Logging**

The model is trained using the **German Traffic Sign Recognition Benchmark (GTSRB)** dataset and supports classification across **43 traffic sign categories**.

During real-time operation, the webcam captures frames, identifies potential traffic-sign regions, preprocesses the detected region and passes it to the trained CNN model.

Predictions are filtered using a confidence threshold and stabilized across multiple frames to reduce unreliable alerts.

---

## ✨ Key Features

| **Feature** | **Description** |
| ------------------------------- | --------------------------------------------- |
| 🚦 **43-Class Recognition** | Classification of 43 traffic sign categories |
| 🧠 **CNN Model** | Custom CNN implemented using TensorFlow/Keras |
| 📷 **Real-Time Detection** | Live webcam-based traffic sign recognition |
| 🎯 **ROI Detection** | Detection of potential traffic-sign regions |
| 📊 **Confidence Filtering** | Filters low-confidence predictions |
| 🔄 **Prediction Stabilization** | Multi-frame prediction stabilization |
| 🔊 **Voice Alerts** | Audible notifications using pyttsx3 |
| 🔌 **Arduino Integration** | Serial communication with Arduino |
| 💡 **LED Alerts** | Visual hardware warning indicators |
| 🔔 **Buzzer Alerts** | Audible hardware warning |
| 📝 **Event Logging** | Records detected signs and confidence |
| 🛠️ **Simulation Mode** | Can operate without Arduino hardware |

---

## 🏗️ System Architecture

```text
                         📷 LIVE WEBCAM
                              │
                              ▼
                   ┌────────────────────────┐
                   │    👁️ OPENCV PROCESSING │
                   │                        │
                   │  Frame Capture         │
                   │  ROI Detection         │
                   │  Image Preprocessing   │
                   └───────────┬────────────┘
                              │
                              ▼
                   ┌────────────────────────┐
                   │      🧠 CNN MODEL      │
                   │                        │
                   │ Traffic Sign           │
                   │ Classification         │
                   └───────────┬────────────┘
                              │
                              ▼
                   ┌────────────────────────┐
                   │ 📊 Prediction &        │
                   │    Confidence Filter   │
                   └───────────┬────────────┘
                              │
                       ┌──────┴──────┐
                       │             │
                       ▼             ▼
                 🔊 VOICE ALERT   🔌 ARDUINO
                    pyttsx3       LED / BUZZER
                       │             │
                       └──────┬──────┘
                              ▼
                      📝 EVENT LOGGING





## 🧠 Machine Learning Model

The recognition system uses a custom Convolutional Neural Network (CNN)
implemented using TensorFlow and Keras.

### 🏗️ CNN Architecture

Input Image
32 × 32 × 3
     │
     ▼
Conv2D — 32 Filters
     │
     ▼
MaxPooling
     │
     ▼
Conv2D — 64 Filters
     │
     ▼
MaxPooling
     │
     ▼
Conv2D — 128 Filters
     │
     ▼
MaxPooling
     │
     ▼
Flatten
     │
     ▼
Dense — 256 Units
     │
     ▼
Dropout — 0.5
     │
     ▼
Dense — 43 Units
     │
     ▼
Softmax
     │
     ▼
Traffic Sign Class

---

## ⚙️ Training Configuration

| Parameter | Configuration |
|---|---|
| 🖼️ Input Size | 32 × 32 × 3 |
| 🚦 Classes | 43 |
| ⚡ Optimizer | Adam |
| 📉 Loss Function | Categorical Cross-Entropy |
| 🔁 Epochs | 15 |
| 📊 Train/Test Split | 80/20 |
| 🔄 Data Augmentation | Rotation, Zoom, Width/Height Shifts |
| 🧠 Framework | TensorFlow / Keras |

---

## 🔄 Real-Time Recognition Pipeline

The system follows the following workflow:

📷 Capture Webcam Frame
          ↓
🖼️ Image Preprocessing
          ↓
🎯 Potential Sign Region Detection
          ↓
🔍 Candidate Filtering
          ↓
📐 Resize → 32 × 32
          ↓
⚖️ Image Normalization
          ↓
🧠 CNN Prediction
          ↓
📊 Confidence Threshold
          ↓
🔄 Multi-Frame Stabilization
          ↓
🚦 Traffic Sign Recognition
          ↓
 ┌─────────┬───────────┬───────────┐
 ▼         ▼           ▼
🖥️ Visual  🔊 Voice    🔌 Arduino
Feedback   Alert       Alert
    \        |          /
     \       |         /
      └──────┴────────┘
             ↓
         📝 Event Log

This pipeline helps reduce unstable predictions and unnecessary alerts during
live testing.

---

## 🚘 Driver Assistance

### 🖥️ Visual Feedback

The application displays:

- 🚦 Detected traffic sign
- 📊 Prediction confidence
- 📦 Detection bounding box
- ⚡ System status
- 🎞️ FPS information

### 🔊 Voice Feedback

The system uses pyttsx3 to provide audible notifications for recognized
traffic signs.

This provides an additional way of communicating the detected sign during
real-time operation.

### 🔌 Arduino Feedback

The application can communicate with an Arduino through serial communication.

The hardware interface demonstrates:

- 💡 LED indicators
- 🔔 Warning buzzer
- 🚦 Sign-specific responses
- ⚠️ Driver warning signals

Arduino connectivity is optional. The software can also operate using its
fallback simulation behavior.

---

## 🔧 Hardware Setup

The hardware prototype uses an Arduino connected to a breadboard containing
LED indicators and a buzzer.

Python Application
       │
       │ Serial Communication
       ▼
     Arduino
       │
    ┌───┴────┐
    ▼        ▼
  💡 LED    🔔 Buzzer

### Arduino Alert Logic

| Serial Command | Hardware Response |
|---|---|
| STOP | White LED ON + Buzzer ON |
| SPEED | Green LED ON |
| CLEAR | LEDs OFF + Buzzer OFF |

Arduino source code:

```text
hardware/
└── arduino/
    └── traffic_sign_alert.ino
📸 Hardware & Project Demo

The project hardware photographs and demonstration video are stored directly
inside the hardware folder.

🔌 Hardware Setup
<p align="center"> <img src="hardware/hardware_setup.jpg" width="700"> </p>

Arduino + breadboard based driver-alert hardware prototype.

🖥️ Complete Project Setup
<p align="center"> <img src="hardware/project_demo.jpg" width="850"> </p>

Complete setup showing the laptop, webcam, Arduino and alert circuit.

🚦 System Demonstration
<p align="center"> <img src="hardware/system_setup.jpg" width="850"> </p>

Real-time AI application and hardware setup demonstration.

🎥 Project Demo Video

🎬 A real-time demonstration of traffic sign recognition,
AI prediction and Arduino-based driver assistance.

▶️ Watch the Project Demo

🎬 Open Project Demo Video

The demo shows:

Webcam starts
Traffic sign enters camera view
CNN recognizes the sign
Prediction appears on screen
Voice alert is generated
Arduino receives the alert
LED/Buzzer responds
📊 Dataset

The project uses the German Traffic Sign Recognition Benchmark (GTSRB)
dataset.

The dataset contains 43 traffic sign categories and is used for training
and evaluation of the classification model.

⚠️ The complete GTSRB image dataset is intentionally not included in this
repository to keep the repository lightweight.

Users should obtain the dataset separately and configure the local dataset path
before training.

Dataset Structure
GTSRB/
├── Train/
├── Test/
├── Meta/
├── Train.csv
├── Test.csv
└── Meta.csv
📁 Project Structure
SMART-TRAFFIC-SIGN-RECOGNITION-ENHANCING-ROAD-SAFETY-WITH-AI/
│
├── 📄 README.md
├── 📄 LICENSE
├── 📄 requirements.txt
├── 📄 .gitignore
│
├── 🧠 Train_model.py
├── 📷 webcam_test.py
├── 🗂️ class_mapping.json
├── 🤖 traffic_sign_model.h5
│
├── 🔌 hardware/
│   ├── arduino/
│   │   └── traffic_sign_alert.ino
│   │
│   ├── 📸 hardware_setup.jpg
│   ├── 📸 project_demo.jpg
│   ├── 📸 system_setup.jpg
│   └── 🎥 project_demo.mp4
│
└── 📚 docs/
    └── PROJECT REPORT.pdf
📄 File Description
File	Purpose
Train_model.py	🧠 CNN training and model generation
webcam_test.py	📷 Real-time recognition and driver alerts
class_mapping.json	🗂️ Traffic-sign class mapping
traffic_sign_model.h5	🤖 Trained CNN model
requirements.txt	📦 Python dependencies
hardware/arduino/traffic_sign_alert.ino	🔌 Arduino alert program
hardware/*.jpg	📸 Hardware and project photographs
hardware/project_demo.mp4	🎥 Project demonstration video
docs/PROJECT REPORT.pdf	📚 Detailed academic project report
README.md	📖 Project documentation
🛠️ Technology Stack
Technology	Purpose
🐍 Python	Core development
🧠 TensorFlow	Deep Learning
🔬 Keras	CNN implementation
👁️ OpenCV	Computer Vision
🔢 NumPy	Numerical computation
🐼 Pandas	Data processing
📈 Matplotlib	Visualization
🔊 pyttsx3	Text-to-Speech
🔌 Arduino	Hardware feedback
📡 Serial Communication	PC ↔ Arduino communication
🚦 GTSRB	Traffic-sign dataset
🚀 Installation
1️⃣ Download the Repository

Download this repository from GitHub and open it in your development
environment.

2️⃣ Create Virtual Environment
python -m venv .venv

Windows:

.venv\Scripts\activate
3️⃣ Install Dependencies
pip install -r requirements.txt

Or:

pip install tensorflow opencv-python numpy pandas matplotlib pyttsx3 pyserial
📂 Dataset Configuration

Before training:

Step 1

Download the GTSRB dataset.

Step 2

Place it on your local computer.

Step 3

Make sure the dataset contains:

Train/
Test/
Meta/
Train.csv
Test.csv
Meta.csv
Step 4

Update the dataset path inside:

Train_model.py

⚠️ The complete dataset should not be uploaded to this repository.

🧪 Model Training

Run:

python Train_model.py
Training Workflow
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
📷 Real-Time Detection

Start the webcam application:

python webcam_test.py

The application uses the webcam to recognize traffic signs in real time.

The system can display:

🖥️ Traffic sign
📊 Confidence score
📦 Bounding box
🎞️ FPS
⚡ System status

And provide:

🔊 Voice feedback
🔌 Arduino feedback
📝 Recognition logging
🔌 Arduino Setup

Arduino integration is optional.

Steps
Connect Arduino to the computer.
Identify the assigned COM/serial port.
Configure the port in webcam_test.py.
Open the Arduino sketch:
hardware/arduino/traffic_sign_alert.ino
Upload the Arduino program.
Start the webcam recognition application.
📝 Detection Logging

Recognition events can be recorded for later analysis.

The log can contain:

Field	Description
🕒 Time	Recognition time
🚦 Sign	Detected traffic sign
📊 Confidence	Model confidence

This allows recognition activity during testing to be reviewed after a session.

🎯 Applications

This project demonstrates concepts relevant to:

🚘 Advanced Driver Assistance Systems (ADAS)
🚦 Intelligent Transportation Systems
🏙️ Smart Mobility
👁️ Computer Vision
🧠 Deep Learning
⚡ Real-Time AI Applications
🔌 Embedded AI Systems
🚗 Autonomous Driving Research
⚠️ Limitations

This project is an academic and research prototype.

Real-world performance may vary depending on:

💡 Lighting conditions
📷 Camera quality
📏 Sign distance
📐 Viewing angle
🌳 Background complexity
💨 Motion blur
🚧 Occlusion
🌦️ Environmental conditions

⚠️ This system is designed for educational and research demonstration and
is not a production automotive safety system.

🔮 Future Development

Possible improvements include:

🎯 YOLO-based traffic-sign detection
🔍 More robust object localization
🚦 Multi-sign detection
🔄 Temporal object tracking
🌙 Improved low-light performance
🌍 Real-world traffic datasets
⚡ Edge-device model optimization
🍓 Raspberry Pi deployment
🟢 NVIDIA Jetson deployment
🚀 GPU-accelerated inference
📍 GPS-based contextual alerts
🚘 Advanced ADAS integration
🎓 Academic Project
Category	Details
🎓 Degree	B.Tech – Artificial Intelligence & Machine Learning
🏫 Institution	COER University, Roorkee
📚 Project Type	Academic Project
🚘 Application Area	Intelligent Transportation / Driver Assistance
👥 Project Team
Muhammad Affan
Keshav Dixit
Mohd Zaid
📜 License

This project is licensed under the MIT License.

See the LICENSE file for details.

⚠️ Disclaimer

This project is intended for educational and research purposes only.

It is not a certified automotive safety system and should not be used as a
replacement for professional driver-assistance or vehicle safety technologies.

⭐ Project Highlights

🧠 Deep Learning + 👁️ Computer Vision + 🚦 Traffic Sign Recognition

🔌 IoT Hardware + 🔊 Voice Assistance

Built as an academic AI/ML project to explore real-time intelligent
driver-assistance systems.
