import time

import cv2

cap = cv2.VideoCapture("video.mp4")

if not cap.isOpened():
    print("Could not open video file")

cap.set(cv2.CAP_PROP_POS_MSEC, 60000)

start = time.time()

while True:
    ret, frame = cap.read()

    if not ret:
        break

    cv2.imshow("Video frame", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyWindow()


