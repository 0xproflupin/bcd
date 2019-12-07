import os
import csv

os.chdir('/home/anvit/Desktop/Data/INbreast/XML_VOC_resized/')
arr = []
for xml in os.listdir('.'):
	arr.append(xml[:-4])

with open('/home/anvit/Desktop/Data/INbreast/Original_Inbreast/INbreast.csv','rb') as inp, open('/home/anvit/Desktop/Data/INbreast/INbreast_343.csv', 'wb') as out:
	writer = csv.writer(out)
	cnt = 0
	for row in csv.reader(inp):
		if(cnt == 0):
			cnt += 1
			continue
		name = row[5]
		if name in arr:
			writer.writerow(row)
