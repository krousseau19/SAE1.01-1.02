from global_var import Joueur, début_de_partie

def afficher_plateau(plateau : list[list[str]]):
    print("   1   2   3")
    print("A  " + plateau[0][0] + " | " + plateau[0][1] + " | " + plateau[0][2])
    print("  ---+---+---")
    print("B  " + plateau[1][0] + " | " + plateau[1][1] + " | " + plateau[1][2])
    print("  ---+---+---")
    print("C  " + plateau[2][0] + " | " + plateau[2][1] + " | " + plateau[2][2])


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

def saisi_case(plateau : list[list[str]]) -> str:
    chaine_c : str
    chaine_l : str
    case : str
    est_valide : bool
    choix : str

    chaine_l = "ABC"  
    chaine_c = "123"  
    case = ""         
    est_valide = False     
    while not est_valide :
        choix = input("Choisissez une case (lettre puis numéro, ex : A1) : ").strip().upper()
        if len(choix) != 2 :
            print("\033c")
            print("Erreur : Coordonnées invalides.")
            afficher_plateau(plateau)
        elif choix[0] in chaine_l and choix[1] in chaine_c :
            case = str(chaine_l.index(choix[0])) + str(chaine_c.index(choix[1]))
            est_valide = True
        else:
            print("\033c")
            print("Erreur : Coordonnées invalides.")
            afficher_plateau(plateau)
    return case

def jeu_morpion(j1 : Joueur, j2 : Joueur):
    partie_finie : bool
    case : str
    ligne : int
    colonne : int
    plateau : list[list[str]]
    joueur : Joueur
    symbole : str

    print("\033c")
    print("\n    === Jeu du morprion ===")
    j1.score = 0
    j2.score = 0
    plateau = [[" " for _ in range(3)] for _ in range(3)]
    partie_finie = False
    joueur = début_de_partie()
    
    while not partie_finie:
        afficher_plateau(plateau)
        print(f"Tour de {joueur.pseudo}")
        if joueur == j1 :
            symbole = '\x1b[31mX\x1b[37m'
        else :
            symbole = '\x1b[34mO\x1b[37m'

        case = saisi_case(plateau)
        ligne = int(case[0])
        colonne = int(case[1])
        print("\033c")
        if plateau[ligne][colonne] != " ":
            print("\033c")
            print("Erreur : Cette case est déjà prise. Choisissez une autre case.")
            continue
        plateau[ligne][colonne] = symbole

        if verifier_victoire(plateau):
            print("\033c")
            afficher_plateau(plateau)
            print("\x1b[32mFélicitations !", joueur.pseudo, " a gagné !\x1b[37m")
            joueur.nb_partieG += 1
            joueur.score += 1
            if joueur.score > joueur.highscore_mor :
                    joueur.highscore_mor = joueur.score
            partie_finie = True
        elif verifier_egalite(plateau):
            print("\033c")
            afficher_plateau(plateau)
            print("\x1b[38;5;208mIl y a eu égalité !\x1b[37m")
            partie_finie = True
        else:
            if joueur == j1 :
                joueur = j2
            else :
                joueur = j1
    j1.nb_partie += 1
    j2.nb_partie += 1
