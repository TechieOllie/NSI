import random as r
import time as t
import csv


def file(data):
    header = ["Pseudo", "Score", "Nb parties", "temps"]
    with open("scores.csv", "a", encoding="UTF8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(data)

def read():
    with open("scores.csv", "r") as q:
        reader = csv.reader(q)
        for row in reader:
            print(row)

def calcul():
    print("Score:")
    read()
    pseudo = input("Votre pseudo:\n")
    games = int(input("Combien de tours voulez vous faire?\n"))
    score = 0
    total = 0
    while games > 0:
        table1 = [2,3,4,5,6,7,8,9,11,15,20,30,40,50,60,70,80,90]
        a,b = r.randint(0, 17), r.randint(0, 17)
        print("\nCombien fait: ", table1[a],"*",table1[b])
        answer_user = int(input())
        start = t.time()
        if answer_user == table1[a]*table1[b]:
            print("\nbravo\n")
            score += 1
        else:
            print("\nDommage")
        total = t.time()-start

        games -= 1
    data = [pseudo, score, games, total]
    file(data)

if __name__ == "__main__":
    calcul()


