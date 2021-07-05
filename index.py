import cv2
import datetime

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')
while True:
    _, frame = cap.read()
    main_frame = frame.copy()
    gray =  cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face = face_cascade.detectMultiScale(gray, 1.3, 5)
    for x,y, w, h in face:
        cv2.rectangle(frame, (x, y), (x+w, y+h),(0,255,255),2)
        face_dect = frame[y:y+h, x:x+w, ]
        gray_dect = gray[y:y + h, x:x + w,]
        smile = smile_cascade.detectMultiScale(gray_dect, 1.3,25)

        for x1, y1, w1, h1 in smile:
            cv2.rectangle(face_dect, (x1, y1), (x1+w1, y1+h1), (0, 0, 114),2)
            time_stamp= datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
            file_name = f'img{time_stamp}.png'
            cv2.imwrite(file_name,main_frame)
    cv2.imshow('Digital Camera', frame)
    if cv2.waitKey(10) == ord('q'):
        break

