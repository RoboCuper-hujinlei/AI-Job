#### 阈值处理

res, dst = cv2.threshold(src, thresh, maxval, type)

thresh: 阈值，一般取127。
maxval: 当像素值超过阈值(或小于阈值， 根据type来决定), 所赋予的值
type: 二值化操作的类型， 包含以下5种类型：

    cv2.THRESH_BINARY       
    cv2.THRESH_BINARY_INV
    cv2.THRESH_TRUNC
    cv2.THRESH_TOZERO
    cv2.THRESH_TOZERO_INV