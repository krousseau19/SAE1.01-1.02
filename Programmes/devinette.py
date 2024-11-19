from global_var import Joueur, début_de_partie

def saisir_victoire(joueur : Joueur, j1 : Joueur, j2 : Joueur, devine : int) -> int :
    choix : int

    if joueur == j1 :
        joueur = j2
    else :
        joueur = j1
    choix = 0
    print("Le nombre de votre adversaire est ", devine, ", celui-ci est-il : ")
    print("1 - Trop petit")
    print("2 - Trop grand")
    print("3 - C'est gagné !")
    try :
        choix = int(input(f" {joueur.pseudo} veuillez saisir un choix :"))
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
    
def saisir_intervalle() -> int :
    borne_sup : int
    choix : int
    borne_sup = 0
    choix = -1

    while choix != 1 and choix != 2 and choix != 3 :
        print("Veuillez choisir un intervalle : ")
        print("1 - [1 - 100]")
        print("2 - [1 - 1 000]")
        print("3 - [1 - 10 000]")
        try :
            choix = int(input("Saisir un choix : "))
            if choix == 1 :
                borne_sup = 100
            elif choix == 2 :
                borne_sup = 1000
            elif choix == 3 :
                borne_sup = 10000
            else :
                print(f"\033[2J")
                print("Choix invalide")
        except : 
            print(f"\033[2J")
            print("Choix invalide")
    print(f"\033[2J")
    return borne_sup


def jeu_devinette(j1 : Joueur, j2: Joueur):
    nombre_secret : int
    devine : int
    tentatives : int
    partie_finie : bool
    joueur : Joueur
    saisi_j1 : bool
    saisi_j2 : bool
    choix : int
    choix_valide : bool
    intervalle : int

    print(f"\033[2J")
    print("\n    === Jeu de devinettes ===")
    joueur = début_de_partie()
    saisi_j1 = False
    j1.score = 0
    j2.score = 0
    nombre_secret = -1
    intervalle = saisir_intervalle()
    while not saisi_j1:
        try:
            while nombre_secret <= 0 or nombre_secret > intervalle :
                nombre_secret = int(input(f"{joueur.pseudo}, entrez un nombre secret à faire deviner : "))
                if nombre_secret <=0 or nombre_secret > intervalle :
                    print(f"\033[2J")
                    print("Erreur : veuillez entrer un nombre entier valide.")
            print(f"\033[2J")
            saisi_j1 = True
        except ValueError:
            print(f"\033[2J")
            print("Erreur : veuillez entrer un nombre entier valide.")
    tentatives = 0
    partie_finie = False
    if joueur == j1 :
        joueur = j2
    else :
        joueur = j1
    saisi_j2 = False
    devine = -1
    joueur.score = intervalle
    while not partie_finie:
        while not saisi_j2 :
            try :
                devine = int(input(f"{joueur.pseudo}, devinez le nombre : "))
                print(f"\033[2J")
                saisi_j2 = True
            except ValueError :
                print("Erreur : veuillez entrer un nombre entier valide.")
        saisi_j2 = False
        tentatives += 1
        joueur.score = int(joueur.score - (intervalle*(10/100)))
        choix_valide = False
        while not choix_valide :
            choix = saisir_victoire(joueur, j1, j2, devine)
            if devine < nombre_secret and choix == 1:
                if joueur.score <= 0 :
                    print(f"\033[2J")
                    print(f"\x1b[38;5;1m{joueur.pseudo} n'a pas réussi à trouver le nombre à temps ! (Score nul)\x1b[37m")
                    partie_finie = True
                else :
                    print(f"\033[2J")
                    print("\x1b[38;5;1mTrop petit.\x1b[37m")
                    print("")
                choix_valide = True
            elif devine > nombre_secret and choix == 2:
                if joueur.score <= 0 :
                    print(f"\033[2J")
                    print(f"\x1b[38;5;1m{joueur.pseudo} n'a pas réussi à trouver le nombre à temps ! (Score nul)\x1b[37m")
                    partie_finie = True
                else :
                    print(f"\033[2J")
                    print("\x1b[38;5;1mTrop grand.\x1b[37m")
                    print("")
                choix_valide = True
            elif devine == nombre_secret and choix == 3:
                print(f"\033[2J")
                print("\x1b[32mBravo ! ", joueur.pseudo, " a trouvé en ", tentatives, " tentatives.")
                print("Votre score : ", joueur.score, "\x1b[37m")
                choix_valide = True
                partie_finie = True
            else :
                print(f"\033[2J")
                print("Erreur : La réponse de ne correspond pas avec le résultat !")