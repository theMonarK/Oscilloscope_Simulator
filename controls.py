# -*- coding: utf-8 -*-

from Tkinter import Tk,Toplevel,Scale,Frame,IntVar,Label,Radiobutton,DoubleVar,Checkbutton,StringVar
from observer import Observer
from generator import *

class Controller(Observer):
    def __init__(self,parent,subject):

        self.cursorFrame = Frame(parent)
        self.selectionFrame = Frame(self.cursorFrame)
        self.xyFrame = Frame (self.cursorFrame)
        self.subject=subject
        self.amp=IntVar()
        self.scale_amp=Scale(self.cursorFrame,variable=self.amp,
                          label="Amplitude",
                          orient="horizontal",length=250,from_=0,to=10,
                          sliderlength=50,tickinterval=1,
                          command=self.update)
        self.freq=IntVar()
        self.scale_freq=Scale(self.cursorFrame,variable=self.freq,
                          label="Frequence",
                          orient="horizontal",length=250,from_=0,to=5,
                          sliderlength=50,tickinterval=1,
                          command=self.update)
        self.offset=DoubleVar()
        self.scale_offset=Scale(self.cursorFrame,variable=self.offset,
                          label="Offset",
                          orient="horizontal",length=250,from_=-10.0,to=10.0,
                          sliderlength=50,tickinterval=5,
                          command=self.update)

        self.phase=IntVar()
        self.scale_phase=Scale(self.cursorFrame,variable=self.phase,
                          label="Phase",
                          orient="horizontal",length=250,from_=-90,to=90,
                          sliderlength=10,tickinterval=45,
                          command=self.update)

        self.voltVar = DoubleVar()
        self.voltVar.set(1)
        self.isOffsetVar= IntVar()
        self.hzVar= IntVar()
        self.secVar= DoubleVar()
        self.isXvar= IntVar()
        self.isYvar= IntVar()
        self.xyVar= StringVar()

        self.button1 = Radiobutton(self.selectionFrame, text="1V", variable=self.voltVar,
                                    value=1.0*5.0)
        self.button1.select()
        self.button1.bind('<Motion>',self.update)

        self.button2 = Radiobutton(self.selectionFrame, text="2V", variable=self.voltVar,
                                    value=2.0*5.0)
        self.button2.bind('<Motion>',self.update)

        self.button5 = Radiobutton(self.selectionFrame, text="5V", variable=self.voltVar,
                                    value=5.0*5.0)
        self.button5.bind('<Motion>',self.update)

        self.buttonX = Radiobutton(self.xyFrame, text="X", variable=self.xyVar,
                                    value="X")
        self.buttonX.select()
        self.buttonX.bind('<Motion>',self.update)

        self.buttonY = Radiobutton(self.xyFrame, text="Y", variable=self.xyVar,
                                    value="Y")
        self.buttonY.bind('<Motion>',self.update)

        self.buttonXY = Radiobutton(self.xyFrame, text="XY", variable=self.xyVar,
                                    value="XY")
        self.buttonXY.bind('<Motion>',self.update)

        self.isOffset = Checkbutton(self.selectionFrame,text = "Offset", variable = self.isOffsetVar)
        self.isOffset.bind('<Motion>',self.update)

    def update(self,event):
        print(self.xyVar.get())
        self.update_amplitude(event)
        self.update_offset(event)
        self.update_frequency(event)
        self.update_phase(event)

    def toggleSignal(self,event,isSelected=1):
        if isSelected:
            self.subject.set_magnitude(1)
            self.update(event)
        else:
            self.subject.set_magnitude(self.amp.get()/self.voltVar.get())


    def update_amplitude(self,event):
        print("update_amplitude(self,event)",self.amp.get())
        self.subject.set_magnitude(self.amp.get()/self.voltVar.get())
    def update_frequency(self,event):
        print("update_frequency(self,event)",self.freq.get())
        self.subject.set_frequency(self.freq.get())
    def update_phase(self,event):
        print("update_phase(self,event)",self.phase.get())
        self.subject.set_phase(self.phase.get())
    def update_XY(self,event):
        print("update_XY(self,event)",self.phase.get())
        self.subject.set_phase(self.phase.get())
    def update_offset(self,event):
        print("update_offset(self,event)",self.offset.get())
        self.xy=self.xyVar.get()

    def packing(self) :
        self.xyFrame.pack(side='top')
        self.buttonX.pack(side='left')
        self.buttonY.pack(side='left')
        self.buttonXY.pack(side='left')
        self.selectionFrame.pack(side='top')
        self.button1.pack(side='left')
        self.button2.pack(side='left')
        self.button5.pack(side='left')
        self.isOffset.pack(side='left')
        self.cursorFrame.pack(side='left',expand=1, fill='both')
        self.scale_amp.pack()
        self.scale_freq.pack()
        self.scale_offset.pack()
        self.scale_phase.pack()

if  __name__ == "__main__" :
    root=Tk()
    model=Generator()
    oscillo=Controller(root,model)
    oscillo.packing()
    root.mainloop()
