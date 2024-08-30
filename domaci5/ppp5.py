
import csv

def prva(fajl):
    reader=csv.reader(fajl, delimiter=";")
    podaci=[]
    zarada_filma={}
    lista_reditelja=[]
    lista_zanrova=[]
    lista_datuma=[]

    for red in reader:
        naziv=red[1]
        zanr=red[2]#.split()
        datum=red[3]
        reditelj=red[4]
        zarada=red[5]
        zarada = (zarada.translate({ord('$'): None}))
        p=float(zarada)
        zarada_filma[naziv]=p
        lista_reditelja.append(reditelj)
        lista_zanrova.append(zanr)
        lista_datuma.append(datum)
        podaci.append(lista_reditelja) #podaci[0]
        podaci.append(lista_zanrova) #podaci[1]
        podaci.append(lista_datuma) #podaci[2]
        podaci.append(zarada_filma) #podaci[3]

    return podaci





with open('pp1_movies_2020.csv','r',encoding='utf-8') as fajl:
    lista=prva(fajl)
    for i in range(len(lista)):
        if i=='Drama':
            print(lista[1][i])
