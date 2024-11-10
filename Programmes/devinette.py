from global_var import Joueur, début_de_partie

def devine_nombre(j1 : Joueur, j2: Joueur):
    nombre_secret : int
    devine : int
    tentatives : int
    partie_finie : bool
    joueur : str
    saisi_j1 : bool
    saisi_j2 : bool

    print("\n    === Jeu de devinettes ===")
    joueur = début_de_partie()
    saisi_j1 = False
    nombre_secret = -1
    while not saisi_j1:
        try:
            nombre_secret = int(input(f"{joueur}, entrez un nombre secret à faire deviner : "))
            saisi_j1 = True
        except ValueError:
            print("Erreur : veuillez entrer un nombre entier valide.")
    tentatives = 0
    partie_finie = False
    if joueur == j1.pseudo :
        joueur = j2.pseudo
    else :
        joueur = j1.pseudo
    saisi_j2 = False
    devine = -1
    while not partie_finie:
        while not saisi_j2 :
            try :
                devine = int(input(f"{joueur}, devinez le nombre : "))
                saisi_j2 = True
            except ValueError :
                print("Erreur : veuillez entrer un nombre entier valide.")
        saisi_j2 = False
        tentatives += 1
        if devine < nombre_secret:
            print("Trop petit.")
        elif devine > nombre_secret:
            print("Trop grand.")
        else:
            print("Bravo ! ", joueur, " a trouvé en ", tentatives, " tentatives.")
            partie_finie = True
            