from UCISB import *

sprite = Sprite()
sprite.Fade()
sprite.Move()
sprite.MoveX()
sprite.MoveY()
sprite.Scale()
sprite.Rotate()
sprite.Color()

path = r"storyboard.osb"
Storyboard.Write(path)

print "Storyboard generation complete"
