def format_index(index):
    index='{}-{}'.format(index[5:],index[2:4])
    return index

def izmedju(vreme,od,do):
    return int(vreme[:2]) in range(od,do)

def citaj_fajl(file1,file2,vreme):
    lista_sala=[]
    with  open(file2) as sale:
        for red2 in sale:
            ime,kapacitet,sati=red2.split(',')
            od=int(vreme[:2])
            do=int(vreme[3:])
            kapacitet=int(kapacitet)
            lista_sala.append([ime,kapacitet,vreme])

    with open(file2) as studenti,open('raspored.txt','w') as ifile:
        for red in studenti:
            indeks,ime=red.split(",")
            ime=ime[:-1]
            indeks=format_index(indeks)
            rasporedjeni=True
            nasao=False
            for sala in lista_sala:
                if sala[1]>0 and izmedju(vreme,sala[2][:2],sala[2][:3]):
                    ifile.write('{} {} {}'.format(indeks,ime,sala[0]))
                    nasao=True
                    sala[1]-=1
                    break
                if not nasao:
                    ifile.write('{} {} Nerasporedjen\n'.format(indeks,ime))
                    rasporedjeni=False
    return rasporedjeni





def glavni():
    file_studenti=input()
    file_sale=input()
    vreme=input()
    rasporedjeni=citaj_fajl(file_studenti,file_sale,vreme)
    print(rasporedjeni)

glavni()

