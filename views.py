# -*- coding: utf-8 -*-
from Tkinter import *

from observer import Observer
from generator import *
from menu import *

class View(Observer):
    def __init__(self,parent,subject,bg="white"):
        self.subject=subject
        self.signal_id=None
        self.menubar=MenuBar(parent,subject)
        self.canvas=Canvas(parent,bg=bg)
        self.width = self.canvas.cget("width")
        self.height = self.canvas.cget("height")
        self.canvas.bind("<Configure>", self.resize)

    def update(self,subject):
        print("View update")
        signal=subject.get_signal()
        self.signal_id=self.plot_signal(signal)

    def resize(self, event):
        if event:
            self.width=event.width
            self.height=event.height
            self.grid()
            self.update(self.subject)

    def plot_signal(self,signal,color="red"):
        width,height=int(self.width),int(self.height)
        if self.signal_id!=None :
            self.canvas.delete(self.signal_id)
        if signal and len(signal)>1:
            plot=[(x*width, height/2.0*(y+1)) for (x, y) in signal]
            self.signal_id=self.canvas.create_line(plot,fill=color,smooth=1,width=3)
        return self.signal_id

    def grid(self, n=10, m=10):
        self.canvas.delete("all")
        w,h=self.width,self.height
        width,height=int(w),int(h)
        print(w,h)
        self.canvas.create_line(n,height/2,width,height/2,arrow="last")
        self.canvas.create_line(m,height,m,5,arrow="last")
        stepX=(width-10)/m*1.
        stepY=(height+10)/n*1.

        for t in range(1,m+1):
            x =t*stepX
            self.canvas.create_line(x,height,x,20)

        for t in range(1,n+1):
            y =t*stepY
            self.canvas.create_line(10,y,width-14,y)

    def packing(self) :
        self.menubar.pack()
        self.canvas.pack(expand=1, fill='both')

if  __name__ == "__main__" :
    root=Tk()
    model=Generator()
    view=View(root,model)
    view.grid()
    view.packing()
    root.mainloop()
