#!/usr/bin/env python

from PIL import Image
import os, sys
import glob

def cmp(a, b):
    return (a > b) - (a < b)

def resizeImage(infile, name, output_dir, size=(2100,1700)):
     im = Image.open(infile)
     im.thumbnail(size, Image.ANTIALIAS)
     im.save(output_dir+name)


if __name__=="__main__":
    output_dir = "/home/anvit/Desktop/Data/AIIMS_Data/image_labelled_20000_resized/"
    dir = "/home/anvit/Desktop/Data/AIIMS_Data/image_labelled_20000/Train3/"
    os.chdir(dir)
    for file in glob.glob("*.png"):
        print(file)
        resizeImage(dir+file,file,output_dir)
