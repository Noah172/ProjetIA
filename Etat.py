class Etat:
    def __init__(self, configuration):
        self.configuration = configuration

    def estPleine(self,ligne):
        for i in range (1,3):
            if ligne[i] == 0:
                return False
        return True
    
    def estVide(self,ligne):
        for i in range (1,3):
            if ligne[i] != 0:
                return False
        return True
    
    def memeTige(self, ligne1, ligne2):
        return ligne1 == ligne2

    def top_tige(self, ligne, colonne):
        if self.configuration[ligne][colonne] == 0:
            return False
        if (ligne == 0):
            return True
        if self.configuration[ligne-1][colonne] == 0:
            return True
        return False
    
    def trouverDestination(self, tige):
        retour= []
        for i in range(len(self.configuration)):
            ligne = self.configuration[i]
            if(not self.estPleine(ligne) and not self.memeTige(ligne, tige)):
                retour.append(i)
        return retour
    
    def sommet(self, tige):
        i = 0
        if tige[0] != 0:
            return i
        else:
            i = 0
            while tige[i] == 0:
                if i == len(tige) - 1:
                    return i
                i += 1
            return i
        
    def indiceLigne(self, ligne):
        for i in range(len(self.configuration)):
            if self.configuration[i] == ligne:
                return i

    def deplacer(self, tige1, tige2):
        retour = [list(ligne) for ligne in self.configuration]
        indLigneT1 = self.indiceLigne(tige1)
        indLigneT2 = self.indiceLigne(tige2)
        sommetT1 = self.sommet(tige1)
        sommetT2 = self.sommet(tige2)
        if not self.estVide(retour[indLigneT2]):
            retour[indLigneT2][sommetT2-1] = tige1[sommetT1]
        else:
            retour[indLigneT2][sommetT2] = tige1[sommetT1]
        retour[indLigneT1][sommetT1] = 0
        return retour

    def filsEtat(self):
        retour = []
        for ligne in self.configuration:
            lst = self.trouverDestination(ligne)
            for elem in lst:
                retour.append(self.deplacer(ligne, self.configuration[elem]))
        return retour
    
    def estBut(self, etat_but):
        for i in range(len(self.configuration)):
            for j in range(len(self.configuration[i])):
                if self.configuration[i][j] != etat_but.configuration[i][j]:
                    return False
        return True
    
    def afficher(self):
        for ligne in self.configuration:
            print('|'.join(str(cube) if cube != 0 else ' ' for cube in ligne))
