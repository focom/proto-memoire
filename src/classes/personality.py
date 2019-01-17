from tkinter import *
# class Personality :
def calculatePersonality(mainFrame):
    for widget in mainFrame.winfo_children():
        widget.destroy()
    q_philanthrope = ['Cela me rend heureux si je peux aider les autres.','J’aime aider les autres à s’orienter dans de nouvelles situations.','J’aime partager mes connaissances.','Le bien-être des autres est important pour moi.']
    q_socialiseur = ['Interagir avec les autres est important pour moi.','J’aime faire partie d’une équipe.','Il est important pour moi de sentir que je fais partie d’une communauté.','J’aime les activités de groupe.']
    q_esprit_libre = ['Il est important pour moi de suivre ma propre voie.','Je me laisse souvent guider par ma curiosité. ','J’aime essayer de nouvelles choses.','L’indépendance est importante pour moi.']
    q_realisateur = ['J’aime vaincre les obstacles.','Il est important pour moi de toujours mener à bien mes tâches de façon complète.','Il m’est difficile de laisser tomber un problème avant d’avoir trouvé une solution.','J’aime maîtriser les tâches difficiles.']
    q_disrupteur = ['J’aime provoquer.','J’aime remettre en question le statu quo.','Je me considère comme un rebelle.','Je n\'aime pas suivre les règles.']
    q_joueur = ['J’aime les concours où un prix peut être gagné.','Les récompenses sont un excellent moyen de me motiver.','Le retour sur investissement est important pour moi.','Si la récompense est suffisante, je ferai l\'effort.']
    
    # def __init__(self,mainFrame):

    
    score = {'philan':0,'social':0,'freeSpi':0,'real':0,'disrup':0,'joueur':0}
    i = 0
    
    t_philan = StringVar()
    t_philan.set(q_philanthrope[i])
    t_social = StringVar()
    t_social.set(q_socialiseur[i])
    t_freeSpi = StringVar()
    t_freeSpi.set(q_esprit_libre[i])
    t_real = StringVar()
    t_real.set(q_realisateur[i])
    t_disrup = StringVar()
    t_disrup.set(q_disrupteur[i])
    t_joueur = StringVar()
    t_joueur.set(q_joueur[i])

    Label(mainFrame,textvariable =t_philan).grid(column=0, row=0, columnspan=3, rowspan=1)
    Label(mainFrame,textvariable =t_social).grid(column=0, row=1, columnspan=3, rowspan=1)
    Label(mainFrame,textvariable =t_freeSpi).grid(column=0, row=2, columnspan=3, rowspan=1)
    Label(mainFrame,textvariable =t_real).grid(column=0, row=3, columnspan=3, rowspan=1)
    Label(mainFrame,textvariable =t_disrup).grid(column=0, row=4, columnspan=3, rowspan=1)
    Label(mainFrame,textvariable =t_joueur).grid(column=0, row=5, columnspan=3, rowspan=1)

    in_philan = Spinbox(mainFrame,from_=0,to=7,increment=1,width=5)
    in_philan.grid(column=4, row=0, columnspan=1, rowspan=1)
    in_social = Spinbox(mainFrame,from_=0,to=7,increment=1,width=5)
    in_social.grid(column=4, row=1, columnspan=1, rowspan=1)
    in_freeSpi = Spinbox(mainFrame,from_=0,to=7,increment=1,width=5)
    in_freeSpi.grid(column=4, row=2, columnspan=1, rowspan=1)
    in_real = Spinbox(mainFrame,from_=0,to=7,increment=1,width=5)
    in_real.grid(column=4, row=3, columnspan=1, rowspan=1)
    in_disrup = Spinbox(mainFrame,from_=0,to=7,increment=1,width=5)
    in_disrup.grid(column=4, row=4, columnspan=1, rowspan=1)
    in_joueur = Spinbox(mainFrame,from_=0,to=7,increment=1,width=5)
    in_joueur.grid(column=4, row=5, columnspan=1, rowspan=1)
    

    Button(mainFrame,text='Soumettre',command=lambda: stepPersonality(i,score,mainFrame,t_philan,t_social,t_freeSpi,t_real,t_disrup,t_joueur)).grid(column=0, row=7, columnspan=4)


    t_philan.set(q_philanthrope[i])
    t_social.set(q_socialiseur[i])
    t_freeSpi.set(q_esprit_libre[i])
    t_real.set(q_realisateur[i])
    t_disrup.set(q_disrupteur[i])
    t_joueur.set(q_joueur[i])

    # for i in range (0,4):

    #     # label_philanthrope 
    #     # label_social 
    #     # label_freeSpi 
    #     # label_real 
    #     # label_disrup 
    #     # label_philanthrope 
    
    return 0

def stepPersonality(step,score,mainFrame,t_philan,t_social,t_freeSpi,t_real,t_disrup,t_joueur):
    t_philan.set('PPPPIIIZZZZAAAA')
    print('HHHHEEELLLOOO')
    return 0