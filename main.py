from Liste import *
from Etat import *
import time


def Profondeur_dabord(etat_initial, but):
    enAttente=[etat_initial]
    vus=[]
    trouve=False
    while enAttente:
        print(enAttente)
        print(taille(enAttente))
        actuel=enAttente.pop(0)
        vus.append(actuel)
        if actuel==but:
            trouve=True
            return (True,actuel)
        else:
            for etat_fils in actuel.filsEtat():
                if etat_fils not in vus:
                    ajouterTete(etat_fils, enAttente)
    if not trouve:
        return (False,etat_initial)

print("Début du test de la recherche en profondeur d'abord bornée...")

etat_debut =[[0, 0, 0, 6],
     [5, 9, 0, 7],
     [1, 3, 0, 3]]


etat_but = [[6, 2, 0, 0],
     [2, 1, 0, 2],
     [1, 3, 0, 3]]

afficher(etat_debut)


liste_fils = fils_etat(etat_debut)
afficher_liste_etat(liste_fils)

"""
trouve, etat_final = Profondeur_dabord(etat_debut, etat_but)

if trouve:
    print("Trouvé ")
else:
    print("Aucun état but n'a été trouvé.")

print("État initial:")
etat_debut.afficher()

print("État atteint:")
etat_final.afficher()

print("État but:")
etat_but.afficher()

"""

"""
. 2 . 1
2 1 . 2
1 3 . 3

Fils d'un Etats

. 2 . .
2 1 . 2
1 3 1 3

. . . 1
2 1 . 2
1 3 2 3

. 2 . 1
. 1 . 2
1 3 2 3

2 . . 1
2 1 . 2
1 3 . 3

1 2 . .
2 1 . 2
1 3 . 3

"""