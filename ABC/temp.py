#program konvertuje temperaturu datu u nekoj odtri skale u celzijusovu skalu

t=int(input('Unesite temperaturu: '))
s=''

while (s!='F' and s!='K' and s!='R'):
    s=input('Izaberite skalu(Farenhajtova, Kelvinova ili Rankinova')

c=''
if s=='F':
   c=(t-32)*(5/9)
elif s=='K':
    c=(t-273.15)
else:
    c=(t-491.67)*(5/9)
print('Temperatura u celzijisima je {} '.format(c,2))
