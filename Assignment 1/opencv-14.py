import cv2
print(cv2.__version__)
import face_recognition
print(face_recognition.__version__)

img_wy = face_recognition.load_image_file('img/wy-1.png')
img_wy = cv2.cvtColor(img_wy, cv2.COLOR_RGB2BGR)
faceLoc_wy = face_recognition.face_locations(img_wy)[0]
encode_wy = face_recognition.face_encodings(img_wy)[0]

capture = cv2.VideoCapture(1)
capture.set(3, 640)
capture.set(4, 480)

while True:
    success, img = capture.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    faceLocCam = face_recognition.face_locations(imgRGB)[0]
    encodeCam = face_recognition.face_encodings(imgRGB)[0]

    cv2.rectangle(img, (faceLocCam[3], faceLocCam[0]), (faceLocCam[1], faceLocCam[2]), (255, 0, 0), 2)

    results = face_recognition.compare_faces([encode_wy], encodeCam)
    print(results)
    cv2.imshow('Frame', img)
    if cv2.waitKey(1) == 27:
        break

capture.release()
cv2.destroyAllWindows()