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

times = []
with open("timingNotes.txt", 'r') as timingSheet:
    times = timingSheet.readlines()

pauseBeginning = 5333
offset = 10666 + pauseBeginning
midX = 320
midY = 240
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

characterWidth = 48
displayTime = 333
fadeInTime = 333
fadeOutTime = 666
rotationMultiplier = 10
lyricsY = 425
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

        multiplyFactor = 2.0
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

path = r"C:\Users\Wax Chug da Gwad\AppData\Local\osu!\Songs\Sweet Regret (3)\osu! UCI - Sweet Regret (osuuci dot com).osb"
Storyboard.Write(path)

print "Storyboard generation complete"