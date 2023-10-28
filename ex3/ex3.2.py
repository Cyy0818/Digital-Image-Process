import cv2
import numpy as np
import time
def equalize_histogram(image):
    hist, bins = np.histogram(image.flatten(), 256, [0, 256])
    cdf = hist.cumsum()
    cdf_normalized = (cdf * 255 / cdf[-1])
    equalized_img = cdf_normalized[image]

    return equalized_img


if __name__ == '__main__':
    img1 = cv2.imread('school.png', cv2.IMREAD_GRAYSCALE)
    start_time = time.time()
    eq_image = equalize_histogram(img1)
    end_time = time.time()
    cv2.imwrite('school_eq.jpg', eq_image)
    execution_time = end_time - start_time
    print(f"手动直方图均衡化school所用时间：{execution_time} 秒")
    start_time = time.time()
    eq_image = cv2.equalizeHist(img1)
    cv2.imwrite('school_cveq.jpg', eq_image)
    print(f"cv库直方图均衡化school所用时间：{execution_time} 秒")

    img2 = cv2.imread('hill.jpg', cv2.IMREAD_GRAYSCALE)
    start_time = time.time()
    eq_image = equalize_histogram(img2)
    end_time = time.time()
    cv2.imwrite('hill_eq.jpg', eq_image)
    execution_time = end_time - start_time
    print(f"手动直方图均衡化hill所用时间：{execution_time} 秒")
    start_time = time.time()
    eq_image = cv2.equalizeHist(img2)
    cv2.imwrite('hill_cveq.jpg', eq_image)
    print(f"cv库直方图均衡化hill所用时间：{execution_time} 秒")

    img3 = cv2.imread('baby.png', cv2.IMREAD_GRAYSCALE)
    start_time = time.time()
    eq_image = equalize_histogram(img3)
    end_time = time.time()
    cv2.imwrite('baby_eq.jpg', eq_image)
    execution_time = end_time - start_time
    print(f"手动直方图均衡化hill所用时间：{execution_time} 秒")
    start_time = time.time()
    eq_image = cv2.equalizeHist(img3)
    cv2.imwrite('baby_cveq.jpg', eq_image)
    print(f"cv库直方图均衡化hill所用时间：{execution_time} 秒")


