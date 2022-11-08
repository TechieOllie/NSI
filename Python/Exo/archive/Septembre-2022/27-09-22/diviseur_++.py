def diviseur():
    a = int(input("Entrez votre nombre: "))
    print("la liste des diviseurs est: ")
    for i in range(1,a+1):
        b=1
        if a % i == 0:
           b=b+1
           print(i)
    if b==3:
        print("le nombre n'est pas premier")
        
    else: 
        print("Le nombre est premier")