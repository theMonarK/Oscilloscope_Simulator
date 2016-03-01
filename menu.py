from Tkinter import *
from save import *
import re,  tkFileDialog, tkMessageBox

class MenuBar(Frame):
  def __init__(self,root,parent,subject):
    Frame.__init__(self,borderwidth=2)
    self.root = root
    self.parent = parent
    self.subject = subject
    self.save = Save(self.root,self.subject)
    self.button_file = Menubutton(self.parent,text="File")
    self.button_file.pack(side="left")
    self.menu_file=Menu(self.button_file)
    self.menu_file.add_command(label='Save', command=self.save.saving)
    self.menu_file.add_command(label='Save as...', command=self.save.savingAs)
    self.menu_file.add_command(label ='Open', command=self.save.load)
    self.menu_file.add_command(label ='Exit', command=self.exit)
    self.button_file.configure(menu=self.menu_file)

    self.button_help = Menubutton(self.parent,text="Help")
    self.button_help.pack(side="left")
    self.menu_help=Menu(self.button_help)
    self.menu_help.add_command(label='About this application...', command=self.about)
    self.button_help.configure(menu=self.menu_help)

  def about(self):
      tkMessageBox.showinfo('Oscilloscope Simulator','\tAnthony Guillier\n\ta2guilli@enib.fr')

  def exit(self):
      self.MsgBox= tkMessageBox.askquestion(title="Quit",message="Save?",type='yesnocancel')
      if self.MsgBox=='yes':
          self.save.savingAsExit()
      if self.MsgBox=='no':
          self.root.destroy()
