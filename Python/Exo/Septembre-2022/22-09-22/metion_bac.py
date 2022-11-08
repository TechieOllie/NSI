def mention_bac(a):
    if a < 8:
        return "refusé"
    elif a >= 8 and a < 10:
        return "ratrapage"
    elif 10 <= a and a < 12:
        return "mention passable"
    elif 12 <= a and a < 14:
        return "mention assez bien"
    elif 14 <= a and a < 16:
        return "mention bien"
    elif 16 <= a and a < 18:
        return "mention trés bien"
    elif 18 <= a:
        return "Félicitations du jury"