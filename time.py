# -*- coding: utf-8 -*-

from Tkinter import Scale,Frame,IntVar
from observer import Observer

class Time(Observer):
    def __init__(self,parent,subjects,view):

        self.parent = parent
        self.signalX=subjects.getSignalX()
        self.signalY=subjects.getSignalY()
        self.view = view
        self.timeFrame = Frame(parent)
        self.timeScale = Scale(self.timeFrame,label="Time",orient="horizontal",from_=1.0,to=10.0,
                          sliderlength=50,tickinterval=0,showvalue=0,command=self.update)

    def update(self,event):
        print("update_time(self,event)",self.timeScale.get())
        self.signalX.update_time(self.timeScale.get())
        self.signalY.update_time(self.timeScale.get())
        self.view.update()

    def packing(self) :
        self.timeFrame.pack(fill='x')
        self.timeScale.pack(fill='x')

if  __name__ == "__main__" :
    root=Tk()
    model=GeneratorXY()
    oscillo=Controller(root,model)
    oscillo.packing()
    root.mainloop()
