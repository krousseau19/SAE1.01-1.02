import global_var as g

liste_allumettes : list[int]
positions : str
liste_pos : list[str]
fin_partie : bool

liste_allumettes = []
liste_pos = []

def creation_plateau(liste_allumettes: list[int]) -> list[int] :
    liste_allumettes = []
    for i in range(1,21):
        liste_allumettes.append(i)
    g.tour = 1        
    print(liste_allumettes)
    return liste_allumettes

fin_partie = False

def coups(liste_allumettes : list[int], j:g.Joueur):
    global fin_partie
    global liste_pos
    i : str
    all : int
    compteur : int
    choix_valide : bool
    compteur = 0
    choix_valide = False
    if not fin_partie :
        while  not choix_valide :
            positions = input("Saisir les allumettes à retirer (séparées par des virgules, avec 3 max) : ")
            liste_pos = positions.split(',')
            choix_valide = True
            for i in liste_pos :
                try :
                    int(i)
                    if (int(i)<1 or int(i)>20) :
                        choix_valide = False
                    elif liste_allumettes[int(i)-1] == 0 :
                        choix_valide = False
                except :
                    choix_valide = False
            if len(liste_pos) > 3 or len(liste_pos) < 1 :
                        choix_valide = False
            if not choix_valide :
                print("Choix invalide")
            print(liste_pos)
        
        
        if choix_valide :
            for i in liste_pos:
                liste_allumettes[int(i)-1] = 0      
            g.tour +=1
            if g.qui_joue == 1 :
                g.qui_joue = 2
            else :
                g.qui_joue = 1
            print(liste_allumettes)
        for all in liste_allumettes :
            if all != 0 :
                compteur += 1
        if compteur == 0 :
            fin_partie = True
            j.score = 0
            j.nb_partiesG += 1


