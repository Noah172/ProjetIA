from Liste import *
from Etat import *
import time

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


################################ETAPE 3##################################

testEtatBut=None
filsEtat=None
fEtat=None
solution=None



def nombreMalMis(etat, but):
    mal_mis=0
    for i in range(3):
        for j in range(4):
            if etat[i][j]!=but[i][j]:
                mal_mis=mal_mis+1
    return mal_mis


def fEtat(etat,but, g):
    return g + h(etat,but)


def h(etat, but):
    return nombreMalMis(etat,but)

def IDA_star():
    g=0
    solution = None
    seuil = h(etat_debut,etat_but)
    terminé=False
    while not terminé:
        terminé,seuil,solution = ProfondeurBornee(seuil,g)
    if solution.size > 0:
        return solution
    else:
        return("Echec")

def ProfondeurBornee(s,g):
    nSeuil = float('inf')
    vus=[]
    enAttente=[etat_debut]

    while enAttente:
        prochain=enAttente.pop(0)
        vus.append(prochain)
        if est_but(prochain,etat_but):
            print("SOLUTION TROUVE")
            solution=prochain
            return True, s, solution
        else:
            for e in fils_etat(prochain):
                cout_fils = fEtat(e, etat_but,g) 
                print(cout_fils)
                if cout_fils <= s and not any(np.array_equal(e, vu) for vu in vus):
                    enAttente.insert(0, e)
                    g+=1
                else:
                    nSeuil = min(nSeuil, cout_fils)
    if nSeuil == float('inf'):
        return True,seuil,None
    else:
        seuil=nSeuil
        return False,seuil,None









etat_debut =[[0, 0, 0, 6],
     [5, 9, 0, 7],
     [1, 3, 0, 3]]


etat_but =[[6, 0, 0, 0],
     [5, 9, 0, 0],
     [1, 3, 7, 3]]






print("ETAT DEBUT : ")
afficher(etat_debut)
print("ETAT FINAL : ")
afficher(etat_but)

print("Début du test de la recherche en profondeur d'abord bornée...")
print(Profondeur_dabord_bornee(etat_debut,etat_but,2))

print("Début du test IDA...")
print(IDA_star())