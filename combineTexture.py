##import libraries 
import sys
import os
from PIL import Image

##Defining the unction that creates new based image.
def createNew(size, mode):
    if mode == "base":
        newbase = Image.new('RGBA', (size, size), color = (255, 255, 255))
    if mode == "normal":
        newbase = Image.new('RGBA', (size, size), color = (153, 153, 255))
    if mode == "metalic":
        newbase = Image.new('RGBA', (size, size), color = (128, 128, 128))
    if mode == "roughness":
        newbase = Image.new('RGBA', (size, size), color = (128, 128, 128))
    if mode == "ao":
        newbase = Image.new('RGBA', (size, size), color = (128, 128, 128))
    if mode == "emissive":
        newbase = Image.new('RGBA', (size, size), color = (0, 0, 0))
    return newbase

##Defining main function that combines multiple testures into one texture by using alpha channel.
def combineImage(folderpath, size, mode):
    newim = createNew(size, mode)
    for image in images:
        im = Image.open(folderpath + image)
        newim.alpha_composite(im, (0,0), (0,0))
    newim.save(folderpath + mode + ".png", "png")
    return newim

##remove unneccesary files from the list
images = os.listdir(str(sys.argv[1]))
if ".DS_Store" in images:
    images.remove(".DS_Store")

##Running main function
result = combineImage(str(sys.argv[1]), int(sys.argv[2]), str(sys.argv[3]))





