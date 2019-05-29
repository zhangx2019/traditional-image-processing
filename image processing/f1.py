import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('opencv.png',0) #直接读为灰度图像，'/others/opencv.png'
for i in range(2000):  #高斯模糊，增加噪声
    temp_x=np.random.randint(0,img.shape[0])
    temp_y=np.random.randint(0,img.shape[1])
    img[temp_x][temp_y]=255

blur_1=cv2.GaussianBlur(img,(5,5),0) #这里(5, 5)表示高斯矩阵的长与宽都是5，标准差取0时OpenCV会根据高斯矩阵的尺寸自己计算
blur_2=cv2.medianBlur(img,5) #img表示当前的图片，5表示当前的方框尺寸

plt.subplot(131),plt.imshow(img,'gray')#默认彩色，另一种彩色bgr
plt.subplot(132),plt.imshow(blur_1,'gray')
plt.subplot(133),plt.imshow(blur_2,'gray')
plt.show()
