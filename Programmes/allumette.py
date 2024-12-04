# Fichier contenant toutes les fonctions relatives au jeu des allumettes
from ressource import Joueur, début_de_partie, qui_joue

def jeu_allumettes(j1 : Joueur, j2 : Joueur):
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
    
    print("\033c")
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
                print("\033c")
                if nb_all < 1 or nb_all > 3:
                    print("\033c")
                    print("Erreur : Veuillez prendre entre 1 et 3 allumettes.")
                    saisi_all = False   
                if nb_all > allumettes :
                    print("\033c")
                    print("Erreur : Il n'y a plus assez d'allumettes.")
                    saisi_all = False
            except ValueError :
                print("\033c")
                print("Erreur : Veuillez saisir un argument valide.")
        saisi_all = False
        allumettes -= nb_all
        # Condition de victoire/défaite
        if allumettes <= 0:
            partie_finie = True
        # Changement de joueur pour faire gagner celui qui n'a pas retiré la dernière
        if partie_finie :
            if joueur == j1 :
                joueur = j2
            else :
                joueur = j1
            print("\033c")
            print("\x1b[32mBravo ! ", joueur.pseudo, " a gagné !\x1b[37m")
            joueur.score += 1
            joueur.nb_partieG += 1
            # Mise à jour du meilleur score si nécessaire
            if joueur.score > joueur.highscore_all :
                    joueur.highscore_all = joueur.score
            j1.nb_partie += 1
            j2.nb_partie += 1
        # Changement de tour (et donc de joueur)
        if joueur == j1 :
            joueur = j2
        else :
            joueur = j1


