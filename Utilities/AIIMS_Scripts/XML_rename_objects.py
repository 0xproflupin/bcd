import xml.etree.ElementTree as ET
import numpy as np
import os
from PIL import Image 
from pascal_voc_writer import Writer

for xml in os.listdir("/home/anvit/Desktop/Data/AIIMS_Data/BIRADS_Both_combined/XML/"):	
	tree = ET.parse("/home/anvit/Desktop/Data/AIIMS_Data/BIRADS_Both_combined/XML/" + xml)
	root = tree.getroot()
	img = Image.open('/home/anvit/Desktop/Data/AIIMS_Data/BIRADS_Both_combined/PNG/' + xml[:-4] + ".png")
	width, height = img.size
	print(len(root.findall('object')))
	if(len(root.findall('object'))>0):
		writer = Writer('/home/anvit/Desktop/Data/AIIMS_Data/BIRADS_Both_combined/PNG/' + xml[:-4] + ".png", width, height)
		print(xml[:-4] + ".png")
		for obj in root.findall('object'):

			if(obj.find('name').text == 'BIRADS 2' or obj.find('name').text == 'birads 2' or obj.find('name').text == 'BIRADS 3' or obj.find('name').text == 'birads 3', obj.find('name').text == 'BENIGN'):
				name = "BENIGN"
				box = obj.find('bndbox')
				xmin = int(float(box.find('xmin').text))
				xmax = int(float(box.find('xmax').text))
				ymin = int(float(box.find('ymin').text))
				ymax = int(float(box.find('ymax').text))
				print(name,xmin,ymin,xmax,ymax)
				writer.addObject(name,xmin,ymin,xmax,ymax)

			elif(obj.find('name').text == 'BIRADS 4' or obj.find('name').text == 'birads 4' or obj.find('name').text == 'BIRADS 5' or obj.find('name').text == 'birads 5', obj.find('name').text == 'MALIGNANT'):
				name = "MALIGNANT"
				box = obj.find('bndbox')
				xmin = int(float(box.find('xmin').text))
				xmax = int(float(box.find('xmax').text))
				ymin = int(float(box.find('ymin').text))
				ymax = int(float(box.find('ymax').text))
				print(name,xmin,ymin,xmax,ymax)
				writer.addObject(name,xmin,ymin,xmax,ymax)
			
		writer.save("/home/anvit/Desktop/Data/AIIMS_Data/BIRADS_Both_combined/XML_BEN_MAL/" + xml)

