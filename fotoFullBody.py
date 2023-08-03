import cv2
import imutils

hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())


image = cv2.imread('foto/foto.jpg')



humans, _ = hog.detectMultiScale(image, winStride=(5, 5), padding=(3, 3),scale=1.05)

print('Human Detected : ', len(humans))

for (x, y, w, h) in humans:
    cv2.rectangle(image, (x, y),(x + w, y + h),  (0, 0, 255), 2)

cv2.imshow("Image", image)
cv2.waitKey(0)

cv2.destroyAllWindows()