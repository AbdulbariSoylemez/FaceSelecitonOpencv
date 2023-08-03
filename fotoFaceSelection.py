import cv2

def face():
    grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

    face = face_detector.detectMultiScale(grey, scaleFactor=1.025, minNeighbors=3, maxSize=(40, 40), minSize=(30, 30))# Haar yüz algılama yöntemini kullanır.

    for (x, y, w, h) in face:
        print("x:", x, "y:", y, "w:", w, "h:", h)

        # Corrected the cv2.rectangle() call
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
        cv2.circle(img, center=(x + w // 2, y + h // 2), radius= w// 2, color=(0, 255, 0), thickness=3)

    cv2.imshow("Face", img)



img = cv2.imread("foto/foto1.jpeg")
face()
cv2.waitKey(0)
cv2.destroyAllWindows()
