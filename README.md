# Real-Time Object Detection and Voice Assistance for Blind People

<<<<<<< HEAD
This project helps visually impaired individuals by detecting objects in real-time and providing voice feedback.

The system uses YOLOv8 for object detection and Text-to-Speech to announce detected objects.

## Features

- Real-time object detection
- Voice feedback for detected objects
- Assistive navigation support
- Webcam based detection

## Technologies Used

Python  
OpenCV  
YOLOv8  
pyttsx3  

## Installation

Clone the repository

git clone https://github.com/omugale21/blind-assistance-system.git

cd blind-assistance-system

Install dependencies

pip install -r requirements.txt

Run the project

python main.py

## Future Improvements

- Mobile camera support
- Distance estimation
- Obstacle warning system
- Smart navigation guidance
=======
This project is an assistive AI system designed to help visually impaired individuals navigate their surroundings using computer vision and voice feedback.

The system detects objects in real time using a webcam and provides spoken guidance about the object's position (left, right, or ahead) and approximate distance. It also alerts the user when an obstacle is very close.

## Features

- Real-time object detection using YOLOv8
- Voice feedback using Text-to-Speech
- Left / Right / Ahead object guidance
- Distance estimation based on object size
- Obstacle warning system
- Webcam-based environment awareness
- Threaded webcam streaming for smoother real-time detection

## How It Works

1. The webcam captures live video frames.
2. YOLOv8 detects objects in the frame.
3. The system calculates the object's position (left, right, or ahead).
4. Distance is estimated using the bounding box size.
5. The system provides voice feedback to inform the user about nearby objects.

Example voice output:

chair left near  
bottle right far  
warning person very close

## Technologies Used

- Python
- OpenCV
- YOLOv8 (Ultralytics)
- pyttsx3 (Text-to-Speech)
- NumPy

## Project Structure
blind-assistance-system
│
├── main.py
├── voice.py
├── webcam_stream.py
├── requirements.txt
├── README.md
└── .gitignore
>>>>>>> f5240bac4b0ff2e254aaa7c30d6f20ce84e36906
