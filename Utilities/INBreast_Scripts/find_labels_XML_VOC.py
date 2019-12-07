import os
import numpy as np
import xml.etree.ElementTree as ET

d = {}

for xml in os.listdir("../XML_VOC_resized/"):
	print(xml)
	tree = ET.parse("../XML_VOC_resized/" + xml)
	root = tree.getroot()
	for obj in root.findall("object"):
		name = obj[0].text
		if name not in d:
			d[name] = 1
		else:
			d[name] += 1

for key in d:
	print(key)
