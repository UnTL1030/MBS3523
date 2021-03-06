import cv2
print(cv2.__version__)

img = cv2.imread('Rec/lena.png')
img = cv2.resize(img, (int(img.shape[1]/1.5),int(img.shape[0]/1.5)))

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'Hello', (10, 300), font, 4, (255, 255, 255), 2, cv2.LINE_AA)

cv2.imshow('Hello', img)

cv2.waitKey(0)