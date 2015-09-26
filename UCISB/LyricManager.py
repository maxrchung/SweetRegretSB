from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFilter
from Separation import *
import math
import os

'''
Use this function to produce images out of text. Insert text into inputString, specify destination path into outputFilePath, put location of font into fontPath, and indicate what font size in fontSize. Separation is an int that determines how many characters to fit into each image. Use the Separation class for more specific options.
'''
def GenerateLyricImages(inputString = "default",
                        outputDirectory = "Output",
                        fontPath = "arial.ttf",
                        fontSize = 64,
                        fontColor = (0,0,0),
                        separation = Separation.FullText,
                        borderWidth = 0,
                        borderColor = (255, 255, 255),
                        destinationName = ""):
    font = ImageFont.truetype(fontPath, fontSize)
    try:
        os.makedirs(outputDirectory)
    except OSError:
        if not os.path.isdir(outputDirectory):
            raise

    if separation == Separation.Character:
        imageIndex = 0
        for character in inputString:
            # Offset is used as a buffer space for borders that may have a bit more smoothing
            offset = 4
            size = getSize(character, font, borderWidth + offset)
            image = Image.new("RGBA", size, (0,0,0,0))
            draw = ImageDraw.Draw(image)

            if borderWidth > 0:
                generateBorder(draw, character, font, borderWidth, borderColor, offset)
                draw = ImageDraw.Draw(image)
                image = image.filter(ImageFilter.SMOOTH_MORE)

            draw.text((borderWidth + offset,borderWidth + offset), character, fontColor, font)

            # Ignore new lines
            if character != '\n':
                fileName = destinationName + str(imageIndex) + ".png"
                path = os.path.join(outputDirectory, fileName)
                image.save(path, "PNG")
                imageIndex += 1

    elif separation == Separation.FullText:
        # Offset is used as a buffer space for borders that may have a bit more smoothing
        offset = 4
        size = getSize(inputString, font, borderWidth + offset)
        image = Image.new("RGBA", size, (0,0,0,0))
        draw = ImageDraw.Draw(image)

        if borderWidth > 0:
            generateBorder(draw, inputString, font, borderWidth, borderColor, offset)
            draw = ImageDraw.Draw(image)
            image = image.filter(ImageFilter.SMOOTH_MORE)

        draw.text((borderWidth + offset,borderWidth + offset), inputString, fontColor, font)

        # Ignore new lines
        if inputString != '\n':
            fileName = destinationName + ".png"
            path = os.path.join(outputDirectory, fileName)
            image.save(path, "PNG")

def generateBorder(draw, character, font, borderWidth, borderColor, offset):
    for degree in range(360):
        radians = math.radians(degree)
        xPos = math.cos(radians) * borderWidth
        yPos = math.sin(radians) * borderWidth
        draw.text((borderWidth + xPos + offset, borderWidth + yPos + offset), character, borderColor, font)

'''
Helper function that calculates the size of text
'''    
def getSize(inputString, font, borderWidth):
    testImage = Image.new('RGBA', (0,0), (0,0,0,0))
    testDraw = ImageDraw.Draw(testImage)
    width, height =  testDraw.textsize(inputString, font)
    return (width + borderWidth * 2, height + borderWidth * 2)
    
def TimeLyrics(lyricDirectory, timingSheet):
    pass
