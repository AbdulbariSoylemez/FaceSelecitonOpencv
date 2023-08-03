import cv2

def eye():
    eyes = cv2.imread("foto/foto2.jpg")

    eyedetector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")

    eye = eyedetector.detectMultiScale(eyes, 1.15, 3)

    for (x, y, w, h) in eye:
        print("x:", x, "y:", y, "w:", w, "h:", h)
        cv2.rectangle(eyes, (x, y), (x + w, y + h), (0, 0, 255), 4)

    cv2.imshow("Eye Detection", eyes)

eye()

cv2.waitKey(0)
cv2.destroyAllWindows()
