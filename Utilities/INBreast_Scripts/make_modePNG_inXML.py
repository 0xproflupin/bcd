#Read equalized_PNG_410 and make equalized_PNG_343 with PNGs only in AllXML 

import os
import numpy
import subprocess

os.chdir('/home/anvit/Desktop/INbreast/AllXML/')
#xml = []
for file in os.listdir('.'):
	string = '/home/anvit/Desktop/INbreast/mode_png2/'+file[:-4]+".png"
	subprocess.call(['cp',string,'/home/anvit/Desktop/INbreast/modePNG_inXML/'])