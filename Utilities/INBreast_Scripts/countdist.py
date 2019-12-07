import os

fil = open("gtauthors.txt", 'r')

lines = fil.readlines()
lines = lines[1:]
d = {}
for line in lines:
	arr = line.split("\t")
	name = arr[0].split("_")
	if(name[0] not in d):
		d[name[0]] = 1
	else:
		d[name[0]] += 1
print(len(d))