from Liste import *
from Etat import *
import time

"""
def Profondeur_dabord(etat_initial, but):
    enAttente=[etat_initial]
    vus=[]
    trouve=False
    while enAttente:
        actuel=enAttente.pop(0)
        vus.append(actuel)
        if est_but(actuel,but):
            trouve=True
            return (True,actuel)
        else:
            for etat_fils in fils_etat(actuel):
                print(etat_fils)
                print(vus)
                if not any(np.array_equal(etat_fils, vu) for vu in vus):
                    ajouterTete(etat_fils, enAttente)
    if not trouve:
        return (False,etat_initial)
"""

def Profondeur_dabord_bornee(etat_initial, but,limite):
    enAttente = [(etat_initial, 0)]
    vus=[]
    trouve=False
    while enAttente:
        actuel,profondeur=enAttente.pop(0)
        vus.append(actuel)
        if est_but(actuel,but):
            trouve=True
            return (True,actuel)
        if profondeur< limite:
            for etat_fils in fils_etat(actuel):
                if not any(np.array_equal(etat_fils, vu) for vu in vus):
                    ajouterTete((etat_fils, profondeur + 1), enAttente)
    if not trouve:
        return (False,etat_initial)

etat_debut =[[0, 0, 0, 6],
     [5, 9, 0, 7],
     [1, 3, 0, 3]]


etat_but = [[0, 0, 0, 0],
     [0, 9, 5, 7],
     [1, 3, 6, 3]]


print("ETAT DEBUT : ")
afficher(etat_debut)
print("ETAT FINAL : ")
afficher(etat_but)

print("Début du test de la recherche en profondeur d'abord bornée...")
print(Profondeur_dabord_bornee(etat_debut,etat_but,2))
