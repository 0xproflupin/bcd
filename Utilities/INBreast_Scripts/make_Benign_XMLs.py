import numpy as np
import math
from PIL import Image 
from pascal_voc_writer import Writer
import xml.etree.ElementTree as ET

fil = open("/home/anvit/Desktop/RetinaNet/pytorch-retinanet/csv_annotation_INbreast_with_benign_normal.csv", 'r')
lines = fil.readlines()
lines = lines[1:]


d = {}

for line in lines:
	arr = line.split(',')
	if arr[0] not in d:
		if arr[-1] == "0\n":
			d[arr[0]] = 0
		elif arr[-1] == "1\n":
			d[arr[0]] = 1
	else:
		if arr[-1] == "0\n":
			d[arr[0]] = max(0, d[arr[0]])
		elif arr[-1] == "1\n":
			d[arr[0]] = max(1, d[arr[0]])

for key in d:
	if(d[key] == 0):
		#IMG IS BENIGN
		print(key)
		reqd = key.split('/')
		name = reqd[-1]
		print(name)
		xml = name[:-4] +".xml"
		tree = ET.parse("/home/anvit/Desktop/Data/INbreast/XML_VOC_resized/" + xml)
		root = tree.getroot()
		img = Image.open('/home/anvit/Desktop/Data/INbreast/equalized_PNG_394_resized_ambiremoved/' + xml[:-4] + ".png")
		width, height = img.size
		print(len(root.findall('object')))

		if(len(root.findall('object'))>0):
			writer = Writer('/home/anvit/Desktop/Data/INbreast/equalized_PNG_394_resized_ambiremoved/' + xml[:-4] + ".png", width, height)
			print(xml[:-4] + ".png")

			for obj in root.findall('object'):	
				box = obj.find('bndbox')
				xmin = int(float(box.find('xmin').text))
				xmax = int(float(box.find('xmax').text))
				ymin = int(float(box.find('ymin').text))
				ymax = int(float(box.find('ymax').text))
				print("BENIGN",xmin,ymin,xmax,ymax)
				writer.addObject("BENIGN",xmin,ymin,xmax,ymax)

			writer.save("/home/anvit/Desktop/Data/INbreast/XML_VOC_resized_BEN/" + xml)