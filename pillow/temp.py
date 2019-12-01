# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from PIL import Image, ImageFilter
im = Image.open("crying.jpg")
print(im.format,im.size,im.mode)
im.show()
blurred = im.filter(ImageFilter.BLUR)
blurred.show()
blurred = im.filter(ImageFilter.CONTOUR)
blurred.show()
blurred = im.filter(ImageFilter.EDGE_ENHANCE)
blurred.show()
blurred = im.filter(ImageFilter.SMOOTH)
blurred.show()
im.thumbnail((128,128))
im.save("thumbnail.jpg")
im.show()

