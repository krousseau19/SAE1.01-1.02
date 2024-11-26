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
    print("1 - Devinettes")
    print("2 - Allumettes")
    print("3 - Morpion")
    print("4 - Puissance 4")
    print("5 - Statistiques")
    print("6 - Quitter")

def saisir_choix() -> int :
     try:
        return int(input("Saisir votre choix : "))
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
    j_existe: bool = False
    fin: bool = False
    res: Joueur
    temp_fic: str
    fic_lecture: BinaryIO
    fic_écriture: BinaryIO

    # Vérifie si le joueur existe déjà
    with open("Data/data.sav", "rb") as fic:
        while not fin:
            try:
                res = load(fic)  # Charge un joueur du fichier
                if res.pseudo == J.pseudo:  # Si le joueur existe déjà
                    j_existe = True
                    fin = True
            except EOFError:
                fin = True

    if j_existe:
        # Si le joueur existe déjà, on met à jour ses informations
        fin = False
        temp_fic = "temp_data.sav"
        
        with open("Data/data.sav", "rb") as fic_lecture, open(temp_fic, "wb") as fic_écriture:
            while not fin:
                try:
                    res = load(fic_lecture)  # Charge chaque joueur
                    if res.pseudo == J.pseudo:
                        # Met à jour le joueur dans le fichier temporaire
                        res.highscore_dev = J.highscore_dev
                        res.highscore_all = J.highscore_all
                        res.highscore_mor = J.highscore_mor
                        res.highscore_pui = J.highscore_pui
                        res.nb_partie = J.nb_partie
                        res.nb_partieG = J.nb_partieG
                    dump(res, fic_écriture)  # Sauvegarde les données mises à jour
                except EOFError:
                    fin = True
        # Remplace l'ancien fichier par le fichier temporaire mis à jour
        os.replace(temp_fic, "Data/data.sav")
    else:
        # Ajoute un nouveau joueur si ce n'est pas déjà le cas
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

def afficher_stats(fic : BinaryIO, J1 : Joueur, J2 : Joueur) :
     res1 : Joueur
     res2 : Joueur
     fin : bool

     fic = open("Data/data.sav", "rb")
     res1 = Joueur()
     res2 = Joueur()
     fin = False
     while not fin :
          try :
               res1 = load(fic)
               if res1.pseudo == J1.pseudo :
                    res2 = load(fic)
                    if res2.pseudo == J2.pseudo :
                         print("\033c")
                         print("\n=========== Statistiques du Joueur 1 =========== Statistiques du Joueur 2 ===========")
                         print("Pseudo                     : ", res1.pseudo, " "*(len(res1.pseudo)), " | ", "Pseudo                : ", res2.pseudo,  )
                         print("Meilleur score Devinettes  : ", res1.highscore_dev, " "*(5+len(res1.pseudo))," | ", "Meilleur score Devinettes  : ", res2.highscore_dev,)
                         print("Meilleur score Allumettes  : ", res1.highscore_all, " "*(5+len(res1.pseudo))," | ", "Meilleur score Allumettes  : ", res2.highscore_all)
                         print("Meilleur score Morpion     : ", res1.highscore_mor, " "*(5+len(res1.pseudo))," | ", "Meilleur score Morpion     : ", res2.highscore_mor)
                         print("Meilleur score Puissance 4 : ", res1.highscore_pui, " "*(5+len(res1.pseudo))," | ", "Meilleur score Puissance 4 : ", res2.highscore_pui)
                         print("Nombre de parties jouées   : ", res1.nb_partie, " "*(5+len(res1.pseudo))," | ", "Nombre de parties jouées   : ", res2.nb_partie)
                         print("Nombre de parties gagnées  : ", res1.nb_partieG, " "*(5+len(res1.pseudo))," | ", "Nombre de parties gagnées  : ", res2.nb_partieG)
                         print("=" * 85)
               elif res1.pseudo == j2.pseudo :
                    res2 = load(fic)
                    if res2.pseudo == j1.pseudo :
                              print("\033c")
                              print("\n=========== Statistiques du Joueur 1 =========== Statistiques du Joueur 2 ===========")
                              print("Pseudo                     : ", res2.pseudo, " "*(len(res1.pseudo)), " | ", "Pseudo                : ", res1.pseudo,  )
                              print("Meilleur score Devinettes  : ", res2.highscore_dev, " "*(5+len(res1.pseudo))," | ", "Meilleur score Devinettes  : ", res1.highscore_dev,)
                              print("Meilleur score Allumettes  : ", res2.highscore_all, " "*(5+len(res1.pseudo))," | ", "Meilleur score Allumettes  : ", res1.highscore_all)
                              print("Meilleur score Morpion     : ", res2.highscore_mor, " "*(5+len(res1.pseudo))," | ", "Meilleur score Morpion     : ", res1.highscore_mor)
                              print("Meilleur score Puissance 4 : ", res2.highscore_pui, " "*(5+len(res1.pseudo))," | ", "Meilleur score Puissance 4 : ", res1.highscore_pui)
                              print("Nombre de parties jouées   : ", res2.nb_partie, " "*(5+len(res1.pseudo))," | ", "Nombre de parties jouées   : ", res1.nb_partie)
                              print("Nombre de parties gagnées  : ", res2.nb_partieG, " "*(5+len(res1.pseudo))," | ", "Nombre de parties gagnées  : ", res1.nb_partieG)
                              print("=" * 85)
          except EOFError :
               fin = True
     fic.close()

def tri_décroissant(l : list[Joueur], jeu : str) :
     i : int

     for i in range(0, len(l)-1):
          for j in range(i+1, len(l)) :
               if jeu == "Devinette" :
                    if l[i].highscore_dev < l[j].highscore_dev :
                         l[i], l[j] = l[j], l[i]
               elif jeu == "Allumette" :
                    if l[i].highscore_all < l[j].highscore_all :
                         l[i], l[j] = l[j], l[i]
               elif jeu == "Morpion" :
                    if l[i].highscore_mor < l[j].highscore_mor :
                         l[i], l[j] = l[j], l[i]
               else :
                    if l[i].highscore_pui < l[j].highscore_pui :
                         l[i], l[j] = l[j], l[i]
     
def afficher_leaderboard(fic : BinaryIO, jeu : str) :
     res : Joueur
     fin : bool
     joueurs : list[Joueur]

     fic = open("Data/data.sav", "rb")
     fin = False
     joueurs = []
     print("===== Leader Board -", jeu ,"=====")
     while not fin :
          try :
               res = load(fic)
               joueurs.append(res)
          except EOFError :
               fin = True
     if jeu == "Devinette" :
          tri_décroissant(joueurs, jeu)
          for res in joueurs :
               if len(res.pseudo) <= 10 :
                    print(" "*13, res.pseudo, end=" : ")
                    print(res.highscore_dev)
     elif jeu == "Allumette" :
          tri_décroissant(joueurs, jeu)
          for res in joueurs :
               if len(res.pseudo) <= 10 :
                    print(" "*13, res.pseudo, end=" : ")
                    print(res.highscore_all)
     elif jeu == "Morpion" :
          tri_décroissant(joueurs, jeu)
          for res in joueurs :
               if len(res.pseudo) <= 10 :
                    print(" "*13, res.pseudo, end=" : ")
                    print(res.highscore_mor)
     else :
          tri_décroissant(joueurs, jeu)
          for res in joueurs :
               if len(res.pseudo) <= 10 :
                    print(" "*13, res.pseudo, end=" : ")
                    print(res.highscore_pui)

     print("="*(27+len(jeu)))
     fic.close()