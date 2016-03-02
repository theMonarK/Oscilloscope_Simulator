from math import sin,pi
from observer import Subject
from generator import *

class GeneratorXY(Subject) :
    def __init__(self,aX=1.0,fX=1.0,pX=0.0,oX=0.0,colorX='red',
                    aY=1.0,fY=1.0,pY=0.0,oY=0.0,colorY='blue'):
        Subject.__init__(self)
        self.X = Generator(aX,fX,pX,oX,colorX)
        self.X.generate_signal()
        self.Y = Generator(aY,fY,pY,oY,colorY)
        self.Y.generate_signal()

    def getSignalX(self):
        return self.X

    def getSignalY(self):
        return self.Y
