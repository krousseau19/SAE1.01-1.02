from devinette import devine_nombre
from allumette import jeu_allumettes
#from morpion import
#from puissance4 import
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
            devine_nombre(j1, j2)
        elif choix == 2 :
            jeu_allumettes(j1, j2)
        elif choix == 3 :
            pass
        elif choix == 4 :
            pass
        elif choix == 5 :
            print("Au revoir !")
            menu_actif = False
        else :
            print(f"\033[2J")
            print("Veuillez entrer un nombre valide.")