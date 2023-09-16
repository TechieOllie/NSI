
def plus_proche(l
,m):
    for i in l:
        a=l[0]
        if abs(m-a) > abs(m-i):
            a=i
    print(a)

if __name__=="__main__":
    plus_proche([1,2,3,5,8,11], 12)