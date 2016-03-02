# -*- coding: utf-8 -*-
from Tkinter import *
import tkFileDialog, tkMessageBox, shelve

class Save(object):
    def __init__(self,parent,subject,controls):
        self.parent = parent
        self.subject = subject
        self.controls = controls

    def load(self):
        self.fileName = tkFileDialog.askopenfilename(parent=self.parent,title="Open...")
        self.setParam(self.fileName)

    def test(self,nameEntry):
        print("enter")

    def saving(self,name='save'):
        self.save=shelve.open(name)
        self.save['amp']=str(self.subject.get_magnitude())
        self.save['freq']=str(self.subject.get_frequency())
        self.save['phase']=str(self.subject.get_phase())
        self.save['offset']=str(self.subject.get_offset())
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
        self.subject.set_magnitude(float(self.save['amp']))
        self.controls.scale_amp.set(float(self.save['amp']))
        self.subject.set_offset(float(self.save['offset']))
        self.controls.scale_offset.set(float(self.save['offset']))
        self.subject.set_frequency(float(self.save['freq']))
        self.controls.scale_freq.set(float(self.save['freq']))
        self.subject.set_phase(float(self.save['phase']))
        self.controls.scale_phase.set(float(self.save['phase']))
        self.save.close()
