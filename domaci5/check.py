import csv


def provera_zanra(zanr):
    lista_zanrova = []
    odabrani_zanr = input()
    for i in range(len(zanr)):
        if odabrani_zanr == zanr[i][0]:
            lista_zanrova.append(zanr[i])
        elif len(zanr[i]) > 1:
            if odabrani_zanr == zanr[i][1]:
                lista_zanrova.append(zanr[i])
        elif len(zanr[i]) > 2:
            if odabrani_zanr == zanr[i][2]:
                lista_zanrova.append(zanr[i])
        elif len(zanr[i]) > 3:
            if odabrani_zanr == zanr[i][3]:
                lista_zanrova.append(zanr[i])
        elif len(zanr[i]) > 4:
            if odabrani_zanr == zanr[i][4]:
                lista_zanrova.append(zanr[i])
        elif len(zanr[i]) > 5:
            if odabrani_zanr == zanr[i][5]:
                lista_zanrova.append(zanr[i])
        elif len(zanr[i]) > 6:
            if odabrani_zanr == zanr[i][6]:
                lista_zanrova.append(zanr[i])

    return lista_zanrova


def provera_datuma(datum):
    datumi = []
    datum1 = input().split('.')
    datum2 = input().split('.')
    for i in range(len(datum1)):
        datum1[0] = int(datum1[0])
        datum1[1] = int(datum1[1])
        datum1[2] = int(datum1[2])
    for i in range(len(datum2)):
        datum2[0] = int(datum2[0])
        datum2[1] = int(datum2[1])
        datum2[2] = int(datum2[2])

    for i in range(len(datum)):
        if (datum[i][2] > datum1[2]):
            if datum[i][2] < datum2[2]:
                datumi.append(datum[i])

    return datumi


def prva(fajl):
    reader = csv.reader(fajl, delimiter=";")
    lista = []
    recnik1 = {}
    podaci = {}
    lista_datuma = []
    lista_zanrova = []
    lista_reditelja = []
    nova_lista_z = []
    nova_lista_d = []

    for red in reader:
        naziv = red[1]
        zanr = red[2].split('|')  #
        datum = red[3].split('.')
        for i in range(len(datum)):
            datum[-1] = int(datum[-1])
            datum[-2] = int(datum[-2])
            datum[-3] = int(datum[-3])
        reditelj = red[4]
        zarada = red[5]
        zarada = (zarada.translate({ord('$'): None}))
        zarada = float(zarada)
        lista_datuma.append(datum)
        lista_zanrova.append(zanr)
        # novi_zanrovi=provera_zanra(zanr)
        # nova_lista_z.append(provera_zanra(lista_zanrova))
        # key1=novi_zanrovi
        lista_reditelja.append(reditelj)

        # zanr_reditelj={}
        # for key in lista_reditelja:



        key = reditelj

        if key not in podaci:
            podaci[key] = [(zarada, naziv)]
        else:
            podaci[key].append((zarada, naziv))

    sortirane_vrd=sorted(podaci.values())
    sortirani_podaci={}
    for i in sortirane_vrd:
            for j in podaci.keys():
                if podaci[j]==i:
                    sortirani_podaci[j]=podaci[j]
                    break
    nova_lista_z.append(provera_zanra(lista_zanrova))
    nova_lista_d.append(provera_datuma(lista_datuma))

    lista.append(sortirani_podaci)
    lista.append(nova_lista_z)
    lista.append(nova_lista_d)


    return sortirani_podaci



with open('pp1_movies_2020.csv', 'r', encoding='utf-8') as fajl:
    lista = prva(fajl)
    print(lista)



