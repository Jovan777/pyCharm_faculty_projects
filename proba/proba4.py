#odredjivanje nzd(najmanji zajednicki delilac)
#odredjuje se po principu da dobijamo ostatak sve dok
# on ne postane 0,e pa onaj pre 0 je nzd
#radi se uz petlju while

a=int(input('Unesite bilo koji ceo broj '))
b=int(input('Unesite bilo koji ceo broj '))


if a<b:
 a,b=(a,b) if a>b else (b,a)
x, y=a,b


r=x%y
while r>0:
    x=y
    y=r
    r=x%y
nzd=y

print('Nzd je ', nzd)


