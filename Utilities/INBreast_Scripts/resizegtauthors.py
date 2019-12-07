import os
from PIL import Image
import xml.etree.ElementTree as ET

fil = open("gtauthors.txt", 'r')

lines = fil.readlines()
lines = lines[1:]

f = open('resizedgtauthors.txt','w')
for line in lines:
	arr = line.split("\t")
	name = arr[0].split("_")
	im = Image.open('./equalized_PNG_343_resized/' + name[0] + '.png')
	width, height = im.size
	tree = ET.parse("./XML_VOC/"+ name[0] + ".xml")
	root = tree.getroot()
	w = float(root.find("size")[0].text)
	ratio = width/w
	new1 = float(arr[1])*ratio
	new2 = float(arr[2])*ratio
	new3 = float(arr[3])*ratio
	new4 = float(arr[4])*ratio
	f.write(name[0]+" "+ str(new1) +" "+ str(new2) +" "+ str(new3) +" "+ str(new4) +"\n")

fil.close()
f.close()
