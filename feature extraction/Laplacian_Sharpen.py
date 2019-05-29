# -*- coding:utf-8 -*-

from PIL import Image  # PIL：Python Imaging Library，已经是Python平台事实上的图像处理标准库
import numpy as np

# 读入原图像
img = Image.open('lena.jpg')
img.show()

# 为减少计算维度，将图像转为灰度图
img_gray = img.convert('L')
img_gray.show()

# 得到转换后灰度图的像素矩阵
img_arr = np.array(img_gray)
h = img_arr.shape[0]
w = img_arr.shape[1]

# 拉普拉斯算子锐化图像，用二阶微分
new_img_arr = np.zeros((h, w))
# 拉普拉斯锐化后的图像像素矩阵
for i in range(2, h - 1):
    for j in range(2, w - 1):
        new_img_arr[i][j] = img_arr[i + 1][ j] + img_arr[i - 1][j] +\
                      img_arr[i][j + 1] + img_arr[i][j - 1] - 4 * img_arr[i][j]

# 拉普拉斯锐化后图像和原图像相加
laplace_img_arr = np.zeros((h, w))
# 拉普拉斯锐化图像和原图像相加所得的像素矩阵
for i in range(0, h):
    for j in range(0, w):
        laplace_img_arr[i][j] = new_img_arr[i][j] + img_arr[i][j]

img_laplace1 = Image.fromarray(np.uint8(new_img_arr))
'''
以数组的形式创建图像，PIL.image.fromarray(obj,mode=None)
obj - 图像的数组，类型可以是numpy.array()
mode - 如果不给出，会自动判断
uint8是无符号八位整型，表示范围是[0, 255]的整数
'''
img_laplace1.show()

img_laplace2 = Image.fromarray(np.uint8(laplace_img_arr))
img_laplace2.show()
