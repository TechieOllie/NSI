tableau = [45, 21, 56, 12, 1, 8]
def moyennetableau():
    moyenne = 0
    for element in tableau:
        moyenne += element
        print(moyenne)
    print("\nrésultat final:\n",moyenne/len(tableau))

def recherchetableau():
    recherche = int(input("que rechercher vous?\n (45, 21, 56, 12, 1, 8):\n"))
    result = 0
    for _ in tableau:
        if recherche in tableau:
            result = tableau.index(recherche)
        else:
            result = -1
    print(result)


if __name__ == "__main__":
    #moyenneTableau()
    recherchetableau()