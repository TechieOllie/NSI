def factorielle(n):
    if n > 0:
        return n*factorielle(n-1)
    else:
        return 1