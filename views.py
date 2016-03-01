# -*- coding: utf-8 -*-
from Tkinter import *

from observer import Observer
from generator import *
from menu import *

class View(Observer):
    def __init__(self,parent,subject,bg="white"):
        self.subject=subject
        self.signalX_id=None
        self.signalY_id=None
        self.menuFrame=Frame(parent)
        self.menubar=MenuBar(parent,self.menuFrame,subject)
        self.canvas=Canvas(parent,bg=bg)
        self.width = int(self.canvas.cget("width"))
        self.height = int(self.canvas.cget("height"))
        self.canvas.bind("<Configure>", self.resize)

    def update(self,subject):
        print("View update")
        signalX=subject.get_signal()
        self.signalX_id=self.plot_signal(signalX,self.subject.get_color())

    def resize(self, event):
        if event:
            self.width=event.width
            self.height=event.height
            self.grid()
            self.update(self.subject)

    def plot_signal(self,signal,color='red'):
        width,height=int(self.width-12),int(self.height)
        if self.signalX_id!=None :
            self.canvas.delete(self.signalX_id)
        if signal and len(signal)>1:
            plot=[(x*width+10, height/2.0*(y+1)) for (x, y) in signal]
            self.signalX_id=self.canvas.create_line(plot,fill=color,smooth=1,width=2)
        return self.signalX_id

    def grid(self, n=10, m=10):
        self.canvas.delete("all")
        w,h=self.width,self.height
        width,height=int(w),int(h)
        self.canvas.create_line(n,height/2,width,height/2,arrow="last")
        self.canvas.create_line(m,height,m,5,arrow="last")
        stepX=(width)/m*1.
        stepY=(height)/n*1.

        for t in range(1,m+1):
            x =t*stepX
            self.canvas.create_line(x,height,x,20)

        for t in range(1,n+1):
            y =t*stepY
            self.canvas.create_line(10,y,width-10,y)

    def packing(self) :
        self.menuFrame.pack(fill='x',side='top')
        self.menubar.pack()
        self.canvas.pack(expand=1, fill='both',side='top')

if  __name__ == "__main__" :
    root=Tk()
    model=Generator()
    view=View(root,model)
    view.packing()
    root.mainloop()
