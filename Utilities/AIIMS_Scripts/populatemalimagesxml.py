import os
import subprocess
import xml.etree.ElementTree as ET

xmls = os.listdir("/home/anvit/Desktop/Data/AIIMS_Data/Both_labelled/AllSetsXMLs_withmasscal_resized/")
for xml in xmls:
	tree = ET.parse("/home/anvit/Desktop/Data/AIIMS_Data/Both_labelled/AllSetsXMLs_withmasscal_resized/" + xml)
	root = tree.getroot()
	for obj in root.findall("object"):
		if obj[0].text == "MALIGNANT":
			str1 = "/home/anvit/Desktop/Data/AIIMS_Data/Both_labelled/AllSetsPNG_resized/" + xml[:-4] + ".png"
			str2 = "/home/anvit/Desktop/Data/AIIMS_Data/Both_labelled/malimagesxml/"
			subprocess.call(['cp', str1, str2])
			str3 = "/home/anvit/Desktop/Data/AIIMS_Data/Both_labelled/AllSetsXMLs_withmasscal_resized/" + xml
			str4 = "/home/anvit/Desktop/Data/AIIMS_Data/Both_labelled/malimagesxml/"
			subprocess.call(['cp', str3, str4])
			break

