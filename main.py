import cv2
from ultralytics import YOLO
from voice import speak
from webcam_stream import WebcamStream
import threading
import time

model = YOLO("yolov8n.pt")

cap = WebcamStream(src=0).start()

last_spoken_time = 0
cooldown = 3

dangerous_objects = ["person","chair","table","car","bicycle","motorcycle"]

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

    left_blocked = False
    center_blocked = False
    right_blocked = False

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
                zone="left"
                left_blocked = True
            elif center_x > frame_width*2/3:
                zone="right"
                right_blocked = True
            else:
                zone="center"
                center_blocked = True

            cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)

            cv2.putText(frame,
                        f"{label} {zone} {distance}",
                        (x1,y1-10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.6,
                        (0,255,0),
                        2)

    navigation_message = None

    if center_blocked:

        if not left_blocked:
            navigation_message = "Obstacle ahead. Safe path on the left"

        elif not right_blocked:
            navigation_message = "Obstacle ahead. Safe path on the right"

        else:
            navigation_message = "Multiple obstacles ahead. Stop"

    current_time = time.time()

    if navigation_message and current_time-last_spoken_time > cooldown:

        threading.Thread(target=speak,args=(navigation_message,)).start()

        last_spoken_time = current_time


    cv2.imshow("Blind Assistance System",frame)

    if cv2.waitKey(1)==27:
        break

cap.stop()
cv2.destroyAllWindows()