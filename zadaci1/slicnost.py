tekst=[[1,2,68],[2,3,30],[1,4,15],[3,4,50],[4,5,1],[5,3,12]]



def broj_pojavljivanja(tekst):
    lista_pojavljivanja=[]
    for i in range(1,501):
        cnt = 0
        for s in range(len(tekst)):
            if i==tekst[s][0] or i==tekst[s][1]:
                cnt+=1
        if(cnt>0):
            lista_pojavljivanja.append((str(i),cnt))
    return lista_pojavljivanja






def br(tekst):
    skup = set()
    lista = []
    for trojka in tekst:
        skup.add(trojka[0])
        skup.add(trojka[1])
        lista.append(trojka[0])
        lista.append(trojka[1])
    for element in skup:
        print(str(element), ": ", lista.count(element))

print(br(tekst))

'''
def funkcija(tekst):
    tr=0
    maks=0
    s=0
    lista=[]
    for i in range(len(tekst)):
        while s<len(tekst):
            if tekst[i][0]==tekst[s][0]:
                if tekst[s][2]>maks:
                    maks=tekst[s][2]
            if tekst[i][1]==tekst[s][0]:
                if tekst[s][2]>maks:
                    maks=tekst[s][2]

            s+=1
        lista.append(maks)
        maks=0
        s=0
    return lista
'''

print(tekst)
print(broj_pojavljivanja(tekst))

