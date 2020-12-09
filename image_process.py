import cv2
import numpy as np

# 入力画像を読み込み
img = cv2.imread("uchitane_near.png")


# グレースケール変換
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

cv2.imwrite("/image/imageoutput_gray/uchitane_near_gray.png", gray)

# 方法2(OpenCVで実装)
dst = cv2.Canny(gray, 100, 200)

cv2.imwrite("/image/imageoutput_filta/uchitane_near_filta.png", dst)
