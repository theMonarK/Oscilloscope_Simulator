# -*- coding: utf-8 -*-
from Tkinter import *
import tkFileDialog, tkMessageBox, shelve

class Save(object):
    def __init__(self,parent,subjects,controlX,controlY):
        self.parent = parent
        self.subjects = subjects
        self.signalX = self.subjects.getSignalX()
        self.signalY = self.subjects.getSignalY()
        self.controlX = controlX
        self.controlY = controlY

    def load(self):
        self.fileName = tkFileDialog.askopenfilename(parent=self.parent,title="Open...")
        self.setParam(self.fileName)

    def test(self,nameEntry):
        print("enter")

    def saving(self,name='save'):
        self.save=shelve.open(name)
        self.save['ampX']=str(self.signalX.get_magnitude())
        self.save['freqX']=str(self.signalX.get_frequency())
        self.save['phaseX']=str(self.signalX.get_phase())
        self.save['offsetX']=str(self.signalX.get_offset())

        self.save['ampY']=str(self.signalY.get_magnitude())
        self.save['freqY']=str(self.signalY.get_frequency())
        self.save['phaseY']=str(self.signalY.get_phase())
        self.save['offsetY']=str(self.signalY.get_offset())
        self.save.close()


    def savingExit(self,name='save'):
        self.saving(name)
        self.parent.destroy()

    def savingAsExit(self):
        self.fileName = tkFileDialog.asksaveasfilename(parent=self.parent,title="Save as...")
        self.savingExit(self.fileName)

    def savingAs(self):
        self.fileName = tkFileDialog.asksaveasfilename(parent=self.parent,title="Save as...")
        self.saving(self.fileName)

    def setParam(self,name='save'):
        self.save=shelve.open(name)
        self.signalX.set_magnitude(float(self.save['ampX'])*5.0)
        print(self.signalX.get_offset())
        self.controlX.scale_amp.set(float(self.save['ampX'])*5.0)
        self.signalX.set_offset(float(self.save['offsetX']))
        self.controlX.scale_offset.set(float(self.save['offsetX'])*5.0)
        self.signalX.set_frequency(float(self.save['freqX']))
        self.controlX.scale_freq.set(float(self.save['freqX']))
        self.signalX.set_phase(float(self.save['phaseX']))
        self.controlX.scale_phase.set(float(self.save['phaseX']))

        self.signalY.set_magnitude(float(self.save['ampY'])*5.0)
        self.controlY.scale_amp.set(float(self.save['ampY'])*5.0)
        self.signalY.set_offset(float(self.save['offsetY']))
        self.controlY.scale_offset.set(float(self.save['offsetY'])*5.0)
        self.signalY.set_frequency(float(self.save['freqY']))
        self.controlY.scale_freq.set(float(self.save['freqY']))
        self.signalY.set_phase(float(self.save['phaseY']))
        self.controlY.scale_phase.set(float(self.save['phaseY']))
        self.save.close()
