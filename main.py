from Liste import *
from Etat import *
from matrice_tests import *

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


def Profondeur_dabord_bornee(etat_initial, but, limite):
    enAttente = [(etat_initial, 0)]
    vus = []
    trouve = False
    while enAttente:
        actuel, profondeur = enAttente.pop(0)
        vus.append(actuel)
        if est_but(actuel, but):
            trouve = True
            return (True, actuel)
        if profondeur < limite:
            for etat_fils in fils_etat(actuel):
                if not any(np.array_equal(etat_fils, vu) for vu in vus):
                    ajouterTete((etat_fils, profondeur + 1), enAttente)
    if not trouve:
        return (False, etat_initial)


################################ETAPE 3##################################




def ProfondeurBornee(seuil, depart, but):
    solution=None
    iteration = 0
    profondeur = 0
    nbcree = 0
    nbDev = 0
    nSeuil = float('inf')
    vus = []
    enAttente = [depart]
    
    while enAttente:
        prochain = enAttente.pop(0)
        vus.append(prochain)
        if est_but(prochain, but):
            solution = prochain
            print("TRUE")
            print("nbDevelopees =", nbDev)
            print("nbcree = ", nbcree)
            print("iteration =", iteration)
            return True, -1,solution
        else:
            iteration += 1
            for elem in fils_etat(prochain):
                
                nbcree += 1
                if fEtat(elem, but,profondeur) <= seuil and not dans_vus(vus, elem):
                    nbDev += 1
                    enAttente.insert(0, elem)
                else:
                    nSeuil = min(nSeuil, fEtat(elem, but,profondeur))
    
    print("nouveau seuil =", nSeuil)
    return False, nSeuil,solution if nSeuil != float('inf') else True, -1,solution


def IDA_star(init, but):
    solution = None
    seuil = fEtat(init, but,0)
    termine = False, -2
    
    while not termine[0]:
        print("Seuil actuel:", seuil)
        termine = ProfondeurBornee(seuil, init, but)
        if termine[1]==seuil:
            print("Probleme de SEUIL, ARRET")
            return False
        seuil = termine[1]  
        if termine[1] == -1:
            solution = termine[2]
            break
        
    
    return solution if solution.size > 0 else False


    

def run_tests_profondeur():
    print("Début du test de la recherche en profondeur d'abord bornée...")

    print("\nEtat Debut || Etat But :")
    resultat = Profondeur_dabord_bornee(etat_debut, etat_but, 4)
    print(resultat[0])
    afficher(resultat[1])

    print("\nEtat initial 1 || Etat But 1 :")
    resultat = Profondeur_dabord_bornee(init1, but1, 4)
    print(resultat[0])
    afficher(resultat[1])

    

def run_tests():
    print("\nEtat initial 1 || Etat But 1 :")
    IDA_star(init1, but1)
    print("\nEtat initial 1 || Etat But 2 :")
    IDA_star(init1, but2)
    print("\nEtat initial 2 || Etat But 3 :")
    IDA_star(init2, but3)
    print("\nEtat initial 2 || Etat But 4 :")
    IDA_star(init2, but4)
    print("\nEtat initial 2 || Etat But 5 :")
    IDA_star(init2, but5)
    print("\nEtat initial 2 || Etat But 6 :")
    IDA_star(init2, but6)
    
run_tests_profondeur()
run_tests()
