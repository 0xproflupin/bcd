import os
import xml.etree.ElementTree as ET

files = os.listdir("/home/anvit/Desktop/Data/AIIMS_Data/newdata/")
f = open("/home/anvit/Desktop/RetinaNet/pytorch-retinanet/csv_annotation_AIIMS_newdata.csv", 'w')


pngs = []
xmls = []
for file in files:
	if file[-3:] == "png":
		pngs.append(file)
	elif file[-3:] == "xml":
		xmls.append(file)

dnames = {}
for xml in xmls:
	tree = ET.parse("/home/anvit/Desktop/Data/AIIMS_Data/newdata/" + xml)
	root = tree.getroot()
	for obj in root.findall("object"):
		name = obj[0].text
		if name not in dnames:
			dnames[name] = 1
		else:
			dnames[name] += 1
		if name == "4" or name == "5" or name == "0" or name == "0+cal" or name == "cal":
			newname = "1"
		if name == "3":
			newname = "0"
		bbox = obj[4]
		xmin = bbox[0].text
		ymin = bbox[1].text
		xmax = bbox[2].text
		ymax = bbox[3].text
		f.write("/home/anvit/Desktop/Data/AIIMS_Data/newdata/" + xml[:-3] + "png" + "," + xmin + "," + ymin + "," + xmax + "," + ymax + "," + newname + "\n")
print(dnames)

