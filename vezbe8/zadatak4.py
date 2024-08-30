'''
with open('v05z04.txt','w+',encoding='utf-8') as dokument:
    dokument.write('prva druga\n')
    dokument.write('treca\n')
    dokument.write('cetvrta peta sesta')
'''
#potrebno je naci srednju duzinu reci
'''
def srednja_duzina_reci(fajl):
    broj_slova=0
    broj_reci=0
    pocetak_reci=True
    f=open(fajl)
    for linija in f:
        for znak in linija:
            if znak.isspace():
                pocetak_reci=True
            else:
                broj_slova+=1
                if pocetak_reci:
                    broj_reci+=1
                    pocetak_reci=False
    f.close()
    return broj_slova/broj_reci
'''
#path=input() #v05z04.txt


def srednja_duzina_reci(fajl):
    broj_reci=0
    broj_slova=0
    for linija in fajl:
        reci=linija.split()
        broj_reci+=len(reci)
        for rec in reci:
            broj_slova+=len(rec)

    return broj_slova/broj_reci if (broj_reci!=0) else 0

fajl=input()

with open(fajl,'r+') as file:
    print(srednja_duzina_reci(file))