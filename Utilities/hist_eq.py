'''
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("/home/anvit/Desktop/Data/DDSM/All_resized_jpegs_removed_black/A_1108_1.LEFT_CC.jpg", cv2.IMREAD_GRAYSCALE)
img_enhanced = cv2.equalizeHist(img)
plt.imshow(img_enhanced, cmap='gray'), plt.axis("off")
plt.show()
'''

import numpy as np
import os
import cv2
for file in os.listdir("/home/anvit/Desktop/Data/DDSM/Normal/nimagesjpg_removed_black_resized/"):
	img = cv2.imread('/home/anvit/Desktop/Data/DDSM/Normal/nimagesjpg_removed_black_resized/'+file,0)
	clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
	cl1 = clahe.apply(img)
	cv2.imwrite('/home/anvit/Desktop/Data/DDSM/Normal/nimagesjpg_removed_black_resized_enhanced/'+file, cl1)
