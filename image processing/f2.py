import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('dave.png',0)
laplacian = cv.Laplacian(img,cv.CV_64F)
'''
在正常图片中边界比较清晰因此方差会比较大；而在模糊图片中包含的边界信息很少，所以方差会较小。
用图片的1个通道用以下3x3的核进行卷积，然后计算输出的方差，如果方差小于一定值则图片视为模糊。如100
cv.CV_64F 输出图像的深度(数据类型)，可使用-1，与原图像保持一致np.uint8
'''
sobelx=cv.Sobel(img,cv.CV_64F,1,0,ksize=5)
'''
第一个参数是需要处理的图像；
第二个参数是图像的深度，-1表示采用的是与原图像相同的深度。目标图像的深度必须大于等于原图像的深度；
dx和dy表示的是求导的阶数，0表示这个方向上没有求导，一般为0、1、2
ksize是Sobel算子的大小，必须为1、3、5、7
'''
sobely=cv.Sobel(img,cv.CV_64F,0,1,ksize=5)
plt.subplot(2,2,1),plt.imshow(img,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,2),plt.imshow(laplacian,cmap = 'gray')
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,3),plt.imshow(sobelx,cmap = 'gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,4),plt.imshow(sobely,cmap = 'gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])
plt.show()