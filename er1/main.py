

def citajfajl(ulaz,sf):
    with open(ulaz) as ufile:
        lista=[]
        recnik={0:'Monday',1:'Tuesday',2:'Wednesday',3:'Thursday',4:'Friday'}
        for red in ufile:
            dan,poc,kraj,*sog=red.split(',')
            sog[-1]=sog[-1][:-1]
            for element in sog:
                sifra,ostatak=element.split("[")
                odsek,pg=ostatak.split("]")
                sifra=sifra[:-1]
                if sifra==sf:
                    lista.append([sifra,odsek,poc,kraj])
                pg=pg[1:]
                predavanje=pg[0]
                grupa=pg[1]
                if sifra==sf:
                    lista.append([predavanje,odsek,grupa,poc,kraj])
    lista=lista.sort()
    return lista

def glavni():
    ulaz=input()
    sf=input()
    rasporedjeni=citajfajl(ulaz,sf)
    print (rasporedjeni)

print(glavni())