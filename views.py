# -*- coding: utf-8 -*-
from Tkinter import *

from observer import Observer
from generator import *
from menu import *

class View(Observer):
    def __init__(self,parent,subject,bg="yellow"):
        self.subject=subject
        self.signal_id=None
        self.menubar = MenuBar(parent)
        self.canvas=Canvas(parent,bg=bg)
    def update(self,subject):
        print("View update")
        signal=subject.get_signal()
        self.signal_id=self.plot_signal(signal)
    def plot_signal(self,signal,color="red"):
        w,h=self.canvas.cget("width"),self.canvas.cget("height")
        width,height=int(w),int(h)
        if self.signal_id!=None :
            self.canvas.delete(self.signal_id)
        if signal and len(signal)>1:
            plot=[(x*width, height/2.0*(y+1)) for (x, y) in signal]
            self.signal_id=self.canvas.create_line(plot,fill=color,smooth=1,width=3)
        return self.signal_id

    def grid(self, n, m):
        w,h=self.canvas.cget("width"),self.canvas.cget("height")
        width,height=int(w),int(h)
        self.canvas.create_line(10,height/2,width,height/2,arrow="last")
        self.canvas.create_line(10,height-5,10,5,arrow="last")
        stepX=(width-10)/m*1.
        stepY=(height+4)/n*1.

        for t in range(1,m+2):
            x =t*stepX
            self.canvas.create_line(x,height,x,10)

        for t in range(1,n+2):
            y =t*stepY
            self.canvas.create_line(10,y,width,y)

    def packing(self) :
        self.menubar.pack()
        self.canvas.pack(fill="both",expand=1)

if  __name__ == "__main__" :
    root=Tk()
    model=Generator()
    view=View(root,model)
    view.grid(10,10)
    view.packing()
    root.mainloop()
