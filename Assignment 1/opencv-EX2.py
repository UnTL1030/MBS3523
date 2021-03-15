import cv2
#import numpy as np
print(cv2.__version__)


capture = cv2.VideoCapture(0)

capture.set(3, 640)
capture.set(4, 480)


x = 0
dx = 1
while True:
    success, img = capture.read()
    cv2.rectangle(img, (x, 200), (x + 50, 250), (255, 255, 255), 2)
    x = x + dx
    if x >= 590 or x <= 0:
        dx = dx * (-1)

    cv2.imshow('Frame', img)
    if cv2.waitKey(20) & 0xff == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()