#Make trainval
import os

tv = open('/home/anvit/Desktop/VOCdevkit1/VOC2007/ImageSets/trainval.txt','w')
for file in os.listdir('/home/anvit/Desktop/VOCdevkit1/VOC2007/JPEGImages/'):
	tv.write(file[:-4]+"\n")
tv.close()