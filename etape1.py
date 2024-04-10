def profondeur_d_abord(depart, test_etat_but, fils_etat):
    en_attente = [depart]  # Pile des états à explorer (LIFO)
    vus = set()  # Ensemble des états déjà explorés

    while en_attente:  # Tant que la pile n'est pas vide
        prochain = en_attente.pop()  # Retire le dernier élément ajouté à la pile
        prochain_tuple = tuple(prochain)  # Convertit la liste en tuple pour la rendre hashable

        if prochain_tuple in vus:
            continue
        vus.add(prochain_tuple)  # Ajoute l'état actuel (sous forme de tuple) aux états déjà vus

        if test_etat_but(prochain):
            return True, prochain  # Retourne vrai et l'état but si trouvé

        for e in fils_etat(prochain):
            if tuple(e) not in vus:
                en_attente.append(e)  # Ajoute les fils non explorés à la pile

    return False, depart  # Retourne faux et l'état initial si aucun but n'est atteint

def test_etat_but(etat):
    # Vérifie si la liste des chiffres est triée
    return etat == sorted(etat)

def fils_etat(etat):
    fils = []
    for i in range(len(etat) - 1):
        etat_fils = etat[:]  # Crée une copie de l'état actuel
        etat_fils[i], etat_fils[i+1] = etat_fils[i+1], etat_fils[i]  # Echange les chiffres à la position i et i+1
        fils.append(etat_fils)
    return fils

# Exemple d'utilisation
etat_initial = [3, 1, 2]
trouve, etat_final = profondeur_d_abord(etat_initial, test_etat_but, fils_etat)
if trouve:
    print("État but atteint :", etat_final)
else:
    print("État but non atteint à partir de l'état initial :", etat_initial)
