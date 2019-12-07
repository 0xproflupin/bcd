import xml.etree.ElementTree as ET
import numpy as np
import os
cnt = 0
for xml in os.listdir("/home/anvit/Desktop/Data/AIIMS_Data/BIRADS_Both_combined/XML_BEN_MAL/"):
	tree = ET.parse("/home/anvit/Desktop/Data/AIIMS_Data/BIRADS_Both_combined/XML/" + xml)
	root = tree.getroot()
	if len(root.findall('object')) == 0:
		print(xml)
		cnt+=1
print(cnt)