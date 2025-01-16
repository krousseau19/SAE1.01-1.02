# Fichier contenant toutes les fonctions relatives au jeu de morpion
from ressource import Joueur, début_de_partie, qui_joue
import random
from time import sleep

def afficher_plateau(plateau : list[list[str]]):
    """
    Entrée : 1 argument, une liste de liste de chaine de caractère (un tableau à deux dimensions de 3x3)

    Sortie : Rien

    Fonctionnement : Affiche un tableau de morpion en concaténant les éléments du tableau à deux dimensions avec
    des caractères pour représenter un tableau avec séparateurs de colonnes, de lignes, et des indices (A, B, C et 1, 2, 3)
    """
    print("   1   2   3")
    print("A  " + plateau[0][0] + " | " + plateau[0][1] + " | " + plateau[0][2])
    print("  ---+---+---")
    print("B  " + plateau[1][0] + " | " + plateau[1][1] + " | " + plateau[1][2])
    print("  ---+---+---")
    print("C  " + plateau[2][0] + " | " + plateau[2][1] + " | " + plateau[2][2])


def verifier_victoire(plateau : list[list[str]]) -> bool :
    """
    Entrée : Un tableau de tableau de chaine de caractère, soit un tableau à deux dimensions de 3x3

    Sortie : Un booléen, True si il y a une victoire, false sinon

    Fonctionnement : Balaye le tableau de tableau de ligne en ligne, de colonne en colonne, et de diagonale
    en diagonale. Si sur ces motifs, il y a 3 fois le même symbole (que ces cases sont identiques mais différentes
    de rien/" " ), alors la fonction retourne True, sinon False 
    """
    for i in range(3):
        # Balayage en ligne
        if plateau[i][0] == plateau[i][1] == plateau[i][2] != ' ':
            return True
        # Balayage en colonne
        if plateau[0][i] == plateau[1][i] == plateau[2][i] != ' ':
            return True
    # Balayage de la diagonale haut-gauche bas-droite
    if plateau[0][0] == plateau[1][1] == plateau[2][2] != ' ':
        return True
    # Balayage de la diagonale haut-droite bas-gauche
    if plateau[0][2] == plateau[1][1] == plateau[2][0] != ' ':
        return True
    return False

def verifier_egalite(plateau : list[list[str]]) -> bool:
    """
    Entrée : Un tableau de tableau de chaîne de caractères, soit un tableau à deux dimensions de 3x3

    Sortie : Un booléen, True si égalité, False sinon

    Fonctionnement : Parcours toutes les cases de la grille de morpion, si toutes les cases sont différentes
    de " ", et donc que la grille est pleine, alors la fonction retourne True, sinon False car il n'y a pas égalité
    """
    return all([case != " " for ligne in plateau for case in ligne])

def saisi_case(plateau : list[list[str]], joueur : Joueur, symbole : str) -> str:
    """
    Entrée : 3 arguments, un plateau de jeu (tableau à deux dimensions de 3x3), le joueur effectuant le saisi et son symbole

    Sortie : Une chaîne de caractère correspondant aux coordonnées de la case à modifier

    Fonctionnement : Demande à l'utilisateur de saisir des coordonnées (ex : A1, B3) composées d'une lettre et d'un chiffre.
    La fonction converti ensuite la lettre et le chiffre pour que cela corresponde bien à la bonne case dans la grille.
    """
    chaine_c : str
    chaine_l : str
    case : str
    est_valide : bool
    choix : str

    chaine_l = "ABC"  # Pour savoir si la lettre est valide
    chaine_c = "123"  # Pour savoir si le chiffre est valide
    case = ""         
    est_valide = False     
    while not est_valide :
        # Prend la coordonnée, peut importe les espaces ou les majuscules/minuscules
        choix = input("Choisissez une case (lettre puis numéro, ex : A1) : ").strip().upper()
        if len(choix) != 2 :
            print("\033c")
            print("\x1b[31mErreur : Coordonnées invalides.\x1b[0m")
            afficher_plateau(plateau)
            print(f"Tour de {joueur.pseudo} ({symbole})")
        elif choix[0] in chaine_l and choix[1] in chaine_c :
            # Concatène les deux résultats pour former les coordonnées de la case
            case = str(chaine_l.index(choix[0])) + str(chaine_c.index(choix[1]))
            est_valide = True
        else:
            print("\033c")
            print("\x1b[31mErreur : Coordonnées invalides.\x1b[0m")
            afficher_plateau(plateau)
            print(f"Tour de {joueur.pseudo} ({symbole})")
    return case


def coup_aleatoire(plateau: list[list[str]]) -> tuple[int, int]:
    """
    Entrée : Une liste de chaîne de caractères correspondant au plateau de jeu

    Sortie : Un tuple de deux entiers correspondant aux coordonnées d'une case libre

    Fonctionnement : Fonction qui sélectionne un coup aléatoire parmi les cases libres.
    """
    libres : list[tuple[int, int]]
    i : int
    j : int
    libres = []
    for i in range(3):
        for j in range(3):
            if plateau[i][j] == " ":
                libres.append((i, j))
    return random.choice(libres)

def coup_optimal(plateau: list[list[str]], symbole : str) -> tuple[int, int] :
    """
    Entrée : Un plateau (liste de liste de chaînes de caractères) : un plateau de morpion de 3x3
    Un symbole (str) : le symbole du joueur, soit 'X' soit 'O'
    
    Sortie : Une tuple contenant les indices (ligne, colonne) de la meilleure case à jouer.
        
    Fonctionnement : Cherche d'abord un coup gagnant pour le joueur.
    Si aucun coup gagnant, cherche à bloquer l'adversaire.
    Sinon, choisit une case stratégique (par exemple le centre, puis les coins).
    """
    adversaire : str
    i : int
    j : int
    coins : list[tuple[int, int]]
    bords : list[tuple[int, int]]
    coin : tuple[int, int]
    bord : tuple[int, int]

    if symbole == '\x1b[34mO\x1b[37m' :
        adversaire = '\x1b[31mX\x1b[37m'
    else :
        adversaire = '\x1b[34mO\x1b[37m'

    # Parcours pour trouver si case gagnante
    for i in range(3):
        for j in range(3):
            if plateau[i][j] == ' ':  # Si la case est vide
                plateau[i][j] = symbole
                if verifier_victoire(plateau):
                    plateau[i][j] = ' '  # Annule le coup après avoir vérifié
                    return (i, j)
                plateau[i][j] = ' '  # Annule le coup

    # Parcours pour trouver si bloquer la victoire possible
    for i in range(3):
        for j in range(3):
            if plateau[i][j] == ' ': 
                plateau[i][j] = adversaire
                if verifier_victoire(plateau):
                    plateau[i][j] = ' ' 
                    return (i, j)
                plateau[i][j] = ' ' 

    # Si aucun des deux cas au dessus, on choisi une case stratégique
    if plateau[1][1] == ' ':  # Le centre
        return (1, 1)

    coins = [(0, 0), (0, 2), (2, 0), (2, 2)] # Les coins
    for coin in coins:
        i = coin[0]
        j = coin[1]
        if plateau[i][j] == ' ':
            return (i, j)

    bords = [(0, 1), (1, 0), (1, 2), (2, 1)] # Les bords
    for bord in bords:
        i = bord[0]
        j = bord[1]
        if plateau[i][j] == ' ':
            return (i, j)

    return None  # type: ignore


def coup_intermediaire(plateau : list[list[str]], symbole : str) -> tuple[int, int]:
    """
    Entrée : Une liste de chaîne de caractères correspondant au plateau de jeu, une chaine de caractère correspondant au symbole du joueur

    Sortie : Un tuple de deux entiers correspondant aux coordonnées d'une case libre

    Fonctionnement : Fonction qui en fonction du résultat de alea, va soit donner un coup aléatoire ou le coup optimal à jouer en fonction du plateau,
    celle-ci est utilisée pour faire jouer la machine en difficulté intermédiaire.
    """
    case : tuple[int, int]
    alea : int
    alea = random.randint(0,1)
    if alea == 0 :
        case = coup_aleatoire(plateau)
    else :
        case = coup_optimal(plateau, symbole)
    return case

def jeu_morpion(j1 : Joueur, j2 : Joueur, mode : int, diff : int):
    """
    Entrée : 2 arguments, les deux joueurs 

    Sortie : Rien

    Fonctionnement : Initialise toutes les variables nécessaires au fonctionnement du morpion ( plateau, ligne, colonne, etc...),
    puis tant que la partie n'est pas finie, chaque joueur se voit attribué un symbole. Une fois cela fait, la fonction va demander un saisi
    au joueur courant et va ensuite modifier la case correspondante avec son symbole. A chaque tour la fonction effectue les tests
    de victoire et d'égalité, puis affiche un message en conséquence si une de ces conditions est valide. A noté que cette fonction utilise
    toutes les fonctions la précédent, pour le saisi, ou les tests par exemple
    """
    partie_finie : bool
    case : str
    case_m : tuple[int, int]
    ligne : int
    colonne : int
    plateau : list[list[str]]
    joueur : Joueur
    symbole : str
    saisi_c : bool

    print("\033c")
    print("\n    === Jeu du morprion ===")
    j1.score = 0
    j2.score = 0
    ligne = -1
    colonne = -1
    plateau = [[" " for _ in range(3)] for _ in range(3)]
    partie_finie = False
    joueur = début_de_partie(j1, j2, qui_joue)
    
    while not partie_finie:
        if joueur == j1 :
            symbole = '\x1b[31mX\x1b[37m'
        else :
            symbole = '\x1b[34mO\x1b[37m'
        saisi_c = False
        while not saisi_c :
            print("\033c")
            afficher_plateau(plateau)
            print(f"Tour de {joueur.pseudo} ({symbole})")
            if joueur.pseudo == "machine 1" or joueur.pseudo == "machine 2" :   # Si machine joue
                case_m = (0,0)
                if diff == 2 :
                    case_m = coup_intermediaire(plateau, symbole)
                elif diff == 3 :
                    case_m = coup_optimal(plateau, symbole)
                else :  # Diff 1 
                    case_m = coup_aleatoire(plateau)
                ligne = case_m[0]
                colonne = case_m[1]
                saisi_c = True
                sleep(2)
            else :  # Si joueur joue
                case = saisi_case(plateau, joueur, symbole)
                saisi_c = True
                ligne = int(case[0])
                colonne = int(case[1])
                print("\033c")
                if plateau[ligne][colonne] != " ":
                    print("\033c")
                    print("\x1b[31mErreur : Cette case est déjà prise. Choisissez une autre case.\x1b[0m")
                    saisi_c = False
        saisi_c = False
        joueur.score += 10
        plateau[ligne][colonne] = symbole 
        if verifier_victoire(plateau):
            print("\033c")
            afficher_plateau(plateau)
            print("\x1b[32mFélicitations !", joueur.pseudo, " a gagné !")
            print("Votre score : ", joueur.score, "\x1b[0m")
            joueur.nb_partieG += 1
            # Mise à jour score gagnant
            if joueur.score > joueur.highscore_mor :
                    joueur.highscore_mor = joueur.score
            if joueur == j1 :
                joueur = j2
            else :
                joueur = j1
            # Mise à jour score perdant
            if joueur.score > joueur.highscore_mor :
                    joueur.highscore_mor = joueur.score
            partie_finie = True
        elif verifier_egalite(plateau):
            print("\033c")
            afficher_plateau(plateau)
            print("\x1b[38;5;208mIl y a eu égalité !\x1b[0m")
            partie_finie = True
        else:
            if joueur == j1 :
                joueur = j2
            else :
                joueur = j1
    j1.nb_partie += 1
    j2.nb_partie += 1
