from global_var import Joueur, début_de_partie

def afficher_plateau(plateau : list[list[str]]):
    print("   0   1   2")
    print("0  " + plateau[0][0] + " | " + plateau[0][1] + " | " + plateau[0][2])
    print("  ---+---+---")
    print("1  " + plateau[1][0] + " | " + plateau[1][1] + " | " + plateau[1][2])
    print("  ---+---+---")
    print("2  " + plateau[2][0] + " | " + plateau[2][1] + " | " + plateau[2][2])


def verifier_victoire(plateau : list[list[str]]):

    for i in range(3):
        if plateau[i][0] == plateau[i][1] == plateau[i][2] != ' ':
            return True
        if plateau[0][i] == plateau[1][i] == plateau[2][i] != ' ':
            return True
    if plateau[0][0] == plateau[1][1] == plateau[2][2] != ' ':
        return True
    if plateau[0][2] == plateau[1][1] == plateau[2][0] != ' ':
        return True
    return False

def verifier_egalite(plateau : list[list[str]]):
    return all([case != " " for ligne in plateau for case in ligne])

def jeu_morpion(j1 : Joueur, j2 : Joueur):
    jeu_termine : bool
    ligne : int
    colonne : int
    plateau : list[list[str]]
    joueur : Joueur
    symbole : str

    print(f"\033[2J")
    print("\n    === Jeu du morprion ===")
    plateau = [[" " for _ in range(3)] for _ in range(3)]
    jeu_termine = False
    joueur = début_de_partie()
    
    while not jeu_termine:
        afficher_plateau(plateau)
        print(f"Tour de {joueur.pseudo}")
        if joueur == j1 :
            symbole = '\x1b[31mX\x1b[37m'
        else :
            symbole = '\x1b[34mO\x1b[37m'

        try:
            ligne = int(input("Choisissez une ligne (0, 1 ou 2) : "))
            colonne = int(input("Choisissez une colonne (0, 1 ou 2) : "))
            print(f"\033[2J")
            if plateau[ligne][colonne] != " ":
                print(f"\033[2J")
                print("Erreur : Cette case est déjà prise. Choisissez une autre case.")
                continue
            plateau[ligne][colonne] = symbole
        except (ValueError, IndexError):
            print(f"\033[2J")
            print("Erreur : Coordonnées invalides. Veuillez entrer des chiffres entre 0 et 2.")
            continue

        if verifier_victoire(plateau):
            print(f"\033[2J")
            afficher_plateau(plateau)
            print("\x1b[32mFélicitations !", joueur.pseudo, " a gagné !\x1b[37m")
            jeu_termine = True
        elif verifier_egalite(plateau):
            print(f"\033[2J")
            afficher_plateau(plateau)
            print("\x1b[38;5;208mIl y a eu égalité !\x1b[37m")
            jeu_termine = True
        else:
            if joueur == j1 :
                joueur = j2
            else :
                joueur = j1
