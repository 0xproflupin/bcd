import os
import csv
import xml.etree.ElementTree as ET
from sets import Set

filenames_mass = Set([])
filenames_cal = Set([])

with open('/home/anvit/py-faster-rcnn_mass/detections_40000_mass_malignant_all_only_Inbreast.csv', 'rb') as inp, open('/home/anvit/py-faster-rcnn_mass/detections_40000_mass_malignant_all_only_Inbreast_calremoved.csv', 'wb') as out:
	writer = csv.writer(out)
	cnt = 0
	for row in csv.reader(inp):
		if(cnt == 0):
			cnt += 1
			continue
		name = row[1]
		print(name)
		annot_name = name[:-4]+".xml"
		tree = ET.parse('/home/anvit/Desktop/Data/INbreast/XML_VOC_resized/'+annot_name)
		root = tree.getroot()
		for obj in root.findall('object'):
			typename = obj.find('name').text
			if(typename == "mass"):
				writer.writerow(row)
				filenames_mass.add(name)
				break

with open('/home/anvit/py-faster-rcnn_cal/detections_40000_cal_malignant_all_only_Inbreast.csv', 'rb') as inp, open('/home/anvit/py-faster-rcnn_cal/detections_40000_cal_malignant_all_only_Inbreast_massremoved.csv', 'wb') as out:
	writer = csv.writer(out)
	cnt = 0
	for row in csv.reader(inp):
		if(cnt == 0):
			cnt += 1
			continue
		name = row[1]
		print(name)
		annot_name = name[:-4]+".xml"
		tree = ET.parse('/home/anvit/Desktop/Data/INbreast/XML_VOC_resized/'+annot_name)
		root = tree.getroot()
		for obj in root.findall('object'):
			typename = obj.find('name').text
			if(typename == "calcification"):
				writer.writerow(row)
				filenames_cal.add(name)
				break

filenames = filenames_mass | filenames_cal
print(len(filenames))	#341
#This means there are 2 files in INbreast which neither have mass nor has cal, has only CLUSTERS

os.chdir('/home/anvit/Desktop/Data/INbreast/XML_VOC_resized/')
arr = []
for xml in os.listdir('.'):
	arr.append(xml[:-4])

for i in arr:
	if i+".png" not in filenames:
		print(i)

