# Fichier assemblant les différents modules et leur fonctions respectives pour permettre à l'application d'être éxécutée correctement
from devinette import jeu_devinette, saisir_intervalle
from allumette import jeu_allumettes
from morpion import jeu_morpion
from puissance4 import jeu_puissance4
from ressource import creation_joueurs, afficher_menu, saisir_choix, j1, j2, afficher_stats, f, sauvegarder_joueur, afficher_leaderboard, Joueur, mode_jeu, choix_difficulté

def restart(jeu : str, j1 : Joueur, j2 : Joueur, mode : int, diff : int) -> bool :
    """
    Entrée : 3 arguments, une chaîne de caractère correspondant au jeu, et 2 joueurs

    Sortie : Un booléen (pour savoir si les joueurs veulent rejouer ou non)

    Fonctionnement : La fonction affiche un menu en continue et demande si le joueur veut refaire une partie ou non,
    si la réponse est oui, la fonction lance le jeu passé en paramètre, et renvoie True, sinon elle ramène au menu principal
    et renvoie False
    """
    choix : int
    intervalle = int

    choix = -1
    restart = False
    while choix != 1 and choix != 2 :
        print("Voulez vous refaire une partie ?")
        print("1 - Oui")
        print("2 - Non")
        choix = saisir_choix()
        if choix == 1 :
            input("Une nouvelle partie va commencer, veuillez appuyer sur ENTRER...")
            if jeu == "Allumette" :
                jeu_allumettes(j1, j2, mode, diff)
            elif jeu == "Morpion" :
                jeu_morpion(j1, j2, mode, diff)
            elif jeu == "Puissance4" :
                jeu_puissance4(j1, j2, mode, diff)
            else :
                intervalle = saisir_intervalle()
                jeu_devinette(j1, j2, intervalle, mode, diff)
            restart = True
        elif choix == 2 :
            input("Veuillez appuyer sur ENTRER pour revenir au menu principal...")
        else :
            print("\x1b[31mErreur : Choix invalide\x1b[0m")
    if choix == 2 :
        print("\033c")    
    return restart

#Programme principal de l'application (Menu et lancement des jeux)
if __name__ == "__main__" :
    menu_actif : bool
    menu_stats_actif : bool
    choix : int
    sous_choix : int
    intervalle : int
    rejoue : bool
    mode : int

    menu_actif = True
    rejoue = True

    diff = 0
    mode = mode_jeu()
    if mode != 1 :
        diff = choix_difficulté()
    creation_joueurs(j1, j2, f, mode)
    while menu_actif :
        afficher_menu()
        choix = saisir_choix()
        if choix == 1 :
            rejoue = True
            intervalle = saisir_intervalle()
            jeu_devinette(j1, j2, intervalle, mode, diff)
            if mode == 1 or mode == 2 :
                sauvegarder_joueur(f, j1)
            if mode == 1 :
                sauvegarder_joueur(f, j2)
            while rejoue :
                rejoue = restart("Devinette", j1, j2, mode, diff)
                if mode == 1 or mode == 2 :
                    sauvegarder_joueur(f, j1)
                if mode == 1 :
                    sauvegarder_joueur(f, j2)
        elif choix == 2 :
            rejoue = True
            jeu_allumettes(j1, j2, mode, diff)
            if mode == 1 or mode == 2 :
                sauvegarder_joueur(f, j1)
            if mode == 1 :
                sauvegarder_joueur(f, j2)
            while rejoue :
                rejoue = restart("Allumette", j1, j2, mode, diff)
                if mode == 1 or mode == 2 :
                    sauvegarder_joueur(f, j1)
                if mode == 1 :
                    sauvegarder_joueur(f, j2)
        elif choix == 3 :
            rejoue = True
            jeu_morpion(j1, j2, mode, diff)
            if mode == 1 or mode == 2 :
                sauvegarder_joueur(f, j1)
            if mode == 1 :
                sauvegarder_joueur(f, j2)
            while rejoue :
                rejoue = restart("Morpion", j1, j2, mode, diff)
                if mode == 1 or mode == 2 :
                    sauvegarder_joueur(f, j1)
                if mode == 1 :
                    sauvegarder_joueur(f, j2)
        elif choix == 4 :
            rejoue = True
            jeu_puissance4(j1, j2, mode, diff)
            if mode == 1 or mode == 2 :
                sauvegarder_joueur(f, j1)
            if mode == 1 :
                sauvegarder_joueur(f, j2)
            while rejoue :
                rejoue = restart("Puissance4", j1, j2, mode, diff)
                if mode == 1 or mode == 2 :
                    sauvegarder_joueur(f, j1)
                if mode == 1 :
                    sauvegarder_joueur(f, j2)
        elif choix == 5 :
            menu_stats_actif = True
            while menu_stats_actif :
                print("    === Statistiques ===")
                print("1 - LeaderBoard")
                print("2 - Infos sur les joueurs")
                print("3 - Quitter les Statistiques")
                sous_choix = saisir_choix()
                if sous_choix == 1 :
                    sous_choix = -1
                    while sous_choix != 5 :
                        print("    === LeaderBoard ===")
                        print("1 - Devinettes")
                        print("2 - Allumettes")
                        print("3 - Morpion")
                        print("4 - Puissance 4")
                        print("5 - Quitter le LeaderBoard")
                        sous_choix = saisir_choix()
                        if sous_choix == 1 :
                            afficher_leaderboard(f, "Devinette")
                        elif sous_choix == 2 :
                            afficher_leaderboard(f, "Allumette")
                        elif sous_choix == 3 :
                            afficher_leaderboard(f, "Morpion")
                        elif sous_choix == 4 :
                            afficher_leaderboard(f, "Puissance 4")
                        elif sous_choix == 5 :
                            print("\033c")
                        else :
                            print("\x1b[31mErreur : Choix invalide.\x1b[0m")
                elif sous_choix == 2 :
                    afficher_stats(f, j1, j2)
                elif sous_choix == 3 :
                    print("\033c")
                    menu_stats_actif = False
                else :
                    print("\x1b[31mErreur : Choix invalide.\x1b[0m")
        elif choix == 6 :
            print("Au revoir !")
            menu_actif = False
        else :
            print("\x1b[31mErreur : Choix invalide.\x1b[0m")