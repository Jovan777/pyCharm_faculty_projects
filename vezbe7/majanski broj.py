#potrebno je napraviti program koji uneti broj transformise u majanski

n=int(input())

mayan_number=[ ]

#osnova majanskog broja je 20, znaci unet broj prvo delimo sa 20 ali uzimamo ostatak

while n>0:
    ostatak = n % 20
    if ostatak>0:
        tacke=ostatak%5
        linije=ostatak//5
        broj_tacaka='{:^5}\n'.format('o'*tacke)
        broj_linija='____\n'*linije
        symbol=broj_tacaka+broj_linija
    else:
        symbol='{:^5}'.format('@')
    mayan_number.append(symbol)
    n=n//20

mayan_number.reverse()

if len(mayan_number)==0:
    print('{:^5}'.format('@'))
else:
    print('\n'.join(mayan_number))

