
'''
K2 2009

import math
x=[3,5,9,11,7,2]
y=[6,8,3,7,1,4]

for i in range(len(x)):
    x[i]=float(x[i])
    y[i]=float(y[i])

lista=[]
k=1

while k<len(x)-1:
   lista.append(
       math.sqrt((x[k]-x[k+1])**2-(y[k]-y[k+1]**2))
   )
   k+=1
lista.append(
    math.sqrt((x[0]-x[1])**2-(y[0]-y[1]**2))
)
lista.append(
    math.sqrt((x[0]-x[-1])**2-(y[0]-y[-1]**2))
)


print(sum(lista))
'''

'''
K2 2009
datum1=[1,1,2009]
datum2=input('Unesite datum prestanka treniranja:').split('.')
for i in range(len(datum2)):
    datum2[i]=int(datum2[i])

dan1=datum1[0]
mesec1=datum1[1]
tr_dan=datum2[0]
tr_mesec=datum2[1]

def trening(dan1,mesec1,tr_dan,tr_mesec):
    brojac=0
    while True:
        if (dan1%7==2) or (dan1%7==5):
            brojac+=1
        dan1+=1
        if dan1>30:
            dan1=0
            mesec1+=1
        if dan1==tr_dan and mesec1==tr_mesec:
            break
    return brojac

print(trening(dan1,mesec1,tr_dan,tr_mesec))
'''''

'''
def tacka(x,y):
    if x>0 and y>0:
        return print('Prvi')
    elif x>0 and y<0:
        return print('Cetvrti')
    elif x<0 and y>0:
        return print('Drugi')
    elif x<0 and y<0:
        return print('Treci')
    else:
        print('Nijedan')


redovi=[
    [12,-5],
    [45,-5],
    [-9,5],
    [5,5],
    [0,0],
    [-8,-8]
]
for i in range(len(redovi)):
    print(tacka(redovi[i][0],redovi[i][1]))
'''''
'''
#K2 2010

lista1=input().split()
for i in range(len(lista1)):
    lista1[i]=int(lista1[i])

def cels(f):
    lista2=[]
    for i in range(len(f)):
        if f[i]>0:
            lista2.append((f[i]-32)*(5/9))
    return lista2

z=cels(lista1)
lista_cels=[]
for member in z:
    form='{:.1f}C'.format(member)
    lista_cels.append(form)
print(lista_cels)
'''
'''
#K2 2010

broj=input()
heks='0123456789abcdef'

for cifra in broj:
    if cifra not in heks:
        print('Neispravan unos')

recnik={'a':10,'b':11,'c':12,'d':13,'e':14,'f':15}

#print(recnik['a'])

dec=[]
s=0
k=len(broj)
while s<len(broj):
    #sad je potrebno za svaku moguce vrednost
    if broj[s]=='a':
        dec.append((16**k)*recnik['a'])
    elif broj[s]=='b':
        dec.append((16**k)*recnik['b'])
    elif broj[s]=='c':
        dec.append((16**k)*recnik['c'])
    elif broj[s]=='d':
        dec.append((16**k)*recnik['d'])
    elif broj[s]=='e':
        dec.append((16**k)*recnik['e'])
    elif broj[s]=='f':
        dec.append((16**k)*recnik['f'])
    elif broj[s]=='0':
        dec.append((16**k)*0)
    elif broj[s]=='1':
        dec.append((16**k)*1)
    elif broj[s]=='2':
        dec.append((16**k)*2)
    elif broj[s]=='3':
        dec.append((16**k)*3)
    elif broj[s]=='4':
        dec.append((16**k)*4)
    elif broj[s]=='5':
        dec.append((16**k)*5)
    elif broj[s]=='6':
        dec.append((16**k)*6)
    elif broj[s]=='7':
        dec.append((16**k)*7)
    elif broj[s]=='8':
        dec.append((16**k)*8)
    elif broj[s]=='9':
        dec.append((16**k)*9)
    k-=1
    s+=1

print(sum(dec))
'''''
'''
#K2 2010 P 18
osnovice=[]
visine=[]
while True:

    a=int(input('Unesite osnovicu'))
    h=int(input('Unesite visinu'))
    if a<0 or h<0:
        break
    else:
        osnovice.append(a)
        visine.append(h)
tr_p=0
max_p=0
am=0
hm=0

for i in range(len(osnovice)):
    if tr_p<((osnovice[i]*visine[i])//2):
        tr_p=osnovice[i]*visine[i]//2
        if tr_p>max_p:
            max_p=tr_p
            am=osnovice[i]
            hm=visine[i]

print(max_p,am,hm)
'''


