import cv2
from ultralytics import YOLO
from voice import speak

# Load YOLOv8 model
model = YOLO("yolov8n.pt")

# Open webcam
cap = cv2.VideoCapture(0)

spoken = set()

# Distance estimation function
def estimate_distance(box_width):

    if box_width > 250:
        return "very close"

    elif box_width > 150:
        return "near"

    else:
        return "far"


while True:

    ret, frame = cap.read()

    if not ret:
        break

    # FIX MIRROR ISSUE
    frame = cv2.flip(frame, 1)

    # frame width for left/right calculation
    frame_width = frame.shape[1]

    results = model(frame)

    for r in results:

        for box in r.boxes:

            cls = int(box.cls[0])
            label = model.names[cls]

            x1, y1, x2, y2 = map(int, box.xyxy[0])

            box_width = x2 - x1

            center_x = (x1 + x2) // 2

            # Distance estimation
            distance = estimate_distance(box_width)

            # Left / Right guidance
            if center_x < frame_width / 3:
                position = "left"

            elif center_x > frame_width * 2 / 3:
                position = "right"

            else:
                position = "ahead"

            message = f"{label} {position} {distance}"

            # Obstacle warning
            if label in ["person", "chair", "table", "car"] and distance == "very close":
                message = f"Warning {label} very close"

            # Draw bounding box
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0,255,0), 2)

            cv2.putText(frame,
                        message,
                        (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.7,
                        (0,255,0),
                        2)

            # Speak message
            if message not in spoken:

                speak(message)

                spoken.add(message)

    cv2.imshow("Blind Assistance System", frame)

    # Press ESC to exit
    if cv2.waitKey(1) == 27:
        break


cap.release()
cv2.destroyAllWindows()