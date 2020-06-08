##import libraries 
import sys
import os
from PIL import Image

##Getting argments
path = str(sys.argv[1])

##loading image list.
images = os.listdir(path)

##Removing unnecessary file.
if ".DS_Store" in images:
    images.remove(".DS_Store")

##Defining the size and Initializing variables. 
im = Image.open(path + images[1])
size = im.size[0]
occlusion = Image.new("L", (size, size))
roughness = Image.new("L", (size, size))
metalic = Image.new("L", (size, size))

##Converting RGB to luminace channel
for image in images:
    im = Image.open(path + image).convert("L")
##Assigning each channel to PIL Image object. Based on the last caharacter of the file.
    channel = image.split(".")[0][-1]
    if channel == "o":
        occlusion = im
    if channel == "r":
        roughness = im
    if channel == "m":
        metalic = im

##Merging the channels.
result = Image.merge("RGB", (occlusion, roughness, metalic))
##Saving the file.
result.save(path + "ORM.png", "png")