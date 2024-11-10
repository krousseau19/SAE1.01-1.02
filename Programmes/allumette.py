from global_var import Joueur, début_de_partie

def jeu_allumettes(j1 : Joueur, j2 : Joueur):
    allumettes : int
    joueur : str
    nb_all : int
    i : int # type: ignore
    saisi_all : bool
    
    print(f"\033[2J")
    print("\n    === Jeu des allumettes ===")
    allumettes = 20
    joueur = début_de_partie()
    while allumettes > 0:
        print(f"\033[2J")
        print("Il reste ", allumettes, "allumettes.")
        for i in range(0,allumettes) :  # type: ignore
            print("\x1b[38;5;1m.", end=" ")
        print("")
        for i in range(0,allumettes) :  # type: ignore
            print("\x1b[38;5;94m|", end=" ")
        print("\x1b[37m")
        saisi_all = False
        nb_all = -1
        while not saisi_all :
            try :
                nb_all = int(input(f"{joueur} combien d'allumettes prenez-vous (1-3) ? "))
                saisi_all = True
            except ValueError :
                print("Erreur : Veuillez saisir un argument valide.")
        saisi_all = False
        if nb_all < 1 or nb_all > 3:
                print("Veuillez prendre entre 1 et 3 allumettes.")
                continue
        allumettes -= nb_all
        if allumettes <= 0:
            print(f"\033[2J")
            print("\x1b[38;5;1m", joueur, " a perdu !")
            print("\x1b[37m")
        if joueur == j1.pseudo :
            joueur = j2.pseudo
        else :
            joueur = j1.pseudo



