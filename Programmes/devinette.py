from global_var import Joueur, début_de_partie

def saisir_victoire(joueur : str, j1 : Joueur, j2 : Joueur, devine : int) -> int :
    choix : int

    if joueur == j1.pseudo :
        joueur = j2.pseudo
    else :
        joueur = j1.pseudo
    choix = 0
    print("Le nombre de votre adversaire est ", devine, ", celui-ci est-il : ")
    print("1 - Trop petit")
    print("2 - Trop grand")
    print("3 - C'est gagné !")
    try :
        choix = int(input(f" {joueur} veuillez saisir un choix :"))
        if choix == 1 :
            return 1
        elif choix == 2 :
            return 2
        elif choix == 3 :
            return 3
        else :
            return -1
    except ValueError :
        return -1

def devine_nombre(j1 : Joueur, j2: Joueur):
    nombre_secret : int
    devine : int
    tentatives : int
    partie_finie : bool
    joueur : str
    saisi_j1 : bool
    saisi_j2 : bool
    choix : int
    choix_valide : bool

    print(f"\033[2J")
    print("\n    === Jeu de devinettes ===")
    joueur = début_de_partie()
    saisi_j1 = False
    nombre_secret = -1
    while not saisi_j1:
        try:
            nombre_secret = int(input(f"{joueur}, entrez un nombre secret à faire deviner : "))
            print(f"\033[2J")
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
                print(f"\033[2J")
                saisi_j2 = True
            except ValueError :
                print("Erreur : veuillez entrer un nombre entier valide.")
        saisi_j2 = False
        tentatives += 1
        choix_valide = False
        while not choix_valide :
            choix = saisir_victoire(joueur, j1, j2, devine)
            if devine < nombre_secret and choix == 1:
                print(f"\033[2J")
                print("\x1b[38;5;1mTrop petit.\x1b[37m")
                choix_valide = True
            elif devine > nombre_secret and choix == 2:
                print(f"\033[2J")
                print("\x1b[38;5;1mTrop grand.\x1b[37m")
                choix_valide = True
            elif devine == nombre_secret and choix == 3:
                print(f"\033[2J")
                print("\x1b[32mBravo ! ", joueur, " a trouvé en ", tentatives, " tentatives.\x1b[37m")
                choix_valide = True
                partie_finie = True
            else :
                print(f"\033[2J")
                print("Erreur : La réponse de ne correspond pas avec le résultat !")