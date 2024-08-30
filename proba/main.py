# testiramo programe sa prezantacija


#preva proba je restit linerarnu jednacinu ax+b=0

a=float(input('Unesite vrednost za a '))
b=float(input('Unesite vredsnost za b '))

#jednacina se resava po prencipu
#ax+b=0, ax=-b, x=-b/a
#srediti slucajeve kad je moguce i kad je nemoguce

if a!=0:
    if b!=0:
        x=-b/a
        print('Resenje je {:0.2f} ', format(x))
    else:
        print('Resenje je 0')
else:
    print('Jednacina nema jednoznacno resenje')
    if b!=0:
        print('Jednacina nema resenja')
    else:
        print('Jednacina ima beskonacno mnogo resenja')