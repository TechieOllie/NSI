import math

def trinome():
    print("Cette equation est sous la forme ax²+bx+c=0")
    a = 0
    b = 0
    c = 0
    print("Quelle est la valeur de ")
    a = float(input("a? "))
    b = float(input("b? "))
    c = float(input("c? "))
    print(" ")
    print(a, "x²", "+", b, "x", "+", c, "= 0")
    
    delta = (b**2)-(4*a)*c
    print("delta est égal à:", delta)
    
    if delta > 0:
        print("2 solutions")
        x1 = (-b-math.sqrt(delta))/2*a
        x2 = (-b+math.sqrt(delta))/2*a
        print("Les solutions sont {", x1, ";", x2, "}")
    elif delta < 0:
        print("pas de solutions")
    elif delta == 0:
        x0 = -b/2*a
        print("La solution est: ", x0)
        