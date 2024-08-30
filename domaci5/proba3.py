#pravljenje funkcije min i max zarada


def zarada(lista):
    trenutna_min_zarada = 10000000000
    trenutna_max_zarada = 1500
    minimun = 1000000000000000000
    maksimum = 15
    for i in range(len(lista)):
        if lista[i] <trenutna_min_zarada:
            trenutna_min_zarada=lista[i]
            if trenutna_min_zarada<minimun:
                minimun=trenutna_min_zarada
        else:
            if lista[i]>trenutna_max_zarada:
                trenutna_max_zarada=lista[i]
                if trenutna_max_zarada>maksimum:
                    maksimum=trenutna_max_zarada


lista=[12,123,56,32,65,1,1231163]
print(zarada(lista))

def provera(uneti_zanr,zanr,datum,datum1,datum2,lista_zarade):

    p=''
    for i in range(len(zanr)):
        if (uneti_zanr==zanr[i]):
            if (datum[2]>datum1[2]):
                if datum[2]<datum2[2]:
                    p=max_min(lista_zarade)

        for i in range(len(lista_zanrova)):
            if lista_zanrova[i] not in recnik1:
                recnik1[lista_zanrova[i]]=[(naziv)]
            else:
                recnik1[lista_zanrova[i]]=(naziv)

