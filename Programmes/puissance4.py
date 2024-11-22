from global_var import Joueur, début_de_partie

def check_victoire(grille : list[list[str]], symbole : str):
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

def afficher_grille(grille : list[list[str]]):
    ligne : list[str]

    for ligne in grille:
        print(" | ".join(ligne))    # séparateurs de colonnes
    print("1 | 2 | 3 | 4 | 5 | 6 | 7")  # indices des colonnes

def jeu_puissance4(j1 : Joueur, j2 : Joueur):
    joueur : Joueur
    grille : list[list[str]]
    symbole : str
    jeu_termine : bool
    colonne_pleine : bool
    colonne : int
    ligne : int

    print("\033c")
    print("=== Jeu de Puissance 4 ===")
    grille = [[" " for _ in range(7)] for _ in range(6)]    # 7 colonnes, 6 lignes
    joueur = début_de_partie()
    j1.score = 0
    j2.score = 0
    jeu_termine = False
    
    while not jeu_termine :
        afficher_grille(grille)
        if joueur == j1 :
            symbole = '\x1b[31mO\x1b[37m'
        else :
            symbole = '\x1b[33mO\x1b[37m'
        try:
            colonne = int(input(f"{joueur.pseudo} ({symbole}), choisissez une colonne (1-7) : "))
            print("\033c")
        except ValueError:
            print("\033c")
            print("Erreur : Veuillez entrer un nombre valide.")
            continue
        if colonne < 1 or colonne > 7:
            print("\033c")
            print("Erreur : Numéro de colonne invalide, réessayez.")
            continue
        colonne_pleine = True
        for ligne in range(5, -1, -1):
            if grille[ligne][colonne-1] == " "  and colonne_pleine == True :
                grille[ligne][colonne-1] = symbole
                colonne_pleine = False
        
        if colonne_pleine :
                print("\033c")
                print("Erreur : Cette colonne est pleine, choisissez-en une autre.")
                
        if check_victoire(grille, symbole):
            afficher_grille(grille)
            print(f"\x1b[32mFélicitations ! {joueur.pseudo} a gagné !\x1b[37m")
            joueur.nb_partieG += 1
            joueur.score = 1
            jeu_termine = True
        else : 
            if joueur == j1 :
                joueur = j2
            else :
                joueur = j1
    j1.nb_partie += 1
    j2.nb_partie += 1