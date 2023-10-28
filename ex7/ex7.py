import cv2
import numpy as np

# 手动实现基本的全局阈值处理
def basic_threshold(image, threshold):
    thresholded_image = np.where(image > threshold, 255, 0)
    return thresholded_image.astype(np.uint8)

# 手动实现OTSU算法
def otsu_threshold(image):
    hist = cv2.calcHist([image], [0], None, [256], [0, 256])
    hist_norm = hist.ravel() / hist.sum()
    Q = hist_norm.cumsum()
    bins = np.arange(256)
    fn_min = np.inf
    thresh = -1
    for i in range(1, 256):
        p1, p2 = np.hsplit(hist_norm, [i])
        q1, q2 = Q[i], Q[255]-Q[i]
        if q1 == 0 or q2 == 0:
            continue
        b1, b2 = np.hsplit(bins,[i])
        m1, m2 = np.sum(p1 * b1) / q1, np.sum(p2 * b2) / q2
        v1, v2 = np.sum(((b1 - m1) ** 2) * p1) / q1, np.sum(((b2 - m2) ** 2) * p2) / q2
        fn = v1 * q1 + v2 * q2
        if fn < fn_min:
            fn_min = fn
            thresh = i
    return thresh, basic_threshold(image, thresh)

if __name__ == '__main__':

    rice_img = cv2.imread("rice.tiff", cv2.IMREAD_GRAYSCALE)
    finger_img = cv2.imread("finger.tif", cv2.IMREAD_GRAYSCALE)
    poly_img = cv2.imread("poly.tif", cv2.IMREAD_GRAYSCALE)

    rice_threshold_value, rice_otsu = otsu_threshold(rice_img)
    finger_threshold_value, finger_otsu = otsu_threshold(finger_img)
    poly_threshold_value, poly_otsu = otsu_threshold(poly_img)

    rice_basic = basic_threshold(rice_img,128)
    finger_basic = basic_threshold(finger_img,128)
    poly_basic = basic_threshold(poly_img,128)

    cv2.imwrite("rice_otsu.jpg", rice_otsu)
    cv2.imwrite("finger_otsu.jpg", finger_otsu)
    cv2.imwrite("poly_otsu.jpg", poly_otsu)

    cv2.imwrite("rice_basic.jpg", rice_basic)
    cv2.imwrite("finger_basic.jpg", finger_basic)
    cv2.imwrite("poly_.basic.jpg", poly_basic)

    print(f"OTSU算法阈值（rice.tif）：{rice_threshold_value}")
    print(f"OTSU算法阈值（finger.tif）：{finger_threshold_value}")
    print(f"OTSU算法阈值（poly.tif）：{poly_threshold_value}")
