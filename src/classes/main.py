# from classes.game import *
from tkinter import *
from classes.student import Student
from classes.personality import Personality
from classes.game import Game
from classes.visualistation import Viz

class Main:
    def __init__(self):
        self.gui = Tk()
        self.gui.title('Prototype de Pierre Valentin')
        self.gui.geometry('1000x400+400+400')

        studentName = StringVar()

        champ = Entry( self.gui, textvariable= studentName,)
        OldButton = Button( self.gui, text ='Ancien Joueur', command = lambda : self.getOldStudent(studentName.get()))
        NewButton = Button( self.gui, text ='Nouveau Joueur aprenant', command = lambda : self.createStudent(studentName.get()))

        champ.pack()
        OldButton.pack()
        NewButton.pack()
        self.gui.mainloop()
        # Ask name:

    def createStudent(self,name):
        print(name)
        self.student = Student(name,self,True,self.gui) 
    
    def getOldStudent(self,name):
        print(name)
        self.student = Student(name,self,False,self.gui)
    
    def mainMenu(self):
        for widget in self.gui.winfo_children():
            widget.destroy()
        Button(self.gui, text='Visualiser',command= lambda: self.visu()).pack(padx=10,pady=10)
        Button(self.gui, text='S\'entrainer', command= lambda: self.train()).pack(padx=10,pady=10)
    
    def train(self):
        self.student.graph.updateGraph()
        id_node, number, instruction, question, correct, wrong = self.student.graph.selectExercise()
        game = Game(self,instruction,question,correct,wrong,number,id_node)
        game.askExercises()
    
    def endExercise(self,grade,id_node):
        print('Noeud: ',id_node,' Grade: ',grade)
        self.student.graph.setGrade([id_node,grade])
        for widget in self.gui.winfo_children():
            widget.destroy()
        Label(self.gui,text=f'Ton grade pour ce chapitre est : {grade}').pack()
        Button(self.gui,text='Retour au menu principal', command= lambda: self.mainMenu()).pack()
        tips = Frame(self.gui,borderwidth=2,relief=GROOVE)
        tips.pack(padx=10,pady=10)
        tip_text = self.getGoodEnding()
        tips_label=Label(tips,text=tip_text)
        tips_label.pack(padx=10,pady=10)
    
    def getGoodEnding(self):
        mecha = self.student.graph.getMechanic()
        if(mecha == 0):
            return 'Aide tes autres camarades à réussir !'
        if(mecha == 1):
            return '/!\ Tableau des scores /!\ '
        if(mecha == 2):
            return 'Discute avec le sage pour t\'aider dans ta quête'
    
    def visu(self):
        self.student.graph.updateGraph()
        self.viz = Viz(self.student.graph)
        self.viz.visual()

if ( __name__ == '__main__'):
   loop = Main()