'''
    图像阈值操作
'''
import cv2
import matplotlib.pyplot as plt
import numpy as np

'''
res, dst = cv2.threshold(src, thresh, maxval, type)

thresh: 阈值，一般取127。
maxval: 当像素值超过阈值(或小于阈值， 根据type来决定), 所赋予的值
type: 二值化操作的类型， 包含以下5种类型：

  - cv2.THRESH_BINARY              二值法， 超过阈值thresh部分取最大值，否则取0
  - cv2.THRESH_BINARY_INV          _INV(反转)，超过阈值thresh部分取0，否则取最大值
  - cv2.THRESH_TRUNC                trunc 大于阈值部分取阈值(thresh)，否则不变
  - cv2.THRESH_TOZERO               tozero 大于阈值部分不变，否则设为0
  - cv2.THRESH_TOZERO_INV           _INV （反转）大于阈值部分设为0，否则不变

'''
def cvshow(name, img):
    cv2.imshow(name, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


img = cv2.imread('../data/cat.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cvshow("gray", gray)

ret, thresh1 = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)      # 二值法， 超过阈值thresh部分取最大值，否则取0
ret, thresh2 = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)  # _INV(反转)，超过阈值thresh部分取0，否则取最大值
ret, thresh3 = cv2.threshold(gray, 127, 255, cv2.THRESH_TRUNC)       # trunc 大于阈值部分取阈值(thresh)，否则不变
ret, thresh4 = cv2.threshold(gray, 127, 255, cv2.THRESH_TOZERO)      # tozero 大于阈值部分不变，否则设为0
ret, thresh5 = cv2.threshold(gray, 127, 255, cv2.THRESH_TOZERO_INV)  # _INV （反转）大于阈值部分设为0，否则不变

print("ret", ret)   # 返回的阈值

titles = ['original image', 'THRESH_BINARY', 'THRESH_BINARY_INV', 'THRESH_TRUNC', 'THRESH_TOZERO', 'THRESH_TOZERO_INV']
images = [cv2.cvtColor(img, cv2.COLOR_BGR2RGB), thresh1, thresh2, thresh3, thresh4, thresh5]

for i in range(6):
    plt.subplot(2, 3, i+1),
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])
plt.show()





