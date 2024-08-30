

libraryName=input()
#library.csv
def readLibrary(libraryName):
    lista = []
    with open(libraryName) as ulaz:
         for linija in ulaz:
            naziv, pisac, isbn, *kategorije, datum, cena = [l.strip() for l in linija.split(',')]
            lista.append([naziv, pisac, kategorije, int(datum[-5:-1])])
    return lista

books=readLibrary(libraryName)
years = {2017, 2018, 2019}
def filterYear(books, years):
    lista_knjiga=[]
    for i in range(len(books)):
        for year in years:
            if books[i][-1]==year:
                lista_knjiga.append(books[i])
    return lista_knjiga


def organizeYearCategory(books):
    recnik={}
    for book in books:
        ime,pisac,zanr,godina=book
        if godina not in recnik:
            recnik[godina]={}
        for z in zanr:
            if z not in recnik[godina]:
                recnik[godina][z]=1
            else:
                recnik[godina][z]+=1
    return recnik

#k=organizeYearCategory(books)
#print(k)

booksByCategory= {'Drama': 2, 'Domaci autori': 1, 'Nagradjene knjige': 1}


def largestCategory(booksByCategory):
    max=0
    najvise=''
    for key,value in booksByCategory.items():
        if booksByCategory[key]>max:
            max=booksByCategory[key]
            najvise=booksByCategory[key]
    zanr=''
    for key,value in booksByCategory.items():
        if value==max:
          zanr=key
    return (zanr)

#library.csv

category = "Drama"
year = 2019
def titles(books, category, year):
    lista=[]
    for i in range(len(books)):
        if books[i][-1]==year:
            if books[i][2][0]==category or books[i][2][1]==category:
                lista.append(books[i][0])
    return ( set(lista))


lista=readLibrary('library.csv')
filtlista=filterYear(lista,{2017, 2018, 2019})
recnik=organizeYearCategory(filtlista)
maks_recnik={}
skup=set()
for godina,zanr in recnik.items():
    maks_recnik[godina]=largestCategory(zanr)
    ime=titles(filtlista,maks_recnik[godina],godina)
    skup=skup.union(ime)
print(maks_recnik)
print(ime)
print(skup)
print(len(skup))
