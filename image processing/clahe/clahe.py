import cv2
import matplotlib.pyplot as plt

img = cv2.imread('timg.jpg',0) #直接读为灰度图像
res = cv2.equalizeHist(img)  #灰度图直方图均衡化

clahe = cv2.createCLAHE(clipLimit=2,tileGridSize=(10,10)) #clipLimit颜色对比度的阈值， titleGridSize进行像素均衡化的网格大小
cl1 = clahe.apply(img)

plt.imshow(img)

# plt.subplot(131),plt.imshow(img,'gray')  #图像灰度化
# plt.subplot(132),plt.imshow(res,'gray')
# plt.subplot(133),plt.imshow(cl1,'gray')

plt.show()

