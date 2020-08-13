import cv2
import numpy as np

faceCascade = cv2.CascadeClassifier('C:/Users/LIZMARY/Desktop/opencv/frontalface default.xml')

cap1 = cv2.VideoCapture(0)
cap1.set(3,640)
cap1.set(4,480)
cap1.set(10, 150)
count=0

minArea = 500
color = (255,0,255)

while True:
    success, img=cap1.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)

    for (x, y, w, h) in faces:
        area=w*h
        if area > minArea:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 2)
            cv2.putText(img, 'face detected',(x,y-5),
                        cv2.FONT_HERSHEY_COMPLEX_SMALL,1,color,2)
            imgRoi = img[y:y+h,x:x+w]
            cv2.imshow('roi', imgRoi)
    cv2.imshow('result', imgGray)
    if cv2.waitKey(1)  & 0xFF ==ord('q'):
        cv2.imwrite('scanned'+str(count)+'.jpg', imgRoi)
        cv2.rectangle(img,(0,200),(640,300),(0.255,0),cv2.FILLED)
        cv2.putText(img,"scan saved", (150,265),cv2.FONT_HERSHEY_DUPLEX,
                    2,(0,0,255),2)
        cv2.imshow('Result',img)
        cv2.waitKey(500)
        count +=1