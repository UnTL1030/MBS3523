import cv2
import time
import numpy as np
import imutils
import random

cap = cv2.VideoCapture('rec/Video3.mp4')

car_cascade = cv2.CascadeClassifier('rec/car.xml')
face=cv2.CascadeClassifier('rec/haarcascade_fullbody.xml')

while True:
    ret, frames = cap.read()
    gray=cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
    c = random.randint(0, 256)
    d = random.randint(0, 256)
    e = random.randint(0, 256)
    f = random.randint(0, 256)
    g = random.randint(0, 256)
    cars= car_cascade.detectMultiScale(gray, 2.22, 3)
    hum= face.detectMultiScale(gray, 1.07, 6)
    for (x, y, w, h) in hum:
        cv2.rectangle(frames, (x, y), (x + w, y + h), (c, d, e), 3)
    for (x, y, w, h) in cars:
        cv2.rectangle(frames, (x, y), (x+w, y+h), (e, f, g), 3)
        cv2.imshow('Detection', frames)
    if cv2.waitKey(1) == 0:
        break
cap.release()
cv2.destroyAllWindows()