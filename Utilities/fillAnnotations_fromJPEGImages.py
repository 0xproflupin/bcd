import os
import subprocess

os.chdir('/home/anvit/Desktop/VOCdevkit1/VOC2007/JPEGImages')

for file in os.listdir('.'):
	string1 = '/home/anvit/Desktop/VOCdevkit1/VOC2007/Annotations/'+file[:-4]+".xml"
	string2 = '/home/anvit/Desktop/VOCdevkit1/VOC2007/Anot_temp/'
	subprocess.call(['cp',string1,string2])
