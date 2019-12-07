
# coding: utf-8

# In[2]:


#Make VOC XML from original INbreast XML format


# In[ ]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import sys
import xml.etree.ElementTree as ET
from PIL import Image
from pascal_voc_writer import Writer
import math

def extractbb(array):
    
    xmax=-1
    ymax=-1
    xmin=sys.maxsize
    ymin=sys.maxsize
    
    flag = False
    for line in array:
        print("line",line)
        x,y=line.split(', ')
        x=x[1:]
        y=y[:-1]
        x=int(float(x))
        y=int(float(y))
        print("xy",x,y)
        if flag==False:
            xmin = x
            xmax = x
            ymin = y
            ymax = y
            flag=True

        
        if x<xmin:
            xmin=x
        elif x>xmax:
            xmax=x
        if y<ymin:
            ymin=y
        elif y>ymax:
            ymax=y
    return xmin,ymin,xmax,ymax


# In[79]:


os.chdir('/home/anvit/Desktop/INbreast/AllXML')
o=0
size=(2100,1700)
for xml in os.listdir('.'):
    print(xml)
    tree = ET.parse(xml)
    print("hi")
    root = tree.getroot()
    #root = ET.fromstring(country_data_as_string)

    p=root[0][1][0]
    numroi=int(p[3].text) 
    q=p[5]
    im = Image.open('/home/anvit/Desktop/INbreast/mode_png2/'+xml[:-4]+'.png')
    width, height = im.size
    writer = Writer('/home/anvit/Desktop/INbreast/mode_png2/'+xml[:-4]+'.png',width,height)

    for i in range(numroi):
        name=q[i][15].text
        name = name.lower()
        nump=int(q[i][17].text)
        arraybb=[]
        r=q[i][21]
        for j in range(nump):
            arraybb.append(r[j].text)
        xmin,ymin,xmax,ymax=extractbb(arraybb)
        writer.addObject(name,xmin,ymin,xmax,ymax)
    writer.save('/home/anvit/Desktop/INbreast/newVOC_XML/'+xml)


# In[11]:


os.chdir('/home/anvit/Desktop/VOCdevkit/VOC2007/JPEGImages')


# In[15]:


xmls=os.listdir('/home/anvit/Desktop/VOCdevkit/VOC2007/Annotations')
for image in os.listdir('.'):
    if image[:-4]+'.xml' not in xmls:
        os.remove(image)


# In[3]:


os.chdir('/home/anvit/Desktop/VOCdevkit/VOC2007/newanno/')
o=0
size=(2100,1700)
for xml in os.listdir('.'):
    print(xml)
    tree = ET.parse(xml)
    root = tree.getroot()
    im = Image.open('/home/anvit/Desktop/VOCdevkit/VOC2007/JPEGImages/'+xml[:-4]+'.png')
    width, height = im.size #Resized sized
    
    actualwidth = int(root[4][0].text)
    actualheight = int(root[4][1].text)
    #im.thumbnail(size, Image.ANTIALIAS)
    #im.save('/home/anvit/Desktop/MCA_labelled/PNG/'+xml[:-4]+'.png')
    #im = Image.open('/home/anvit/Desktop/VOCdevkit/VOC2007/JPEGImages/'+xml[:-4]+'.png')
    #w2,h2=im.size
    #print(width,height,w2,h2)

    writer = Writer('/home/anvit/Desktop/VOCdevkit/VOC2007/JPEGImages/'+xml[:-4]+'.png',width,height)
    ratio=float(height)/actualheight
    
    print(ratio)
    
    for obj in root.findall('object'):
        
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
    writer.save('/home/anvit/Desktop/VOCdevkit/VOC2007/finalanno/'+xml)


# In[25]:


im = Image.open('/home/anvit/Desktop/VOCdevkit/VOC2007/JPEGImages/20586908.png')
width, height = im.size
print(width)
print(height)


# In[ ]:


for xml in os.listdir('.')
    xml[:-4]+
    

