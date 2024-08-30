#potrebno je napraviti program koji uzima listu i kolicnik i proverava da li su svi elementi deljivi tim
#kolicnikom i da li je makar jedan deljiv tim kolicnikom
'''
def convert(lista,k):
    return [(x % k == 0) for x in lista]

def anydivisble(lista,k):
    return any(convert(lista,k))

def alldivisible(lista,k):
    return all(convert(lista,k))

lista=[x for x in range(0,22)]
print(lista)

z=convert(lista,3)
print(z)
print()
a=anydivisble(lista,3)
print(a)
A=alldivisible(lista,3)
print(A)
'''

#potrebno je napraviti program koji iz studentskog maila izvlaci godinu i indeks studiranja
#tip studija(osnovne ili master) i fakultet

email=input() #jj200631d@student.etf.rs

tip=''
if email[8]=='d':
    tip='Osnovne studije'
elif email[8]=='m':
    tip='Master studije'
else:
    tip='Neispravan unos'

fac=email[-6:-3]

year=email[2:4]

fullyear=('19' if int(year)>20 else '20')+year

print(fullyear)

indeks=email[4:8]

print('Vasi inicijali su ',email[0:2])
print('Vi ste student ',fac) #za fakultet
print("Upisali ste se ",fullyear)
print("Vas broj indeksa je ",indeks)
print("Vas tip studija je ",tip)
print('Vas kod je ',fullyear+'/'+indeks)


