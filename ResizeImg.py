import cv2
import imutils
img = cv2.imread("me.jpg")
resizeImg = imutils.resize(img,width=100)
cv2.imwrite("resizedImageMe.jpg",resizeImg)
