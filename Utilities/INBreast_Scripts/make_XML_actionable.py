
import os
import numpy as np
import pickle
import xml.etree.ElementTree as ET
from pascal_voc_writer import Writer
from PIL import Image


one = os.listdir("/home/anvit/Desktop/Data/INbreast/XML_VOC_resized/")
two = os.listdir("/home/anvit/Desktop/Data/INbreast/XML_VOC_malignant_BIRADS_resized/")

d = pickle.load(open("actionable_info.pk", 'rb'))

print(d)
print(d["20588308"])

'''
mam = []

for file in one:
	if file not in two:
		actionable = d[file[:-4]]
		if actionable == 1:
			tree = ET.parse("/home/anvit/Desktop/Data/INbreast/XML_VOC_resized/" + file)
			root = tree.getroot()
			num_objects = len(root.findall('object'))
			cnt = 0
			for obj in root.findall('object'):
				if obj[0].text == "mass" or obj[0].text == "cluster":
					cnt += 1

			if cnt == 1:
				try:
					im = Image.open('/home/anvit/Desktop/Data/INbreast/equalized_PNG_394_resized_ambiremoved/' + file[:-3] + "png")
				except:
					print(file[:-3]+"png")
					print("h")
					continue
				width, height = im.size
				writer = Writer('/home/anvit/Desktop/INbreast/equalized_PNG_394_resized_ambiremoved/' + file[:-3] + "png", width, height)
				for obj in root.findall('object'):
					if obj[0].text == "mass" or obj[0].text == "cluster":
						name = "ACTIONABLE"
						xmin = obj[4][0].text
						ymin = obj[4][1].text
						xmax = obj[4][2].text
						ymax = obj[4][3].text
						writer.addObject(name, xmin, ymin, xmax, ymax)
						writer.save('/home/anvit/Desktop/Data/INbreast/XML_Actionable_temp/' + file[:-3] + "xml")
						break
			if cnt > 1:
				mam.append(file)

print(mam)
'''
