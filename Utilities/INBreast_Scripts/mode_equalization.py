#Read all dicoms from AllDICOMs and do mode equalization and save as PNGs in equalized_PNG_410

#import pydicom
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import scipy.misc
import os
import cv2

xy=os.listdir('/home/anvit/Desktop/Data/DDSM/All_resized_jpegs_removed_black_withnormal/')
for f in xy:
    print(f)
    #ds = pydicom.dcmread('AllDICOMs/'+f)
    data = cv2.imread('/home/anvit/Desktop/Data/DDSM/All_resized_jpegs_removed_black_withnormal/'+f, 0)
    #data=ds.pixel_array
#    n,m=data.shape
    a = np.hstack(data)
    b = a[a>0]
    x=stats.mode(b)[0][0]
#    c=np.clip(b,x-500,x+800)
#    z=np.interp(c, (c.min(), c.max()), (0, 255))
#    k=0
#    for i in range(a.shape[0]):
#        if a[i]!=0:
#            a[i]=z[k]
#            k+=1

#    newa=np.split(a,n)
#    scipy.misc.imsave('/home/anvit/Desktop/Data/DDSM/All_resized_jpegs_removed_black_equalized/'+f[:-4]+'.png', newa)
    print(b.max())
    print(x)
