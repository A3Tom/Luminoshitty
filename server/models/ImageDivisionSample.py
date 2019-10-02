class ImageDivisionSample:
    red = 0
    green = 0
    blue = 0
    luminosity = 0
    row = 0
    column = 0
    filename = ""

    def __init__(self, TileInfo, Position, FileName = "") :
        self.red, self.green, self.blue = TileInfo
        self.column, self.row = Position
        self.luminosity = round(sum(TileInfo)/3)
        self.filename = FileName


    def output(self) :
        output = ""
        if(self.filename > "") :
            output += "{4} | "

        output += "[ {5} ] [ {6} ] "
        output += "R: {0}, G: {1}, B: {2}, L: {3}"

        print(output.format(self.red, self.green, self.blue, self.luminosity, self.filename, self.row, self.column))