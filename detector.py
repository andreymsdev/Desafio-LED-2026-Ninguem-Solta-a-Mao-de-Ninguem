import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

import cv2
import mediapipe as mp
import time
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

cap = cv2.VideoCapture(0)

base_options = python.BaseOptions(
    model_asset_path="coloque o caminho/../"
)

options = vision.HandLandmarkerOptions(
    base_options=base_options,
    num_hands=1,
    running_mode=vision.RunningMode.VIDEO
)

detector = vision.HandLandmarker.create_from_options(options)

prev_time = 0

def dedos_levantados(landmarks):
    dedos = []

    # polegar
    dedos.append(landmarks[4].x > landmarks[3].x)

    # outros dedos
    dedos.append(landmarks[8].y < landmarks[6].y)
    dedos.append(landmarks[12].y < landmarks[10].y)
    dedos.append(landmarks[16].y < landmarks[14].y)
    dedos.append(landmarks[20].y < landmarks[18].y)

    return dedos

    # posição das letras 

def reconhecer_letra(dedos):

    if dedos == [0,0,0,0,0]:
        return "A"

    if dedos == [0,1,1,1,1]:
        return "B"

    if dedos == [1,1,1,1,1]:
        return "C"

    if dedos == [0,1,0,0,0]:
        return "D"

    if dedos == [0,0,0,0,1]:
        return "E"

    return ""

while cap.isOpened():

    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame,1)

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb)

    timestamp = int(time.time()*1000)

    result = detector.detect_for_video(mp_image, timestamp)

    letra = ""

    if result.hand_landmarks:

        for hand_landmarks in result.hand_landmarks:

            dedos = dedos_levantados(hand_landmarks)
            letra = reconhecer_letra(dedos)

            for lm in hand_landmarks:
                x = int(lm.x * frame.shape[1])
                y = int(lm.y * frame.shape[0])
                cv2.circle(frame,(x,y),4,(0,255,0),-1)

    cv2.putText(frame,f"Letra: {letra}",(20,60),
                cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,255),3)

    curr_time = time.time()
    fps = 1/(curr_time-prev_time) if prev_time else 0
    prev_time = curr_time

    cv2.putText(frame,f"FPS:{int(fps)}",(20,30),
                cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2)

    cv2.imshow("ASL Detector",frame)

    # Esc fecha

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()