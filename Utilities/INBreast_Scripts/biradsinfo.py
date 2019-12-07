import pickle
f = open("../INbreast.csv", 'r')
lines = f.readlines()
d = {}
d2 = {}
lines = lines[1:]

for line in lines:
	line = line.rstrip()
	arr = line.split(',')
	name = arr[-3]
	birads = arr[-1]
	d2[name] = birads
	if birads == "1" or birads == "2":
		d[name] = 0
	else:
		d[name] = 1

print(d)
pickle.dump(d, open("actionable_info.pk", 'wb'))
pickle.dump(d2, open("birads_info.pk", 'wb'))
