import os
import subprocess

arr = os.listdir("/home/anvit/Desktop/Data/DDSM/mal_cal_nonblack_jpg/")
for i in range(len(arr)):
	if(i % 5 == 0):
		str1 = "/home/anvit/Desktop/Data/DDSM/mal_cal_nonblack_jpg/" + arr[i]
		str2 = "/home/anvit/Desktop/Data/DDSM/mal_cal_nonblack_jpg_reduced/"
		subprocess.call(['cp', str1, str2])
		str3 = "/home/anvit/Desktop/Data/DDSM/mal_cal_nonblack_xml/" + arr[i][:-3] + "xml"
		str4 = "/home/anvit/Desktop/Data/DDSM/mal_cal_nonblack_xml_reduced/"
		subprocess.call(['cp', str3, str4])
