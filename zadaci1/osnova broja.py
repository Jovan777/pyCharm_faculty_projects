
def unos():
    lista=list(map(int, input().split(" ")))

    return lista

brojevi=[12,16,19,8]

def promena(broj,n):
    n=int(n)
    brojevi = "0123456789ABCDEF"
    x = (broj % n)
    rest = broj // n
    if (rest == 0):
        return brojevi[x]
    return promena(rest,n) + brojevi[x]


def ispis(lista):
    x=0
    y=0
    nova_lista=[]
    for i in range(len(lista)):
       x=lista[i]
       y=lista[i+1]
       nova_lista.append(promena(x,y))
    return nova_lista

promena(brojevi)