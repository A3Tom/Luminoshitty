class ImageDTO: 
    filename = ""
    row = 0
    column = 0
    lum = 0

def make_imageDTO(self, filename) :
    result = ImageDTO()
    result.filename = filename

    return result

