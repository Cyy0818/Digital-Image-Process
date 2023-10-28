import cv2
import numpy as np

# 读取图像并进行二值化处理
image = cv2.imread("connect.png", cv2.IMREAD_GRAYSCALE)
_, connect_img = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# 定义8连通结构元素
connectivity = 8
connectivity_structure = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

# 形态学腐蚀操作，用于断开相邻的连通域
eroded_image = cv2.erode(connect_img, connectivity_structure, iterations=1)

# 形态学膨胀操作，用于合并同一个连通域内的分散区域
dilated_image = cv2.dilate(eroded_image, connectivity_structure, iterations=1)

# 连通域标记
_, markers = cv2.connectedComponents(dilated_image, connectivity)

# 随机生成颜色
colors = np.random.randint(0, 255, size=(np.max(markers) + 1, 3), dtype=np.uint8)

# 将标记区域上色
colored_markers = colors[markers]

# 保存标记后的图像
cv2.imwrite("connected_components.png", colored_markers)
