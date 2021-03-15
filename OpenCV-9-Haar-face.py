
print(cv2.__version__)


faceCascade = cv2.CascadeClassifier('Resources/haarcascade_frontalface_default.xml')


img = cv2.imread('Resources/lena.png')
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Locate the features in the face(s) and return 4 values: x, y, width and height of the detected faces
faces = faceCascade.detectMultiScale(imgGray, 1.03, 5)

# draw rectangle on each face using the 4 values found for each face
for (x,y,w,h) in faces:
    cv2.rectangle(img, (x,y),(x+w,y+h),(255,0,0),2)

# Show the color image with rectangle on each face
cv2.imshow('Faces Detected',img)
cv2.waitKey(0)

