

def ulaz(file):
    with open(file) as fajl:
        lista1=[]
        for linija in fajl:
            indeks,koord=[item.strip() for item in linija.split(':')]
            lista1.append(koord.split(','))

    for i in range(len(lista1)):
        lista1[i][0] = int(lista1[i][0])
        lista1[i][1] = int(lista1[i][1])
        lista1[i][2] = int(lista1[i][2])
        lista1[i][3] = int(lista1[i][3])
    return lista1

z=ulaz('pravougaonici.txt')
#print(ulaz('pravougaonici.txt'))

def unos():
    lista1=input('Unesite koordinate tacaka:').split(',')
    for i in range(len(lista1)):
        lista1[i]=int(lista1[i])
    return lista1

def obrada(p):
    u=unos()
    brojac=0
    for i in range(len(p)):
        if u[0]>=p[i][0] and  u[0]<=p[i][2]:
            if u[1]>=p[i][1] and u[1]<=p[i][3]:
                brojac+=1
    return brojac


j=obrada(z)
print(j)