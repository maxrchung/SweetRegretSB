import xml.etree.ElementTree as ET

tree = ET.parse("finalshitv5.vsqx")
root = tree.getroot()

with open("timingSheet.txt", "w") as output:
    counter = 0;
    lines = ""
    for note in root.iter("note"):
        posTick = note.find("posTick")
        timing = int(posTick.text)
        timing = timing / 240 * 333 / 2
        lines += str(timing) + '\t'
        lines += "Note:" + str(counter) + '\n'
        counter += 1

    output.write(lines)

print "VSQx parsing complete"