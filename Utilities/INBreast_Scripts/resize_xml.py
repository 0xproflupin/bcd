import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import sys
import xml.etree.ElementTree as ET
from PIL import Image
from pascal_voc_writer import Writer
import math


size=(2100,1700)
for xml in os.listdir('/home/anvit/Desktop/Data/INbreast/XML_VOC/'):
    print(xml)
    tree = ET.parse("/home/anvit/Desktop/Data/INbreast/XML_VOC/" + xml)
    root = tree.getroot()
    im = Image.open('/home/anvit/Desktop/Data/INbreast/equalized_PNG_410_resized/'+xml[:-4]+'.png')
    width, height = im.size #Resized sized
    img = Image.open('/home/anvit/Desktop/Data/INbreast/equalized_PNG_410/'+xml[:-4]+'.png')
    width_nonresized, height_nonresized = img.size

    actualwidth = int(root[4][0].text)
    actualheight = int(root[4][1].text)
    assert width_nonresized == actualwidth
    assert height_nonresized == actualheight

    writer = Writer('/home/anvit/Desktop/Data/INbreast/equalized_PNG_410_resized/'+xml[:-4]+'.png', width, height)
    ratio=float(height)/actualheight

    print(ratio)

    for obj in root.findall('object'):
        print("inobject loop")
        typename=obj.find('name').text
        name=obj.find('bndbox')
        xmin=float(name.find('xmin').text)
        xmax=float(name.find('xmax').text)
        ymin=float(name.find('ymin').text)
        ymax=float(name.find('ymax').text)
        print(xmin,ymin,xmax,ymax)
        if(xmin<1):
            xmin=1
        if(ymin<1):
            ymin=1
        if(xmax>=actualwidth):
            xmax=actualwidth-1
        if(ymax>=actualheight):
            ymax=actualheight-1
        xmin*=ratio
        ymin*=ratio
        xmax*=ratio
        ymax*=ratio
        xmin=int(math.ceil(xmin))
        ymin=int(math.ceil(ymin))
        xmax=int(math.ceil(xmax))
        ymax=int(math.ceil(ymax))
        print(xmin,ymin,xmax,ymax)
        writer.addObject(typename,xmin,ymin,xmax,ymax)
    writer.save('/home/anvit/Desktop/Data/INbreast/XML_VOC_resized_again/'+xml)
