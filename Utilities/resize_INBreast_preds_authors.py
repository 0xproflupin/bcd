import pandas as pd
import numpy as np
import os
import pickle
from PIL import Image
import xml.etree.ElementTree as ET

#f = pd.read_csv("/home/anvit/Desktop/inbreast_predictions.tsv", sep = "\t")

f = open("/home/anvit/Desktop/inbreast_predictions.tsv", 'r')
lines = f.read().splitlines()
#arr = np.array(f)
#print(arr)
lines = lines[1:]

#names = arr[0]
#scores = arr[1]
#xmin = arr[2]
#xmax = arr[3]
#ymin = arr[4]
#ymax = arr[5]


fil = open("./FasterRCNN_output_files/INbreast_author_preds.txt", 'w')

#newnames = []
for line in lines:
	#res = name.split("_")
	#filename = res[0] + ".png"
	#newnames.append(filename)

	arr = line.split("\t")
	name = arr[0].split("_")
	print(name[0])
	im = Image.open('/home/anvit/Desktop/Data/INbreast/equalized_PNG_410_resized/' + name[0] + '.png')
	width, height = im.size
	im2 = Image.open("/home/anvit/Desktop/Data/INbreast/equalized_PNG_410/"+ name[0] + ".png")
	#root = tree.getroot()
	#w = float(root.find("size")[0].text)
	w,h = im2.size
	ratio = width/w
	xmin = float(arr[2])*ratio
	xmax = float(arr[3])*ratio
	ymin = float(arr[4])*ratio
	ymax = float(arr[5])*ratio
	fil.write(name[0]+".png,"+ str(xmin) +","+ str(ymin) +","+ str(xmax) +","+ str(ymax) + ","+ arr[1] + "\n")

f.close()
fil.close()


