from global_var import Joueur, début_de_partie, qui_joue

def check_victoire(grille : list[list[str]], symbole : str) -> bool :
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
    ligne : list[str]

    for ligne in grille:
        if " " in ligne:  # Si une case vide est trouvée, donc la grille n'est pas pleine
            return False
    return True  # Aucune case vide n'a été trouvée, donc la grille est pleine

def afficher_grille(grille : list[list[str]]):
    ligne : list[str]

    ligne = []
    for ligne in grille:
        print(" | ".join(ligne))    # séparateurs de colonnes
    print("1 | 2 | 3 | 4 | 5 | 6 | 7")  # indices des colonnes

def jeu_puissance4(j1 : Joueur, j2 : Joueur):
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
            symbole = '\x1b[33mO\x1b[37m'
        saisi_j = False
        while not saisi_j :
            afficher_grille(grille)
            try:
                colonne = int(input(f"{joueur.pseudo} ({symbole}), choisissez une colonne (1-7) : "))
                print("\033c")
                saisi_j = True
            except ValueError:
                print("\033c")
                print("Erreur : Veuillez entrer un nombre valide.")
                saisi_j = False
            if colonne < 1 or colonne > 7:
                print("\033c")
                print("Erreur : Numéro de colonne invalide, réessayez.")
                saisi_j = False
            if saisi_j :
                colonne_pleine = True
                for ligne in range(5, -1, -1):
                    if grille[ligne][colonne-1] == " "  and colonne_pleine == True :
                        grille[ligne][colonne-1] = symbole 
                        colonne_pleine = False
            
                if colonne_pleine :
                    print("\033c")
                    print("Erreur : Cette colonne est pleine, choisissez-en une autre.")
                    saisi_j = False
        saisi_j = False       
        if check_victoire(grille, symbole):
            print("\033c")
            afficher_grille(grille)
            print(f"\x1b[32mFélicitations ! {joueur.pseudo} a gagné !\x1b[37m")
            joueur.nb_partieG += 1
            joueur.score += 1
            if joueur.score > joueur.highscore_pui :
                    joueur.highscore_pui = joueur.score
            partie_finie = True
        elif check_égalité(grille):
            print("\033c")
            afficher_grille(grille)
            print("\x1b[38;5;208mIl y a eu égalité ! La grille est pleine !\x1b[37m")
            partie_finie = True
        else : 
            if joueur == j1 :
                joueur = j2
            else :
                joueur = j1
    j1.nb_partie += 1
    j2.nb_partie += 1