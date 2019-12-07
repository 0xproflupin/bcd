#INbreast_107_mass.csv
#INbreast_313_mass.csv

import os
import pandas as pd 
import numpy
import csv

c = pd.read_csv("/home/anvit/py-faster-rcnn_mass/detections_40000_mass_malignant_all_only_Inbreast_calremoved.csv")
c = numpy.array(c)
filenames_mass = c[:,1]
filenames_mass = set(filenames_mass)

with open('/home/anvit/Desktop/Data/INbreast/INbreast_341.csv','rb') as inp, open('/home/anvit/Desktop/Data/INbreast/INbreast_107_onlymass.csv', 'wb') as out:
	writer = csv.writer(out)
	cnt = 0
	for row in csv.reader(inp):
		if(cnt == 0):
			cnt += 1
			writer.writerow(row)	#Write header row
			continue
		name = row[5]
		if name+".png" in filenames_mass:
			writer.writerow(row)

c = pd.read_csv("/home/anvit/py-faster-rcnn_cal/detections_40000_cal_malignant_all_only_Inbreast_massremoved.csv")
c = numpy.array(c)
filenames_cal = c[:,1]
filenames_cal = set(filenames_cal)

with open('/home/anvit/Desktop/Data/INbreast/INbreast_341.csv','rb') as inp, open('/home/anvit/Desktop/Data/INbreast/INbreast_313_onlycal.csv', 'wb') as out:
	writer = csv.writer(out)
	cnt = 0
	for row in csv.reader(inp):
		if(cnt == 0):
			cnt += 1
			writer.writerow(row)	#Write header row
			continue
		name = row[5]
		if name+".png" in filenames_cal:
			writer.writerow(row)