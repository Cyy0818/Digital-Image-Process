import numpy as np
import cv2
#读入所要用的letter图片
img=cv2.imread('letter.jpg')
#为了能够更清晰的识别图片字母的轮廓，将其首先转化为灰度图
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#再通过灰度图转化为二值图
ret,img_thresh=cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)
#用findcontours函数对二值图进行轮廓的检测，并保留父子集关系
contours, hierarchy = cv2.findContours(img_thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#对于提取出的轮廓，用boundingRect函数获得能包围每个轮廓的最小矩形，并获取其在图片上的xy轴坐标和宽度高度
for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    #保留宽度大于20，高度大于30的拆分轮廓
    if w > 20 and h > 30:
        cropped = img[y:y+h, x:x+w]
        cv2.imwrite(f'{x}_{y}.jpg', cropped)
img_1=cv2.imread('141_409.jpg')
img_2=cv2.imread('200_408.jpg')
img_7=cv2.imread('214_504.jpg')
img_9=cv2.imread('347_503.jpg')
img_5=cv2.imread('403_409.jpg')
img_C=cv2.imread('193_26.jpg')
img_H=cv2.imread('81_123.jpg')
img_E=cv2.imread('361_27.jpg')
img_N=cv2.imread('493_123.jpg')
img_Y=cv2.imread('368_313.jpg')
img_U=cv2.imread('481_218.jpg')
img_G=cv2.imread('496_26.jpg')
img_A=cv2.imread('39_27.jpg')
#用reszie函数将所有图片的大小统一为img_1的大小，便于后续使用hstack方法进行拼接
img_2 = cv2.resize(img_2, (img_1.shape[1], img_1.shape[0]))
img_7 = cv2.resize(img_7, (img_1.shape[1], img_1.shape[0]))
img_9 = cv2.resize(img_9, (img_1.shape[1], img_1.shape[0]))
img_5 = cv2.resize(img_5, (img_1.shape[1], img_1.shape[0]))
img_C = cv2.resize(img_C, (img_1.shape[1], img_1.shape[0]))
img_H = cv2.resize(img_H, (img_1.shape[1], img_1.shape[0]))
img_E = cv2.resize(img_E, (img_1.shape[1], img_1.shape[0]))
img_N = cv2.resize(img_N, (img_1.shape[1], img_1.shape[0]))
img_Y = cv2.resize(img_Y, (img_1.shape[1], img_1.shape[0]))
img_U = cv2.resize(img_U, (img_1.shape[1], img_1.shape[0]))
img_G = cv2.resize(img_G, (img_1.shape[1], img_1.shape[0]))
img_A = cv2.resize(img_A, (img_1.shape[1], img_1.shape[0]))
number = np.hstack((img_2, img_1, img_1,img_2,img_2,img_7,img_9,img_5))
name = np.hstack((img_C,img_H,img_E,img_N,img_Y,img_U,img_Y,img_A,img_N,img_G))
number=cv2.resize(number,(name.shape[1],name.shape[0]))
combine=np.concatenate([number, name], axis=0)
cv2.imwrite('Combined Image.jpg', combine)
cv2.imshow('Combined Image', combine)
cv2.waitKey(0)
cv2.destroyAllWindows()