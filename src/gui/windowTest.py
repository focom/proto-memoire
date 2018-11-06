import tkinter

class Window:
  def __init__ (self, sentence):
    self.sentence = sentence

  def testWindow(self):
    root = tkinter.Tk()
    var = tkinter.StringVar()
    label = tkinter.Label(root, textvariable='C\'est le label', text='Hello je suis le label')
    button = tkinter.Button(root ,textvariable=var, command=lambda text='yoyo', var=var, root=root, label = label: self.handler(text,var,root, label) )
    var.set('Hello world')
    button.pack()
    label.pack()
    root.mainloop()

  def handler(self,text,var,root, label):
    label.pack_forget()
    button = tkinter.Button(root, textvariable=var)
    var.set(text)
    button.pack

if (__name__=='__main__'):
    test = Window('hello')
    test.testWindow()