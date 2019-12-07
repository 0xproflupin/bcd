#Check whether AllXML and XML_VOC contains same files
import os

os.chdir('/home/anvit/Desktop/INbreast/AllXML/')
xml = []
for file in os.listdir('.'):
	xml.append(file)
os.chdir('/home/anvit/Desktop/INbreast/newVOC_XML/')
cnt = 1
for f in os.listdir('.'):
	if(f not in xml):
		print("ERROR")
	else:
		print("OK")
		print(cnt)
		cnt = cnt + 1
