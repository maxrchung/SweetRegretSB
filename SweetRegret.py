from UCISB import *

times = []
with open("timingNotes.txt", 'r') as timingSheet:
    times = timingSheet.readlines()

offset = 10666
for time in times:
    if time == "EOL\n":
        pass
    else:
        split = time.split('\n')[0]
        split = split.split(' ')
        image = split[1]
        sprite = Sprite("Lyrics/Text/" + str(image), 300, 300)
        timing = split[0]
        timeOffset = int(timing) + offset
        sprite.Move(timeOffset, timeOffset + 200, 300, 300, 300, 300)

path = r"C:\Users\Wax Chug da Gwad\AppData\Local\osu!\Songs\Sweet Regret (3)\osu! UCI - Sweet Regret (osuuci dot com).osb"
Storyboard.Write(path)

print "Storyboard generation complete"