#program treba da ima funkcije za izracunavanje aritmeticke i geometrijske sredine

def ar(lista):
    s=0
    for i in lista:
        s+=i
    return s/len(lista)

#sad je potrebno isto ovo ali za geometrijsku listu

def gr(lista1):
    z=1
    for i in lista1:
        z*=i
    return z**(1/len(lista1))

l=input('Unesite listu: ').split()
for i in range(len(l)):
    l[i]=int(l[i])

a=ar(l)
g=gr(l)

print('Aritmeticka sredina je: {:.2f}'.format(a))
print('Geometrijska sredina je: {:.2f}'.format(g))