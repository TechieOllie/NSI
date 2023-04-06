def compter_tout():
    text = list(str(input("Votre phrase a compter:\n")))
    answer = {}
    for i in text:
        a = text.count(i)
        answer.__setitem__(i, a)
    print(answer)

if __name__ == "__main__":
    compter_tout()


