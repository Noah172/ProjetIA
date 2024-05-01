from Etat import *
import sys
import io

def pop(liste):
    return liste.pop(0)

def ajouterTete(e, liste):
    liste.insert(0, e)

def taille(liste):
    return len(liste)

def afficher_liste_etat(liste):
    print("\nFils d'un Etats : \n")
    line_buffer = []
    for i, etat in enumerate(liste):
        old_stdout = sys.stdout
        sys.stdout = mystdout = io.StringIO()
        
        afficher(etat)
        
        sys.stdout = old_stdout
        state_output = mystdout.getvalue()
        line_buffer.append(state_output.strip().split('\n'))
        
        max_lines = max(len(lines) for lines in line_buffer)
        for lines in line_buffer:
            while len(lines) < max_lines:
                lines.append('') 
        
        if (i + 1) % 3 == 0 or i == len(liste) - 1:
            for lines in zip(*line_buffer):
                print(' '.join(f"{line:<13}" for line in lines))
            
            line_buffer = [] 