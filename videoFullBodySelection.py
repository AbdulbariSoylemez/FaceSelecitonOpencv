import cv2

vid = cv2.VideoCapture("video/video.mp4")
body = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_fullbody.xml")

while True:
    ret, frame = vid.read()

    if not ret:
        break

    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    bodyFull = body.detectMultiScale(grey, 1.1, 1)

    for (x, y, w, h) in bodyFull:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        cv2.imshow("Body", frame)

    if cv2.waitKey(1) & 0XFF == ord("q"):
        break

cv2.destroyAllWindows()

