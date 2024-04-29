


def filsEtat(etat):
    fils = []
    for i, tige in enumerate(etat.configuration):
        if tige: 
            cube = tige[-1] 
            for j, cible in enumerate(etat.configuration):
                if j != i and len(cible) < 3: 
                    nouvel_etat = [list(t) for t in etat.configuration] 
                    nouvel_etat[i].remove(cube) 
                    nouvel_etat[j].append(cube) 
                    fils.append(Etat(nouvel_etat))  
    return fils
