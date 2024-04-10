def test_etat_but(etat):
    return etat==sorted(etat)

def fils_etat(etat):
    return [etat[:i] + [etat[i+1], etat[i]] + etat[i+2:] for i in range(len(etat) - 1)]


def profondeur_d_abord(depart, test_etat_but, fils_etat):
    en_attente = [depart]  
    vus = set()  
    
    while en_attente: 
        prochain = en_attente.pop()
        prochain_tuple = tuple(prochain) 

        if prochain_tuple in vus:
            continue
        vus.add(prochain_tuple)  

        if test_etat_but(prochain):
            return True, prochain  

        for e in fils_etat(prochain):
            if tuple(e) not in vus:
                en_attente.append(e)  

    return False, depart  



etat_initial = [3, 1, 2]
trouve, etat_final = profondeur_d_abord(etat_initial, test_etat_but, fils_etat)
print("État but:", etat_final)
print("fils etat",fils_etat(etat_initial))

