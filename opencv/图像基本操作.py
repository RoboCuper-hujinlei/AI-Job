import cv2
import matplotlib.pyplot as plt
import numpy as np
# %matplotlib inline  # 不需要plt.show


def cvshow(name, img):
    cv2.imshow(name, img)
    cv2.waitKey(0)
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


# 仅保留R通道
copy_img[:, :, 0] = 0
copy_img[:, :, 1] = 0
cvshow('R', copy_img)

def padding():
    '''
        填充方法：
        cv2.BORDER_REPLICATE：复制法，复制最边缘的像素填充
        cv2.BORDER_REFLECT：反射法，对感兴趣的像素在两边进行复制，gfedcb|abcdefgh|gfedcba
        cv2.BORDER_REFLECT_101：反射法，也就是以最边缘像素为轴对称
        cv2.BORDER_WRAP：外包装法 cdefgh|abcdefgh|abcdefg
        cv2.BORDER_CONSTANT：敞亮法，常数值填充
    '''
    
    # plt 用RGB格式显示，opencv用BGR格式显示
    img = cv2.imread("../data/dog.jpg") 
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    top_size, bottom_size, left_size, right_size  = (50, 50, 50, 50)    # 指定上下左右填充的值
    # 不同的填充方法, copy Make Border通过复制已有元素 制作边界 填充
    replicate = cv2.copyMakeBorder(img,  top_size, bottom_size, left_size, right_size, borderType=cv2.BORDER_REPLICATE) # replicate复制
    reflect = cv2.copyMakeBorder(img,  top_size, bottom_size, left_size, right_size, borderType=cv2.BORDER_REFLECT) # reflect 
    reflect101 = cv2.copyMakeBorder(img,  top_size, bottom_size, left_size, right_size, borderType=cv2.BORDER_REFLECT_101) # reflect101 
    wrap = cv2.copyMakeBorder(img, top_size, bottom_size, left_size, right_size, borderType=cv2.BORDER_WRAP)    # wrap

    constant = cv2.copyMakeBorder(img, top_size, bottom_size, left_size, right_size, borderType=cv2.BORDER_CONSTANT, value=0)    # 常量法 常数填充

    import matplotlib.pyplot as plt

    plt.subplot(231), plt.imshow(img, 'gray'), plt.title('original')
    plt.subplot(232), plt.imshow(replicate, 'gray'), plt.title('BORDER_REPLICATE')
    plt.subplot(233), plt.imshow(reflect, 'gray'), plt.title('BORDER_REFLECT')
    plt.subplot(234), plt.imshow(reflect101, 'gray'), plt.title('BORDER_REFLECT_101')
    plt.subplot(235), plt.imshow(wrap, 'gray'), plt.title('BORDER_WRAP')
    plt.subplot(236), plt.imshow(constant, 'gray'), plt.title('BORDER_CONSTANT')
    plt.show()

# part 8 数值计算
def image_compute():
    img_cat = cv2.imread("../data/cat.jpg") 
    img_dog = cv2.imread("../data/dog.jpg") 
    
    print('\n\nimg_cat\n', img_cat[:5, :, 0])
    img_cat2 = img_cat + 10         
    print('img_cat2\n', img_cat2[:5, :, 0])     # 每个位置都加10
    
    # 图像加法：维度相同的图像才能加减运算，每个像素点[0, 255], 越界后会自动 % 256
    print("sum(img_cat, img_cat2): \n", (img_cat + img_cat2)[:5, :, 0])     # 两个图像的像素值相加，等于对256取余(%256). 相加 < 256, 是和；相加 > 256 像素值超了%256
    print("cv2.add: ", cv2.add(img_cat, img_cat))                           # 相加 > 255, 取最大值255；相加 < 256, 取相加的和
    
    cvshow("sum(img_cat, imgcat2): ", img_cat + img_cat2)
    cvshow("cv2.add(img_cat, imgcat2): ", cv2.add(img_cat, img_cat2))       
    
    # 图像融合，叠加
    if img_cat.shape == img_dog.shape:
        # 通过res = α * x1 + β * x2 + b,  α,β是猫和狗两幅图像的权重系数
        res = cv2.addWeighted(img_cat, 0.5, img_dog, 0.5, 10)
        cvshow("img_cat-img_dog ronghe", res)
    else:
        img_cat = cv2.resize(img_cat, (400, 300))
        img_dog = cv2.resize(img_dog, (400, 300))
        res = cv2.addWeighted(img_cat, 0.5, img_dog, 0.5, 10)       # α * x1 + β * x2 + b
        cvshow("img_cat-img_dog ronghe", res)
        
    print(img_cat.shape)
    print(img_dog.shape)
    
    
    
    
    
    
if __name__ == '__main__':
    padding()     # 
    image_compute()     # 图像数值计算、两个图像按比例融合
    