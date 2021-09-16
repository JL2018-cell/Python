import cv2
import numpy as np

def cropImg(num):
 img = cv2.imread('Slide' + str(num) + '.JPG')
 h, w, c = img.shape
 print('Image', num, ':')
 print('h =,', h, ', w =', w)
 x = 90
 y = 100
 dh = int(960/2) - 120
 dw = 380
 cv2.imwrite('Pr' + str(num) + '-a.JPG', img[x:x+dh, y:y+dw])
 cv2.imwrite('Pr' + str(num) + '-b.JPG', img[x:x+dh, y+380:y+dw+380])

for i in range(19):
  cropImg(i+1)
