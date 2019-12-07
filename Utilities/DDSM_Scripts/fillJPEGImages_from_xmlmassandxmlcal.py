import os
import subprocess

os.chdir('/home/anvit/Desktop/Data/DDSM/XML_Ben_Mal/xml_cal')
for file in os.listdir('.'):
	tofind = file[:-4]+".jpg"
	string1 = '/home/anvit/Desktop/Data/DDSM/All_resized_jpegs/'+tofind
	string2 = '/home/anvit/Desktop/VOCdevkit1/VOC2007/JPEGImages/'
	subprocess.call(['cp',string1,string2])
