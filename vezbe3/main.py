'''
def rastuci(niz):
    s=0
    d=0
    while s<len(niz)-1:
        if int(niz[s])<int(niz[s+1]):
            d=1
        else:
            d=0
        s+=1
    if d==1:
        return True
    elif d==0:
        return False




while True:
    niz1=input('Unesite prvi niz').split()
    if rastuci(niz1):
        break

while True:
    niz2=input('Unesite drugi niz').split()
    if rastuci(niz2):
        break

for i in range(len(niz1)):
    niz1[i]=int(niz1[i])

for i in range(len(niz2)):
    niz2[i]=int(niz2[i])

niz3=[]


for i in range(len(niz2)):
    niz3.append(niz2[i])

for i in range(len(niz1)):
    niz3.append(niz1[i])

niz3.sort(reverse=False)

print(niz3)
'''
'''
#K2 2012
import math
x=[]
y=[]
r=[]
while True:
    krug=input('Unesite podatke za krug:').split()
    if ' ' not in krug:
        if len(krug)==3:
            x.append(krug[0])
            y.append(krug[1])
            r.append(krug[2])
        else:
            break
    else:
        break

for i in range(len(x)):
    x[i]=int(x[i])
    y[i]=int(y[i])
    r[i]=int(r[i])

def krugovi(x,y,r):
    k=0 #k je element koji poredimo
    s=0 #s je brojac u petlji
    b=0
    lista_b=[]
    rv=0
    rm=0
    a=0
    while k<len(x)-1:
        s=0
        while s<len(x)-1:
            if r[s]==r[k]:
                s+=1
            elif r[s]>r[k]: #znaci sledeci iter je veci od poredjenog
                rv=r[s]
                rm=r[k]
                a=math.sqrt((x[s]-x[k])**2 + (y[s]-y[k])**2)
                if rv>rm:
                    if a<rv:
                        b+=1
            elif r[k]>r[s]:
                rv=r[k]
                rm=r[s]
                a = math.sqrt((x[k] - x[s]) ** 2 + (y[k] - y[s]) ** 2)
                if rv>rm:
                    if a<rv:
                        b+=1
            s+=1
            lista_b.append(b)
        k+=1
        s=0
    return sum(lista_b)

print(krugovi(x,y,r))

string1=input().strip().lower().replace(" ","")
string2=input().strip().lower().replace(" ","")

if string1 in string2:
    print('Jeste')
else:
    print('Nije')
'''''

#K2 2012 P

n=int(input('Unesite duzinu niza'))
s=0
while True:
    niz=input('Unesite niz').split(' ')
    if len(niz)==n:
        break

b=''
for i in range(len(niz)):
  b+=niz[i]

d=int(b,2)
print(hex(d))

for i in range(len(niz)):
    niz[i]=int(niz[i])

def provere(niz):
    d=True
    for i in range(len(niz)):
        if niz[i]==0 or niz[i]==1:
            d=True
        else:
            d=False
    return d

def heks(niz):
    if provere(niz):
        h=0
        l=len(niz)
        s=0
        #if len(niz)//4==0:
        bn=niz
        s=int(bn,2)
        h=hex(s)

    else:
        return print('Niz nije binaran')
    return h

#print(heks(niz))

#bn=bin(200)
#print(bn)
#print(int(bn,2))
