# -*- coding: utf-8 -*-
from Tkinter import *

from observer import Observer
from generator import *
from menu import *

class View(Observer):
    def __init__(self,parent,subjects,bg="white"):
        self.subjects=subjects
        self.signals_id={"X":None,"Y":None,"XY":None}
        self.canvas=Canvas(parent,bg=bg)
        self.xyFrame = Frame (parent)
        self.width = int(self.canvas.cget("width"))
        self.height = int(self.canvas.cget("height"))

        self.xyVar= StringVar()
        self.buttonX = Radiobutton(self.xyFrame, text="X", variable=self.xyVar,
                                    value="X", command=lambda:self.deleteSignal("Y"))

        self.buttonY = Radiobutton(self.xyFrame, text="Y", variable=self.xyVar,
                                value="Y", command=lambda:self.deleteSignal("X"))

        self.buttonX_Y = Radiobutton(self.xyFrame, text="X-Y", variable=self.xyVar,
                                    value="XY", command=self.update)
        self.buttonX_Y.select()

        self.canvas.bind("<Configure>", self.resize)

    def update(self):
        print("View update")
        signalX = self.subjects.getSignalX()
        signalY = self.subjects.getSignalY()
        self.signals_id["X"] = self.plot_signal(signalX,"X",signalX.get_color())
        self.signals_id["Y"] = self.plot_signal(signalY,"Y",signalY.get_color())

    def resize(self, event):
        if event:
            self.width=event.width
            self.height=event.height
            self.grid()
            self.update()

    def plot_signal(self,signal,deletedSignal="X",color='red'):
        width,height=int(self.width-12),int(self.height)
        signal = signal.get_signal()
        if signal!=None :
            self.canvas.delete(self.signals_id[deletedSignal])
        if signal and len(signal)>1:
            plot=[(x*width+10, height/2.0*(y+1)) for (x, y) in signal]
            signalValue=self.canvas.create_line(plot,fill=color,smooth=1,width=2)
        return signalValue

    def animate(self,x,y,color):
        width,height=int(self.width-12),int(self.height)
        plot=(x*width+10, height/2.0*(y+1))
        signal=self.canvas.create_line(plot,fill=color,smooth=1,width=2)
        return signal

    def deleteSignal(self,choice="Y"):
        self.update()
        self.canvas.delete(self.signals_id[choice])

    def setColor(self,signal):
        self.signal = signal
        (triple, hexstr) = tkColorChooser.askcolor()
        if hexstr:
            if signal=="bg":
                self.canvas.configure(bg=hexstr)
            if signal=="grid":
                self.grid(color=hexstr)
            else:
                self.signal.set_color(hexstr)
            self.update()

    def grid(self, n=10, m=10,color='black'):
        self.canvas.delete("all")
        w,h=self.width,self.height
        width,height=int(w),int(h)
        self.canvas.create_line(n,height/2,width,height/2,arrow="last",fill=color)
        self.canvas.create_line(m,height,m,5,arrow="last",fill=color)
        stepX=(width)/m*1.0
        stepY=(height)/n*1.0

        for t in range(1,m+1):
            x =t*stepX
            self.canvas.create_line(x,height,x,20,fill=color)

        for t in range(1,n+1):
            y =t*stepY
            self.canvas.create_line(10,y,width-10,y,fill=color)

    def packing(self) :
        self.xyFrame.pack(side='top')
        self.buttonX_Y.pack(side='left')
        self.buttonX.pack(side='left')
        self.buttonY.pack(side='left')
        self.canvas.pack(expand=1, fill='both',side='top')

if  __name__ == "__main__" :
    root=Tk()
    model=GeneratorXY()
    view=View(root,model)
    view.packing()
    root.mainloop()
