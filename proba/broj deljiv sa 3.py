#program koji proverava da li je uneti broj deljiv sa 3
#nakon toga unese se novi broj i opet se proveri da li je i on deljiv sa 3
#radi se preko petlje while


while True:
    broj=int(input('Unesite broj: '))
    if broj<0:
        break
    elif broj%3==0:
        print('Broj {} je deljiv sa 3'.format(broj))
    else:
        print('Broj {} nije deljiv sa 3'.format(broj))


