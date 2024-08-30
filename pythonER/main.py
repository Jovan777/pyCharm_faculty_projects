'''

n=int(input('Unesite broj'))

while True:
    rec=input('Unesite rec')
    if len(rec)<30:
        break


lista_reci=[]
for i in range(n):
    nova_rec=input()
    lista_reci.append(nova_rec)


def provera(rec,lista_reci):
    rec=rec[::-1]
    for i in range(len(lista_reci)):
        if rec in lista_reci[i]:
            return lista_reci[i]


print(provera(rec,lista_reci))
'''''

zbirka=[]
delovi=input('unesite delove:').split()
for i in range(len(delovi)):
    delovi[i]=int(delovi[i])

zbirka.append([delovi[0],delovi[1]])
s=2
while s<len(delovi)-1:
    zbirka.append([delovi[s],delovi[s+1]])
    s+=2

def provera(zbirka):
    postoji={}
    lista_p=[]
    lista_strana=[]
    while True:
        strana=int(input())
        if strana<0:
            break
        else:
            lista_strana.append(strana)

    s=0
    while s<len(zbirka):
        for i in range(len(lista_strana)):
            if lista_strana[i] in range(zbirka[s][0],zbirka[s][1]):
                lista_p.append('Postoji')
                if lista_strana[i] not in postoji:
                    postoji[lista_strana[i]]=lista_p[i]
                #else:
                    #postoji[lista_strana[i]].append(lista_p[s])


        s+=1

    return postoji

#1 187 250 340 400 500 550 600

print(provera(zbirka))