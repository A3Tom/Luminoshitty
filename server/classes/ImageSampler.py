from PIL import Image

from models.ImageDivisionSample import ImageDivisionSample

class ImageSampler:
        
    def sampleImage(self, imageDTO, pixelSamplePoints = 6):
        image = Image.open(imageDTO.filename)
        image = image.convert ('RGB')
        
        tR = tG = tB = 0

        for i in range(pixelSamplePoints) :
        
            X, Y = image.size
            X = (X / pixelSamplePoints * (i+1)) - 1
            Y = (Y / pixelSamplePoints * (i+1)) - 1
            pixelRGB = image.getpixel((X, Y))
            
            R,G,B = pixelRGB 
            tR += R
            tG += G
            tB += B

        dto = [
            round(tR / pixelSamplePoints), 
            round(tG / pixelSamplePoints), 
            round(tB / pixelSamplePoints)
        ]

        result = ImageDivisionSample(
            dto, 
            imageDTO.position,
            imageDTO.basename)

        return result