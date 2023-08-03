import cv2

def face2():
    face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

    video = cv2.VideoCapture("video/video2.MOV")

    while True:
        ret, frame = video.read()

        if not ret:
            break

        grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        face = face_detector.detectMultiScale(grey,2,2)

        for (x, y, w, h) in face:
            print("x:", x, "y:", y, "w:", w, "h:", h)


            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 3)
            cv2.circle(frame, center=(x + w // 2, y + h // 2), radius=w // 2, color=(0, 255, 0), thickness=3)

        cv2.imshow("Face", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()


face2()
cv2.destroyAllWindows()