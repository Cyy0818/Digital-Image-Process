import cv2
import numpy as np
def erode(image,size):
    kernel = np.ones((size, size), dtype=np.uint8)
    new_image = cv2.erode(image, kernel, iterations=1)
    return new_image

def dilate(image,size):
    kernel = np .ones((size,size), dtype=np.uint8)
    new_image = cv2.dilate(image, kernel, iterations=1)
    return new_image

def Open(image,size):
    return dilate(erode(image, size), size)

def Close(image,size):
    return erode(dilate(image, size), size)



if __name__ == '__main__':
    wire_img = cv2.imread("wire.tif")
    shape_img = cv2.imread("shape.tif")
    cv2.imwrite("wire_erode.jpg", erode(wire_img,8))
    cv2.imwrite("shape_erode.jpg", erode(shape_img, 20))
    cv2.imwrite("shape_dilate.jpg",dilate(shape_img,20))
    cv2.imwrite("shape_Open.jpg", Open(shape_img, 20))
    cv2.imwrite("shape_Close.jpg", Close(shape_img, 20))

    connect_img = cv2.imread("connect.png", cv2.IMREAD_GRAYSCALE)
    _, connect_img = cv2.threshold(connect_img, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    temp_connect=Open(connect_img,3)
    #标记联通区域
    _, markers = cv2.connectedComponents(temp_connect, 8)
    colors = np.random.randint(0, 255, size=(np.max(markers) + 1, 3), dtype=np.uint8)
    # 将标记区域上色
    colored_markers = colors[markers]
    # 保存标记后的图像
    cv2.imwrite("connected_components.png", colored_markers)
