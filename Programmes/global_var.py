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

j1 = Joueur()
j2 = Joueur()

def Creation_joueurs() :
    global nb_j_valide
    global j1
    global j2
    if not nb_j_valide :
        print("Création du Joueur 1...")
        j1.pseudo = input("Veuillez saisir votre pseudo : ")
        print("Création du Joueur 2...")
        j2.pseudo = input("Veuillez saisir votre pseudo : ")
        nb_j_valide = True
    else :
         print("Il y a déjà assez de joueurs pour commencer une partie")

j1.highscore_dev = 0
j1.highscore_all = 0
j1.highscore_mor = 0
j1.highscore_pui = 0
j1.score = 0
j1.nb_parties = 0
j1.nb_partiesG = 0

j2.highscore_dev = 0
j2.highscore_all = 0
j2.highscore_mor = 0
j2.highscore_pui = 0
j2.score = 0
j2.nb_parties = 0
j2.nb_partiesG = 0

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
          print("1.", j1.pseudo)
          print("2.", j2.pseudo)
          print("3. Quitter")
          choix = int(input("Saisir un choix : "))
          if choix == 1 :
             qui_joue = 1
             choix = 3
          elif choix == 2 :
             qui_joue = 2
             choix = 3
          elif choix == 3 :
               print("La partie va commencer.")
          else :
               print("Choix invalide")