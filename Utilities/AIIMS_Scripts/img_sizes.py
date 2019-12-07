import os
import numpy as np
from PIL import Image

for img in os.listdir("/home/anvit/Desktop/Data/AIIMS_Data/BIRADS_Both_combined/PNG/"):
	im = Image.open("/home/anvit/Desktop/Data/AIIMS_Data/BIRADS_Both_combined/PNG/" + img)
	print(im.size)

