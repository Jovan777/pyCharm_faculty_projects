#program za krugove
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
        print(r,xkruga,ykruga,bojakruga)
    return r,xkruga,ykruga,bojakruga


def tacke():
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

    return koordinate

def obrada(r,xkruga,ykruga,bojakruga,xtacke,ytacke):
        if xtacke<=(xkruga+r) and ytacke<=(ykruga+r):
            bojatacke=bojakruga
        elif xtacke<=(xkruga-r) and ytacke<=(ykruga-r):
            bojatacke=bojakruga
        elif xtacke<=(xkruga+r) and ytacke<=(ykruga-r):
            bojatacke=bojakruga
        elif xtacke<=(xkruga-r) and ytacke<=(ykruga+r):
            bojatacke=bojakruga
        else:
            bojatacke='bela'
        return bojatacke

k=krug()
print(k)