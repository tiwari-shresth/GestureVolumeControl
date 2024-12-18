import cv2
from time import time
import numpy as np
import mediapipe as mp
import pyautogui



Wcam, Hcam = 500, 500


cap = cv2.VideoCapture(0)
cap.set(4, Wcam)
cap.set(3, Hcam)

pTime = 0  # Initialize previous time
my_hands = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils
x1, y1, x2, y2 = 0, 0, 0, 0

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    rgb_img  = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    output = my_hands.process(rgb_img)
    hands = output.multi_hand_landmarks

    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(img, hand)
            landmarks = hand.landmark
            for id , landmark in enumerate(landmarks):
                h, w, c = img.shape
                cx, cy = int(landmark.x*w), int(landmark.y*h)
                cx, cy = int(landmark.x * w), int(landmark.y * h)
                if id == 8:
                    cv2.circle(img, (cx, cy), 7, (255,0,0), cv2.FILLED)
                    x1, y1 = cx, cy
                if id == 4:
                    cv2.circle(img, (cx, cy), 7, (0,255,0), cv2.FILLED)
                    x2, y2 = cx, cy

            dist = np.sqrt((x2-x1)**2 + (y2-y1)**2)
            cv2.line(img, (x1, y1), (x2, y2), (0,0,255), 3)
            if dist > 50:
                pyautogui.press('volumeup')
            else :
                pyautogui.press('volumedown')





    if not success or img is None:
        print("Failed to grab frame")
        break
    
    cTime = time()
    fps = 1 / max(cTime - pTime, 1e-6)  # Avoid division by zero
    pTime = cTime

    cv2.putText(img, f'FPS: {int(fps)}', (20,50), cv2.FONT_HERSHEY_PLAIN, 2, (255,0,0), 2)

    cv2.imshow('image', img)
    cv2.waitKey(1)

cap.release()
cv2.destroyAllWindows()
