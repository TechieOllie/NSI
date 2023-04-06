# -*- coding: utf-8 -*-


## Import des modules
import random as r
import matplotlib.pyplot as plt
import time as t

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
    return t



def trace(x, y, legende):
    """fonction qui trace un graphique avec X en abscisses et Y en ordonnées"""
    plt.plot(x, y, label=legende)
    plt.legend()
    plt.show()
    
    
def temps_execution():
    """fonction qui donne le temps d'exécution de la fonction comprise entre
    deux variables : debut et fin
    
    Entrée : aucune
    Sortie : temps, un réel
    """
    debut = t.time()
    remplissage_aleatoire(100)
    fin = t.time()
    temps = debut - fin
    return temps
 



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
    liste_temps = 100*[0]
    liste_n = list(range(1, 101))
    for i in range(1, 101, 1):
        liste = remplissage_aleatoire(i)
        debut = t.time()
        moyenne_liste(liste)
        fin = t.time()
        liste_temps[i-1]= fin-debut
    trace(liste_n, liste_temps, "moyenne")
    


def recherche(liste, x):
    """fonction qui renvoie le plus petit indice tel que liste[i] = x.
    
    Entrée : 
        liste : une liste de nombres
        x : un entier
    
    Sortie : indice : un entier
    
    Exemples d'exécution :

    """

    for i in range(1, len(liste)):
        if list[i] == x:
            return i
        else:
            return -1

def trace_temps_recherche():
    """fonction qui trace le temps d'exécution de la fonction recherche(liste, x)"""
    liste = list(range(1, 101))
    liste_temps = 100 * [0]
    for i in range(1, 101, 1):
        x = r.randint(1, 101)
        debut = t.time()
        recherche(liste, x)
        fin = t.time()
        liste_temps[i-1]= fin - debut
    trace(liste, liste_temps, "recherche")
    

def extremum(liste):
    """fonction qui renvoie le plus petit indice tel que liste[i] = x.
    
    Entrée : liste : une liste de nombres    
    Sortie : maximum, minimum : des nombres
    
    Exemples d'exécution :
    
    >>> extremum(0)
    
    
    """
    smallest = min(liste)
    largest = max(liste)
    return smallest, largest


def trace_temps_extremum():
    """fonction qui trace le temps d'exécution de la fonction extremum(liste)"""
    liste_temps = 100*[0]
    liste_ex = 100*[0]
    for i in range(1, 101, 1):
        liste = remplissage_aleatoire(i)
        debut = t.time()
        liste_ex[i-1] = extremum(liste)
        fin = t.time()
        liste_temps[i-1] = fin - debut
    trace(liste_ex, liste_temps, "extremum")





## Test des fonctions
if __name__ == "__main__":
    trace_temps_extremum()
    # import doctest
    # doctest.testmod()
    # docs ici: https://www.fil.univ-lille1.fr/~L1S2API/CoursTP/tp_doctest.html

