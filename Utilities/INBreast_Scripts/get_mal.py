import os
import numpy as np

f = open("/home/anvit/Desktop/Data/INbreast/INbreast.csv",'r')
lines = f.readlines()
lines = lines[1:]
file = open("/home/anvit/Desktop/Data/INbreast/INbreast_onlymal.txt",'w')

for line in lines:
	arr = line.split(",")
	print(arr[7])
	if(arr[7] == '4a\n' or arr[7] == '4b\n' or arr[7] == '4c\n' or arr[7] == '5\n' or arr[7] == '6\n'):
		print("writing into file")
		file.write(arr[5]+"\n")

file.close()
f.close()




