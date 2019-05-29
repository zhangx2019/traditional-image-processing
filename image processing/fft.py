import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('opencv.png',0)
f=np.fft.fft2(img)  #傅里叶变换得到图谱，一般来说，低频过滤得图像主体
fshift=np.fft.fftshift(f)  #平移频谱到图像中央
magnitude_specturm=20*np.log(np.abs(fshift)) #将频谱转换成db
plt.subplot(121),plt.imshow(img,cmap='gray')
plt.title('Input Image'),plt.xticks([]),plt.yticks([])
plt.subplot(122),plt.imshow(magnitude_specturm,cmap='gray')
plt.title('Magnitude Specturm'),plt.xticks([]),plt.yticks([])
plt.show()
