import csv

def sortiranje(prvi,drugi):
    if prvi<drugi:
        return prvi+'-'+drugi
    else:
        return drugi+'-'+prvi

def readfile(file):
    ruta={}
    reader=csv.reader(file)
    for red in reader:
        prvi=red[0].strip().lower()
        drugi=red[1].strip().lower()
        minuti=int(red[2])
        key=sortiranje(prvi,drugi)
        ruta[key]=minuti

    return ruta

def sati(vreme):
    sat=vreme//60
    minuti=vreme%60
    return '{}:{}'.format(sat,minuti)

with open('ruta.csv','r',encoding='utf-8') as fajl:
    rute=readfile(fajl)

destinacije=[]

while True:
    destinacija=input()
    if len((destinacija))==0:
        break
    else:
        destinacije.append(destinacija.strip().lower())

vreme=0
for i in range(1,len(destinacije)):
    key=sortiranje(destinacije[i],destinacije[i-1])
    vreme+=rute[key]

print(sati(vreme))