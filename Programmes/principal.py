from devinette import jeu_devinette
from allumette import jeu_allumettes
from morpion import jeu_morpion
from puissance4 import jeu_puissance4
from global_var import creation_joueurs, afficher_menu, saisir_choix, j1, j2, afficher_stats, f, sauvegarder_joueur, afficher_leaderboard

if __name__ == "__main__" :
    menu_actif : bool
    menu_stats_actif : bool
    choix : int
    sous_choix : int

    menu_actif = True
    creation_joueurs()
    while menu_actif :
        afficher_menu()
        choix = saisir_choix()
        if choix == 1 :
            jeu_devinette(j1, j2)
            sauvegarder_joueur(f, j1)
            sauvegarder_joueur(f, j2)
        elif choix == 2 :
            jeu_allumettes(j1, j2)
            sauvegarder_joueur(f, j1)
            sauvegarder_joueur(f, j2)
        elif choix == 3 :
            jeu_morpion(j1, j2)
            sauvegarder_joueur(f, j1)
            sauvegarder_joueur(f, j2)
        elif choix == 4 :
            jeu_puissance4(j1, j2)
            sauvegarder_joueur(f, j1)
            sauvegarder_joueur(f, j2)
        elif choix == 5 :
            menu_stats_actif = True
            print("\033c")
            while menu_stats_actif :
                print("    === Statistiques ===")
                print("1 - LeaderBoard")
                print("2 - Infos sur les joueurs")
                print("3 - Quitter les Statistiques")
                sous_choix = saisir_choix()
                if sous_choix == 1 :
                    sous_choix = -1
                    print("\033c")
                    while sous_choix != 5 :
                        print("    === LeaderBoard ===")
                        print("1 - Devinettes")
                        print("2 - Allumettes")
                        print("3 - Morpion")
                        print("4 - Puissance 4")
                        print("5 - Quitter le LeaderBoard")
                        sous_choix = int(input("Le leaderboard de quel jeu voulez-vous consulter ? : "))
                        if sous_choix == 1 :
                            print("\033c")
                            afficher_leaderboard(f, "Devinette")
                        elif sous_choix == 2 :
                            print("\033c")
                            afficher_leaderboard(f, "Allumette")
                        elif sous_choix == 3 :
                            print("\033c")
                            afficher_leaderboard(f, "Morpion")
                        elif sous_choix == 4 :
                            print("\033c")
                            afficher_leaderboard(f, "Puissance 4")
                        elif sous_choix == 5 :
                            print("\033c")
                        else :
                            print("\033c")
                            print("Choix invalide.")
                elif sous_choix == 2 :
                    print("\033c")
                    afficher_stats(f, j1, j2)
                elif sous_choix == 3 :
                    print("\033c")
                    menu_stats_actif = False
                else :
                    print("\033c")
                    print("Choix invalide.")
        elif choix == 6 :
            print("\033c")
            print("Au revoir !")
            menu_actif = False
        else :
            print("\033c")
            print("Choix invalide.")