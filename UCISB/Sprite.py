from Storyboard import *
'''
Layer: The layer the object appears on, valid values include:
'''
class Layer:
    Background = 0
    Fail = 1
    Pass = 2
    Foreground = 3
LayerMapping = ["Background", "Fail", "Pass", "Foreground"]

'''
Origin: where on the image should osu! consider that image's origin (coordinate) to be.
'''    
class Origin:
    TopLeft = 0
    TopCentre = 1
    TopRight = 2
    CentreLeft = 3
    Centre = 4
    CentreRight = 5
    BottomLeft = 6
    BottomCentre = 7
    BottomRight = 8
OriginMapping = ["TopLeft", "TopCentre", "TopRight", "CentreLeft", "Centre", "CentreRight", "BottomLeft", "BottomCentre", "BottomRight"]

class Sprite:
    def __init__(self,
                 layer = Layer.Background,
                 origin = Origin.Centre,
                 filePath = "default.png",
                 x = 0,
                 y = 0):
        self.Layer = LayerMapping[layer]
        self.Origin = OriginMapping[origin]
        
        # Quotes around the filePath allow for files that have spaces in them
        self.FilePath = '"' + filePath + '"';
        self.X = x;
        self.Y = y;
        
        sprites.append(self)
    
    def write(self):
        sprite = "Sprite,{Layer},{Origin},{FilePath},{X},{Y}".format(Layer = self.Layer,
                                                                     Origin = self.Origin,
                                                                     FilePath = self.FilePath,
                                                                     X = self.X,
                                                                     Y = self.Y)
        return sprite;
    
