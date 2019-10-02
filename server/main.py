import image_slicer
import glob
import os

from PIL import Image
from math import sqrt
from models.imageDTO import ImageDTO
from models.ImageDivisionSample import ImageDivisionSample
from classes.ImageSampler import ImageSampler
from image_slicer import Tile

dirname = os.path.dirname(__file__)
filename = 'Test_Images/FlapjacksAreGash'
fullfilepath = os.path.join(dirname, filename + '.png')
imageList = image_slicer.slice(fullfilepath, 64)
lighterImageCount = 0

print('Remo mate, images created')

sampler = ImageSampler()

mainImage = Image.open(fullfilepath)
tile = Tile(mainImage, 1, mainImage.size, (mainImage.size), fullfilepath)
mainImageSample = sampler.sampleImage(tile, 30)

for image in imageList :

    
    imageSample = sampler.sampleImage(image)

    imageSample.output()

    if(imageSample.luminosity > mainImageSample.luminosity) :
        print("Aye")
    else:
        print("Naw")