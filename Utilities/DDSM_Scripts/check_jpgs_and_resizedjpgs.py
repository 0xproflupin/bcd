import os

os.chdir('/home/anvit/Desktop/Data/DDSM/Malignant/mimagesjpg')
list1 =[]
for file in os.listdir('.'):
	list1.append(file)

os.chdir('/home/anvit/Desktop/Data/DDSM/Malignant/mimagesresized')
list2 =[]
for file in os.listdir('.'):
	list2.append(file)

for i in list1:
	if(i not in list2):
		print(i)