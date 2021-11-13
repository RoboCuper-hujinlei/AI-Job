import cv2
import matplotlib.pyplot as plt
import numpy as np
# %matplotlib inline  # 不需要plt.show


def cvshow(name, img):
    cv2.imshow(name, img)
    cv2.waitKey(1000)
    cv2.destroyAllWindows()

img = cv2.imread('../data/cat.jpg')
print(img.shape)        # (600, 600, 3) dtype=ndarray

img = cv2.imread('../data/dog.jpg', cv2.IMREAD_GRAYSCALE)   # cv2.IMREAD_GRAYSCALE 灰度图
cvshow("cat", img)
print(img.shape)

# 读取视频

def read_video(videopath):
    capture = cv2.VideoCapture(videopath)
    if capture.isOpened():
        open, frame = capture.read()
    else:
        open = False
    
    while open:
        ret, frame = capture.read()
        if frame is None:
            break
        if ret == True:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cv2.imshow('gray', gray)
            if cv2.waitKey(10) & 0xFF == 27:        # cv2.waitKey(delay)，等待delay的时间内有按键，返回按键的ASCII码(ESC的ASCII码为27)。等待期间没有按键返回 -1 
                break                               # 任何二进制数 & 0xFF都是它本身， 27 & 0xFF = 27
    capture.release()
    cv2.destroyAllWindows()     

read_video("../data/person.mp4")

#### 简单截取部分图像
img = cv2.imread("../data/dog.jpg") 
dog = img[0:100, 0:200]     # H W
cvshow('dog', dog)

#### 颜色通道提取

b, g, r = cv2.split(img)        # 法 1
print(b)
print(b.shape)

copy_img = img.copy()
_b, _g, _r = img[:, :, 0], img[:, :, 1], img[:, :, 2]       # 法 2
print(b == _b)


img[:, :, 0] = 0
img[:, :, 1] = 0
cvshow('R', img)


            

    






