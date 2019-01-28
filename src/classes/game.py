from tkinter import *
import numpy as np
import time
class Game:
  def __init__(self,main,instruction,question,correct,wrong,number_exer,id_node):
    
    self.a_instruction = instruction
    self.a_question = question
    self.a_correct = correct
    self.a_wrong = wrong
    
    self.gui = main.gui
    self.main = main
 
    self.number_exo = number_exer
    self.id_node = id_node
    self.iteration = 0
    self.numberCorrect = 0
    self.numberWrong = 0

    self.timesCorrect = []
    self.timesWrong = []
    self.nbCorrect = 0
    self.nbFalse = 0
    self.instruction = StringVar()
    self.question = StringVar()
    self.correct = StringVar()
    self.false = StringVar()

  
  def askExercises(self):
    # efface l'ecran 
    for widget in self.gui.winfo_children():
      widget.destroy()
    # Met en place l'archi pour les exos
    instruction = Label(self.gui,textvariable=self.instruction)
    instruction.grid(column=1,row=0,columnspan=3,rowspan=1)
    question = Label(self.gui,textvariable=self.question)
    question.grid(column=1,row=2,columnspan=3,rowspan=1)

    correct = Button(self.gui,textvariable=self.correct, command= lambda: self.stepInExercise(True))
    false = Button(self.gui,textvariable=self.false, command= lambda: self.stepInExercise(False))
    correct.grid(column=1,row=4,columnspan=2,rowspan=1)
    false.grid(column=3,row=4,columnspan=2,rowspan=1)

    tips = Frame(self.gui,borderwidth=2,relief=GROOVE)
    tips.grid(column=1, columnspan=4,row=6, rowspan=3)
    # tips_label=Frame(tips,text='Essai du tips')
    # tips_label.pack(padx=10,pady=10)

    self.instruction.set(self.a_instruction[self.iteration])
    self.question.set(self.a_question[self.iteration])
    self.correct.set(self.a_correct[self.iteration])
    self.false.set(self.a_wrong[self.iteration])

    self.startTime =  time.time()
    # affiche premier exo

    # demarre le chrono
    # Enregistre input
      # Si au bout de 3 echec montrer mecanique de jeux
      # Si au bout de 3 reussite montrer mecanique de recompense
    # Cycle jusqua epuisement des exos

    # Une fois epuise donne un message selon la personalite du joueur

    # Calcul du grade pour la session, fin de l'entrainement

  def stepInExercise(self,bool):
    # Save the time to answer 
    if(bool == True):
      self.nbCorrect += 1
      time_to_answer = time.time() - self.startTime
      self.timesCorrect.append(time_to_answer)
    else:
      self.nbFalse += 1
      time_to_answer = time.time() - self.startTime
      self.timesWrong.append(time_to_answer)
    
    # iterate on exercise
    self.iteration += 1

    # Calculate time to answer
    
    if(self.iteration == self.number_exo):
      #si plus de positif
      if (self.nbCorrect > self.nbFalse):
        a = np.array(self.timesCorrect)
        mean = a.mean()
        # si moyenne temps inferieur a 15s alors 4
        if (mean < 15):
          grade = 4
        # sinon 3
        else:
          grade = 3
      # Si plus de negatif
      else:
        a = np.array(self.timesWrong)
        mean = a.mean()
        # si moyenne temps inferieur a 35s alors 2
        if (mean < 35):
          grade = 2
        # sinon 1
        else:
          grade = 1

      # Quit exercise
      print('end')
      self.main.endExercise(grade,self.id_node)
      return 0
        # Change text on screen
    self.instruction.set(self.a_instruction[self.iteration])
    self.question.set(self.a_question[self.iteration])
    self.correct.set(self.a_correct[self.iteration])
    self.false.set(self.a_wrong[self.iteration])

