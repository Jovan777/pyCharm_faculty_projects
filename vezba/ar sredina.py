'''
n=int(input('Unesite duzinu niza: '))

niz1=[]
for i in range(n):
    niz1.append(input())
'''
'''  K2 2006
for i in range(len(niz1)):
    niz1[i]=int(niz1[i])

niz2=[]
for i in range(1,(len(niz1)-1)):
    if niz1[i]==(niz1[i-1]+niz1[i+1])/2:
        niz2.append(niz1.index(niz1[i]))

print(niz2)
'''
'''
#K2 2007
for i in range(len(niz1)):
    niz1[i]=int(niz1[i])
niz2=[]
for i in range(len(niz1)):
    for j in range(len(niz1)):
        if niz1[i]==niz1[j]:
            continue
        else:
            if niz1[i]+niz1[j]==100:
                niz2.append([niz1[i],niz1[j]])

a=len(niz2)
for i in range(0,(len(niz2))//2):
    if niz2[i][0]==niz2[i+1][1]:
            niz2.remove(niz2[i+1])

print(niz2)
'''
'''
#K2 2008
n=input('Unesite niz karaktera:')

rec=''
while len(rec)>6 or len(rec)==0:
    rec=input('Unesite rec koja ima manje od 6 slova:')
#wxyazmljk
lista1=[]
for char in rec:
    if char not in n:
        lista1.append(char)

if len(lista1)==0:
    print('Uspeh')
else:
    print('Neuspeh')

counter=0
slova='abc'
for i in range(len(lista1)):
    if lista1[i] in slova:
        counter+=1

if counter==1:
    print('Jedno od slova abc se pojavljuje jedanput.')
else:
    print('Slova abc se pojavljuju',counter,'puta')
'''
'''
#K2 2008 1
n=input('Unesite niz realnih brojeva:').split()
for i in range(len(n)):
    n[i]=float(n[i])

indeks=input('Unesite listu indeksa:').split()
for i in range(len(indeks)):
    indeks[i]=int(indeks[i])

lista1=[]
for i in range(len(n)):
    for i in range(len(indeks)):
        if indeks[i]>(len(n)-1):
            continue
        else:
            lista1.append(n[indeks[i]])

lista1=set(lista1)
lista2=list(lista1)
ar_sredina=0
for i in range(len(lista2)):
    ar_sredina+=lista2[i]
ar_sredina=ar_sredina/len(lista2)

print('Aritmeticka sredina je {:.2}'.format(ar_sredina))
'''
'''
#K2 2008 2
niz1=[]
broj=777
while broj>0:
    broj=float(input())
    niz1.append(broj)
    if broj<0:
        break


for i in range(len(niz1)):
    if niz1[i]<0:
        niz1.remove(niz1[i])
niz1=sorted(niz1)
print(niz1)
'''
