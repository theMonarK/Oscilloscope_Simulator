# -*- coding: utf-8 -*-

from Tkinter import Tk,Toplevel,Scale,Frame,IntVar,Label,Radiobutton,DoubleVar,Checkbutton
from observer import Observer
from generator import *

class Controller(Observer):
    def __init__(self,parent,subject):

        self.cursorFrame = Frame(parent)
        self.radiobuttonFrame = Frame(parent)
        self.subject=subject
        self.amp=IntVar()
        self.scale_amp=Scale(self.cursorFrame,variable=self.amp,
                          label="Amplitude",
                          orient="horizontal",length=250,from_=0,to=10,
                          sliderlength=50,tickinterval=1,
                          command=self.update_amplitude)
        self.freq=IntVar()
        self.scale_freq=Scale(self.cursorFrame,variable=self.freq,
                          label="Frequence",
                          orient="horizontal",length=250,from_=0,to=5,
                          sliderlength=50,tickinterval=1,
                          command=self.update_frequency)
        self.offset=DoubleVar()
        self.scale_offset=Scale(self.cursorFrame,variable=self.offset,
                          label="Offset",
                          orient="horizontal",length=250,from_=-10.0,to=10.0,
                          sliderlength=50,tickinterval=5,
                          command=self.update_offset)

        self.phase=IntVar()
        self.scale_phase=Scale(self.cursorFrame,variable=self.phase,
                          label="Phase",
                          orient="horizontal",length=250,from_=-90,to=90,
                          sliderlength=10,tickinterval=45,
                          command=self.update_phase)

        self.voltVar = DoubleVar()
        self.voltVar.set(1)

        self.button1 = Radiobutton(self.radiobuttonFrame, text="1V", variable=self.voltVar,
                                    value=1.0*5.0,indicatoron = 0,command=lambda:self.update_amplitude)
        self.button1.select()

        self.button2 = Radiobutton(self.radiobuttonFrame, text="2V", variable=self.voltVar,
                                    value=2.0*5.0,indicatoron = 0,command=lambda:self.update_amplitude)

        self.button5 = Radiobutton(self.radiobuttonFrame, text="5V", variable=self.voltVar,
                                    value=5.0*5.0,indicatoron = 0, command=lambda:self.update_amplitude)

        self.isOffsetVar= IntVar()
        self.isOffset = Checkbutton(self.radiobuttonFrame,text = "Offset", variable = self.isOffsetVar
                                    ,command=lambda:self.update_offset)

    def test(self):
        print('check')

    def update(self,subject):
        pass

    def update_amplitude(self,event):
        print("update_amplitude(self,event)",self.amp.get())
        self.subject.set_magnitude(self.amp.get()/self.voltVar.get())
    def update_frequency(self,event):
        print("update_frequency(self,event)",self.freq.get())
        self.subject.set_frequency(self.freq.get())
    def update_phase(self,event):
        print("update_phase(self,event)",self.phase.get())
        self.subject.set_phase(self.phase.get())
    def update_offset(self,event):
        print("update_offset(self,event)",self.offset.get())
        self.subject.set_offset(self.offset.get()*self.isOffsetVar.get()/(self.voltVar.get()))
    def packing(self) :
        self.cursorFrame.pack(side='bottom')
        self.scale_amp.pack()
        self.scale_freq.pack()
        self.scale_offset.pack()
        self.scale_phase.pack()
        self.radiobuttonFrame.pack(side='top')
        self.button1.pack(side='left')
        self.button2.pack(side='left')
        self.button5.pack(side='left')
        self.isOffset.pack(side='left')

if  __name__ == "__main__" :
    root=Tk()
    model=Generator()
    oscillo=Controller(root,model)
    oscillo.packing()
    root.mainloop()
