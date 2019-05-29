import numpy as np
import cv2 as cv

img=cv.imread('./data/butterfly.jpg',0)

surf=cv.xfeatures2d.SURF_create(400)
#初始Hessian矩阵的阈值
surf.setHessianThreshold(50000)
#指定Hessian矩阵的阈值
kp, des=surf.detectAndCompute(img,None)
img2=cv.drawKeypoints(img,kp,None,(255,0,0),4)
'''
drawKeypoints(image, keypoints, outImage, color=None, flags=None)
image:也就是原始图片
keypoints：从原图中获得的关键点，这也是画图时所用到的数据
outputimage：输出
flags：绘图功能的标识设置
color：颜色设置，通过修改（b,g,r）的值,更改画笔的颜色，b=蓝色，g=绿色，r=红色。
'''
cv.imshow('surf',img2)
cv.waitKey(0)
cv.destroyAllWindows()





