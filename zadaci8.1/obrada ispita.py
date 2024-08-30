import csv
import os


def obrada(fajl):
    pitalice={
        '1':15,
        '0':0,
        '-1':-3.75
    }
    reader=csv.reader( fajl )
    results={}
    for red in reader:
        indeks,godina=red[0].strip().split('/')
        indeks='{:0>4}'.format(indeks)
        name,surname=red[1].strip().lower().split()
        test=red[2].strip()
        poeni_pitalice=sum(pitalice[item.strip()] for item in red[3:7])
        zadatak=float(red[7])*0.55
        poeni=max( min(poeni_pitalice,45),0)+zadatak

        key=surname[0]+name[0]+godina[2:]+indeks+'d.txt'

        if key not in results:
            results[key]=[(test,poeni)]
        else:
            results[key].append((test,poeni))

    return results

with open('ispit.csv','r',encoding='utf-8') as fajl:
    results=obrada(fajl)

if not os.path.exists('rezultati'):
    os.mkdir('rezultati')

os.chdir('rezultati')

sortFoo=lambda testScore: testScore[0]
for key,testScores in results.items():
    testScores.sort(key=sortFoo)
    with open(key,'w') as file:
        total=0
        for testScore in testScores:
            file.write('{} : {:.2f}\n'.format(testScore[0],testScore[1]))
            total+=testScore[1]*0.33 if testScore[0]=='K1' else testScore[1]*0.35
        file.write('TOTAL {:.2f}'.format(total))
