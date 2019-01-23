# from classes.game import *
from tkinter import *
from classes.student import Student
from classes.personality import Personality

class Main:
    def __init__(self):
        self.guiRoot = Tk()
        self.guiRoot.title('Prototype de Pierre Valentin')
        self.guiRoot.geometry('1000x400+400+400')

        studentName = StringVar()

        champ = Entry( self.guiRoot, textvariable= studentName,)
        OldButton = Button( self.guiRoot, text ='Ancien Joueur', command = lambda : self.getOldStudent(studentName.get()))
        NewButton = Button( self.guiRoot, text ='Nouveau Joueur aprenant', command = lambda : self.createStudent(studentName.get()))

        champ.pack()
        OldButton.pack()
        NewButton.pack()
        self.guiRoot.mainloop()
        # Ask name:

    def createStudent(self,name):
        print(name)
        self.student = Student(name,True,self.guiRoot) 
    
    def getOldStudent(self,name):
        print(name)
        self.student = Student(name,False,self.guiRoot)

        if (name==''):
            #ask name and personaliy
            print('main ui')

        else :
            #lauch ui to visualise or train
            print('main ui')


if ( __name__ == '__main__'):
   loop = Main()