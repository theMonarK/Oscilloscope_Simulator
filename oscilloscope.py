# -*- coding: utf-8 -*-
from Tkinter import Tk,Toplevel,Scale,Frame,Canvas,IntVar

from observer import Observer
from generator import *
from generatorXY import *
from time import Time

from views import *
from controls import *

class Oscilloscope(object) :
    def __init__(self,parent):
        self.model=GeneratorXY()
        self.view=View(parent,self.model)
        self.menuFrame=Frame(parent)
        self.model.attach(self.view)
        self.time = Time(parent,self.model,self.view)
        self.controlY=Controller(parent,self.view,self.model.getSignalY())
        self.controlX=Controller(parent,self.view,self.model.getSignalX())
        self.menubar=MenuBar(parent,self.menuFrame,self.model,self.controlX,self.controlY,self.view)


    def packing(self) :
        self.menuFrame.pack(fill='x',side='top')
        self.menubar.packing()
        self.view.packing()
        self.time.packing()
        self.controlX.packing()
        self.controlY.packing()

if  __name__ == "__main__" :
    root=Tk()
    root.title("Oscilloscope Simulator")
    oscillo=Oscilloscope(root)
    oscillo.packing()
    root.mainloop()
