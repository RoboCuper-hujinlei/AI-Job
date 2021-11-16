import cv2
import matplotlib.pyplot as plt
import numpy as np
import random


def cvshow(name, img):
    cv2.imshow(name, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


class Noise:
    def __init__(self):
        pass
    
    def sp_noise(self, image, prob):
        """
        随机添加椒盐噪声
        prob: 噪声比例
        """
        output = np.zeros(image.shape, np.uint8)
        thres = 1 - prob
        
        for i in range(image.shape[0]):     # h
            for j in range(image.shape[1]):
                rdn = random.random()
                
                if rdn < prob:
                    output[i][j] = 0
                elif rdn > thres: 
                    output[i][j] = 255
                else:
                    output[i][j] = image[i][j]
        return output


    def gaussian_noise(self, image, mean=0, var=0.001):
        """给图像添加均值为mean和方差为var的高斯噪声
        
        Args:
            mean (int, optional): [description]. Defaults to 0.
            var (float, optional): [description]. Defaults to 0.001.
        """
        image = np.array(image/255, dtype=float)
        noise = np.random.normal(mean, var ** 0.5, image.shape)
        print("shape", image.shape, noise.shape)
        
        out = image + noise
        print(out[:5, :, :])
        
        if out.min() < 0:
            low_clip = -1.
        else:
            low_clip = 0.
            
        out = np.clip(out, low_clip, 1.0)
        out = np.uint8(out * 255)
        
        return out
    
    
def main():
    
    img = cv2.imread("../data/cat.jpg")
    noise = Noise()
    sp_img = noise.sp_noise(img, 0.08)
    cvshow("sp_noise cat", sp_img)

    # 均值滤波
    img_blur = cv2.blur(img, (5, 5))
    cv2.imshow("img_blur", img_blur)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    gaussian_img = noise.gaussian_noise(img, 0, 0.001)
    cvshow('gaussian_img', gaussian_img)
    
    
main()


def GaussianBlur():
       # cv2.GaussianBlur(src, ksize, sigmaX, dst=None, sigmaY=None, borderType=None)
   """
   GaussianBlur（src，ksize，sigmaX [，dst [，sigmaY [，borderType]]]）-> dst
      ——src输入图像；图像可以具有任意数量的通道，这些通道可以独立处理，但深度应为CV_8U，CV_16U，CV_16S，CV_32F或CV_64F。
      ——dst输出图像的大小和类型与src相同。
      ——ksize高斯内核大小。 ksize.width和ksize.height可以不同，但​​它们都必须为正数和奇数，也可以为零，然后根据sigma计算得出。
      ——sigmaX X方向上的高斯核标准偏差。
      ——sigmaY Y方向上的高斯核标准差；如果sigmaY为零，则将其设置为等于sigmaX；如果两个sigmas为零，则分别从ksize.width和ksize.height计算得出；为了完全控制结果，而不管将来可能对所有这些语义进行的修改，建议指定所有ksize，sigmaX和sigmaY。
   """