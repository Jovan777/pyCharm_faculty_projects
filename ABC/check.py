#drugi nacin za komplemt dvojke
n=int(input('Unesite broj bitova: '))
p=input('Unesite binarni broj: ')
k=int(p,2)
if n==len(p) and p[0]=='1': #znaci ovo je negativan broj
    k=-(2**n-k)
elif n>=len(p):
    print(k)
else:
    print('Nepravilan unos podataka')