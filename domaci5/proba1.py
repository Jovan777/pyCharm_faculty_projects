
import csv

def provera_datuma(datum):
    datumi=[]
    datum1=input().split('.')
    datum2=input().split('.')
    for i in range(len(datum)):
        datum[-1] = int(datum[-1])
        datum[-2] = int(datum[-2])
        datum[-3] = int(datum[-3])
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
    reader=csv.reader(fajl, delimiter=";")
    lista=[]
    podaci={}
    lista_datuma=[]
    lista_zanrova=[]

    for red in reader:
        naziv=red[1]
        zanr=red[2].split('|')#
        datum=red[3].split('.')
        #for i in range(len(datum)):
            #datum[-1]=int(datum[-1])
            #datum[-2] = int(datum[-2])
            #datum[-3] = int(datum[-3])
        reditelj=red[4]
        zarada=red[5]
        zarada = (zarada.translate({ord('$'): None}))
        zarada=float(zarada)
        novi_datumi=provera_datuma(datum)
        lista_datuma.append(novi_datumi)
        lista_zanrova.append(zanr)
        key=reditelj
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
        lista.append(sortirani_podaci)
    #lista.append(lista_zanrova)
    #lista.append(lista_datuma)

    return lista_datuma

'''
def provera_zanra(upisani_zanr,zanr):
    lista_zanrova=[]
    for i in range(len(zanr)):
        if upisani_zanr==zanr[i]:
            lista_zanrova.append(zanr[i])
    return lista_zanrova
'''
'''
def provera_datuma(datum,datum1,datum2):
    datumi=[]
    #datum1=input().split('.')
    #datum2=input().split('.')
    for i in range(len(datum)):
        datum1[i][0] = int(datum1[i][0])
        datum1[i][1] = int(datum1[i][1])
        datum1[i][2] = int(datum1[i][2])
    for i in range(len(datum)):
        datum2[i][0] = int(datum2[i][0])
        datum2[i][1] = int(datum2[i][1])
        datum2[i][2] = int(datum2[i][2])

    if (datum[2] > datum1[2]):
        if datum[2] < datum2[2]:
            datumi.append(datum)

    return datumi
'''



with open('pp1_movies_2020.csv','r',encoding='utf-8') as fajl:
    lista=prva(fajl)
    #upisani_zanr=input()
    #datum1 = input().split('.')
    #datum2 = input().split('.')
    #upis_datuma=provera_datuma(lista[2],datum1,datum2)
    #zanr=provera_zanra(lista[1],upisani_zanr)
    #print(upis_datuma)
    #print(zanr)
    print(lista)