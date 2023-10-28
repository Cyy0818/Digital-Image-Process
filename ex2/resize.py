import numpy as np
import cv2
import time

#最邻近插值
def nearest(img,size):
 originH,originW,_=img.shape
 newW=originW*size
 newH=originH*size
 newimg=np.zeros((newH, newW, 3), dtype=np.uint8)
 for i in range(newH-1):
  for j in range(newW-1):
   originH=round(i/size)
   originW=round(j/size)
   newimg[i, j]=img[originH, originW]
 return newimg

#双线性插值
def bilinear(img,size):
 originH, originW, _ = img.shape
 newH, newW = int(originH * size), int(originW * size)
 newimg = np.zeros((newH, newW, 3), dtype=np.uint8)
 for i in range(newH-1):
  for j in range(newW-1):
   x, y = i / size, j / size
   x1, y1 = int(x), int(y)
   x2, y2 = min(x1 + 1, originH - 1), min(y1 + 1, originW - 1)
   newimg[i, j] = img[x1, y1] * (x2 - x) * (y2 - y) + img[x1, y2] * (x2 - x) * (y - y1) + img[x2, y1] * (x - x1) * ( y2 - y) + img[x2, y2] * (x - x1) * (y - y1)
 return newimg


if __name__ == '__main__':
 img1 = cv2.imread('test1.jpg')
 img2 = cv2.imread('test2.jpg')

 print("输入缩放方式")
 print('1.最邻近插值')
 print('2.双线性插值')
 mode = int(input())
 print("输入缩放倍数")
 n = int(input())

 start_time = time.time()
 img_resize = cv2.resize(img1, (0, 0), fx=n, fy=n)
 end_time = time.time()
 cv2.imwrite('resized img1.jpg', img_resize)
 print(f"cv2.resize执行时间：{end_time - start_time} 秒")

 if mode == 1:
  start_time = time.time()
  imgtest = nearest(img1, n)
  end_time = time.time()
  cv2.imwrite("NearestResized img1.jpg", imgtest)
  print(f"最邻近插值执行时间：{end_time - start_time} 秒")

 elif mode == 2:
  start_time = time.time()
  imgtest = bilinear(img1, n)
  end_time = time.time()
  cv2.imwrite("BilinearResized img1.jpg", imgtest)
  print(f"双线性插值执行时间：{end_time - start_time} 秒")





