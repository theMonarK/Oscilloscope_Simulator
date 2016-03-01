# -*- coding: utf-8 -*-
from Tkinter import Tk,Toplevel,Scale,Frame,Canvas,IntVar

from observer import Observer
from generator import *

from views import *
from controls import *

class Oscilloscope(object) :
    def __init__(self,parent):
        self.model=Generator()
        self.modelY=Generator(color='blue')
        self.view=View(parent,self.model)
        self.model.attach(self.view)
        self.modelY.attach(self.view)
        self.controls=Controller(parent,self.model)
        self.controlsY=Controller(parent,self.modelY)
    def packing(self) :
        self.view.packing()
        self.controls.packing()
        self.controlsY.packing()

if  __name__ == "__main__" :
    root=Tk()
    root.title("Oscilloscope Simulator")
    oscillo=Oscilloscope(root)
    oscillo.packing()
    root.mainloop()
