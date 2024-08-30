#potrebno je napraviti program koji tabelira polinom
#prvo se unesu koeficijenti
#unesu se vrednosti za x po koracima

koeficijenti=[float(x) for x in input().split()]
#sad se unesu vrednosti za x po koracima
prva,zadnja,korak=[float(x) for x in input().split()]

x=prva
while x<=zadnja:
        p=0 #polinom
        for broj in koeficijenti:
            p=p*x+broj
        print('Za x={} ,p(x)={}'.format(x,p))
        x=x+korak




