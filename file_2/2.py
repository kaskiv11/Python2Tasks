import cv2

cap = cv2.VideoCapture("output.mp4")

if not cap.isOpened():
    print("Could not open video file")
    exit()

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
fps = 20.0

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output.mp4', fourcc, fps, (frame_width, frame_height))

while True:
    ret, frame = cap.read()

    if not ret:
        break

    out.write(frame)

    cv2.imshow("Кадр камери", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
