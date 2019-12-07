import os
import numpy as np
import xml.etree.ElementTree as ET
import subprocess


nonblack = os.listdir("/home/anvit/Desktop/Data/DDSM/All_resized_jpegs_removed_black_withnormal_enhanced/")

d = []
for xml in os.listdir("/home/anvit/Desktop/Data/DDSM/XML_Ben_Mal/xml_all/"):
	tree = ET.parse("/home/anvit/Desktop/Data/DDSM/XML_Ben_Mal/xml_all/" + xml)
	root = tree.getroot()
	for obj in root.findall('object'):
		if(obj.find('name').text == 'MALIGNANT'):
			bbox = obj.find('bndbox')
			xmin = bbox[0].text
			ymin = bbox[1].text
			xmax = bbox[2].text
			ymax = bbox[3].text
			try:
				tree2 = ET.parse("/home/anvit/Desktop/Data/DDSM/XML_Mass_Cal/allxml/" + xml)
				root2 = tree2.getroot()
				flag = 0
				for o in root2.findall('object'):
					#print(o.find('name').text)
					if(o.find('name').text == 'CALCIFICATION'):
						bb = o.find('bndbox')
						if(xml[:-3] + "jpg" in nonblack and bb[0].text == xmin and bb[1].text == ymin and bb[2].text == xmax and bb[3].text == ymax):
							d.append(xml)
							str1 = "/home/anvit/Desktop/Data/DDSM/All_resized_jpegs_removed_black_withnormal_enhanced/" + xml[:-3] + "jpg"
							str2 = "/home/anvit/Desktop/Data/DDSM/mal_cal_nonblack_jpg/"
							subprocess.call(['cp', str1, str2])
							str3 = "/home/anvit/Desktop/Data/DDSM/XML_Ben_Mal/xml_all/" + xml
							str4 = "/home/anvit/Desktop/Data/DDSM/mal_cal_nonblack_xml/"
							subprocess.call(['cp', str3, str4])
							flag = 1
							break
				if flag == 1:
					break
			except:
				continue
print(len(d))
print(d)

