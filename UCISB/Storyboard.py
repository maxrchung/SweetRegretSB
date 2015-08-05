sprites = []

def write(path="storyboard.osb"):
    data = ""
    for sprite in sprites:
        data += sprite.write() + "\n"
    with open(path, 'w') as output:
        output.write(data)
