import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img=cv.imread('opencv.png',0)
kernel_1=np.ones((5,5),np.float32)/25 #平滑卷积核,均值滤波
dst_1=cv.filter2D(img,-1,kernel_1) #-1为图像深度自适应
kernel_2=np.array([[0,-1,0],[-1,5,-1],[0,-1,0]],np.float32) #Laplacian锐化
dst_2=cv.filter2D(img,-1,kernel_2) #-1为图像深度自适应
plt.subplot(131),plt.imshow(img,'gray')
plt.title('Original'),plt.xticks([]),plt.yticks([])
plt.subplot(132),plt.imshow(dst_1,'gray')
plt.title('Averaging'),plt.xticks([]),plt.yticks([])
plt.subplot(133),plt.imshow(dst_2,'gray')
plt.title('Laplacian'),plt.xticks([]),plt.yticks([])
plt.show()