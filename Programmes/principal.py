#import devinette as dev
import allumette as all
#import morpion as mor
#import puissance4 as pui
import global_var as g

def Menu_principal() :
    choix : int
    print("1. Devinette")
    print("2. Allumettes")
    print("3. Morpion")
    print("4. Puissance 4")
    print("5. Création de joueurs")
    print ("6. Quitter")
    choix = int(input("Veuillez saisir votre choix : "))
    return choix

if __name__ == "__main__" :
    menu_actif : bool
    menu_actif = True
    allumette : list[int]

    while menu_actif :
        choix = Menu_principal()
        if choix == 1 :
            if g.nb_j_valide :
                pass
            else :
                print("Pas assez de joueurs")
        elif choix == 2 :
            if g.nb_j_valide :
                g.début_de_partie()
                allumette = all.creation_plateau(all.liste_allumettes)
                g.j1.score = 1
                g.j2.score = 1
                while not all.fin_partie :
                    print("Tour : ", g.tour, "(",g.qui_joue,")")
                    if g.qui_joue == 1 :
                        all.coups(allumette, g.j1)
                    else :
                        all.coups(allumette, g.j2)
                if g.j1.score == 0 : # type: ignore (pour ignorer un warning)
                    print(g.j2.pseudo," a gagné la partie en ", g.tour," tours !")
                else :
                    print(g.j1.pseudo," a gagné la partie en ", g.tour," tours !")
            else :
                print("Pas assez de joueurs")
        elif choix == 3 :
            if g.nb_j_valide :
                pass
            else :
                print("Pas assez de joueurs")
        elif choix == 4 :
            if g.nb_j_valide :
                pass
            else :
                print("Pas assez de joueurs")
        elif choix == 5 :
            g.Creation_joueurs()
        elif choix == 6 :
            print("Au revoir !")
            menu_actif = False