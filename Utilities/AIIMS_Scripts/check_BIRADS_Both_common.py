import os
import numpy as np

list1 = os.listdir("/home/anvit/Desktop/Data/AIIMS_Data/BIRADS_labelling/PNG/")
list2 = os.listdir("/home/anvit/Desktop/Data/AIIMS_Data/Both_labelled/AllSetsPNG/")

# Note - len(list1) = 563
# Note - len(list2) = 851

count1 = 0
for img in list1:
	if(img not in list2):
		count1 += 1
		#print(img)

print("COUNT1", count1) #563

count2 = 0
for img in list2:
        if(img not in list1):
                count2 += 1
                #print(img)

print("COUNT2", count2) #0

#Conclusion - BIRADS_labelling does not have any file which is not in Both_labelled. BIRADS labelling is a subset of Both labelled.

