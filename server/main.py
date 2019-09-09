import image_slicer
import glob
import os
from models.imageDTO import ImageDTO

dirname = os.path.dirname(__file__)
filename = 'Test_Images/FlapjacksAreGash'
fullfilepath = os.path.join(dirname, filename + '.png')
imageList = []

image_slicer.slice(fullfilepath, 64)

print('Remo mate, images created')

for file in glob.glob(os.path.join(dirname, filename) + '*.png'):
    newImageDTO = ImageDTO()
    newImageDTO.filename = file

    imageList.append(newImageDTO)

#print(imageList)

for image in imageList :
    print(image.filename)