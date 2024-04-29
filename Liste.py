from Etat import Etat


def pop(liste):
    return liste.pop(0)

def ajouterTete(e, liste):
    liste.insert(0, e)

def taille(liste):
    return len(liste)

def afficher_liste_etat(liste):
    print("\nFils d'un Etats : \n")
    for etat in liste:
        etat.afficher()
        print("\n")