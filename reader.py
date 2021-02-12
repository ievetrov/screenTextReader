import time
import numpy as np
import pyscreenshot as ImageGrab
import cv2
import os
import pytesseract
 
 
filename = 'Image.png'
x = 1
last_time = time.time()
 
while(True):
    screen =  np.array(ImageGrab.grab(bbox=(20, 75, 614, 475)))
    # print('loop took {} seconds'.format(time.time()-last_time))
    last_time = time.time()
    # cv2.imshow('window',cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
    cv2.imwrite(filename, screen)
    x = x + 1
    # print(x)
    img = cv2.imread('Image.png')
    text = pytesseract.image_to_string(img)
    print(text)

    # cv2.destroyAllWindows
