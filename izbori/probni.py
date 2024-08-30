


library_name=input()
#ulazni.csv

def readLibrary(library_name):
    lista=[]
    with open(library_name) as ulaz:
        for red in ulaz:
            naziv,autor,isbn,*zanr,datum,cena=[l.strip() for l in  red.split(',')]
            lista.append([autor,isbn,zanr,float(cena)])
    return lista


def checkIsbn ( isbn ):
    isbn=isbn.replace('-',"")
    s=0
    nep=[]
    parn=[]
    for i in range(len(isbn)):
        if i%2==0:
            parn.append(int(isbn[i])*3)
        else:
            nep.append(int(isbn[i]))
    zbir1=sum(nep)
    zbir2=sum(parn)
    zbir=zbir2+zbir1
    if zbir%10==0:
        return True
    else:
        return False


def provIsbn(isbn):
     isbn = isbn.replace('-', '')
     s, k = 0, 1
     for x in isbn:
        s += int(x) * k
        k = 3 if k == 1 else 1
     return s % 10 == 0


def ok_isbn(books):
    #return [knjiga for knjiga in books if checkIsbn(books[1])]
    lista=[]
    for i in range(len(books)):
        if provIsbn(books[i][1]):
            lista.append(books[i])
    return lista

def pricesbycatt(books):
    recnik={}
    for book in books:
        autor,isbn,kategorija,cena=book
        for k in kategorija:
            if k not in recnik:
                recnik[k]=[cena]
            else:
                recnik[k].append(cena)
    return recnik

def averaagePrice(prices):
    return sum(prices)/len(prices)


def titles(books,avgprice,category):
    skup=set()
    for book in books:
        if category in book[2] and book[3]>avgprice:
            skup.add(book[0])
    return skup


#ulazni.csv
lista=readLibrary(library_name)

filt_lista=(ok_isbn(lista))
recnik=pricesbycatt(filt_lista)

prosecni_recnik={}
skup=set()

for key,value in recnik.items():
    prosecni_recnik[key]=averaagePrice(value)
    skup=skup.union(titles(filt_lista,prosecni_recnik[key],key))

print(len(skup))


