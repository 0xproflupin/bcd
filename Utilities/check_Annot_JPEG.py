#check if annotations and jpegImages have the same files

import numpy
import os

os.chdir('/home/anvit/Desktop/VOCdevkit/VOC2007/JPEGImages/')
#count=0
for x in os.listdir('.'):
	k = x[:-4]+".xml"
	cnt = 0
	for f in os.listdir('/home/anvit/Desktop/VOCdevkit/VOC2007/Annotations/'):
		if(f!=k):
			cnt+=1
	if(cnt == 588)		
		print("CRY")
	# flag = False
	# for f in os.listdir('/home/anvit/Desktop/VOCdevkit/VOC2007/Annotations/'):
	# 	if(f==k):
	# 		flag = True
	# if(flag==False):
	# 	print("CRY")


