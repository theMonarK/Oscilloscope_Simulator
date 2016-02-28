from Tkinter import *
import shelve
import os.path
import re,  tkFileDialog, tkMessageBox

class MenuBar(Frame):
  def __init__(self,parent,subject):
    Frame.__init__(self,borderwidth=2)
    self.parent = parent
    self.subject = subject
    button_file = Menubutton(self,text="File")
    button_file.pack(side="left")
    menu_file=Menu(button_file)
    menu_file.add_command(label='Save', command=self.saving)
    menu_file.add_command(label='Save as...', command=self.savingAs)
    menu_file.add_command(label ='Load', command=self.load)
    menu_file.add_command(label ='Exit', command=self.exit)
    button_file.configure(menu=menu_file)

    button_help = Menubutton(self,text="About")
    button_help.pack(side="left")
    menu_help=Menu(button_help)
    menu_help.add_command(label='About this application...', command=self.about)
    button_help.configure(menu=menu_help)

  def about(self):
      tkMessageBox.showinfo('Oscilloscope Simulator','\tAnthony Guillier\n \ta2guilli@enib.fr',icon='info')

  def error(self):
      errorTop=Toplevel()
      errorTop.title("Error")
      msg = Message(errorTop, text="Le fichier n'existe pas")
      msg.pack()
      buttonOK = Button(errorTop, text="OK", command=errorTop.destroy)
      buttonOK.pack()

  def exit(self):
      MsgBox=tkMessageBox.askquestion(icon='question',title="Quit",message="Save?",type='yesnocancel')
      if MsgBox=='yes':
          self.savingAsExit()
      if MsgBox=='no':
          self.parent.destroy()

  def load(self):
      fileName = tkFileDialog.askopenfilename(parent=self.parent,title="Open...")
      self.setParam(fileName)

  def test(self,nameEntry):
      print("enter")

  def saving(self,name='save'):
      save=shelve.open(name)
      save['amp']=str(self.subject.get_magnitude())
      save['freq']=str(self.subject.get_frequency())
      save['phase']=str(self.subject.get_phase())
      save.close()


  def savingExit(self,name='save'):
      self.saving(name)
      self.parent.destroy()

  def savingAsExit(self):
      fileName = tkFileDialog.asksaveasfilename(parent=self.parent,title="Save as...")
      self.savingExit(fileName)

  def savingAs(self):
      fileName = tkFileDialog.asksaveasfilename(parent=self.parent,title="Save as...")
      self.saving(fileName)

  def setParam(self,name='save'):
      save=shelve.open(name)
      self.subject.set_magnitude(int(save['amp']))
      self.subject.set_frequency(int(save['freq']))
      self.subject.set_phase(int(save['phase']))
      save.close()
