#tiff to png batch conversion

from PIL import Image
import glob
import os
os.chdir("/home/anvit/Desktop/Data/AIIMS_Data/smallmass_tif/") 
for name in glob.glob('*.tif'):
    print(name)
    im = Image.open(name)
    name = str(name).rstrip(".tif")
    im.save("/home/anvit/Desktop/Data/AIIMS_Data/smallmass_png/"+name+".png", 'PNG')

print("Conversion from tif/tiff to jpg completed!")
