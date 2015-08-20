import codecs

lyricLines = []
with codecs.open("lyricsTilde.txt", 'r', encoding="utf-8") as lyrics:
    for line in lyrics:
        lyricLines.append(line)

removeLines = []
for line in lyricLines:
    split = line.split(" ")
    split = split[0].lower()
    if split == "verse" or split == "bridge" or split == "outro" or split == "chorus" or line == '\n':
        removeLines.append(line)

for removeLine in removeLines:
    lyricLines.remove(removeLine)

punctuations = []
with codecs.open("punctuation.txt", 'r', encoding="utf-8") as punctuationFile:
    for punctuation in punctuationFile:
        for character in punctuation:
            punctuations.append(character)
            break
punctuations.pop(0)

imageCounter = -1
counter = 0
text = ""
with open("timingSheet.txt", 'r') as timingSheet:
    timings = timingSheet.readlines()
    for time in range(len(timings)):
        timings[time] = timings[time].split('\t')[0]

    with open("timingNotes.txt", "w") as timingNotes:
        firstCharacter = True
        for line in lyricLines:
            for character in line:
                if counter >= len(timings):
                    continue
                if firstCharacter:
                    firstCharacter = False
                    continue
                if character == '\n' or character == '\r' or repr(character) == '\ufeff':
                    continue
                isPunctuation = False
                for punctuation in punctuations:
                    if character == punctuation:
                        isPunctuation = True
                        break
                if not isPunctuation:
                    if character != '~':
                        imageCounter += 1
                        text += timings[counter] + ' ' + str(imageCounter) + ' ' + \
                                character.encode(encoding='utf-8') + ' ' + \
                                repr(character) + '\n'
                        counter += 1
                    else:
                        text += timings[counter] + ' ' + str(imageCounter) + '\n'
                        counter += 1
                else:
                    imageCounter += 1
                    text += timings[counter-1] + ' ' + str(imageCounter) + '\n'

            text += "EOL" + '\n'
        timingNotes.write(text)