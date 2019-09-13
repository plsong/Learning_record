import cv2 as cv
import numpy as np


input_img = cv.imread('D://images//test.png')
print(type(input_img))
print(input_img.shape)
cv.imshow('input image',input_img)



gary_img=cv.cvtColor(input_img,cv.COLOR_RGB2GRAY)
cv.imshow('gary img',gary_img)

w,h=gary_img.shape

# Laplacian算子
res  =np.zeros((w,h))#初始化一个与原图相同尺寸的图片
print(res[0,0])
cv.imshow('res',res)

# boberts 算子
roberts_x = np.array([[0,1,0],[1,-4,1],[0,1,0]])
roberts_y = np.array([[1,1,1],[1,-8,1],[1,1,1]])
for x in range(1,w-1):
    for y in range(1,h-1):

        sub=[[gary_img[x-1,y-1],gary_img[x,y-1],gary_img[x+1,y-2]],[gary_img[x-1,y],gary_img[x,y],gary_img[x+1,y]],[gary_img[x-1,y+1],gary_img[x,y+1],gary_img[x+1,y+1]]]
        sub_array = np.array(sub)

        var_x = sum(sum(sub_array*roberts_x))
        var_y = sum(sum(sub_array*roberts_y))

        var = abs(var_x) + abs(var_y)
        res[x,y] = var

res = cv.convertScaleAbs(res)
cv.imshow('var',res)

cv.waitKey(0)
cv.destroyAllWindows()
