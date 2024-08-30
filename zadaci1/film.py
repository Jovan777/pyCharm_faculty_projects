def unos():
    n = int(input())
    red = list(map(int, input().split(" ")))
    return red

kritike=unos()
ocene=[10,9,8,7,6,5,4,3,2,1]
oznaka=0
brojac=0
while brojac<len(kritike):
    for i in range(len(kritike)):
        oznaka+=kritike[brojac]*ocene[brojac]
        brojac+=1
print(oznaka/sum(kritike))

c=len(kritike)
if c%2==0:
   c//=2
   c=kritike[c]+kritike[c-1]
   c//=len(kritike)//2
print(c)
