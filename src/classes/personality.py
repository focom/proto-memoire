from tkinter import *

q_philanthrope = ['Cela me rend heureux si je peux aider les autres.','J’aime aider les autres à s’orienter dans de nouvelles situations.','J’aime partager mes connaissances.','Le bien-être des autres est important pour moi.']
q_socialiseur = ['Interagir avec les autres est important pour moi.','J’aime faire partie d’une équipe.','Il est important pour moi de sentir que je fais partie d’une communauté.','J’aime les activités de groupe.']
q_esprit_libre = ['Il est important pour moi de suivre ma propre voie.','Je me laisse souvent guider par ma curiosité. ','J’aime essayer de nouvelles choses.','L’indépendance est importante pour moi.']
q_realisateur = ['J’aime vaincre les obstacles.','Il est important pour moi de toujours mener à bien mes tâches de façon complète.','Il m’est difficile de laisser tomber un problème avant d’avoir trouvé une solution.','J’aime maîtriser les tâches difficiles.']
q_disrupteur = ['J’aime provoquer.','J’aime remettre en question le statu quo.','Je me considère comme un rebelle.','Je n\'aime pas suivre les règles.']
q_joueur = ['J’aime les concours où un prix peut être gagné.','Les récompenses sont un excellent moyen de me motiver.','Le retour sur investissement est important pour moi.','Si la récompense est suffisante, je ferai l\'effort.']
i = 0


class Personality:
    def __init__(self):
        self.i = 0
        self.score = {'philan':0,'social':0,'freeSpi':0,'real':0,'disrup':0,'joueur':0}
        self.t_philan = StringVar()
        self.t_social = StringVar()
        self.t_freeSpi = StringVar()
        self.t_real = StringVar()
        self.t_disrup = StringVar()
        self.t_joueur = StringVar()

    def calculatePersonality(self,mainFrame):
        for widget in mainFrame.winfo_children():
            widget.destroy()
        
        
        self.t_philan.set(q_philanthrope[self.i])
        self.t_social.set(q_socialiseur[self.i])
        self.t_freeSpi.set(q_esprit_libre[self.i])
        self.t_real.set(q_realisateur[self.i])
        self.t_disrup.set(q_disrupteur[self.i])
        self.t_joueur.set(q_joueur[self.i])


        Label(mainFrame,textvariable =self.t_philan).grid(column=0, row=0, columnspan=3, rowspan=1)
        Label(mainFrame,textvariable =self.t_social).grid(column=0, row=1, columnspan=3, rowspan=1)
        Label(mainFrame,textvariable =self.t_freeSpi).grid(column=0, row=2, columnspan=3, rowspan=1)
        Label(mainFrame,textvariable =self.t_real).grid(column=0, row=3, columnspan=3, rowspan=1)
        Label(mainFrame,textvariable =self.t_disrup).grid(column=0, row=4, columnspan=3, rowspan=1)
        Label(mainFrame,textvariable =self.t_joueur).grid(column=0, row=5, columnspan=3, rowspan=1)

        score_philan = StringVar()
        score_social = StringVar()
        score_freespi = StringVar()
        score_real = StringVar()
        score_disrup = StringVar()
        score_joueur = StringVar()

        in_philan = Spinbox(mainFrame,from_=0,to=7,increment=1,width=5, textvariable=score_philan)
        in_philan.grid(column=4, row=0, columnspan=1, rowspan=1)
        in_social = Spinbox(mainFrame,from_=0,to=7,increment=1,width=5,textvariable=score_social)
        in_social.grid(column=4, row=1, columnspan=1, rowspan=1)
        in_freeSpi = Spinbox(mainFrame,from_=0,to=7,increment=1,width=5,textvariable=score_freespi)
        in_freeSpi.grid(column=4, row=2, columnspan=1, rowspan=1)
        in_real = Spinbox(mainFrame,from_=0,to=7,increment=1,width=5,textvariable=score_real)
        in_real.grid(column=4, row=3, columnspan=1, rowspan=1)
        in_disrup = Spinbox(mainFrame,from_=0,to=7,increment=1,width=5,textvariable=score_disrup)
        in_disrup.grid(column=4, row=4, columnspan=1, rowspan=1)
        in_joueur = Spinbox(mainFrame,from_=0,to=7,increment=1,width=5,textvariable=score_joueur)
        in_joueur.grid(column=4, row=5, columnspan=1, rowspan=1)
        

        Button(mainFrame,text='Soumettre',command=lambda: Personality.stepPersonality(self,mainFrame)).grid(column=0, row=7, columnspan=4)


        # self.t_philan.set(q_philanthrope[self.i])
        # self.t_social.set(q_socialiseur[self.i])
        # self.t_freeSpi.set(q_esprit_libre[self.i])
        # self.t_real.set(q_realisateur[self.i])
        # self.t_disrup.set(q_disrupteur[self.i])
        # self.t_joueur.set(q_joueur[self.i])

        # for i in range (0,4):

        #     # label_philanthrope 
        #     # label_social 
        #     # label_freeSpi 
        #     # label_real 
        #     # label_disrup 
        #     # label_philanthrope 
        
        return 0

    def stepPersonality(self,mainFrame):
        if(self.i !=3):
            self.i = self.i + 1
            print(self.i)
            self.t_philan.set(q_philanthrope[self.i])
            self.t_social.set(q_socialiseur[self.i])
            self.t_freeSpi.set(q_esprit_libre[self.i])
            self.t_real.set(q_realisateur[self.i])
            self.t_disrup.set(q_disrupteur[self.i])
            self.t_joueur.set(q_joueur[self.i])
            print('call is working')
            return 0
        else:
            print('Done')