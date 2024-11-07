import global_var as g

liste_allumettes : list[int]
positions : str
liste_pos : list[str]
fin_partie : bool

liste_allumettes = []

def creation_plateau(liste_allumettes: list[int]) -> list[int] :
    liste_allumettes = []
    for i in range(1,21):
        liste_allumettes.append(i)
    g.tour = 0        
    print(liste_allumettes)
    return liste_allumettes

fin_partie = False

def coups(liste_allumettes : list[int], j:g.Joueur):
    global fin_partie
    i : str
    all : int
    compteur : int
    compteur = 0
    fin_partie = False
    if not fin_partie :
        positions = input("Saisir les allumettes à retirer (séparées par des virgules, avec 3 max) : ")
        liste_pos = positions.split(',')
        print(liste_pos)
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


