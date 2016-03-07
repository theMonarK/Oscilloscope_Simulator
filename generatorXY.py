from math import sin,pi
from observer import Subject
from generator import *

class GeneratorXY(Subject) :
    def __init__(self,aX=0.0,fX=0.0,pX=0.0,oX=0.0,colorX='red',
                    aY=0.0,fY=0.0,pY=0.0,oY=0.0,colorY='blue'):
        Subject.__init__(self)
        self.X = Generator(aX,fX,pX,oX,colorX)
        self.X.generate_signal()
        self.Y = Generator(aY,fY,pY,oY,colorY)
        self.Y.generate_signal()
        self.XY = []
        self.generate_XYCurve()

    def getSignalX(self):
        return self.X

    def getSignalY(self):
        return self.Y

    def getSignalXY(self):
        return self.XY

    def generate_XYCurve(self):
        del self.XY[0:]
        self.sX = self.X.get_signal()
        self.sY = self.Y.get_signal()
        for i in range(0, len(self.sX)):
            self.XY.append((self.sX[i][1], self.sY[i][1]))
        self.X.notify()
        self.Y.notify()
        return self.XY
