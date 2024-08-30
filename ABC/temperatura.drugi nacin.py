#unesemo vrednost temperature tipa 156K,-135F...

t=input('Unesite vrednost temperature u jednoj od tri skale: ')


j=t[-1]
c=t[0:-1]
c=float(c)

if  j=='K':
    c=c-273.15
elif  j=='F':
    c = (c-32)*(5/9)
elif j=='R':
    c = (c - 491.67) * (5 / 9)
else:
    print('Nepravilan unos')

print('Temperatura u celzijusima je ', c)