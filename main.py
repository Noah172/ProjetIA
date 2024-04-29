def test_etat_but(etat):
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
    return liste.append(e)


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
print("État initial:", etat_initial)
print("État but:", etat_final)
print("fils etat",fils_etat(etat_initial))
print("inserer 6: ", ajouterTete(6,etat_initial))
