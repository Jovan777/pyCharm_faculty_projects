
import csv

def prva(fajl):
    reader=csv.reader(fajl, delimiter=';')
    podaci={}
    reditelji={}
    filmovi={}
    for red in reader:
        naziv=red[1]
        zanr=red[2]
        datum=red[3]
        reditelj=red[4]
        zarada=red[5]
        key=naziv
        if key not in filmovi:
            filmovi[key]=[zarada]
        else:
            filmovi[key].append(zarada)



    return filmovi

with open('filmovi.csv','r') as ulaz:

    with open('newfile','w') as file:
        file.write(prva(ulaz))
