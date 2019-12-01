#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 12:24:14 2019

@author: owner
"""
import statistics as st
import random
import math
from PIL import Image ,ImageDraw , ImageFilter
#from PIL import ImageDraw
# 1
x = [3,1.5,4.5,6.75,2.25,5.75,2.25]
#print(st.mean(x))
#print(st.harmonic_mean(x))
#print(st.median(x))
#print(st.median_low(x))
#print(st.median_high(x))
#print(st.median_grouped(x))
#print(st.mode(x))
#print(st.pstdev(x))
#print(st.pvariance(x))
#print(st.stdev(x))
#print(st.variance(x))

# 2

#print(random.random())
#print(random.randrange(10))
#print(random.choice(["Ali","khalid","hussam"]))
#print(random.sample((range(100)),10))
#print(random.choice("Orange Academy"))
#shuffleList = [1,5,8,9,2,4]
#random.shuffle(shuffleList)
#print(shuffleList)
#print(random.randint(20,30))
#print(random.randrange(100,2111,5))
#print(random.uniform(1000,11000))

# 3
#print( math.pi)
#print(math.cos(200))
#print(math.sin(30))
#print(math.tan(180))
#print(math.floor(10.8))
#print(math.ceil(10.8))

# 4
im = Image.open("two.png")
print(im.format,im.size,im.mode)
#im.show()
im_Flip = im.transpose(Image.FLIP_TOP_BOTTOM)
#im_Flip.show()
greyyscale_img = im.convert('L')
#greyyscale_img.show()
cropped_im = im.crop((0,0,50,50))
#cropped_im.show()
draw  = ImageDraw.Draw(im)
draw.line((0,0) + im.size,fill=(255,255,255))
draw.line((0,im.size[1],im.size[0],0),fill=(255,255,255))
#im.show()
EDGE_ENHANCE = im.filter(ImageFilter.EDGE_ENHANCE)
#EDGE_ENHANCE.show()
FIND_EDGES = im.filter(ImageFilter.FIND_EDGES)
#FIND_EDGES.show()
SMOOTH = im.filter(ImageFilter.SMOOTH)
#SMOOTH.show()
SHARPEN = im.filter(ImageFilter.SHARPEN)
#SHARPEN.show()
alpha = 0.5
im2 = Image.open("three.png").resize(im.size)
Image.blend(im,im2,alpha).save("new.png".format(alpha))
im3 = Image.open("new.png")
#im3.show()
BLUR = im.filter(ImageFilter.BLUR)
#BLUR.show()
size = (128,128)
saved = "thumbnail.png"
im.thumbnail(size)
im.save(saved)
#im.show()
image_rotate = im.rotate(90)
#image_rotate.show()
mask = Image.open("1.png")
mask = mask.resize(im.size)
mask.show()
Image.composite(im,im2,mask).save("img_com.jpg")
com = Image.open("img_com.jpg")
#com.show()