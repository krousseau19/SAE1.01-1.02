from global_var import Joueur, début_de_partie, qui_joue

def jeu_allumettes(j1 : Joueur, j2 : Joueur):
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
    while not partie_finie:
        saisi_all = False
        nb_all = -1
        while not saisi_all :
            print("Il reste ", allumettes, "allumettes.")
            for _ in range(0,allumettes) :  
                print("\x1b[38;5;1m.", end=" ")
            print("")
            for _ in range(0,allumettes) :  
                print("\x1b[38;5;94m|", end=" ")
            print("\x1b[37m")
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
        if allumettes <= 0:
            partie_finie = True
        if partie_finie :
            if joueur == j1 :
                joueur = j2
            else :
                joueur = j1
            print("\033c")
            print("\x1b[32mBravo ! ", joueur.pseudo, " a gagné !\x1b[37m")
            joueur.score += 1
            joueur.nb_partieG += 1
            if joueur.score > joueur.highscore_all :
                    joueur.highscore_all = joueur.score
            j1.nb_partie += 1
            j2.nb_partie += 1
        if joueur == j1 :
            joueur = j2
        else :
            joueur = j1


