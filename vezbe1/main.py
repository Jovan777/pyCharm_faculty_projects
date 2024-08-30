books=[['Frederik Bakman','978-86-521-2465-7',['Drama','Komedija'],899.0],
       ['Danijel Kraus','978-86-521-546',['Fantastika','Akcija'],900.0]]

avgprice=849.0
category='Drama'
def titles(books,price,cat):
    autori=[]
    for book in books:
        if cat in book[2]: #ako je vise da ne bi proveravali celu listu samo stavi in operator
                if book[-1]>price:
                    autori.append(book[0])
    return set(autori)

print(titles(books,avgprice,category))