# Fichier contenant toutes les fonctions relatives au jeu des allumettes
from ressource import Joueur, début_de_partie, qui_joue
from random import randint
from time import time

def jeu_allumettes(j1 : Joueur, j2 : Joueur, mode : int, diff : int):
    """
    Entrée : 2 arguments, qui sont les 2 joueurs

    Sortie : Rien

    Fonctionnement : Une fois le premier joueur désigné avec début_de_partie, tant que la partie n'est pas finie,
    la fonction affiche le nombre d'allumette (20 au départ) et demande au joueur du tour (alternant à chaque fois)
    combien d'allumette il veut retirer, selon son choix, l'affichage va changer en conséquence et cela passera au joueur
    d'après si aucune condition de défaite/victoire n'est atteinte, soit donc si le nombre d'allumette n'est pas nul au tour
    du joueur en question. Une fois ces conditions atteintes, la fonction affiche le message de victoire et modifie les attributs
    du gagnant/perdant en conséquence.
    """
    allumettes : int
    joueur : Joueur
    nb_all : int
    saisi_all : bool
    partie_finie : bool
    t1 : float
    t2 : float
    t : float
    
    print("\n    === Jeu des allumettes ===")
    j1.score = 0
    j2.score = 0
    allumettes = 20
    partie_finie = False
    joueur = début_de_partie(j1, j2, qui_joue)
    # Tant que la partie n'est pas finie
    while not partie_finie:
        saisi_all = False
        nb_all = -1
        # Tant que le saisi du nombre d'allumette n'est pas correct
        while not saisi_all :
            if joueur.pseudo == "machine 1" or joueur.pseudo == "machine 2" :
                print("Il reste ", allumettes, "allumettes.")
                # Affichage "tête" des allumettes
                for _ in range(0,allumettes) :  
                    print("\x1b[38;5;1m.", end=" ")
                print("")
                # Affichage "corps" des allumettes
                for _ in range(0,allumettes) :  
                    print("\x1b[38;5;94m|", end=" ")
                print("\x1b[0m")
                if diff == 1 :
                    t1 = time()
                    if allumettes == 1 or allumettes == 2 : # type: ignore
                        nb_all = 1
                    else :
                        nb_all = randint(1,3)
                    saisi_all = True
                    t2 = time()
                    t = t2 - t1
                    print("Temps Facile : ", t)
                elif diff == 2 :
                    t1 = time()
                    nb_all = randint(1,2)
                    if allumettes == 8 and nb_all == 2 :  # type: ignore
                        nb_all = 3
                    elif allumettes == 7 and nb_all == 2 : # type: ignore
                        nb_all = 2
                    elif allumettes == 6 and nb_all == 2 :  # type: ignore 
                        nb_all = 1
                    elif allumettes == 4 and nb_all == 2 : # type: ignore
                        nb_all = 3
                    elif allumettes == 3 and nb_all == 2 : # type: ignore
                        nb_all = 2
                    elif allumettes == 2 and nb_all == 2 : # type: ignore
                        nb_all = 1
                    elif allumettes == 1 and nb_all == 2 :  # type: ignore
                        nb_all = 1
                    else :
                        if allumettes == 1 or allumettes == 2 : # type: ignore
                            nb_all = 1
                        else :
                            nb_all = randint(1,3)
                    saisi_all = True
                    t2 = time()
                    t = t2 - t1
                    print("Temps Intermédiaire : ", t)
                else :
                    t1 = time()
                    if allumettes == 20 :
                        nb_all = 3
                    elif allumettes == 19 :
                        nb_all = 2
                    elif allumettes == 18 :
                        nb_all = 1
                    elif allumettes == 16 :
                        nb_all = 3
                    elif allumettes == 15 :
                        nb_all = 2
                    elif allumettes == 14 :
                        nb_all = 1
                    elif allumettes == 12 :
                        nb_all = 3
                    elif allumettes == 11 :
                        nb_all = 2
                    elif allumettes == 10 : 
                        nb_all = 1
                    elif allumettes == 8 :
                        nb_all = 3
                    elif allumettes == 7 :
                        nb_all = 2
                    elif allumettes == 6 :
                        nb_all = 1
                    elif allumettes == 4 :
                        nb_all = 3
                    elif allumettes == 3 :
                        nb_all = 2
                    elif allumettes == 2 :
                        nb_all = 1
                    elif allumettes == 1 : 
                        nb_all = 1
                    else :
                        if allumettes == 1 or allumettes == 2 : 
                            nb_all = 1
                        else :
                            nb_all = randint(1,3)
                    saisi_all = True
                    t2 = time()
                    t = t2 - t1
                    print("Temps Optimal : ", t)
                print(f"{joueur.pseudo} a retiré {nb_all} allumettes.")
            else :
                print("Il reste ", allumettes, "allumettes.")
                # Affichage "tête" des allumettes
                for _ in range(0,allumettes) :  
                    print("\x1b[38;5;1m.", end=" ")
                print("")
                # Affichage "corps" des allumettes
                for _ in range(0,allumettes) :  
                    print("\x1b[38;5;94m|", end=" ")
                print("\x1b[37m")
                # Saisi du joueur courant
                try :
                    nb_all = int(input(f"{joueur.pseudo} combien d'allumettes prenez-vous (1-3) ? "))
                    saisi_all = True
                    if nb_all < 1 or nb_all > 3:
                        print("\x1b[31mErreur : Veuillez prendre entre 1 et 3 allumettes.\x1b[0m")
                        saisi_all = False   
                    if nb_all > allumettes :
                        print("\x1b[31mErreur : Il n'y a plus assez d'allumettes.\x1b[0m")
                        saisi_all = False
                except ValueError :
                    print("\x1b[31mErreur : Veuillez saisir un argument valide.\x1b[0m")
        saisi_all = False
        allumettes -= nb_all
        joueur.score += nb_all
        # Condition de victoire/défaite
        if allumettes <= 0:
            partie_finie = True
        # Changement de joueur pour faire gagner celui qui n'a pas retiré la dernière
        if partie_finie :
            # Mise à jour score perdant
            if joueur.score > joueur.highscore_all :
                    joueur.highscore_all = joueur.score
            if joueur == j1 :
                joueur = j2
            else :
                joueur = j1
            print("\x1b[32mBravo ! ", joueur.pseudo, " a gagné !")
            print("Votre score : ", joueur.score, "\x1b[0m")
            joueur.nb_partieG += 1
            # Mise à jour du score gagnant 
            if joueur.score > joueur.highscore_all :
                    joueur.highscore_all = joueur.score
            j1.nb_partie += 1
            j2.nb_partie += 1
        # Changement de tour (et donc de joueur)
        if joueur == j1 :
            joueur = j2
        else :
            joueur = j1


