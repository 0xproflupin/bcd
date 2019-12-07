import os
import numpy as np

list1 = os.listdir("/home/anvit/Desktop/Data/AIIMS_Data/BIRADS_labelling/PNG/")
list2 = os.listdir("/home/anvit/Desktop/Data/AIIMS_Data/MCA_labelled/PNG_245/")

# Note - len(list1) = 563
# Note - len(list2) = 245

print(len(list1))
print(len(list2))

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

#Conclusion - There are no files in common between BIRADS labelling and MCA labelled.
