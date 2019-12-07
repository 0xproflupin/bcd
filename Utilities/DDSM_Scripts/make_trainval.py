import os
tv = open('/home/anvit/Desktop/VOCdevkit1/VOC2007/ImageSets/trainval.txt','w')
os.chdir('/home/anvit/Desktop/VOCdevkit1/VOC2007/JPEGImages/')
for f in os.listdir('.'):
	tv.write(f[:-4]+"\n")
tv.close()
