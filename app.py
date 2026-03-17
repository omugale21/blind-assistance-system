import gradio as gr
import cv2
from ultralytics import YOLO
import os

# Load model
model = YOLO("yolov8n.pt")
model.to("cpu")


def detect_image(image):

    image = cv2.resize(image, (640, 640))

    results = model(image)

    annotated = results[0].plot()

    return annotated


def detect_video(video):

    cap = cv2.VideoCapture(video)

    # Use safe temp path
    output_path = "/tmp/output.mp4"

    width = 640
    height = 640

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, 20.0, (width, height))

    while cap.isOpened():

        ret, frame = cap.read()

        if not ret:
            break

        frame = cv2.resize(frame, (640, 640))

        results = model(frame)

        annotated = results[0].plot()

        out.write(annotated)

    cap.release()
    out.release()

    print("Video saved at:", output_path)

    return output_path


with gr.Blocks() as demo:

    gr.Markdown(
    """
    # 🧑‍🦯 Blind Assistance AI System

    AI-based object detection system for assisting visually impaired individuals.

    ### Features
    - YOLOv8 object detection
    - Image detection
    - Video detection

    Upload an image or video to test.
    """
    )

    with gr.Tab("Image Detection"):

        image_input = gr.Image(type="numpy", label="Upload Image")
        image_output = gr.Image(label="Detection Result")

        image_button = gr.Button("Run Detection")

        image_button.click(detect_image, inputs=image_input, outputs=image_output)

    with gr.Tab("Video Detection"):

        video_input = gr.Video(label="Upload Video")
        video_output = gr.Video(label="Processed Video")

        video_button = gr.Button("Run Detection")

        video_button.click(detect_video, inputs=video_input, outputs=video_output)

    gr.Markdown(
    """
    ---
    🔗 GitHub: https://github.com/omugale21/blind-assistance-system
    """
    )

demo.launch(share=False)