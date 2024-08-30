
def read(fajl):
    with open(fajl) as ulaz:
        lista=[]
        for linija in ulaz:
            id,cena,povrsina=linija.split(';')
            lista.append([id,int(cena[0:-1]),int(povrsina[:-4])])
        return lista

def unos():
    lista=[]
    cena=int(input('Unesite cenu'))
    p=int(input('Unesite kvadraturu'))
    lista.append(cena)
    lista.append(p)
    return lista

z=read('Stanovi.txt') #radi

def obrada(n):
    lista=[]
    u=unos()
    for i in range(len(n)):
        if n[i][1]<=u[0]:
            if (n[i][2] >= (u[1]-0.1*u[1])) or (n[i][2] <= (u[1]+0.1*u[1])):
                lista.append(n[i])
    max=[]
    for i in range(len(lista)):
        if lista[i][1]>lista[i+1][1]:
            max.append(lista[i])
        return max

k=obrada(z)
print(k)