import random
import os
from typing import BinaryIO # type: ignore
from pickle import dump, load

class Joueur :
        pseudo : str
        score : int
        highscore_dev : int
        highscore_all : int
        highscore_mor : int
        highscore_pui : int
        nb_partie : int
        nb_partieG : int

j1 : Joueur
j2 : Joueur
tour : int
qui_joue : Joueur
f : BinaryIO

j1 = Joueur()
j2 = Joueur()
tour = 1
qui_joue = Joueur()
try :
     f = open("Data/data.sav", "xb")
except FileExistsError :
     f = open("Data/data.sav", "rb")
f.close()

def creation_joueurs() :
     global nb_j_valide
     global j1
     global j2
     global f
     j_existe : bool

     print("\033c")
     print("Création du Joueur 1...")
     j1.pseudo = input("Veuillez saisir votre pseudo : ")
     j1.score = 0
     j_existe = recherche_joueur(f, j1)
     if  not j_existe :
          j1.highscore_dev = 0
          j1.highscore_all = 0
          j1.highscore_mor = 0
          j1.highscore_pui = 0
          j1.nb_partie = 0
          j1.nb_partieG = 0
          sauvegarder_joueur(f, j1)
     else :
          charger_joueur(f, j1)
     print("Création du Joueur 2...")
     j2.pseudo = input("Veuillez saisir votre pseudo : ")
     j2.score = 0
     j_existe = recherche_joueur(f, j2)
     if not j_existe : 
          j2.highscore_dev = 0
          j2.highscore_all = 0
          j2.highscore_mor = 0
          j2.highscore_pui = 0
          j2.nb_partie = 0
          j2.nb_partieG = 0
          sauvegarder_joueur(f, j2)
     else :
          charger_joueur(f, j2)
     nb_j_valide = True
     print("\033c")

def afficher_menu():
    print("    === MENU ===")
    print("1 - Jeu de devinettes")
    print("2 - Jeu des allumettes")
    print("3 - Jeu de morpion")
    print("4 - Jeu de puissance 4")
    print("5 - Afficher les scores")
    print("6 - Quitter")

def saisir_choix() -> int :
     try:
        return int(input("Choisissez un jeu : "))
     except ValueError:
        return -1

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
                    print("\033c")
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
               print("\033c")
               print("Erreur : Veuillez saisir un choix valide.")
     print("\033c")
     return qui_joue

def sauvegarder_joueur(fic: BinaryIO, J: Joueur):
     j_existe: bool
     fin: bool
     res: Joueur
     temp_fic : str

     j_existe = False  
     fin = False
     with open("Data/data.sav", "rb") as fic:
            while not fin:
                try:
                    res = load(fic)  # Charger un joueur du fichier
                    if res.pseudo == J.pseudo:  # Le joueur existe déjà
                        j_existe = True
                        break
                except EOFError:
                    fin = True 
     if j_existe:
        fin = False
        temp_fic = "Data/temp_data.sav" 
        with open("Data/data.sav", "rb") as fic_in, open(temp_fic, "wb") as fic_out:
            while not fin :
                try:
                    res = load(fic_in)
                    if res.pseudo == J.pseudo:
                        res.highscore_dev = J.highscore_dev
                        res.highscore_all = J.highscore_all
                        res.highscore_mor = J.highscore_mor
                        res.highscore_pui = J.highscore_pui
                        res.nb_partie = J.nb_partie
                        res.nb_partieG = J.nb_partieG
                    dump(res, fic_out)  
                except EOFError:
                    fin = True
        os.replace(temp_fic, "Data/data.sav")
     else:
        with open("Data/data.sav", "ab") as fic:
            dump(J, fic)

def recherche_joueur(fic : BinaryIO, J : Joueur) -> bool : 
     res : Joueur
     fin : bool
     est_trouvé : bool

     fic = open("Data/data.sav", "rb")
     fin = False
     est_trouvé = False
     res = Joueur()
     while not fin and not est_trouvé :
          try :
               res = load(fic)
               if res.pseudo == J.pseudo :
                    est_trouvé = True
          except EOFError :
               fin = True
     fic.close()
     return est_trouvé

def charger_joueur(fic : BinaryIO, J : Joueur) :
     res : Joueur
     fin : bool

     fic = open("Data/data.sav", "rb")
     res = Joueur()
     fin = False
     while not fin :
          try :
               res = load(fic)
               if res.pseudo == J.pseudo :
                    J.highscore_dev = res.highscore_dev
                    J.highscore_all = res.highscore_all
                    J.highscore_mor = res.highscore_mor
                    J.highscore_pui = res.highscore_pui
                    J.nb_partie = res.nb_partie
                    J.nb_partieG = res.nb_partieG
          except EOFError :
               fin = True
     fic.close()

def afficher_score(fic : BinaryIO, J : Joueur) :
     res : Joueur
     fin : bool

     fic = open("Data/data.sav", "rb")
     res = Joueur()
     fin = False
     while not fin :
          try :
               res = load(fic)
               if res.pseudo == J.pseudo :
                    print(res.pseudo, end=" : ")
                    print(res.highscore_dev, end=" | ")
                    print(res.highscore_all, end=" | ")
                    print(res.highscore_mor, end=" | ")
                    print(res.highscore_pui, end=" | ")
                    print(res.nb_partie, end=" | ")
                    print(res.nb_partieG)
          except EOFError :
               fin = True
     fic.close()