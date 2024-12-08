# Fichier contenant toutes les fonctions relatives au jeu de devinettes
from ressource import Joueur, début_de_partie, qui_joue

def saisir_victoire(joueur : Joueur, j1 : Joueur, j2 : Joueur, devine : int) -> int :
    """
    Entrée : 4 arguments, le joueur actuel, le joueur 1 et le joueur 2, et le nombre saisi par celui qui cherche

    Sortie : Un entier, le choix de celui qui fait deviner

    Fonctionnement : Echange les joueurs (pour que ce soit le joueur qui fasse deviner qui réponde), puis affiche un menu
    en continu. Après cela, la fonction demande au joueur un saisi, et en fonction de ce saisi, la fonction se termine ou non.
    Si le résultat est 1, 2, ou 3 alors elle renvoie ce résultat, sinon l'affichage continu et le saisi recommence après un message d'erreur.
    """
    choix : int
    fin : bool

    if joueur == j1 :
        joueur = j2
    else :
        joueur = j1
    choix = 0
    fin = False
    while not fin :
        print("Le nombre de votre adversaire est ", devine, ", celui-ci est-il : ")
        print("1 - Trop petit")
        print("2 - Trop grand")
        print("3 - C'est gagné !")
        try :
            choix = int(input(f" {joueur.pseudo} veuillez saisir un choix :"))
        except ValueError :
            fin = False
        if choix in [1 , 2, 3] :
            fin = True
            return choix
    
def saisir_intervalle() -> int :
    """
    Entrée : Rien

    Sortie : Un entier, correspondant à la borne supérieure de l'intervalle

    Fonctionnement : Affiche en continu un menu permettant de choisir un intervalle, si le choix est valide (donc 1, 2 ou 3)
    alors l'affichage s'arrête, et la valeur de la borne supérieure est retournée, sinon, l'affichage continu et le saisi recommence.
    """
    borne_sup : int
    choix : int
    borne_sup = 0
    choix = -1
    print("\033c")
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
                print("\033c")
                print("Choix invalide")
        except : 
            print("\033c")
            print("Choix invalide")
    print("\033c")
    return borne_sup


def jeu_devinette(j1 : Joueur, j2: Joueur, intervalle : int):
    """
    Entrée : 3 arguments, les deux joueurs, ainsi qu'un entier représentant la borne supérieure de l'intervalle

    Sortie : Rien

    Fonctionnement : Fonction principale du jeu de devinettes, initialise toutes les variables nécessaires au fonctionnement du jeu ( le nombre de tentatives, le nomrbe à trouver,
    le nombre à comparer avec le nombre à trouver, etc...). Après l'initialisation, tant que 2 manches ne se sont pas écoulées (2 manches pour que chaque joueur puisse avoir un score),
    la fonction va demander au joueur de saisir le nombre à faire deviner, il doit se trouver entre 1 et la borne supérieure de l'intervalle, si ce n'est pas le cas, le saisi recommence
    après un message d'erreur. Une fois cela fait, l'autre joueur va saisir le nombre qu'il pense avoir été saisi par son adversaire, par la suite, le joueur ayant choisi le nombre à faire
    deviner va devoir saisir si le nombre de son adversaire est correct ou non (trop petit, trop grand, ou c'est le bon), la fonction effectue ensuite des tests pour s'assurer que le joueur
    ne triche pas, et que par exemple le nombre est bien plus petit que le nombre à deviner. Si la réponse est cohérente avec le saisi du joueur, alors la manche se termine et une nouvelle recommence,
    une fois les deux manches finies, la fonction compare le score des deux joueurs, celui avec le meilleur score gagne (les joueurs commençent avec un score équivalent à l'intervalle choisi, à chaque tentative,
    le joueur perd 10% de son score, la partie s'arrête si le joueur n'a plus de score).
    """
    nombre_secret : int
    devine : int
    tentatives : int
    partie_finie : bool
    joueur : Joueur
    joueur_d : str
    saisi_j1 : bool
    saisi_j2 : bool
    choix : int
    choix_valide : bool
    manche : int

    print("\033c")
    print("\n    === Jeu de devinettes ===")
    joueur = début_de_partie(j1, j2, qui_joue)
    joueur_d = joueur.pseudo
    j1.score = 0
    j2.score = 0
    manche = 1
    while manche <=2 :
        partie_finie = False
        choix_valide = False
        saisi_j1 = False
        saisi_j2 = False
        nombre_secret = -1
        print("\033c")
        while not saisi_j1:
            try:
                while nombre_secret <= 0 or nombre_secret > intervalle :
                    nombre_secret = int(input(f"{joueur.pseudo}, entrez un nombre secret à faire deviner : "))
                    if nombre_secret <=0 or nombre_secret > intervalle :
                        print("\033c")
                        print("Erreur : veuillez entrer un nombre entier valide.")
                print("\033c")
                saisi_j1 = True
            except ValueError:
                print("\033c")
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
                    while devine <= 0 or devine > intervalle :
                        devine = int(input(f"{joueur.pseudo}, devinez le nombre : "))
                        if devine <= 0 or devine > intervalle :
                            print("\033c")
                            print("Veuillez saisir un nombre dans l'intervalle.")
                    print("\033c")
                    saisi_j2 = True
                except ValueError :
                    print("\033c")
                    print("Erreur : veuillez entrer un nombre entier valide.")
            saisi_j2 = False
            tentatives += 1
            joueur.score = int(joueur.score - (intervalle*(10/100)))
            choix_valide = False
            while not choix_valide :
                choix = saisir_victoire(joueur, j1, j2, devine)
                if devine < nombre_secret and choix == 1:
                    if joueur.score <= 0 :
                        print("\033c")
                        print(f"\x1b[38;5;1m{joueur.pseudo} n'a pas réussi à trouver le nombre à temps ! (Score nul)\x1b[37m")
                        partie_finie = True
                    else :
                        print("\033c")
                        print("\x1b[38;5;1mTrop petit.\x1b[37m")
                        print("")
                    choix_valide = True
                elif devine > nombre_secret and choix == 2:
                    if joueur.score <= 0 :
                        print("\033c")
                        print(f"\x1b[38;5;1m{joueur.pseudo} n'a pas réussi à trouver le nombre à temps ! (Score nul)\x1b[37m")
                        partie_finie = True
                    else :
                        print("\033c")
                        print("\x1b[38;5;1mTrop grand.\x1b[37m")
                        print("")
                    choix_valide = True
                elif devine == nombre_secret and choix == 3:
                    print("\033c")
                    print("\x1b[32mBravo ! ", joueur.pseudo, " a trouvé en ", tentatives, " tentatives.")
                    print("Votre score : ", joueur.score, "\x1b[37m")
                    if joueur.score > joueur.highscore_dev :
                        joueur.highscore_dev = joueur.score
                    choix_valide = True
                    partie_finie = True
                else :
                    print("\033c")
                    print("Erreur : La réponse de ne correspond pas avec le résultat !")
            devine = -1
                
        if joueur_d == j1.pseudo :
            joueur = j2
        else :
            joueur = j1
        manche += 1
        if manche <= 2 :
            input("Une nouvelle manche va commencer, veuillez appuyer sur ENTRER...")
    if j1.score > j2.score :
        print("\033c")
        print("\x1b[32mBravo ! ", j1.pseudo, " a gagné la partie !")
        print("Votre score : ", j1.score, "\x1b[0m")
        j1.nb_partieG += 1
    elif j2.score > j1.score :
        print("\033c")
        print("\x1b[32mBravo ! ", j2.pseudo, " a gagné la partie !")
        print("Votre score : ", j2.score, "\x1b[0m")
        j2.nb_partieG += 1
    else :
        print("\033c")
        print("\x1b[38;5;208mIl y a eu égalité.\x1b[0m") 
    j1.nb_partie += 1
    j2.nb_partie += 1