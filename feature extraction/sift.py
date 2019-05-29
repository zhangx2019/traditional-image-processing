import numpy as np
import cv2 as cv

img=cv.imread('./data/home.jpg')
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
sift=cv.xfeatures2d.SIFT_create()
#sift.detect()可以在图像中找到关键点
kp=sift.detect(gray,None)
img=cv.drawKeypoints(gray,kp,img)
#drawKeypoints(image, keypoints, outImage, color=None, flags=None)

cv.imshow('SIFT',img)
# cv.imwrite('sift_keypoints.jpg',img)
cv.waitKey(0)
cv.destroyAllWindows()

