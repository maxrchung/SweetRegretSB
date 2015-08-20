sprites = []

def Write(path="storyboard.osb"):
    data = "[Events]\n"
    for sprite in sprites:
        data += sprite.Write()
    data += '\n'
    with open(path, 'w') as output:
        output.write(data)
