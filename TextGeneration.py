from UCISB import *
import math

kanji = open("textInput.txt", 'r').read()
kanji.decode("utf-8")

split = kanji.split("\n")

kanjiTitle = split[1]

englishTitle = "sweet regret"
producedBy = "made by osu! UCI"

multiplyFactor = 2
imageSize = 36 * multiplyFactor
greenBorderWidth = 3 * multiplyFactor
orangeBorderWidth = 6 * multiplyFactor
font = "yuzuPopA.ttf"
destinationPath = "C:/Users/Wax Chug da Gwad/AppData/Local/osu!/Songs/Sweet Regret (3)/Title"
LyricManager.GenerateLyricImages(unicode(kanjiTitle, encoding="utf-8"),
                                 destinationPath,
                                 font,
                                 imageSize,
                                 (0, 0, 0),
                                 Separation.Character,
                                 destinationName="kanjiBlack")
LyricManager.GenerateLyricImages(unicode(kanjiTitle, encoding="utf-8"),
                                 destinationPath,
                                 font,
                                 imageSize,
                                 (150, 255, 144),
                                 Separation.Character,
                                 greenBorderWidth,
                                 (150, 255, 144),
                                 destinationName="kanjiGreen")
LyricManager.GenerateLyricImages(unicode(kanjiTitle, encoding="utf-8"),
                                 destinationPath,
                                 font,
                                 imageSize,
                                 (255, 173, 134),
                                 Separation.Character,
                                 orangeBorderWidth,
                                 (255, 173, 134),
                                 destinationName="kanjiOrange")
imageSize = 36 * multiplyFactor
LyricManager.GenerateLyricImages(unicode(englishTitle, encoding="utf-8"),
                                 destinationPath,
                                 font,
                                 imageSize,
                                 (0, 0, 0),
                                 Separation.Character,
                                 destinationName="englishBlack")
LyricManager.GenerateLyricImages(unicode(englishTitle, encoding="utf-8"),
                                 destinationPath,
                                 font,
                                 imageSize,
                                 (150, 255, 144),
                                 Separation.Character,
                                 greenBorderWidth,
                                 (150, 255, 144),
                                 destinationName="englishGreen")
LyricManager.GenerateLyricImages(unicode(englishTitle, encoding="utf-8"),
                                 destinationPath,
                                 font,
                                 imageSize,
                                 (255, 173, 134),
                                 Separation.Character,
                                 orangeBorderWidth,
                                 (255, 173, 134),
                                 destinationName="englishOrange")
font = "Roboto-Thin.ttf"
imageSize = 36 * multiplyFactor
LyricManager.GenerateLyricImages(unicode(producedBy, encoding="utf-8"),
                                 destinationPath,
                                 font,
                                 imageSize,
                                 (255, 255, 255),
                                 destinationName="producedBy")

print "Text generation complete"
