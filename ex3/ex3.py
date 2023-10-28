import cv2
import numpy as np
import time
#不查表
def Gamma(img, g):
    w, h, d = img.shape
    newimg = np.zeros((w, h, d), dtype=np.uint8)
    for i in range(w):
        for j in range(h):
            #运用伽马变换的公式，将每个像素值转换为灰度值，用指数函数的形式，提升或降低不同部分的亮度
            newimg[i, j] = np.power(((img[i, j]+0.5)/255), g)*255
    return newimg
#查表
def LUT_Gamma(img, g):
    LUT = np.zeros(255 + 1, dtype=np.uint8)
    for i in range(255 + 1):
            #创建每个像素值归一化转换构对应的表
       LUT[i] = np.power(((i+0.5)/255), g)*255
    output_image = LUT[img]
    return output_image

if __name__ == '__main__':
    print("输入gamma值：")
    g = float(input())
    dark_img = cv2.imread('dark.jpg')
    start_time = time.time()
    dark_gamma = Gamma(dark_img, g)
    end_time=time.time()
    cv2.imwrite("dark_gamma.jpg", dark_gamma)
    print(f"dark.jpg未查表的伽马变换所用时间：{end_time - start_time} 秒")
    start_time = time.time()
    dark_gamma = LUT_Gamma(dark_img, g)
    end_time = time.time()
    cv2.imwrite("dark_gamma_LUT.jpg", dark_gamma)
    print(f"dark.jpg 查表的伽马变换所用时间：{end_time - start_time} 秒")
    print("输入gamma值：")
    g = float(input())
    light_img = cv2.imread('light.tif')
    start_time = time.time()
    light_gamma = Gamma(light_img, g)
    end_time = time.time()
    cv2.imwrite("light_gamma.jpg", light_gamma)
    print(f"light.tif未查表的伽马变换所用时间：{end_time - start_time} 秒")
    start_time = time.time()
    light_gamma = LUT_Gamma(light_img, g)
    end_time = time.time()
    cv2.imwrite("light_gamma_LUT.jpg", light_gamma)
    print(f"light.tif查表的伽马变换所用时间：{end_time - start_time} 秒")
