from devinette import jeu_devinette
from allumette import jeu_allumettes
from morpion import jeu_morpion
from puissance4 import jeu_puissance4
from global_var import creation_joueurs, afficher_menu, saisir_choix, j1, j2

if __name__ == "__main__" :
    menu_actif : bool
    menu_actif = True
    choix : int

    creation_joueurs()
    while menu_actif :
        afficher_menu()
        choix = saisir_choix()
        if choix == 1 :
            jeu_devinette(j1, j2)
        elif choix == 2 :
            jeu_allumettes(j1, j2)
        elif choix == 3 :
            jeu_morpion(j1, j2)
        elif choix == 4 :
            jeu_puissance4(j1, j2)
        elif choix == 5 :
            print(f"\033[2J")
            print("Au revoir !")
            menu_actif = False
        else :
            print(f"\033[2J")
            print("Veuillez entrer un nombre valide.")