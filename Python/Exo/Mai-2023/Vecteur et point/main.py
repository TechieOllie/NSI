from cmath import sqrt


def vecteurs():
    Ax, Ay = float(input("Coordonnés de Ax:\n")), float(input("\nCoordonnés de Ay:\n"))
    Bx, By = float(input("Coordonnés de Bx:\n")), float(input("\n Coordonnés de By:\n"))
    vecteur_AB = [Bx - Ax, By - Ay]
    norme_AB = ((Bx - Ax) ** 2 + (By - Ay) ** 2)**0.5
    norme_rounded = round(norme_AB, 2)
    coord_milieu = [(Ax + Bx) / 2, (Ay + By) / 2]
    print("\n\nLe vecteur AB à pour coordonnées: ", vecteur_AB)
    print("\n La norme du vecteur est: ", norme_rounded)
    print("\n Les coordonnées du milieu sont: ", coord_milieu)








if __name__ == "__main__":
    vecteurs()