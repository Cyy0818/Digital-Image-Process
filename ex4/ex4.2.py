import cv2
import numpy as np

def sharpen_image(img):
    laplacian_kernel = np.array([[0, -1, 0],
                                  [-1, 4, -1],
                                  [0, -1, 0]])
    sharpened_image = np.zeros_like(img, dtype=np.float32)
    h, w,_ = img.shape
    for i in range(1, h - 1):
        for j in range(1, w - 1):
            sharpened_image[i, j] = np.sum(img[i - 1:i + 2, j - 1:j + 2] * laplacian_kernel)
    sharpened_image = np.uint8(np.clip(sharpened_image, 0, 255))
    return sharpened_image

if __name__ == '__main__':
    img=cv2.imread("blurry_moon.tif")
    new_moon = sharpen_image(img)
    cv2.imwrite("bulrry_sharped_moon.jpg", new_moon)

