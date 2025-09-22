import cv2 as cv
import numpy as np
import time
import winsound
import os
from datetime import datetime

cap = cv.VideoCapture(0)

motion_detected = False
recording = False
base_dir = "motion_videos"
os.makedirs(base_dir, exist_ok=True)
video_writer = None

fourcc = cv.VideoWriter_fourcc(*'XVID')
fps = 20.0
frame_size = (int(cap.get(3)), int(cap.get(4)))

def get_timestamp():
    return datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

while cap.isOpened():
    ret, frame1 = cap.read()
    ret, frame2 = cap.read()

    if not ret:
        break

    motionDiff = cv.absdiff(frame1, frame2)
    motionGray = cv.cvtColor(motionDiff, cv.COLOR_BGR2GRAY)
    motionBlur = cv.GaussianBlur(motionGray, (7,7), 0)

    _, thres = cv.threshold(motionBlur, 25, 255, cv.THRESH_BINARY)
    motionDilate = cv.dilate(thres, None, iterations=6)
    motionDilate = cv.morphologyEx(motionDilate, cv.MORPH_CLOSE, np.ones((15, 15), np.uint8))

    motionContours, _ = cv.findContours(motionDilate, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
    current_motion = False

    for cnt in motionContours:
        if cv.contourArea(cnt) > 5000:
            x, y, w, h = cv.boundingRect(cnt)
            cv.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)
            current_motion = True

    if current_motion and not motion_detected:
        cv.putText(frame1, "HAREKET ALGILANDI!", (10, 50), cv.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 3)
        winsound.Beep(1000, 500)
        timestamp = get_timestamp()
        video_dir = os.path.join(base_dir, f"motion_{timestamp}")
        os.makedirs(video_dir, exist_ok=True)
        video_path = os.path.join(video_dir, f"{timestamp}.avi")
        video_writer = cv.VideoWriter(video_path, fourcc, fps, frame_size)
        recording = True
        motion_detected = True

    elif not current_motion and motion_detected:
        cv.putText(frame1, "HAREKET BITTI", (10, 50), cv.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 3)
        motion_detected = False
        if recording:
            video_writer.release()
            recording = False

    if recording:
        video_writer.write(frame1)

    cv.imshow("Security Camera", frame1)
    frame1 = frame2
    ret, frame2 = cap.read()

    if cv.waitKey(1) & 0xFF == ord("q"):
        break

if recording:
    video_writer.release()
cap.release()
cv.destroyAllWindows()
