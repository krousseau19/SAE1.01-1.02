class Joueur :
        pseudo : str
        highscore_dev : int
        highscore_all : int
        highscore_mor : int
        highscore_pui : int
        score : int
        nb_parties : int
        nb_partiesG : int

nb_j_valide : bool
nb_j_valide = False
j1 : Joueur
j2 : Joueur

def Creation_joueurs() :
    global nb_j_valide
    global j1
    global j2
    if not nb_j_valide :
        j1 = Joueur()
        print("Création du Joueur 1...")
        j1.pseudo = input("Veuillez saisir votre pseudo : ")
        j1.score = 0
        j2 = Joueur()
        print("Création du Joueur 2...")
        j2.pseudo = input("Veuillez saisir votre pseudo : ")
        j2.score = 0
        nb_j_valide = True
    else :
         print("Il y a déjà assez de joueurs pour commencer une partie")

tour : int
tour = 1

qui_joue : int
qui_joue = 1

def début_de_partie() :
     global qui_joue
     global j1
     global j2
     choix : int
     choix = 0
     print("Qui joue en premier ?")
     while choix != 3 :
        print("1. ", j1.pseudo)
        print("2.", j2.pseudo)
        print("3. Quitter")
        choix = int(input("Saisir un choix : "))
        if choix == 1 :
             qui_joue = 1
        elif choix == 2 :
             qui_joue = 2
        else :
             print("Choix invalide")