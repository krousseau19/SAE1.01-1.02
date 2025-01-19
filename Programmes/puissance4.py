# Fichier contenant toutes les fonctions relatives au jeu de puissance 4
from ressource import Joueur, début_de_partie, qui_joue
import random
from time import sleep

def check_victoire(grille : list[list[str]], symbole : str) -> bool :
    """
    Entrée : Tableau de tableau (6x7) contenant des chaînes de caractères, et le symbole du joueur

    Sortie : Un booléen, True si il y a une victoire, False sinon

    Fonctionnement : Utilise 2 boucles imbriquées pour parcourir les lignes, les colonnes, et les diagonales afin de
    trouver un paterne contenant 4 fois d'affilé le symbole du joueur, dans ce cas, la fonction renvoie True, sinon il n'y
    a pas de victoire donc la fonction renvoie False
    """
    lignes : int
    colonnes : int

    lignes = len(grille)
    colonnes = len(grille[0])
    # Vérifie les lignes
    for i in range(lignes):
        for j in range(colonnes - 3):  # seulement jusqu'à la 4e dernière colonne (suite de 4 jetons et évite IndexError)
            if grille[i][j] == grille[i][j+1] == grille[i][j+2] == grille[i][j+3] == symbole:
                return True
    # Vérifie les colonnes
    for j in range(colonnes):
        for i in range(lignes - 3):  # seulement jusqu'à la 4e dernière ligne (suite de 4 jetons et évite IndexError)
            if grille[i][j] == grille[i+1][j] == grille[i+2][j] == grille[i+3][j] == symbole:
                return True
    # Vérifie les diagonales (haut-gauche vers bas-droite)
    for i in range(lignes - 3):
        for j in range(colonnes - 3): # //
            if grille[i][j] == grille[i+1][j+1] == grille[i+2][j+2] == grille[i+3][j+3] == symbole:
                return True
    # Vérifie les diagonales (bas-gauche vers haut-droite)
    for i in range(3, lignes):
        for j in range(colonnes - 3): # //
            if grille[i][j] == grille[i-1][j+1] == grille[i-2][j+2] == grille[i-3][j+3] == symbole:
                return True
    return False

def check_égalité(grille : list[list[str]]) -> bool :
    """
    Entrée : Un tableau de tableau (6x7) contenant des chaînes de caractères

    Sortie : Un booléen, True si il y a égalité, False sinon

    Fonctionnement : Parcours chaque ligne du tableau, si une case vide est trouvée alors la fonction renvoie
    False, sinon si elle n'en trouve pas, alors le tableau et plein, il y a égalité, et elle renvoie True
    """
    ligne : list[str]
    # Parcours chaque ligne de la grille
    for ligne in grille:
        if " " in ligne:  # Si une case vide est trouvée, donc la grille n'est pas pleine
            return False
    return True  # Aucune case vide n'a été trouvée, donc la grille est pleine

def afficher_grille(grille : list[list[str]]):
    """
    Entrée : Un tableau de tableau (6x7) contenant des chaînes de caractères

    Sortie : Rien

    Fonctionnement : Affiche la grille passée en paramètre avec en jointure des " | " pour faire les séparateurs
    de colonnes, une fois cela fait, la fonction affiche les indicces de chaque colonne en dessous de celles-ci
    """
    ligne : list[str]

    ligne = []
    for ligne in grille:
        print(" | ".join(ligne))    # séparateurs de colonnes
    print("1 | 2 | 3 | 4 | 5 | 6 | 7")  # indices des colonnes

def coup_aleatoire(grille : list[list[str]])  -> int :
    """
    Entrée : Une liste de chaîne de caractères correspondant à la grille du puissance 4 

    Sortie : Un entier correspondant à l'indice de la colonne à jouer

    Fonctionnement : Fonction qui sélectionne un coup aléatoire parmi les colonnes libres (colonnes avec
    au moins une case vide)
    """
    libres : list[int]
    i : int
    j : int
    libres = []
    for i in range(6) :
        for j in range(5, -1, -1):
            if grille[i][j-1] == " " :
                libres.append(i)
    return random.choice(libres)

def coup_optimal(grille: list[list[str]], symbole: str) -> int:
    """
    Entrée : Une grille (liste de liste de chaînes de caractères) : une grille de puissance 4 de 6x7
    Un symbole (str) : le symbole du joueur, un cercle "O" rouge ou jaune.
    
    Sortie : Un entier, correspondant à la meilleure colonne jouer
        
    Fonctionnement : Cherche d'abord un coup gagnant pour le joueur.
    Si aucun coup gagnant, cherche à bloquer l'adversaire.
    Sinon, choisit une case stratégique (en commençant par le centre).
    """
    lignes : int
    colonnes : int
    adversaire : str
    lignes_disponibles : list[int]
    recherche : bool
    col : int
    ligne : int
    ordre_priorite : list[int]

    lignes = len(grille)
    colonnes = len(grille[0])
    if symbole == "\x1b[31mO\x1b[37m" :
        adversaire = "\x1b[38;5;226mO\x1b[37m" 
    else :
        adversaire = "\x1b[31mO\x1b[37m"
    
    # Trouver les lignes disponibles pour chaque colonne
    lignes_disponibles = [-1] * colonnes
    for col in range(colonnes):
        recherche = True  # Indique si une ligne disponible a été trouvée pour cette colonne
        for ligne in range(lignes - 1, -1, -1):
            if grille[ligne][col] == " " and recherche:
                lignes_disponibles[col] = ligne
                recherche = False  # On arrête la recherche pour cette colonne
    
    # Tester un coup gagnant pour la machine
    for col in range(colonnes):
        if lignes_disponibles[col] != -1:
            grille[lignes_disponibles[col]][col] = symbole
            if check_victoire(grille, symbole):
                grille[lignes_disponibles[col]][col] = " "
                return col + 1
            grille[lignes_disponibles[col]][col] = " "

    # Bloquer un coup gagnant pour l'adversaire
    for col in range(colonnes):
        if lignes_disponibles[col] != -1:
            grille[lignes_disponibles[col]][col] = adversaire
            if check_victoire(grille, adversaire):
                grille[lignes_disponibles[col]][col] = " "
                return col + 1
            grille[lignes_disponibles[col]][col] = " "

    # Choisir une colonne stratégique
    ordre_priorite = [3, 4, 2, 5, 1, 6, 0]
    for col in ordre_priorite:
        if lignes_disponibles[col] != -1:
            return col + 1

    # Si aucune colonne jouable (normalement impossible)
    return -1

def coup_intermediaire(grille : list[list[str]], symbole : str)  -> int :
    """
    Entrée : Une liste de chaîne de caractères correspondant au plateau de jeu, une chaine de caractère correspondant au symbole du joueur

    Sortie : Un entier correspondant à la colonne choisie

    Fonctionnement : Fonction qui en fonction du résultat de alea, va soit donner un coup aléatoire ou le coup optimal à jouer en fonction de la grille,
    celle-ci est utilisée pour faire jouer la machine en difficulté intermédiaire.
    """
    colonne : int
    alea : int
    alea = random.randint(0,1) # Génère aléatoirement un entier entre 0 et 1
    if alea == 0 : # Si 0 alors un coup aléatoire
        colonne = coup_aleatoire(grille)
    else : # Sinon le meilleur coup possible
        colonne = coup_optimal(grille, symbole) 
    return colonne

def jeu_puissance4(j1 : Joueur, j2 : Joueur, mode : int, diff : int):
    """
    Entrée : 2 arguments, les 2 joueurs

    Sortie : Rien

    Fonctionnement : Fonction qui gère les principales fonctionnalités du puissance 4, et qui fait aussi appel aux autres fonctions la précédant. 
    Elle initialise les variables concernant le jeu (la grille, le symbole, les booléens de contrôle, etc...). Une fois cela fait, tant que la partie
    n'est pas finie, la fonction affiche la grille et demande un saisi à l'utilisateur, puis modifie la grille en conséquence. A chaque tour la fonction
    effectue les différents tests de victoire/égalité et affiche les messages en fonction des résultats, ainsi que la modification du booléen partie_finie
    si nécessaire. Une fois la partie finie, les attributs des joueurs sont modifiés selon leur score et la fonction s'arrête
    """
    joueur : Joueur
    grille : list[list[str]]
    symbole : str
    partie_finie : bool
    colonne_pleine : bool
    saisi_j : bool
    colonne : int
    ligne : int

    print("\033c")
    print("=== Jeu de Puissance 4 ===")
    grille = [[" " for _ in range(7)] for _ in range(6)]    # 7 colonnes, 6 lignes
    joueur = début_de_partie(j1, j2, qui_joue)
    j1.score = 0
    j2.score = 0
    ligne = -1
    colonne = -1
    partie_finie = False
    
    while not partie_finie :
        if joueur == j1 :
            symbole = '\x1b[31mO\x1b[37m'
        else :
            symbole = '\x1b[38;5;226mO\x1b[37m'
        saisi_j = False
        while not saisi_j :
            afficher_grille(grille)
            print(f"Tour de {joueur.pseudo} ({symbole})")
            if joueur.pseudo == "machine 1" or joueur.pseudo == "machine 2" : # Si une machine joue
                if diff == 1 :
                    colonne = coup_aleatoire(grille)
                    saisi_j = True
                elif diff == 2 :
                    colonne = coup_intermediaire(grille, symbole)
                    saisi_j = True
                else :
                    colonne = coup_optimal(grille, symbole)
                    saisi_j = True
                sleep(2)
                print("\033c")
            else :
                try:
                    colonne = int(input(f"{joueur.pseudo} ({symbole}), choisissez une colonne (1-7) : "))
                    print("\033c")
                    saisi_j = True
                except ValueError:
                    print("\033c")
                    print("\x1b[31mErreur : Veuillez entrer un nombre valide.\x1b[0m")
                    saisi_j = False
                if colonne < 1 or colonne > 7:
                    print("\033c")
                    print("\x1b[31mErreur : Numéro de colonne invalide, réessayez.\x1b[0m")
                    saisi_j = False
            if saisi_j :
                colonne_pleine = True
                for ligne in range(5, -1, -1):
                    if grille[ligne][colonne-1] == " "  and colonne_pleine == True :
                        grille[ligne][colonne-1] = symbole
                        joueur.score += 5
                        colonne_pleine = False
                
                if colonne_pleine :
                    print("\033c")
                    print("\x1b[31mErreur : Cette colonne est pleine, choisissez-en une autre.\x1b[0m")
                    saisi_j = False
        saisi_j = False       
        if check_victoire(grille, symbole):
            print("\033c")
            afficher_grille(grille)
            print(f"\x1b[32mFélicitations ! {joueur.pseudo} a gagné !")
            print("Score : ", joueur.score, "\x1b[0m")
            joueur.nb_partieG += 1
            joueur.score += 1
            # Mise à jour score gagnant
            if joueur.score > joueur.highscore_pui :
                    joueur.highscore_pui = joueur.score
            #Mise à jour score perdant
            if joueur == j1 :
                joueur = j2
            else :
                joueur = j1
            if joueur.score > joueur.highscore_pui :
                    joueur.highscore_pui = joueur.score
            partie_finie = True
        elif check_égalité(grille):
            print("\033c")
            afficher_grille(grille)
            print("\x1b[38;5;208mIl y a eu égalité ! La grille est pleine !\x1b[0m")
            partie_finie = True
        else : 
            if joueur == j1 :
                joueur = j2
            else :
                joueur = j1
    j1.nb_partie += 1
    j2.nb_partie += 1