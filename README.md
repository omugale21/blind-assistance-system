# 🧑‍🦯 Real-Time Object Detection and Voice Assistance for Blind People

This project is an AI-based assistive system designed to help visually impaired individuals navigate their surroundings using computer vision and voice feedback.

The system uses **YOLOv8** for real-time object detection and provides intelligent guidance such as object position (left/right/ahead), distance estimation, and obstacle warnings.

---

## 🚀 Live Demo

🔗 Try the deployed application here:
https://huggingface.co/spaces/omugale/blind-assistance-system

> **Note:** The live demo focuses on visual object detection. Voice assistance and real-time navigation features are available in the local system due to browser limitations.

---

## ✨ Features

* Real-time object detection using YOLOv8
* Voice feedback using Text-to-Speech
* Left / Right / Ahead object guidance
* Distance estimation based on object size
* Obstacle warning system
* Webcam-based environment awareness
* Threaded webcam streaming for smoother performance

---

## 🧠 How It Works

1. Webcam captures live video frames
2. YOLOv8 detects objects in each frame
3. System determines object position (left, right, ahead)
4. Distance is estimated using bounding box size
5. Voice feedback informs the user about surroundings

### 🔊 Example Output

```
chair left near  
bottle right far  
warning person very close
```

---

## 🛠️ Technologies Used

* Python
* OpenCV
* YOLOv8 (Ultralytics)
* pyttsx3 (Text-to-Speech)
* NumPy

---

## 📦 Project Structure

```
blind-assistance-system
│
├── main.py
├── voice.py
├── webcam_stream.py
├── app.py
├── requirements.txt
├── requirements-local.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Setup Instructions

### 🔹 For Local System (Full Features)

Includes webcam, voice assistance, and navigation:

```
pip install -r requirements-local.txt
python main.py
```

---

### 🔹 For Deployment (Web Demo)

Used for Hugging Face deployment:

```
pip install -r requirements.txt
python app.py
```

---

## 🔮 Future Improvements

* Mobile camera integration
* Advanced distance estimation (depth-based)
* Smart navigation path visualization
* Edge device deployment (Raspberry Pi / Jetson)

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and share it!
