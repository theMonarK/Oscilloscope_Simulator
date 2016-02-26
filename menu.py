from Tkinter import *
import shelve
import os.path

class MenuBar(Frame):
  def __init__(self,parent,subject):
    Frame.__init__(self,borderwidth=2)
    self.parent = parent
    self.subject = subject
    button_file = Menubutton(self,text="File")
    button_file.pack(side="left")
    menu_file=Menu(button_file)
    menu_file.add_command(label='Save', command=self.saving(None))
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
      self.aboutTop=Toplevel()
      self.aboutTop.title("About...")
      msg = Message(self.aboutTop, text="Author: \nAnthony Guillier\na2guilli@enib.fr")
      msg.pack()
      buttonOK = Button(self.aboutTop, text="OK", command=self.aboutTop.destroy)
      buttonOK.pack()

  def error(self):
      errorTop=Toplevel()
      errorTop.title("Error")
      msg = Message(errorTop, text="Le fichier n'existe pas")
      msg.pack()
      buttonOK = Button(errorTop, text="OK", command=errorTop.destroy)
      buttonOK.pack()

  def exit(self):
      exitTop=Toplevel()
      exitTop.title("Quit")
      msg = Message(exitTop, text="Save ?")
      msg.pack()
      buttonNo = Button(exitTop, text="No", command=lambda: self.parent.destroy())
      buttonNo.pack(side="left")
      buttonSave = Button(exitTop, text="Save", command=lambda: self.savingExit(exitTop))
      buttonSave.pack(side="left")
      buttonSaveAs = Button(exitTop, text="Save as...", command=self.savingAsExit)
      buttonSaveAs.pack(side="left")
      buttonCancel = Button(exitTop, text="Cancel", command=exitTop.destroy)
      buttonCancel.pack(side="left")

  def load(self):
      loadTop=Toplevel()
      loadTop.title('Load...')
      name=StringVar()
      nameLabel = Label(loadTop, text = "Name :")
      nameEntry = Entry(loadTop,textvariable=name)
      nameLabel.grid(row=0)
      nameEntry.grid(row=0,column=1)
      buttonOk = Button(loadTop, text="OK", command=lambda: self.setParam(loadTop,name.get()))
      buttonOk.grid(row=2,column=1)
      buttonCancel = Button(loadTop, text="Cancel", command=loadTop.destroy)
      buttonCancel.grid(row=2,column=2)

  def test(self,nameEntry):
      print("enter")

  def saving(self,toplevel,name='save'):
      if not(os.path.exists(name)):
          save=shelve.open(name)
          save['amp']=str(self.subject.get_magnitude())
          save['freq']=str(self.subject.get_frequency())
          save['phase']=str(self.subject.get_phase())
          save.close()
          toplevel.destroy()


  def savingExit(self,toplevel,name='save'):
      self.saving(toplevel,name)
      self.parent.destroy()

  def savingAsExit(self):
      saveAsTop=Toplevel()
      saveAsTop.title("Save as...")
      name=StringVar()
      nameLabel = Label(saveAsTop, text = "Name :")
      nameEntry = Entry(saveAsTop,textvariable=name)
      nameLabel.grid(row=0)
      nameEntry.grid(row=0,column=1)
      buttonOk = Button(saveAsTop, text="OK", command=lambda: self.savingExit(saveAsTop,name=str(name.get())))
      buttonOk.grid(row=2,column=1)
      buttonCancel = Button(saveAsTop, text="Cancel", command=saveAsTop.destroy)
      buttonCancel.grid(row=2,column=2)

  def savingAs(self):
      saveAsTop=Toplevel()
      saveAsTop.title("Save as...")
      name=StringVar()
      nameLabel = Label(saveAsTop, text = "Name :")
      nameEntry = Entry(saveAsTop,textvariable=name)
      nameLabel.grid(row=0)
      nameEntry.grid(row=0,column=1)
      buttonOk = Button(saveAsTop, text="OK", command=lambda: self.saving(saveAsTop,name=str(name.get())))
      buttonOk.grid(row=2,column=1)
      buttonCancel = Button(saveAsTop, text="Cancel", command=saveAsTop.destroy)
      buttonCancel.grid(row=2,column=2)

  def setParam(self,toplevel,name='save'):
      if(os.path.exists(name)):
          save=shelve.open(name)
          print(save['amp'])
          self.subject.set_magnitude(int(save['amp']))
          self.subject.set_frequency(int(save['freq']))
          self.subject.set_phase(int(save['phase']))
          save.close()
          toplevel.destroy()
      else:
          self.error()
