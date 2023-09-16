def plus_proche(liste, nombre):
    n=liste[0]
    for i in liste:
        if abs(nombre-n) > abs(nombre-i):
            n=i
    print(n)

def compter_position(liste,lettre):
    result=[]
    result2= 0
    for i in liste:
        if lettre == liste[i]:
            result.append(i)
            result2 += 1
    print(result2,",",result)

if __name__ == "__main__":
    plus_proche([45,21,56,12,1,8,30,22,6,33],20)
    compter_position("Numérique et Sciences Informatiques !", "m")