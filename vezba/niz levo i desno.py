'''
niz1=[]
for i in range(100,1000):
    niz1.append(i)

for i in range(len(niz1)):
    niz1[i]=str(niz1[i])
niz2=[]

for i in range(len(niz1)):
    if int(niz1[i][0])==int(niz1[i][1])+int(niz1[i][2]):
        niz2.append(niz1[i])

for i in range(len(niz2)):
    niz2[i]=int(niz2[i])

print(niz2)
'''
'''
#K2P 2009

lista1=[]
for i in range(100,1000):
    lista1.append(i)

for i in range(len(lista1)):
    lista1[i]=str(lista1[i])

lista2=[]
for i in range(len(lista1)):
    if lista1[i][0]==lista1[i][2]:
        lista2.append(lista1[i])
#print(lista2)

def ispis(n):
    broj=[]
    global lista2
    for i in range(n):
        broj.append(lista2[i])
    return broj

print(ispis(21))
'''
''''''
'''
#K2 2011
#duzina izlomljene linije


import math
x=[]
y=[]
while True:
    x1=int(input('Unesite x:'))
    y1=int(input('Unesite y:'))
    if x1<0 or y1<0:
        break
    else:
        x.append(x1)
        y.append(y1)

def duz(lista1,lista2):
    d=[]
    s=0
    while s<len(lista1)-1:
        d.append(math.sqrt(abs((lista1[s+1]-lista1[s])**2-(lista2[s+1]-lista2[s])**2)))
        s+=1

    return sum(d)

print(duz(x,y))
'''
#napraviti program koji proverava da li je uneta recenica palindrom

tekst=input()
tekst=tekst.strip(' ').lower().replace(' ',"")
s=0
d=0
while s<len(tekst):
        if tekst[s]==tekst[-s-1]:
            d=1
        else:
            d=0
        s+=1
if d==1:
            print('Palidrom')
elif d==0:
            print('Nije')