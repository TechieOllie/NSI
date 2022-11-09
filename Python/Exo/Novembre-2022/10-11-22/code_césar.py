
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


print("limite phrase 255 caractères\n")
decal = int(input("Décalage des lettres\n"))
phrase = str.lower(input("Votre Phrase?\n"))
phrase = phrase.lower()
version = str(input("chiffrer ou déchiffrer?\n"))
lettre = str()


if version == "chiffrer":
    # noinspection PyTypeChecker
    for i in range(255):
        alphabet.append(alphabet[i])

    def chiffrage():
        for x in range(len(alphabet)):
            if lettre == " ":
                return " "
            elif lettre == "'":
                return "'"
            elif alphabet[x] == lettre:
                return str(alphabet[x + decal])
        return "?"
    done = str()

    for lettre in phrase:
        done += chiffrage()

    print(done)
elif version == "déchiffrer":
    # noinspection PyTypeChecker
    for i in range(len(alphabet)):
        alphabet.append(alphabet[i])


    def déchiffrage():
        for x in range(255):
            if lettre == " ":
                return " "
            elif alphabet[x] == lettre:
                return str(alphabet[x - decal])
        return "?"

    done = str()

    for lettre in phrase:
        done += déchiffrage()

    print(done)

