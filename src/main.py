# from classes.game import *
from tkinter import *
from classes.personality import Personality
if ( __name__ == '__main__'):
    guiRoot = Tk()
    guiRoot.title('Demande de personalité')
    guiRoot.geometry('1000x400+400+400')



    Frame1 = Frame(guiRoot,borderwidth=2,relief=GROOVE,width=400,height=400)
    # Frame1.grid(column=0, row=0)
    # Création d'un widget Button (bouton Lancer)
    context = Personality()
    BoutonLancer = Button(guiRoot, command= lambda: context.calculatePersonality(guiRoot),text ='Lancer')
    # Positionnement du widget avec la méthode pack()
    BoutonLancer.grid(column=0, row=0)


    guiRoot.mainloop()
