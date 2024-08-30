# crta pravougaonik dimenzija a x b
 # koristi simbol * za ispunu pravougaonika
# gornja leva * pravougaonika u k-toj koloni tekućeg reda
def lik(a,b,k,sim):
    for linija in range(a):
        print((k-1) * ' ', end='')
        print(b * sim)

glava=lik(2,3,10,"*")
print(glava)