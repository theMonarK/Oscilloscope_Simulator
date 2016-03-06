from Tkinter import *
from save import *
import tkFileDialog, tkMessageBox, tkColorChooser

class MenuBar(Frame):
  def __init__(self,root,parent,subjects,controlX,controlY,view):
    Frame.__init__(self,borderwidth=2)
    self.root = root
    self.parent = parent
    self.subjects = subjects
    self.view = view
    self.controlX = controlX
    self.controlY = controlY
    self.save = Save(self.root,self.subjects,self.controlX,self.controlY)
    self.button_file = Menubutton(self.parent,text="File",underline=0)
    self.menu_file=Menu(self.button_file)
    self.menu_file.add_command(label='Save           ctrl+s', command=self.save.saving,underline=0)
    self.menu_file.add_command(label='Save as...   ctrl+maj+s', command=self.save.savingAs,underline=0)
    self.menu_file.add_command(label='Open          ctrl+o', command=self.save.load,underline=0)
    self.menu_file.add_separator()
    self.menu_file.add_command(label ='Exit             ctrl+q', command=self.exit,underline=0)
    self.button_file.configure(menu=self.menu_file,underline=0)

    self.button_edit = Menubutton(self.parent,text="Edit",underline=0)
    self.menu_edit=Menu(self.button_edit)
    self.menu_edit_sub=Menu(self.button_edit)
    self.menu_edit_sub.add_command(label = 'Background    ctrl+b',command=lambda:self.view.setColor("bg"))
    self.menu_edit_sub.add_command(label = 'Signal X           ctrl+x',command=lambda:self.view.setColor(self.subjects.getSignalX()))
    self.menu_edit_sub.add_command(label = 'Signal Y           ctrl+y',command=lambda:self.view.setColor(self.subjects.getSignalY()))
    self.menu_edit.add_cascade(label='Color', command=self.about,menu=self.menu_edit_sub)
    self.button_edit.configure(menu=self.menu_edit,underline=0)

    self.button_help = Menubutton(self.parent,text="Help",underline=0)
    self.menu_help=Menu(self.button_help)
    self.menu_help.add_command(label='About this application...    ctrl+a', command=self.about)
    self.button_help.configure(menu=self.menu_help,underline=0)

  def about(self):
      tkMessageBox.showinfo('Oscilloscope Simulator','\tAnthony Guillier\n\ta2guilli@enib.fr')

  def exit(self):
      self.MsgBox= tkMessageBox.askquestion(title="Quit",message="Save?",type='yesnocancel')
      if self.MsgBox=='yes':
          self.save.savingAsExit()
      if self.MsgBox=='no':
          self.root.destroy()
  def getSave(self):
      return self.save

  def packing(self):
      self.button_file.pack(side="left")
      self.button_edit.pack(side="left")
      self.button_help.pack(side="right")
