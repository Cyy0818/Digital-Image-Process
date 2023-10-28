import numpy as np
import cv2
def Image_R(img):
    r=[]#用于存储R值
    w,h,d = img.shape
    new_img_R = np.zeros((w, h, d), dtype=np.uint8)
    #因为图像是BGR分布的，通过切片操作，提取R通道的颜色值
    for i in range(w):
        for j in range(h):
            r.append(img[i][j][2:])
    count = 0
    #将R通道的颜色值存入新图像中，返回新图像
    for i in range(w):
        for j in range(h):
            new_img_R[i][j][2:] = r[count]
            count = count + 1
    return new_img_R

def Image_B(img):
    b = []
    w, h, d = img.shape
    new_img_B = np.zeros((w, h, d), dtype=np.uint8)
    for i in range(w):
        for j in range(h):
            b.append(img[i][j][:1])
    count = 0
    for i in range(w):
        for j in range(h):
            new_img_B[i][j][:1] = b[count]
            count = count + 1
    return new_img_B

def Image_G(img):
    g = []
    w, h, d = img.shape
    new_img_G = np.zeros((w, h, d), dtype=np.uint8)
    for i in range(w):
        for j in range(h):
            g.append(img[i][j][1:2])

    count = 0
    for i in range(w):
        for j in range(h):
            new_img_G[i][j][1:2] = g[count]
            count = count + 1
    return new_img_G

def Turn_Gray(img):
    new_img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    return new_img_gray
def RGB_Merge_equalize_histogram(image):
    #对R，G，B通道分别进行直方图均衡化，然后整合到一起
    new_img_eq = cv2.merge([cv2.equalizeHist(image[:, :, 0]), cv2.equalizeHist(image[:, :, 1]), cv2.equalizeHist(image[:, :, 2])])
    return new_img_eq
def HSL_equalize_histogram(image):
    #转换到HSL空间
    new_img_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    # 对亮度分量V做直方图均衡化
    new_img_hsv[:, :, 2] = cv2.equalizeHist(new_img_hsv[:, :, 2])
    # 转换回RGB空间
    new_img_eq = cv2.cvtColor(new_img_hsv, cv2.COLOR_HSV2BGR)
    return new_img_eq

def Green_Screen(image,background):
    # 统一图像大小
    w,h,_= background.shape
    image = cv2.resize(image, (w, h))
    #转换到HSL空间操作
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    # 计算图像绿值的范围，则除了图像人物以外，其他均为白色255，图像人物为黑色0
    mask = cv2.inRange(hsv, (35, 43, 46), (77, 255, 255))
    # 取反操作，绿幕区域变为黑色（0），其他区域变为白色（255）
    cv2.bitwise_not(mask,mask)
    cv2.imwrite("mask.jpg", mask)
    # 背景与人物保留的部分不同，再次取反
    mask_inv = cv2.bitwise_not(mask, 1)
    # 与原图与操作，得到白色部分在原图的样子
    person = cv2.bitwise_and(image, image, mask=mask)
    # 反转模板与背景图与操作，得到反转模板部分在背景的样子
    background = cv2.bitwise_and(background, background, mask=mask_inv)
    cv2.imwrite("person.png", person)
    cv2.imwrite("background.png", background)
    result = cv2.add(person, background)
    cv2.imwrite("result.jpg", result)



if __name__ == '__main__':
    araras_img = cv2.imread("araras.jpg")
    sky_img = cv2.imread("sky.bmp")
    mush_img = cv2.imread("mushroom.png")
    tree_img = cv2.imread("tree.jpg")
    person_img = cv2.imread("green.png")


    #提取RGB通道的值
    Image_R(araras_img)
    Image_G(araras_img)
    Image_B(araras_img)

    #RGB灰度图
    cv2.imwrite("img_R_Gray.jpg",Turn_Gray(Image_R(araras_img)))
    cv2.imwrite("img_G_Gray.jpg", Turn_Gray(Image_G(araras_img)))
    cv2.imwrite("img_B_Gray.jpg", Turn_Gray(Image_B(araras_img)))

    #RGB通道直方图均衡化
    cv2.imwrite("RGB_Sky_eq_img.jpg", RGB_Merge_equalize_histogram(sky_img))
    cv2.imwrite("RGB_Mush_eq_img.jpg", RGB_Merge_equalize_histogram(mush_img))

    #HSL 对L直方图均衡化
    cv2.imwrite("HSL_Sky_eq_img.jpg", HSL_equalize_histogram(sky_img))
    cv2.imwrite("HSL_Mush_eq_img.jpg",HSL_equalize_histogram(mush_img))

    Green_Screen(person_img, tree_img)


