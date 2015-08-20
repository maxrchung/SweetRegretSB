from UCISB import *

lyrics = open("lyrics.txt", 'r').read()
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

LyricManager.GenerateLyricImages(unicode(block, encoding="utf-8"),
                                 "Lyrics//Text",
                                 "JKG-L_3.ttf",
                                 128,
                                 (0, 0, 0),
                                 Separation.Character)
LyricManager.GenerateLyricImages(unicode(block, encoding="utf-8"),
                                 "Lyrics/GreenBorder",
                                 "JKG-L_3.ttf",
                                 128,
                                 (150, 255, 144),
                                 Separation.Character,
                                 8,
                                 (150, 255, 144))
LyricManager.GenerateLyricImages(unicode(block, encoding="utf-8"),
                                 "Lyrics/OrangeBorder",
                                 "JKG-L_3.ttf",
                                 128,
                                 (255, 173, 134),
                                 Separation.Character,
                                 12,
                                 (255, 173, 134))

print "Lyric generation complete"
