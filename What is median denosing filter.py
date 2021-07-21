# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 20:03:56 2021

@author: abc
"""

import cv2
import numpy as np
from skimage import io, img_as_float
from skimage.filters import median

#read our image and convert it into floating point value
img_salt_pepper_noise =cv2.imread("BSE_salt_pepper.jpg", 0)

#activate our image
img = img_salt_pepper_noise

#define median filter in opencv
median_using_cv2 = cv2.medianBlur(img, 3)

#define median filter in skimage
from skimage.morphology import disk
median_using_skimage = median(img, disk(3), mode="constant", cval=0.0)

#show our images
cv2.imshow("Original image", img)
cv2.imshow("cv2 filter", median_using_cv2)
cv2.imshow("skimage filter", median_using_skimage)
cv2.waitKey(0)
cv2.destroyAllWindows()


    
    