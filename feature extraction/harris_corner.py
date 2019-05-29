import numpy as np
import cv2 as cv

filename='./data/chessboard.png'
img=cv.imread(filename)
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY) #图像灰度化
gray=np.float32(gray)
dst=cv.cornerHarris(gray,2,3,0.04)
'''
cv2.cornerHarris(src, blockSize, ksize, k, dst=None, borderType=None)
src：数据类型为 float32 的输入图像
blockSize：角点检测中考虑的区域大小
ksize：Sobel求导中使用的窗口大小
k：Harris 角点检测方程中的自由参数，取值参数为 [0.04 0.06]
dst：输出图像
borderType：边界的类型
'''
# cv.namedWindow("Image")
# cv.imshow("Image", gray)
dst=cv.dilate(dst,None) #result is dilated for marking the corners, not important
img[dst>0.01*dst.max()]=[0,0,255]
'''
Threshold for an optimal value, it may vary depending on the image
设定一个阈值，当大于这个阈值分数的都可以判定为角点
'''
cv.imshow('dst',img)
if cv.waitKey(0)&0xff==27:
'''
cv2.waitKey(delay)返回值：
1、等待期间有按键：返回按键的ASCII码(比如：Esc的ASCII码为27)
2、等待期间没有按键：返回 -1
'''
    cv.destroyAllWindows()
