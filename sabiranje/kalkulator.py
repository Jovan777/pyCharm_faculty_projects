a=input('Unesite prvi broj ')
b=input('Unesite drugi broj ')
a=int(a)
b=int(b)

moduo=' '
while (moduo!= 'sabiranje' and moduo!= 'mnozenje' and
moduo!= 'oduzimanje' and moduo!= 'deljenje'):
   moduo=input('Izaberite operaciju ')

if moduo=='sabiranje':
    c=a+b
    print('Rezultat sabiranja dva broja je', c,sep=' ',end='.'  )
elif moduo=='mnozenje':
    c=a*b
    print('Rezultat mnozenja dva broja je ', c)
elif moduo=='oduzimanje':
    c=a-b
    print('Rezultat oduzimanja dva broja je ', c)
else:
    c=a/b
    print('Rezultat deljenja dva broja je ', c)
