import os
import numpy as np
from PIL import Image
import xml.etree.ElementTree as ET
from pascal_voc_writer import Writer
import math
import glob

os.chdir("/home/anvit/Desktop/Data/AIIMS_Data/smallmass_xml/")
for xml in glob.glob("*.xml"):

	print(xml, xml[:-3]+"png")
	img = Image.open("/home/anvit/Desktop/Data/AIIMS_Data/smallmass_png/" + xml[:-3] + "png")
	width, height = img.size
	img_resized = Image.open("/home/anvit/Desktop/Data/AIIMS_Data/smallmass_png_resized/" + xml[:-3] + "png")
	width_resized, height_resized = img_resized.size
	print(width, width_resized)
	ratio = float(width_resized)/width
	print(ratio)

	try:
		writer = Writer("/home/anvit/Desktop/Data/AIIMS_Data/smallmass_png_resized/" + xml[:-3] + "png", width_resized, height_resized)
		tree = ET.parse("/home/anvit/Desktop/Data/AIIMS_Data/smallmass_xml/" + xml)
		root = tree.getroot()
		bboxdict = []

		for obj in root.findall('object'):
			flag = 0
			label = "MALIGNANT"
			'''
			label = obj.find('name').text
			#print(label)
			if label == "mass" or label == "architectural distortion" or label == "AD" or label == "ad":
				label = "MASS"
			elif label == "cal" or label == "calcification" or label == "ca":
				label = "CALCIFICATION"
			elif label == "birads2" or label == "birads 2" or label == "BIRADS 2" or label == "birads3" or label == "birads 3" or label == "BIRADS 3":
				label = "BENIGN"
			elif label == "birads4" or label == "birads 4" or label == "BIRADS 4" or label == "Birads 4" or label == "BIRADS4" or label == "BIRADS 4C" or label == "birads 5" or label == "BIRADS 5" or label == "BIRADS5":
				label = "MALIGNANT"
			else:
				continue
			'''

			bbox = obj.find('bndbox')
			xmin = float(bbox[0].text)
			ymin = float(bbox[1].text)
			xmax = float(bbox[2].text)
			ymax = float(bbox[3].text)

			'''
			if label == "MASS" or label == "CALCIFICATION":
				canbelabels = ["BENIGN", "MALIGNANT"]
			if label == "BENIGN" or label == "MALIGNANT":
				canbelabels = ["MASS", "CALCIFICATION"]

			print("current box")
			print(xmin, ymin, xmax, ymax)
			print("boxes till now")
			print(bboxdict)

			for box in bboxdict:
				#print(box[0] - xmin)
				#print(box[1] - ymin)
				#print(box[2] - xmax)
				#print(box[3] - ymax)
				if abs(box[0] - xmin) <= 100.0 and abs(box[1] - ymin) <= 100.0 and abs(box[2] - xmax) <= 100.0 and abs(box[3] - ymax) <= 100.0 and box[4] in canbelabels and box[5] == 0:
					xmin = box[0]
					ymin = box[1]
					xmax = box[2]
					ymax = box[3]
					box[5] = 1
					print("Found same box")
					xmin*=ratio
					ymin*=ratio
					xmax*=ratio
					ymax*=ratio
					xmin=int(math.ceil(xmin))
					ymin=int(math.ceil(ymin))
					xmax=int(math.ceil(xmax))
					ymax=int(math.ceil(ymax))
					writer.addObject(label,xmin,ymin,xmax,ymax)
					writer.addObject(box[4],xmin,ymin,xmax,ymax)
					flag = 1
			if flag == 0:
				bboxdict.append([xmin, ymin, xmax, ymax, label, 0])
			'''


			xmin*=ratio
			ymin*=ratio
			xmax*=ratio
			ymax*=ratio
			print(xmin, ymin, xmax, ymax)
			xmin=int(math.ceil(xmin))
			ymin=int(math.ceil(ymin))
			xmax=int(math.ceil(xmax))
			ymax=int(math.ceil(ymax))
			print(xmin,ymin,xmax,ymax)
			writer.addObject(label,xmin,ymin,xmax,ymax)
		writer.save("/home/anvit/Desktop/Data/AIIMS_Data/smallmass_xml_resized/" + xml)
	except:
		continue
