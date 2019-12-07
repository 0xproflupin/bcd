#fill VOCDevkit'i' for ith fold, with corresponding jpeg and annotations


import os
import subprocess
from sklearn.model_selection import KFold
import numpy as np

arr = []
with open('/home/anvit/Desktop/filelist.txt') as f:
	for l in f:
		arr.append(l[:-1])

arr.sort()
arr = np.array(arr)
np.random.seed(1)
np.random.shuffle(arr)

kf = KFold(n_splits=10)
spl = kf.split(arr)
i = 1
for x,y in spl:
	string = "/home/anvit/Desktop/VOCdevkit_"+str(i)+"/VOC2007/ImageSets/trainval.txt"
	trainval = open(string,'w')
	for k in arr[x]:
		trainval.write(k+"\n")
		string1 = "/home/anvit/Desktop/VOCdevkit/VOC2007/Annotations/"+k+".xml"
		string2 = "/home/anvit/Desktop/VOCdevkit_"+str(i)+"/VOC2007/Annotations/"
		subprocess.call(['cp',string1,string2])
		string3 = "/home/anvit/Desktop/VOCdevkit/VOC2007/JPEGImages/"+k+".png"
		string4 = "/home/anvit/Desktop/VOCdevkit_"+str(i)+"/VOC2007/JPEGImages/"
		subprocess.call(['cp',string3,string4])
	trainval.close()

	#for l in arr[y]:
		#Make test set for each from here, when reqd
	i = i + 1
