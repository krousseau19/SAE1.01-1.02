class Joueur :
        pseudo : str
        score : int

j1 : Joueur
j2 : Joueur

j1 = Joueur()
j2 = Joueur()

def creation_joueurs() :
     global nb_j_valide
     global j1
     global j2
     print("Création du Joueur 1...")
     j1.pseudo = input("Veuillez saisir votre pseudo : ")
     j1.score = 0
     print("Création du Joueur 2...")
     j2.pseudo = input("Veuillez saisir votre pseudo : ")
     j2.score = 0
     nb_j_valide = True

def afficher_menu():
    print("\n    === MENU ===")
    print("1 - Jeu de devinettes")
    print("2 - Jeu des allumettes")
    print("3 - Jeu de morpion")
    print("4 - Jeu de puissance 4")
    print("5 - Quitter")

def saisir_choix() -> int :
     try:
        return int(input("Choisissez un jeu : "))
     except ValueError:
        return -1

tour : int
tour = 1

qui_joue : str
qui_joue = ""

def début_de_partie() :
     global qui_joue
     global j1
     global j2
     choix : int
     choix_valide : bool

     choix = 0
     choix_valide = False
     print("Qui joue en premier ?")
     while choix != 3 :
          print("1.", j1.pseudo)
          print("2.", j2.pseudo)
          print("3. Quitter")
          while not choix_valide :
               try :
                    choix = int(input("Saisir un choix : "))
                    choix_valide = True
               except ValueError :
                    print("Erreur : Veuillez saisir un choix valide.")
          choix_valide = False
          if choix == 1 :
             qui_joue = j1.pseudo
             choix = 3
          elif choix == 2 :
             qui_joue = j2.pseudo
             choix = 3
          elif choix == 3 :
               print("La partie va commencer.")
          else :
               print("Choix invalide")
     return qui_joue
     