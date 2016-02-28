# -*- coding: utf-8 -*-

from Tkinter import Tk,Toplevel,Scale,Frame,IntVar,Label,Radiobutton,DoubleVar
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
                          orient="horizontal",length=250,
                          showvalue=0,from_=0,to=5,
                          sliderlength=20,tickinterval=25,
                          command=self.update_amplitude)
        self.labelAmp=Label(self.cursorFrame, textvariable=self.amp,fg="black")
        self.freq=IntVar()
        self.scale_freq=Scale(self.cursorFrame,variable=self.freq,
                          label="Frequence",
                          orient="horizontal",length=250,
                          showvalue=0,from_=0,to=5,
                          sliderlength=20,tickinterval=25,
                          command=self.update_frequency)
        self.labelFreq=Label(self.cursorFrame, textvariable=self.freq,fg="black")

        self.phase=IntVar()
        self.scale_phase=Scale(self.cursorFrame,variable=self.phase,
                          label="Phase",
                          orient="horizontal",length=250,
                          showvalue=0,from_=-90,to=90,
                          sliderlength=20,tickinterval=25,
                          command=self.update_phase)
        self.labelPhase=Label(self.cursorFrame, textvariable=self.phase,fg="black")

        self.voltVar = DoubleVar()
        self.voltVar.set(1)

        self.button1 = Radiobutton(self.radiobuttonFrame, text="1V", variable=self.voltVar,
                                    value=1.0,indicatoron = 0,command=lambda:self.update_amplitude)
        self.button1.select()

        self.button2 = Radiobutton(self.radiobuttonFrame, text="2V", variable=self.voltVar,
                                    value=2.0,indicatoron = 0,command=lambda:self.update_amplitude)

        self.button5 = Radiobutton(self.radiobuttonFrame, text="5V", variable=self.voltVar,
                                    value=5.0,indicatoron = 0, command=lambda:self.update_amplitude)

    def test(self):
        print(self.voltVar.get())

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
    def packing(self) :
        self.cursorFrame.pack(side='bottom')
        self.scale_amp.pack()
        self.labelAmp.pack()
        self.scale_freq.pack()
        self.labelFreq.pack()
        self.scale_phase.pack()
        self.labelPhase.pack()
        self.radiobuttonFrame.pack(side='bottom')
        self.button1.pack(side='left')
        self.button2.pack(side='left')
        self.button5.pack(side='left')

if  __name__ == "__main__" :
    root=Tk()
    model=Generator()
    oscillo=Controller(root,model)
    oscillo.packing()
    root.mainloop()
