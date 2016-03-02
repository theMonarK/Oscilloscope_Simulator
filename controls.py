# -*- coding: utf-8 -*-

from Tkinter import Tk,Toplevel,Scale,Frame,IntVar,Label,Radiobutton,DoubleVar,Checkbutton,StringVar
from observer import Observer
from generator import *

class Controller(Observer):
    def __init__(self,parent,view,subjectSig):

        self.cursorFrame = Frame(parent)
        self.selectionFrame = Frame(self.cursorFrame)
        self.view = view
        self.subjectSig=subjectSig
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
        self.button1 = Radiobutton(self.selectionFrame, text="1V", variable=self.voltVar,
                                    value=1.0*5.0,command =lambda:self.update(None))
        self.button1.select()

        self.button2 = Radiobutton(self.selectionFrame, text="2V", variable=self.voltVar,
                                    value=2.0*5.0, command =lambda:self.update(None))

        self.button5 = Radiobutton(self.selectionFrame, text="5V", variable=self.voltVar,
                                    value=5.0*5.0, command =lambda:self.update(None))

        self.isOffsetVar= IntVar()
        self.isOffset = Checkbutton(self.selectionFrame,text = "Offset",variable = self.isOffsetVar,
                                    command =lambda:self.update(None))

    def update(self,event):
        self.update_amplitude(event)
        self.update_offset(event)
        self.update_frequency(event)
        self.update_phase(event)
        self.view.update()


    def update_amplitude(self,event):
        print("update_amplitude(self,event)",self.amp.get())
        self.subjectSig.set_magnitude(self.amp.get()/self.voltVar.get())
    def update_frequency(self,event):
        print("update_frequency(self,event)",self.freq.get())
        self.subjectSig.set_frequency(self.freq.get())
    def update_phase(self,event):
        print("update_phase(self,event)",self.phase.get())
        self.subjectSig.set_phase(self.phase.get())
    def update_offset(self,event):
        if self.isOffsetVar.get():
            print(self.isOffsetVar.get())
            print("update_offset(self,event)",self.isOffsetVar.get())
            self.subjectSig.set_offset(self.offset.get()/self.voltVar.get())
        else:
            self.subjectSig.set_offset(0.0)

    def packing(self) :
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
    model=GeneratorXY()
    oscillo=Controller(root,model)
    oscillo.packing()
    root.mainloop()
