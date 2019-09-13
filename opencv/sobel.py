import cv2 as cv
import numpy as np

input_img = cv.imread('D://images//bin1.png')
print(type(input_img))
print(input_img.shape)
cv.imshow('input image',input_img)

gary_img=cv.cvtColor(input_img,cv.COLOR_RGB2GRAY)
cv.imshow('gary img',gary_img)

# sobel x方向边缘检测
edgesx = cv.Sobel(gary_img,cv.CV_16SC1,1,0)
edgesx = cv.convertScaleAbs(edgesx)
cv.imshow('sobel edgex',edgesx)

# sobel y方向边缘检测
edgesy = cv.Sobel(gary_img,cv.CV_16S,0,1)
edgesy = cv.convertScaleAbs(edgesy) #16位short转成uint8型[0,255]
cv.imshow('sobel edgey',edgesy)

# sobel边缘检测
edges = cv.Sobel(gary_img,-1,1,1)
edges = cv.convertScaleAbs(edges)
cv.imshow('sobel edge',edges)

cv.waitKey(0)
cv.destroyAllWindows()