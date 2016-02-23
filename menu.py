from Tkinter import *

class MenuBar(Frame):
  def __init__(self,parent):
    Frame.__init__(self,borderwidth=2)
    button_file = Menubutton(self,text="File")
    button_file.pack()
    menu_file=Menu(button_file)
    menu_file.add_command(label='Save')
    menu_file.add_command(label ='Load')
    menu_file.add_command(label ='Exit')
    button_file.configure(menu=menu_file)
