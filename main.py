"""def test_etat_but(etat):
    return etat==sorted(etat)

def fils_etat(etat):
    fils=[]
    for i in range(len(etat) - 1):
        etat_fils = etat[:] 
        etat_fils[i],etat_fils[i+1] = etat_fils[i+1], etat_fils[i] 
        fils.append(etat_fils)
    return fils

def pop(liste):
    return liste.pop()

def ajouterTete(e, liste):
    return liste.append(e)*)
"""

from liste import Liste
from etat import Etat


def Profondeur_dabord(etat_initial, but):
    enAttente=[etat_initial]
    vus=[]
    trouve=False
    while enAttente:
        actuel=enAttente.pop()
        vus.append(actuel)
        if actuel==but:
            trouve=True
            return (True,actuel)
        else:
            for etat_fils in actuel.filsEtat():
                if etat_fils not in vus:
                    enAttente.ajouterTete(0,etat_fils)
    if not trouve:
        return (False,etat_initial)

etat_debut=Etat(
    [[0,2,0,1],
     [2,1,0,2],
     [1,3,0,3]]
)

etat_but=Etat(
    [[1,2,0,0],
     [2,1,0,2],
     [1,3,0,3]]
)

""""
etat_initial = [3, 1, 2]
trouve, etat_final = profondeur_d_abord(etat_initial, test_etat_but, fils_etat)
print("État initial:", etat_initial)
print("État but:", etat_final)
print("fils etat",fils_etat(etat_initial))
print("inserer 6: ", ajouterTete(6,etat_initial))
"""
