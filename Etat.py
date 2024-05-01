import numpy as np

etat = []

def cubes_dans_tige(etat, numero_tige):
    return [ligne[numero_tige] for ligne in etat]


def est_pleine(ligne):
    for elem in ligne:
        if elem == 0:
            return False
    return True


def meme_tige(ligne1, ligne2):
    return ligne1 == ligne2

def top_tige(ligne, colonne):
    if ligne[colonne] == 0:
        return False
    return ligne == 0 or ligne[colonne-1] == 0

def trouver_destination(etat,ntige):
    retour= []
    for i in range(len(etat)):
        tige = [ligne[i] for ligne in etat]
        if (i != ntige) and (not est_pleine(tige)):
            retour.append(i)
    return retour

def sommet(tige):
    x=0
    for i in tige:
        if i != 0:
            return x
        x=x+1
    return 0

def indiceLigne(etat, tige):
    for i in range(len(etat)+1):
        if np.array_equal([ligne[i] for ligne in etat], tige):
            return i


def estVide(etat, indice):
    return np.all(np.array([ligne[indice] for ligne in etat]) == 0)


def deplacer(etat, tige1, tige2):
    retour = np.copy(etat)
    indLigneT1 = indiceLigne(retour, tige1)
    indLigneT2 = indiceLigne(retour, tige2)
    sommetT1 = sommet(tige1)
    sommetT2 = sommet(tige2)
    if not estVide(retour, indLigneT2):
        retour[sommetT2-1][indLigneT2] = retour[sommetT1][indLigneT1]
    else:
        retour[2][indLigneT2] = retour[sommetT1][indLigneT1]
    retour[sommetT1][indLigneT1] = 0
    return retour


def fils_etat(etat):
    retour = []
    for i in range (4):
        ligne = [ligne[i] for ligne in etat]  
        lst = trouver_destination(etat, i)
        for elem in lst:
            tige_deplacement= [ligne[elem] for ligne in etat]
            nouveau_etat = deplacer(etat, ligne, tige_deplacement)
            if not est_but(etat,nouveau_etat):
                retour.append(nouveau_etat)
    return retour

def est_but(etat, etat_but):
    return all(etat[i][j] == etat_but[i][j] for i in range(len(etat)) for j in range(len(etat[i])))

def afficher(etat):
    bold_start = "\033[1m"
    bold_end = "\033[0m"
    print(bold_start)
    for ligne in etat:
        print('|' + '|'.join(str(cube) if cube != 0 else ' ' for cube in ligne) + '|')
    print(bold_end)
