import random as r
import time as t

def tableMulti():
    choice = int(input("\nCombien de partie?:\n"))
    vict = 0
    for i in range(choice):
        n1 = r.randint(0, 10)
        n2 = r.randint(0, 10)
        nf = n1 * n2
        print("\n", n1, "*", n2 ,"= ?")
        nj = int(input("\nvotre réponse\n"))
        start = t.time()
        elapsed = 0
        while elapsed < 3*choice:
            if nf == nj:
                vict += 1
            else:
                print("partie", i+1, "/", choice, "\n")
            if i+1 == choice:
                print("\nvous avez gagner", vict, "partie sur", choice)

if __name__ == "__main__":
    tableMulti()