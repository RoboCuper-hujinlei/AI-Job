import cv2
import os


"""
   滤波算法主要包括： 均值滤波，高斯滤波，中值滤波和双边滤波
"""
def cvshow(name, img):
    cv2.imshow(name, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
img_path = "../data/cat.jpg"
img = cv2.imread(img_path)
cvshow("img", img)

# 均值滤波
img_blur = cv2.blur(img, (5, 5))
cv2.imshow("img_blur", img_blur)
cv2.waitKey(0)
cv2.destroyAllWindows()



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



