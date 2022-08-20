import cv2
import numpy as np
import matplotlib.pyplot as plt

original = cv2.imread('1024.jpg')
img = cv2.imread('1024.jpg', 0)
template = cv2.imread('zidong.bmp', 0)

h, w = template.shape[:2]

methods = ['cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCOEFF', 'cv2.TM_SQDIFF_NORMED', 'cv2.TM_SQDIFF',
           'cv2.TM_CCORR', 'cv2.TM_CCORR_NORMED']
ret = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(ret)

draw_img = original.copy()
ret = cv2.rectangle(draw_img, max_loc, (max_loc[0]+w, max_loc[1]+h), (0, 0, 255), 2)
print(max_loc)
print(int(max_loc[0]+w/2), int(max_loc[1]+h/2))
cv2.imshow('ret', ret)
cv2.waitKey(0)
cv2.destroyAllWindows()