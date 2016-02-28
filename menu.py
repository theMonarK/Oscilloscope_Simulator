from Tkinter import *
import shelve
import os.path
import re,  tkFileDialog, tkMessageBox

class MenuBar(Frame):
  def __init__(self,parent,subject):
    Frame.__init__(self,borderwidth=2)
    self.parent = parent
    self.subject = subject
    self.button_file = Menubutton(self,text="File")
    self.button_file.pack(side="left")
    self.menu_file=Menu(self.button_file)
    self.menu_file.add_command(label='Save', command=self.saving)
    self.menu_file.add_command(label='Save as...', command=self.savingAs)
    self.menu_file.add_command(label ='Load', command=self.load)
    self.menu_file.add_command(label ='Exit', command=self.exit)
    self.button_file.configure(menu=self.menu_file)

    self.button_help = Menubutton(self,text="About")
    self.button_help.pack(side="left")
    self.menu_help=Menu(self.button_help)
    self.menu_help.add_command(label='About this application...', command=self.about)
    self.button_help.configure(menu=self.menu_help)

  def about(self):
      tkMessageBox.showinfo('Oscilloscope Simulator','\tAnthony Guillier\n\ta2guilli@enib.fr')

  def exit(self):
      self.MsgBox= tkMessageBox.askquestion(title="Quit",message="Save?",type='yesnocancel')
      if self.MsgBox=='yes':
          self.savingAsExit()
      if self.MsgBox=='no':
          self.parent.destroy()

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
      self.subject.set_magnitude(int(self.save['amp']))
      self.subject.set_frequency(int(self.save['freq']))
      self.subject.set_phase(int(self.save['phase']))
      self.save.close()
