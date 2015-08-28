from UCISB import *
import math

lyrics = open("lyricsTilde.txt", 'r').read()
lyrics.decode("utf-8")
lyrics = lyrics.split('\n')

'''
Loops through lyrics and breaks up the sections into
verses, chorus, bridge, or outro tuples.
'''
block = ""
byteOrderMark = True
for line in lyrics:
    if byteOrderMark:
        byteOrderMark = False
        continue
    split = line.split(' ')
    section = split[0].lower()
    if section != "verse" and \
        section != "chorus" and \
        section != "bridge" and \
        section != "outro":
        block += line

block = block.replace('~', '')
block = block.replace('\\', '')

multiplyFactor = 2
imageSize = 36 * multiplyFactor
greenBorderWidth = 3 * multiplyFactor
orangeBorderWidth = 6 * multiplyFactor
font = "yuzuPopA.ttf"
destinationPath = "C:/Users/Wax Chug da Gwad/AppData/Local/osu!/Songs/Sweet Regret (3)/"

LyricManager.GenerateLyricImages(unicode(block, encoding="utf-8"),
                                 destinationPath + "Lyrics//Text",
                                 font,
                                 imageSize,
                                 (0, 0, 0),
                                 Separation.Character)
LyricManager.GenerateLyricImages(unicode(block, encoding="utf-8"),
                                 destinationPath + "Lyrics/GreenBorder",
                                 font,
                                 imageSize,
                                 (150, 255, 144),
                                 Separation.Character,
                                 greenBorderWidth,
                                 (150, 255, 144))
LyricManager.GenerateLyricImages(unicode(block, encoding="utf-8"),
                                 destinationPath + "Lyrics/OrangeBorder",
                                 font,
                                 imageSize,
                                 (255, 173, 134),
                                 Separation.Character,
                                 orangeBorderWidth,
                                 (255, 173, 134))

print "Lyric generation complete"
