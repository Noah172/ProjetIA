def profondeurDAbord(depart):
    def testEtatBut(etat):
        # Votre logique pour vérifier si 'etat' est un état but
        pass

    def filsEtat(etat):
        # Votre logique pour générer et retourner tous les fils de 'etat'
        pass

    def pop(liste):
        return liste.pop(0)

    def ajouterTete(e, liste):
        liste.insert(0, e)

    enAttente=[depart]
    vus=[]
    trouve=False

    while enAttente and not trouve:
        prochain=pop(enAttente)
        vus.append(prochain)
        if testEtatBut(prochain):
            trouve=True
            return True, prochain
        else:
            for e in filsEtat(prochain):
                if e not in vus:
                    ajouterTete(e, enAttente)
    return False, depart
