import cv2
#import numpy as np
print(cv2.__version__)

capture = cv2.VideoCapture(0)
capture.set(3, 640)
capture.set(4, 480)

# Select font
font = cv2.FONT_HERSHEY_SIMPLEX

# Start capturing and show frames on window named 'Frame'
while True:
    success, img = capture.read()

    # Put a red text on img
    cv2.putText(img, 'Oh, Hi Mark!!!', (20, 50), font, 1.3, (0, 255, 0), 2)

    cv2.imshow('Frame', img)
    if cv2.waitKey(20) & 0xff == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()