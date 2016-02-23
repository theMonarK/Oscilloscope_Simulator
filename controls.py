# -*- coding: utf-8 -*-

from Tkinter import Tk,Toplevel,Scale,Frame,IntVar

from observer import Observer
from generator import *

class Controller(Observer):
    def __init__(self,parent,subject):

        self.cursorFrame = Frame(parent)
        self.subject=subject
        self.amp=IntVar()
        self.scale_amp=Scale(self.cursorFrame,variable=self.amp,
                          label="Amplitude",
                          orient="horizontal",length=250,
                          showvalue=0,from_=0,to=5,
                          sliderlength=20,tickinterval=25,
                          command=self.update_amplitude)
        self.freq=IntVar()
        self.scale_freq=Scale(self.cursorFrame,variable=self.freq,
                          label="Frequence",
                          orient="horizontal",length=250,
                          showvalue=0,from_=0,to=5,
                          sliderlength=20,tickinterval=25,
                          command=self.update_frequency)

        self.phase=IntVar()
        self.scale_phase=Scale(self.cursorFrame,variable=self.phase,
                          label="Phase",
                          orient="horizontal",length=250,
                          showvalue=0,from_=-90,to=90,
                          sliderlength=20,tickinterval=25,
                          command=self.update_phase)

    def update(self,subject):
        print("Control update")
        pass
    def update_amplitude(self,event):
        print("update_amplitude(self,event)",self.amp.get())
        self.subject.set_magnitude(self.amp.get())
    def update_frequency(self,event):
        print("update_frequency(self,event)",self.freq.get())
        self.subject.set_frequency(self.freq.get())
    def update_phase(self,event):
        print("update_phase(self,event)",self.phase.get())
        self.subject.set_phase(self.phase.get())
    def packing(self) :
        self.cursorFrame.pack(side='bottom')
        self.scale_amp.pack()
        self.scale_freq.pack()
        self.scale_phase.pack()

if  __name__ == "__main__" :
    root=Tk()
    model=Generator()
    oscillo=Controller(root,model)
    oscillo.packing()
    root.mainloop()
