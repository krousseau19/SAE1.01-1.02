import random

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
     print(f"\033[2J")

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

qui_joue : Joueur
qui_joue = Joueur()

def début_de_partie() -> Joueur :
     global qui_joue
     global j1
     global j2
     choix : int
     choix_valide : bool
     aleatoire : int

     choix = 0
     choix_valide = False
     print("Qui joue en premier ?")
     while choix != 3 :
          print("1.", j1.pseudo)
          print("2.", j2.pseudo)
          print("3. Aléatoire")
          while not choix_valide :
               try :
                    choix = int(input("Saisir un choix : "))
                    choix_valide = True
               except ValueError :
                    print("Erreur : Veuillez saisir un choix valide.")
          choix_valide = False
          if choix == 1 :
             qui_joue = j1
             choix = 3
          elif choix == 2 :
             qui_joue =j2
             choix = 3
          elif choix == 3 :
               aleatoire = random.randint(1,2)
               if aleatoire == 1 :
                    qui_joue = j1
               else :
                    qui_joue = j2
          else :
               print("Erreur : Veuillez saisir un choix valide.")
     #os.system('cls' if os.name == 'nt' else 'clear') -> pas sûr d'avoir le droit, à demander
     print(f"\033[2J")
     return qui_joue
     