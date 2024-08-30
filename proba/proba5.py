
#ispisvanje sume svih parnih brojeva u opsegu od 0 do n

n=int(input('Unesite bilo koji pozitivan ceo broj '))

while n<=0:
    n = int(input('Unesite bilo koji pozitivan ceo broj '))

suma=0
zbir=0

for i in range (0,n+1):
    if i%2==0:
        suma=suma+i
    else:
        suma=suma
print(suma)

#laksi nacin
for i in range (0,n+1,2):
    zbir=zbir+i

print(zbir)

