zanrovi=[['Comedy', 'Drama'], ['Comedy'], ['Comedy', 'Romance'], ['Comedy'], ['Thriller'], ['Adventure', 'Western'], ['Comedy'], ['Documentary'], ['Comedy', 'Drama', 'Fantasy']]


def provera_zanra(zanr):
    lista_zanrova=[]
    odabrani_zanr=input()
    for i in range(len(zanr)):
        if zanr[i][0]==odabrani_zanr:
            lista_zanrova.append(zanr[i])
        elif zanr[i][1]==odabrani_zanr:
            lista_zanrova.append(zanr[i])
        elif zanr[i][2]==odabrani_zanr:
            lista_zanrova.append(zanr[i])
        elif zanr[i][3]==odabrani_zanr:
            lista_zanrova.append(zanr[i])


    return lista_zanrova


p=provera_zanra(zanrovi)
print(p)