#program tabelira polinom
#unese se stepen, pa se unesu koeficijenti
#unese se intervel od kog do kog ce x da ide

stepen=int(input('Unesite stepen polinoma: '))
koeficijenti=input('Unesite koeficijente polinoma: ').split()
xmin, xmax, dx=input('xmin=, xmax=, dx= ').split(', ')
xmin=float(xmin)
xmax=float(xmax)
dx=float(dx)


x=xmin

while x<=xmax:
    p=0
    s=stepen
    for k in koeficijenti:
        p+=float(k) * x**s
        s=s-1
    print(p)
    x=x+dx

