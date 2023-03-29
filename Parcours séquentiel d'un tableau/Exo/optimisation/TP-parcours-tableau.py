# -*- coding: utf-8 -*-


## Import des modules
import random as r

## Constantes
abscisses = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
ordonnees = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]


## Fonctions

def remplissage_aleatoire(n):
    """fonction générant un tableau de longueur n, et contenant
    un entier aléatoire contenu entre 1 et 100

    Entrée : n, un entier
    Sortie : t, un tableau d'entiers
    
    Postcondition :

    """
    t = []
    for i in range(n):
        t.append(r.randint(1, 100))
    print(t)



def trace(x, y, legende):
    """fonction qui trace un graphique avec X en abscisses et Y en ordonnées"""
    
    
def temps_execution():
    """fonction qui donne le temps d'exécution de la fonction comprise entre
    deux variables : debut et fin
    
    Entrée : aucune
    Sortie : temps, un réel
    """
    
 



def moyenne_liste(liste):
    """fonction qui calcule la moyenne de tous les éléments d'une liste

    Entrée : liste : une liste de nombres
    Sortie : moyenne : un réel

    Exemples d'exécution :

    """
    
    somme = 0
    for element in liste :
            somme = somme + element
    moyenne = somme / len(liste)
    return moyenne


def trace_temps_moyenne():
    """fonction qui trace le temps d'exécution de la fonction moyenne_liste()"""
    
    


def recherche(liste, x):
    """fonction qui renvoie le plus petit indice tel que liste[i] = x.
    
    Entrée : 
        liste : une liste de nombres
        x : un entier
    
    Sortie : indice : un entier
    
    Exemples d'exécution :

    """


def trace_temps_recherche():
    """fonction qui trace le temps d'exécution de la fonction recherche(liste, x)"""
    

def extremum(liste):
    """fonction qui renvoie le plus petit indice tel que liste[i] = x.
    
    Entrée : liste : une liste de nombres    
    Sortie : maximum, minimum : des nombres
    
    Exemples d'exécution :
    
    >>> extremum(0)
    
    
    """


def trace_temps_extremum():
    """fonction qui trace le temps d'exécution de la fonction extremum(liste)"""
    




## Test des fonctions
if __name__ == "__main__":
    # import doctest
    # doctest.testmod()
    remplissage_aleatoire(1000)
    # docs ici: https://www.fil.univ-lille1.fr/~L1S2API/CoursTP/tp_doctest.html

