import cv2
from ultralytics import YOLO
from voice import speak
from webcam_stream import WebcamStream
import threading

model = YOLO("yolov8n.pt")

# start threaded webcam
cap = WebcamStream(src=0).start()

spoken = set()

def estimate_distance(box_width):

    if box_width > 250:
        return "very close"
    elif box_width > 150:
        return "near"
    else:
        return "far"


while True:

    frame = cap.read()

    if frame is None:
        continue

    frame = cv2.flip(frame,1)
    frame = cv2.resize(frame,(640,480))

    frame_width = frame.shape[1]

    results = model(frame, stream=True)

    for r in results:

        for box in r.boxes:

            cls = int(box.cls[0])
            label = model.names[cls]

            x1,y1,x2,y2 = map(int,box.xyxy[0])

            box_width = x2-x1
            center_x = (x1+x2)//2

            distance = estimate_distance(box_width)

            if center_x < frame_width/3:
                position="left"
            elif center_x > frame_width*2/3:
                position="right"
            else:
                position="ahead"

            message=f"{label} {position} {distance}"

            if label in ["person","chair","table","car"] and distance=="very close":
                message=f"Warning {label} very close"

            cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)

            cv2.putText(frame,
                        message,
                        (x1,y1-10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.7,
                        (0,255,0),
                        2)

            if message not in spoken:
                threading.Thread(target=speak,args=(message,)).start()
                spoken.add(message)

    cv2.imshow("Blind Assistance System",frame)

    if cv2.waitKey(1)==27:
        break

cap.stop()
cv2.destroyAllWindows()