def krug():
    while True:
        r,x,y,boja=input().split()
        r=int(r)
        if r<0:
            break
        else:
            r=int(r)
            xkruga=int(x)
            ykruga=int(y)
            bojakruga=str(boja)

    n = input().split()
    xtacke = []
    ytacke = []
    koordinate = []
    for i in range(0, len(n), 2):
        xtacke.append(n[i])
    for i in range(1, len(n), 2):
        ytacke.append(n[i])
    for i in range(len(xtacke)):
        koordinate.append(int(xtacke[i]))
        koordinate.append(int(ytacke[i]))

    return r,xkruga,ykruga,bojakruga,koordinate

q=krug()
print(q)