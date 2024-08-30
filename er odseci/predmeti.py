

def citajFile(ulazni,sp):
    with open(ulazni,'r') as ufile:
        lista=[]
        dani={0:'Monday',1:'Tuesday',2:'Wednesday',3:'Thursday',4:'Friday'}
        for red in ufile:
            dan,poc,kraj,*sog=red.split(',')
            dan=int(dan)
            sog[-1]=sog[-1][:-1]
            for element in sog:
                sifra,ostatak=element.split('[')
                odsek,pg=ostatak.split(']')
                sifra=sifra[:-1]
                pg=pg[1:]
                predavanje=pg[0]
                grupa=pg[1]
                if sifra==sp:
                    lista.append([predavanje,odsek,grupa,poc,kraj,dani[dan]])
        lista.sort()
    return lista

def ispis(sp,lista):
    with open(sp+'txt','w') as ifile:
        for element in lista: #element je u stvari red u novo dobijenoj listi
            ifile.write('{} {} {} {} {}\n'.format(element[5],element[0],element[2],element[1],element[3]))

def glavni():
    ulazni=input()
    sp=input()
    z=citajFile(ulazni,sp)
    ispis(sp,z)

glavni()