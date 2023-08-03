import cv2
import numpy as np

video=cv2.VideoCapture(0)
face_detector= cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")
eye_detector= cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_eye.xml")


while True:
    ret , frame=video.read()
    if ret==0:
        break

    frame=cv2.flip(frame,1)
    grey=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    faces=face_detector.detectMultiScale(grey,1.2,4)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,pt1=(x,y),pt2=(x+w,y+h),color=(255,0,0),thickness=3)
        roi_grey=grey[y:(y+h),x:(x+w)]
        roi_color=frame[y:y+h,x:x+w]
        eyes = eye_detector.detectMultiScale(roi_grey,1.2,8)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ew + ex, eh + ey), (0, 255, 0), 5)
        cv2.imshow("Frame", frame)

    if cv2.waitKey(1) & 0XFF==ord("q"):
        break



video.release()
cv2.destroyAllWindows()