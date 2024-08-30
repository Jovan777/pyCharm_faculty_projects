import csv

def read(dadoteka):
     lista = []
     with open(dadoteka) as ulaz:
        ulaz=csv.reader(ulaz)
        for linija in ulaz:
            id_filma,naziv, zanr, datum,reditelj, zarada = linija.split(';')
            lista.append([naziv, reditelj, zanr, int(datum[-5:-1]),zarada])
     return lista

read('filmovi.csv')