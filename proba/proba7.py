#unosimo brojeve i ukoliko su pozitivni i parni dodati ih u sumu

suma=0

while True: # ovde sada mozemo da unesemo koliko hocemo proizvoljnih brojeva
    n=int(input('Unesite broj '))
   
    if n<0:
        break
    elif n%2==1:
        continue
    suma=suma+n


print(suma)
