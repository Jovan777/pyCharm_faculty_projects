#isprobavanje funkcije pass

print("""
0. Unesi broj
1. Dodaj na sumu
2. Ispisi sumu
3. Pomoc
4. Izlazak
""")

broj=suma=0

while True:
    izbor = int(input('Unesite komandu '))

    if izbor==1:
        broj=int(input('Unesite bilo koji broj '))
    elif izbor==2:
        suma=suma+broj
    elif izbor==3:
        pass
    elif izbor==4:
        break
    else:
        print('Nedozvoljen unos ')

print('Suma brojeva koje ste uneli je ',suma)
