# -*- coding: utf-8 -*-
from Tkinter import Tk, Canvas, Frame
from observer import Observer


class Lissajou(Observer):
    def __init__(self, parent,subjects,bg="white"):
        self.parent=parent
        self.subjects=subjects
        self.lissajouFrame = Frame (parent)
        self.canvas=Canvas(self.lissajouFrame,bg=bg)
        self.width = int(self.canvas.cget("width"))
        self.height = int(self.canvas.cget("height"))

        self.signalXY_id = None
        self.canvas.bind("<Configure>", self.resize)
        self.packing()

    def update(self):
        print("Lissajou update")
        self.signalXY_id = self.plot_lissajou()

    def resize(self, event):
        if event:
            self.width=event.width
            self.height=event.height
            self.grid()
            self.update()
            self.packing()

    def grid(self, n=10, m=10):
        self.canvas.delete("all")
        w,h=self.width,self.height
        width,height=int(w),int(h)
        self.canvas.create_line(n,height/2,width,height/2,arrow="last")
        self.canvas.create_line(width/2,height,width/2,5,arrow="last")
        stepX=(width)/m*1.0
        stepY=(height)/n*1.0

        for t in range(1,m+1):
            x =t*stepX
            self.canvas.create_line(x,height,x,20)

        for t in range(1,n+1):
            y =t*stepY
            self.canvas.create_line(10,y,width-10,y)

    def plot_lissajou(self,color='green'):
        width,height=int(self.width-12),int(self.height)
        signalXY = self.subjects.getSignalXY()
        if signalXY!=None:
            self.canvas.delete(self.signalXY_id)
        if signalXY and len(signalXY)>1:
            plot=[((x+1)*width/2, height/2.0*(y+1)) for (x, y) in signalXY]
            signalValue = self.canvas.create_line(plot, fill=color, smooth=1, width=2)
        return signalValue

    def packing(self):
        self.lissajouFrame.pack(side='top')
        self.canvas.pack(expand=1, fill='both',side='top')

if __name__ == "__main__":
    root = Tk()
    model = GeneratorXY()
    lissajou = Lissajou(root,model)
    lissajou.packing()
    root.mainloop()
