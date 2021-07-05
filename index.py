import cv2

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')
while True:
    _, frame = cap.read()
    gray =  cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face = face_cascade.detectMultiScale(frame, 1.3, 5)
    for x,y, w, h in face:
        cv2.rectangle(frame, (x, y), (x+w, y+h),(0,255,255),2)
    cv2.imshow('cam pondit', gray)
    if cv2.waitKey(10) == repr('q'):
        break

