# -*- coding: utf-8 -*-
from Tkinter import Tk,Toplevel,Scale,Frame,Canvas,IntVar

from observer import Observer
from generator import *
from generatorXY import *
from lissajou import *
from time import Time

from views import *
from controls import *

class Oscilloscope(object) :
    def __init__(self,parent):
        self.parent = parent
        self.model=GeneratorXY()
        self.view=View(parent,self.model)
        self.menuFrame=Frame(parent)
        self.lissajouTimaFrame=Frame(parent)
        self.lissajouTopLevel = None
        self.lissajou = None
        self.model.attach(self.view)
        self.time = Time(self.lissajouTimaFrame,self.model,self.view)
        self.lissajouButton = Button(self.lissajouTimaFrame, text = "XY Curve",
                                    command=lambda:self.createLissajou(self.model),pady = 18)
        self.controlY=Controller(parent,self.view,None,self.model.getSignalY(),self.model)
        self.controlX=Controller(parent,self.view,None,self.model.getSignalX(),self.model)
        self.menubar=MenuBar(parent,self.menuFrame,self.model,self.controlX,self.controlY,self.view)

        self.parent.protocol('WM_DELETE_WINDOW', lambda:self.menubar.exit())
        self.save = self.menubar.getSave()
        self.parent.bind('<Control-o>', lambda x:self.save.load())
        self.parent.bind('<Control-s>', lambda x:self.save.saving())
        self.parent.bind('<Control-q>', lambda x:self.menubar.exit())
        self.parent.bind('<Control-d>', lambda x:self.save.savingAs())
        self.parent.bind('<Control-b>', lambda x:self.view.setColor("bg"))
        self.parent.bind('<Control-g>', lambda x:self.view.setColor("grid"))
        self.parent.bind('<Control-x>', lambda x:self.view.setColor(self.model.getSignalX()))
        self.parent.bind('<Control-y>', lambda x:self.view.setColor(self.model.getSignalY()))
        self.parent.bind('<Control-a>', lambda x:self.menubar.about())
        self.parent.bind('<Control-l>', lambda x:self.createLissajou(self.model))


    def test(self) :
        save = self.menubar.getSave()
        save.load()

    def createLissajou(self,model) :
        if self.lissajou == None:
            self.lissajouTopLevel = Toplevel(self.parent)
            self.lissajouTopLevel.protocol('WM_DELETE_WINDOW', lambda:self.deleteLissajou())
            self.lissajouTopLevel.wm_attributes("-topmost", True)
            self.lissajouTopLevel.title("XY Curve")
            self.lissajou = Lissajou (self.lissajouTopLevel,self.model)
            self.model.attach(self.lissajou)
            self.controlX.setLissajou(self.lissajou)
            self.controlY.setLissajou(self.lissajou)
            self.lissajou.packing()


    def deleteLissajou(self):
        self.lissajou = None
        self.controlX.setLissajou(self.lissajou)
        self.controlY.setLissajou(self.lissajou)
        self.lissajouTopLevel.destroy()

    def packing(self) :
        self.menuFrame.pack(fill='x',side='top')
        self.menubar.packing()
        self.view.packing()
        self.lissajouTimaFrame.pack(fill='x')
        self.lissajouButton.pack(side="right")
        self.time.packing()
        self.controlX.packing()
        self.controlY.packing()

if  __name__ == "__main__" :
    root=Tk()
    root.title("Oscilloscope Simulator")
    oscillo=Oscilloscope(root)
    oscillo.packing()
    root.mainloop()
