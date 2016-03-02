# -*- coding: utf-8 -*-
from Tkinter import Tk,Toplevel,Scale,Frame,Canvas,IntVar

from observer import Observer
from generator import *
from generatorXY import *

from views import *
from controls import *

class Oscilloscope(object) :
    def __init__(self,parent):
        self.model=Generator()
        self.view=View(parent,self.model)
        self.menuFrame=Frame(parent)
        self.model.attach(self.view)
        self.controls=Controller(parent,self.model)
        self.menubar=MenuBar(parent,self.menuFrame,self.model,self.controls)

    def packing(self) :
        self.menuFrame.pack(fill='x',side='top')
        self.menubar.pack()
        self.view.packing()
        self.controls.packing()

if  __name__ == "__main__" :
    root=Tk()
    root.title("Oscilloscope Simulator")
    oscillo=Oscilloscope(root)
    oscillo.packing()
    root.mainloop()
