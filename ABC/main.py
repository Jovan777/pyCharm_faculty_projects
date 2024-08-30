#program treba da ispisi da li broj zadovoljava svojstvo ABC=AB^2-C^2
#primer je 147,,14^2-7^2=196-49=147

n=''
while len(n)!=3:
    n=int(input('Unesite trocifreni broj: '))
    n=str(n)

n=int(n)

ab=n//10
c=n%10

if n==ab**2-c**2:
    print('Broj ',n, ' zadovoljava svojstvo.')
else:
    print('Broj ', n,' ne zadovoljava svojstvo.')


