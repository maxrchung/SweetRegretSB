from UCISB import *
import random

bottomY = 480
fadeTime = 333
def generateExplosion(timing):
    image = random.randint(0, 5)
    explosion = Sprite("Shapes/" + str(image) + ".png", midX, midY, layer=Layer.Background)
    degrees = random.randint(225, 315)
    radians = math.radians(degrees)

    distance = random.randint(100, 200)
    offsetX = math.cos(radians) * distance
    offsetY = math.sin(radians) * distance

    posX = random.randint(0, 640)

    endPosX = posX + offsetX
    endPosY = bottomY + offsetY

    timeMultiple = random.randint(5, 10)
    endTime = timing + 333 * timeMultiple
    explosion.Move(timing, endTime, posX, bottomY, endPosX, endPosY)

    opacity = random.random() * 0.2 + 0.6
    explosion.Fade(timing, timing + fadeTime, 0.0, opacity)
    explosion.Fade(endTime - 333, endTime, opacity, 0.0)

    scale = random.random() * 0.3 + 0.4
    explosion.Scale(timing, endTime, scale, scale)

    rotation = math.radians(degrees + 90)
    explosion.Rotate(timing, endTime, rotation, rotation)

pauseBeginning = 0
offset = 10666 + pauseBeginning
midX = 320
midY = 240
characterWidth = 48
displayTime = 333
fadeInTime = 333
fadeOutTime = 666
rotationMultiplier = 10
lyricsY = 425
producedByEnd = 5333
multiplyFactor = 2.0
titleFadeOut = fadeOutTime

blackBg = Sprite("blackBG.png", midX, midY, layer=Layer.Background)
blackBg.Move(-1000, producedByEnd + 1333, midX, midY, midX, midY)
blackBg.Fade(producedByEnd, producedByEnd + 1333, 1.0, 0.0)

englishTitle = [] # (orangeBorder, greenBorder, blackText)
for i in range(12):
    orangeBorder = Sprite("Title/englishOrange" + str(i) + ".png", midX, midY, layer=Layer.Foreground)
    greenBorder = Sprite("Title/englishGreen" + str(i) + ".png", midX, midY, layer=Layer.Foreground)
    blackText = Sprite("Title/englishBlack" + str(i) + ".png", midX, midY, layer=Layer.Foreground)
    englishTitle.append((orangeBorder, greenBorder, blackText))

kanjiTitle = [] # (orangeBorder, greenBorder, blackText)
for i in range(4):
    orangeBorder = Sprite("Title/kanjiOrange" + str(i) + ".png", midX, midY, layer=Layer.Foreground)
    greenBorder = Sprite("Title/kanjiGreen" + str(i) + ".png", midX, midY, layer=Layer.Foreground)
    blackText = Sprite("Title/kanjiBlack" + str(i) + ".png", midX, midY, layer=Layer.Foreground)
    kanjiTitle.append((orangeBorder, greenBorder, blackText))

producedBy = Sprite("Title/producedBy.png", midX, midY, layer=Layer.Foreground)

titleStart = pauseBeginning
titleWidth = characterWidth * (len(englishTitle) - 1) # Because of center origin
titleDisplayTime = 166
titleEnd = pauseBeginning + titleDisplayTime * len(englishTitle)

for i in range(30):
    timing = producedByEnd
    image = random.randint(0, 5)
    explosion = Sprite("Shapes/" + str(image) + ".png", midX, midY, layer=Layer.Background)
    degrees = random.randint(0, 359)
    radians = math.radians(degrees)

    distance = random.randint(300, 1000)
    offsetX = math.cos(radians) * distance
    offsetY = math.sin(radians) * distance

    endPosX = midX + offsetX
    endPosY = midY + offsetY

    timeMultiple = random.randint(5, 10)
    endTime = pauseBeginning + 10666
    startX = math.cos(radians) * 25
    startY = math.sin(radians) * 25
    explosion.Move(timing, endTime, midX + startX, midY + startY, endPosX, endPosY)

    opacity = random.random() * 0.2 + 0.6
    explosion.Fade(timing, timing + fadeTime, 0.0, opacity)
    explosion.Fade(endTime - 333, endTime, opacity, 0.0)

    scale = random.random() * 0.3 + 0.4
    explosion.Scale(timing, endTime, scale, scale)

    rotation = math.radians(degrees + 90)
    explosion.Rotate(timing, endTime, rotation, rotation)

offsetX = midX - titleWidth/2
for i in range(len(englishTitle)):
    counter = i
    if i >= 6:
        counter -= 1

    rotation = random.uniform(0.5, 1.0) * rotationMultiplier * 3
    rotation = math.radians(rotation)
    if random.randint(0, 1) == 0:
        rotation *= -1
    startRotation = rotation * 0.8
    endRotation = rotation * -1 * 0.8

    orangeSprite = englishTitle[i][0]
    greenSprite = englishTitle[i][1]
    textSprite = englishTitle[i][2]

    scaling = random.uniform(0.7, 0.9) / multiplyFactor

    beginDisplay = titleStart + titleDisplayTime * counter
    xPos = characterWidth * i + offsetX
    greenSprite.Move(beginDisplay - fadeInTime, producedByEnd + titleFadeOut, xPos, midY, xPos, midY)
    greenSprite.Fade(beginDisplay - fadeInTime, beginDisplay, 0.0, 1.0)
    greenSprite.Fade(producedByEnd, producedByEnd + titleFadeOut, 1.0, 0.0)
    greenSprite.Rotate(titleStart - fadeInTime, producedByEnd + titleFadeOut, startRotation, endRotation)
    greenSprite.Scale(beginDisplay - fadeInTime, beginDisplay, 0.50 * scaling, 0.50)
    greenSprite.Scale(producedByEnd, producedByEnd + titleFadeOut, 0.50, scaling)

    orangeSprite.Move(beginDisplay - fadeInTime, producedByEnd + titleFadeOut, xPos, midY, xPos, midY)
    orangeSprite.Fade(beginDisplay - fadeInTime, beginDisplay, 0.0, 1.0)
    orangeSprite.Fade(producedByEnd, producedByEnd + titleFadeOut, 1.0, 0.0)
    orangeSprite.Rotate(titleStart - fadeInTime, producedByEnd + titleFadeOut, startRotation, endRotation)
    orangeSprite.Scale(beginDisplay - fadeInTime, beginDisplay, 0.50 * scaling, 0.50)
    orangeSprite.Scale(producedByEnd, producedByEnd + titleFadeOut, 0.50, scaling)

    startRotation = rotation
    endRotation = rotation * -1

    textSprite.Move(beginDisplay - fadeInTime, producedByEnd + titleFadeOut, xPos, midY, xPos, midY)
    textSprite.Fade(beginDisplay - fadeInTime, beginDisplay, 0.0, 1.0)
    textSprite.Fade(producedByEnd, producedByEnd + titleFadeOut, 1.0, 0.0)
    textSprite.Rotate(titleStart - fadeInTime, producedByEnd + titleFadeOut, startRotation, endRotation)
    textSprite.Scale(beginDisplay - fadeInTime, beginDisplay, 0.50 * scaling, 0.50)
    textSprite.Scale(producedByEnd, producedByEnd + titleFadeOut, 0.50, scaling)

titleWidth = characterWidth * (len(kanjiTitle) - 1) # Because of center origin
offsetX = midX - titleWidth/2
midTopY = midY - 60
for i in range(len(kanjiTitle)):
    counter = i

    rotation = random.uniform(0.5, 1.0) * rotationMultiplier
    rotation = math.radians(rotation)
    if random.randint(0, 1) == 0:
        rotation *= -1
    startRotation = rotation * 0.5
    endRotation = rotation * -1 * 0.5

    orangeSprite = kanjiTitle[i][0]
    greenSprite = kanjiTitle[i][1]
    textSprite = kanjiTitle[i][2]

    scaling = random.uniform(0.7, 0.9) / multiplyFactor

    beginDisplay = titleStart + titleDisplayTime * counter
    xPos = characterWidth * i + offsetX
    greenSprite.Move(beginDisplay - fadeInTime, producedByEnd + titleFadeOut, xPos, midTopY, xPos, midTopY)
    greenSprite.Fade(beginDisplay - fadeInTime, beginDisplay, 0.0, 1.0)
    greenSprite.Fade(producedByEnd, producedByEnd + titleFadeOut, 1.0, 0.0)
    greenSprite.Rotate(titleStart - fadeInTime, producedByEnd + titleFadeOut, startRotation, endRotation)
    greenSprite.Scale(beginDisplay - fadeInTime, beginDisplay, 0.50 * scaling, 0.50)
    greenSprite.Scale(producedByEnd, producedByEnd + titleFadeOut, 0.50, scaling)

    orangeSprite.Move(beginDisplay - fadeInTime, producedByEnd + titleFadeOut, xPos, midTopY, xPos, midTopY)
    orangeSprite.Fade(beginDisplay - fadeInTime, beginDisplay, 0.0, 1.0)
    orangeSprite.Fade(producedByEnd, producedByEnd + titleFadeOut, 1.0, 0.0)
    orangeSprite.Rotate(titleStart - fadeInTime, producedByEnd + titleFadeOut, startRotation, endRotation)
    orangeSprite.Scale(beginDisplay - fadeInTime, beginDisplay, 0.50 * scaling, 0.50)
    orangeSprite.Scale(producedByEnd, producedByEnd + titleFadeOut, 0.50, scaling)

    startRotation = rotation
    endRotation = rotation * -1

    textSprite.Move(beginDisplay - fadeInTime, producedByEnd + titleFadeOut, xPos, midTopY, xPos, midTopY)
    textSprite.Scale(beginDisplay - fadeInTime, producedByEnd + titleFadeOut, 0.50, 0.50)
    textSprite.Fade(beginDisplay - fadeInTime, beginDisplay, 0.0, 1.0)
    textSprite.Fade(producedByEnd, producedByEnd + titleFadeOut, 1.0, 0.0)
    textSprite.Rotate(titleStart - fadeInTime, producedByEnd + titleFadeOut, startRotation, endRotation)
    textSprite.Scale(beginDisplay - fadeInTime, beginDisplay, 0.50 * scaling, 0.50)
    textSprite.Scale(producedByEnd, producedByEnd + titleFadeOut, 0.50, scaling)

producedByStart = 2666 + pauseBeginning
producedByStartDelay = 666
midBottomY = midY + 60
producedBy.Move(producedByStart - producedByStartDelay, producedByEnd + titleFadeOut, midX, midBottomY, midX, midBottomY)
producedBy.Fade(producedByStart - producedByStartDelay, producedByStart, 0.0, 1.0)
producedBy.Fade(producedByEnd, producedByEnd + titleFadeOut, 1.0, 0.0)
producedBy.Scale(producedByStart - fadeInTime, producedByEnd + titleFadeOut, 0.5, 0.5)

times = []
with open("timingNotes.txt", 'r') as timingSheet:
    times = timingSheet.readlines()
lines = []
line = [] # ([orangeBorder, greenBorder, sprite], startTime)
for time in times:
    if time == "EOL\n":
        if len(line) > 0:
            lines.append(line)
        line = []
    else:
        split = time.split('\n')[0]
        split = split.split(' ')
        image = split[1]
        orangeBorder = Sprite("Lyrics/OrangeBorder/" + str(image), midX, midY, layer=Layer.Foreground)
        greenBorder = Sprite("Lyrics/GreenBorder/" + str(image), midX, midY, layer=Layer.Foreground)
        text = Sprite("Lyrics/Text/" + str(image), midX, midY, layer=Layer.Foreground)
        timing = split[0]
        line.append(([orangeBorder, greenBorder, text], int(timing) + offset))

for lineIndex in range(len(lines)):
    lineLength = len(lines[lineIndex])
    posXOffset = midX - ((lineLength - 1) * characterWidth / 2.0)
    startTime = lines[lineIndex][0][1]
    endTime = lines[lineIndex][-1][1] + displayTime
    for spriteIndex in range(lineLength):
        sprites = lines[lineIndex][spriteIndex][0]
        timing = lines[lineIndex][spriteIndex][1]

        generateExplosion(timing)

        posX = spriteIndex * characterWidth + posXOffset
        start = timing - fadeInTime

        posY = lyricsY

        rotation = random.uniform(0.5, 1.0) * rotationMultiplier
        rotation = math.radians(rotation)

        if random.randint(0, 1) == 0:
            rotation *= -1

        startRotation = rotation * 0.5
        endRotation = rotation * -1 * 0.5

        scaling = random.uniform(0.7, 0.9) / multiplyFactor

        sprites[0].Move(start, endTime, posX, posY, posX, posY)
        sprites[0].Fade(start, start + fadeInTime, 0.0, 1.0)
        sprites[0].Scale(start, start + fadeInTime, scaling, 1.0 / multiplyFactor)
        sprites[0].Fade(endTime, endTime + fadeOutTime, 1.0, 0.0)
        sprites[0].Scale(start, endTime, 1.0 / multiplyFactor, 1.0 / multiplyFactor)
        sprites[0].Scale(endTime, endTime + fadeOutTime, 1.0 / multiplyFactor, scaling)
        sprites[0].Rotate(startTime - fadeInTime, endTime + fadeOutTime, startRotation, endRotation)

        sprites[1].Move(start, endTime, posX, posY, posX, posY)
        sprites[1].Fade(start, start + fadeInTime, 0.0, 1.0)
        sprites[1].Scale(start, start + fadeInTime, scaling, 1.0 / multiplyFactor)
        sprites[1].Fade(endTime, endTime + fadeOutTime, 1.0, 0.0)
        sprites[1].Scale(start, endTime, 1.0 / multiplyFactor, 1.0 / multiplyFactor)
        sprites[1].Scale(endTime, endTime + fadeOutTime, 1.0 / multiplyFactor, scaling)
        sprites[1].Rotate(startTime - fadeInTime, endTime + fadeOutTime, startRotation, endRotation)

        startRotation = rotation
        endRotation = rotation * -1

        sprites[2].Move(start, endTime, posX, posY, posX, posY)
        sprites[2].Fade(start, start + fadeInTime, 0.0, 1.0)
        sprites[2].Scale(start, start + fadeInTime, scaling, 1.0 / multiplyFactor)
        sprites[2].Fade(endTime, endTime + fadeOutTime, 1.0, 0.0)
        sprites[2].Scale(start, endTime, 1.0 / multiplyFactor, 1.0 / multiplyFactor)
        sprites[2].Scale(endTime, endTime + fadeOutTime, 1.0 / multiplyFactor, scaling)
        sprites[2].Rotate(startTime - fadeInTime, endTime + fadeOutTime, startRotation, endRotation)

team = Sprite("credits.png", layer=Layer.Foreground)
teamBegin = pauseBeginning + 279000
teamEnd = teamBegin + 5000
team.Move(teamBegin, teamEnd, midX, midY, midX, midY)
team.Scale(teamBegin, teamEnd, 0.5, 0.5)
team.Fade(teamBegin - 333, teamBegin, 0.0, 1.0)

blackBg.Move(teamBegin, teamEnd, midX, midY, midX, midY)
blackBg.Fade(teamBegin - 1333, teamBegin, 0.0, 1.0)
blackBg.Fade(teamBegin, teamEnd, 1.0, 1.0)

path = r"C:\Users\Wax Chug da Gwad\AppData\Local\osu!\Songs\SweetRegret\osu! UCI - Sweet Regret (osuuci dot com).osb"
Storyboard.Write(path)

print "Storyboard generation complete"