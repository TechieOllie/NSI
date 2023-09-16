def compter_position():
    text = str(input("Votre phrase a compter:\n"))
    lettre = str(input("\nLa lettre a trouver:\n"))
    end = 0
    for lettre in text:
        end += 1
        result = enumerate(lettre)
        x = list(result)

if __name__ == "__main__":
    compter_position()