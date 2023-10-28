import cv2
import numpy as np
import time
def Mid_Filter(img, size):
    w, h, d = img.shape
    new_img = np.zeros((w, h, d), dtype=np.uint8)
    for i in range(w):
        for j in range(h):
            matrix = []
            for x in range(i - size // 2, i + size // 2 + 1):
                for y in range(j - size // 2, j + size // 2 + 1):
                    if x >= 0 and x < w and y >= 0 and y < h:
                        matrix.append(img[x, y])
            median_value = np.median(matrix)
            new_img[i, j] = median_value
    return new_img

def Avg_Filter(img, size):
    w, h, d = img.shape
    new_img = np.zeros((w, h, d), dtype=np.uint8)
    for i in range(w):
        for j in range(h):
            matrix = []
            for x in range(i - size // 2, i + size // 2 + 1):
                for y in range(j - size // 2, j + size // 2 + 1):
                    if x >= 0 and x < w and y >= 0 and y < h:
                        matrix.append(img[x, y])
            median_value = np.average(matrix)
            new_img[i, j] = median_value
    return new_img


if __name__ == '__main__':
    print("输入滤波器的大小(n*n)：")
    size = int(input())
    space = cv2.imread('Space.jpg')
    pcb = cv2.imread('pcb.png')
    mona = cv2.imread('Mona.jpg')

    # 中值滤波并记录时间
    start_time = time.time()
    newmid_space = Mid_Filter(space, size)
    end_time = time.time()
    print("space中值滤波时间:", end_time - start_time, "秒")

    start_time = time.time()
    newmid_mona = Mid_Filter(mona, size)
    end_time = time.time()
    print("mona中值滤波时间:", end_time - start_time, "秒")

    start_time = time.time()
    newmid_pcb = Mid_Filter(pcb, size)
    end_time = time.time()
    print("pcb中值滤波时间:", end_time - start_time, "秒")

    cv2.imwrite('space_mid.jpg', newmid_space)
    cv2.imwrite('Mona_mid.jpg', newmid_mona)
    cv2.imwrite('Pcb_mid.png', newmid_pcb)

    # 均值滤波并记录时间
    start_time = time.time()
    newavg_space = Avg_Filter(space, size)
    end_time = time.time()
    print("space均值滤波时间:", end_time - start_time, "秒")

    start_time = time.time()
    newavg_mona = Avg_Filter(mona, size)
    end_time = time.time()
    print("mona均值滤波时间:", end_time - start_time, "秒")

    start_time = time.time()
    newavg_pcb = Avg_Filter(pcb, size)
    end_time = time.time()
    print("pcb均值滤波时间:", end_time - start_time, "秒")

    cv2.imwrite('space_avg.jpg', newavg_space)
    cv2.imwrite('Mona_avg.jpg', newavg_mona)
    cv2.imwrite('Pcb_avg.png', newavg_pcb)