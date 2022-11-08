def somme(n):
    S = 0
    for i in range(1,n+1):
        S = S +i
    return S


def puissance(x, n):
    S=x**n
    return S

def max_cube(n):
    k=0
    while k**3 <= n:
        k=k+1
    k=k-1
    return k