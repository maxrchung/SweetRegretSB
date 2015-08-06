import Storyboard
from Layer import *
from Origin import *
from Easing import *

class Sprite:
    def __init__(self,
                 filePath = "default.png",
                 x = 0,
                 y = 0,
                 origin = Origin.Centre,
                 layer = Layer.Background):
        # Quotes around the filePath allow for files that have spaces in them
        self.FilePath = '"' + filePath + '"';
        self.X = x;
        self.Y = y;
        self.Layer = layer
        self.Origin = origin
        self.Commands = []
        
        Storyboard.sprites.append(self)

    def Fade(self,
             startTime = 0,
             endTime = 0,
             startOpacity = 1.0,
             endOpacity = 1.0,
             easing = Easing.Linear):
        self.Commands.append("_F,"\
                             "{Easing},"\
                             "{StartTime},"\
                             "{EndTime},"\
                             "{StartOpacity},"\
                             "{EndOpacity}\n".format(Easing = easing,
                                                     StartTime = startTime,
                                                     EndTime = endTime,
                                                     StartOpacity = startOpacity,
                                                     EndOpacity = endOpacity))

    def Move(self,
             startTime = 0,
             endTime = 0,
             startX = 0,
             startY = 0,
             endX = 0,
             endY = 0,
             easing = Easing.Linear):
        self.Commands.append("_M,"\
                             "{Easing},"\
                             "{StartTime},"\
                             "{EndTime},"\
                             "{StartX},"\
                             "{StartY},"\
                             "{EndX},"\
                             "{EndY}\n".format(Easing = easing,
                                               StartTime = startTime,
                                               EndTime = endTime,
                                               StartX = startX,
                                               StartY = startY,
                                               EndX = endX,
                                               EndY = endY))


    def MoveX(self,
              startTime = 0,
              endTime = 0,
              startX = 0,
              endX = 0,
              easing = Easing.Linear):
        self.Commands.append("_MX,"\
                             "{Easing},"\
                             "{StartTime},"\
                             "{EndTime},"\
                             "{StartX},"\
                             "{EndX}\n".format(Easing = easing,
                                               StartTime = startTime,
                                               EndTime = endTime,
                                               StartX = startX,
                                               EndX = endX))

    def MoveY(self,
              startTime = 0,
              endTime = 0,
              startY = 0,
              endY = 0,
              easing = Easing.Linear):
        self.Commands.append("_MY,"\
                             "{Easing},"\
                             "{StartTime},"\
                             "{EndTime},"\
                             "{StartY},"\
                             "{EndY}\n".format(Easing = easing,
                                               StartTime = startTime,
                                               EndTime = endTime,
                                               StartY = startY,
                                               EndY = endY))

    def Scale(self,
              startTime = 0,
              endTime = 0,
              startScale = 1.0,
              endScale = 1.0,
              easing = Easing.Linear):
        self.Commands.append("_S,"\
                             "{Easing},"\
                             "{StartTime},"\
                             "{EndTime},"\
                             "{StartScale},"\
                             "{EndScale}\n".format(Easing = easing,
                                                   StartTime = startTime,
                                                   EndTime = endTime,
                                                   StartScale = startScale,
                                                   EndScale = endScale))

    def Rotate(self,
               startTime = 0,
               endTime = 0,
               startRotate = 0.0,
               endRotate = 0.0,
               easing = Easing.Linear):
        self.Commands.append("_R,"\
                             "{Easing},"\
                             "{StartTime},"\
                             "{EndTime},"\
                             "{StartRotate},"\
                             "{EndRotate}\n".format(Easing = easing,
                                                    StartTime = startTime,
                                                    EndTime = endTime,
                                                    StartRotate = startRotate,
                                                    EndRotate = endRotate))

    def Color(self,
              startTime = 0,
              endTime = 0,
              startR = 255,
              startG = 255,
              startB = 255,
              endR = 255,
              endG = 255,
              endB = 255,
              easing = Easing.Linear):
        self.Commands.append("_C,"\
                             "{Easing},"\
                             "{StartTime},"\
                             "{EndTime},"\
                             "{StartR},"\
                             "{StartG},"\
                             "{StartB},"\
                             "{EndR},"\
                             "{EndG},"\
                             "{EndB}\n".format(Easing = easing,
                                               StartTime = startTime,
                                               EndTime = endTime,
                                               StartR = startR,
                                               StartG = startG,
                                               StartB = startB,
                                               EndR = endR,
                                               EndG = endG,                                               
                                               EndB = endB))        
    
    def Write(self):
        sprite = "Sprite,"\
                 "{Layer},"\
                 "{Origin},"\
                 "{FilePath},"\
                 "{X},{Y}\n".format(Layer = self.Layer,
                                    Origin = self.Origin,
                                    FilePath = self.FilePath,
                                    X = self.X,
                                    Y = self.Y)
        for command in self.Commands:
            sprite += command
        return sprite;
    
