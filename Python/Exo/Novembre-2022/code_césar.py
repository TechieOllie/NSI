def code_cesar(decal, phrase, version):
    alphabet = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
    ]

    print("limite phrase 255 caractères\n")
    # decal = int(input("Décalage des lettres\n"))
    # phrase = str.lower(input("Votre Phrase?\n"))
    phrase = phrase.lower()
    # version = str(input("chiffrer ou déchiffrer?\n"))
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
                elif lettre == "ç":
                    return "ç"
                elif lettre == "!":
                    return "!"
                elif lettre == "é":
                    return "é"
                elif lettre == "è":
                    return "è"
                elif alphabet[x] == lettre:
                    return str(alphabet[x + decal])
            return "?"

        done = str()

        for lettre in phrase:
            done += chiffrage()

        print(done)
    elif version == "déchiffrer":
        # noinspection PyTypeChecker
        for i in range(255):
            alphabet.append(alphabet[i])

        def chiffrage():
            for x in range(len(alphabet)):
                if lettre == " ":
                    return " "
                elif lettre == "'":
                    return "'"
                elif lettre == "ç":
                    return "ç"
                elif lettre == "!":
                    return "!"
                elif lettre == "é":
                    return "é"
                elif lettre == "è":
                    return "è"
                elif alphabet[x] == lettre:
                    return str(alphabet[x - decal])
            return "?"

        done = str()

        for lettre in phrase:
            done += chiffrage()

        print(done)


for i in range(0, 26):
    code_cesar(i, "RWNGAYJ NMTCPRW ZMYR QNMR", "chiffrer")
