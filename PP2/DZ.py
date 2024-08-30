'''program od unete liste pravi novu listu u kojoj su na pocetku elementi deljivi sa 3
pa elementi deljivi sa 2(bez da su deljivi i sa 3) i na kraju neparni elementi. Potrebno je ispisati i
koliko ima elemata deljivih samo sa 3, deljivih sa 2 (bez da su deljivi i sa 3),
i koliko ima preostalih elemanta'''

list=[]
n=int(input('Unesite broj elemenata liste: '))

for i in range (0,n):
    ele=int(input())
    list.append(ele)         #pravljenje liste

list2=[]

for i in range(len(list)):     #pravimo novu listu u kojoj su za sada samo elementi deljivi sa 3
    if list[i]%3==0:
        list2.append(list[i])

def razlika(lista1, lista2):
    lista3= [i for i in lista1 + lista2 if i not in lista1 or i not in lista2]
    return lista3

list3=razlika(list,list2) #mogu postojati elementi poput 6 koji su deljivi i sa 3 i sa 2.
                          #zato pravimo pomocnu listu gde ce biti elementi deljivi sa 2, koji nisu deljivi i sa
                          #3, i preostali elementi

for i in range(len(list3)):
    if list3[i]%2==0:
        list2.append(list3[i])   #dodavanje elemenata deljivih sa 2 u novu listu

for i in range(len(list)):
    if not list[i]%3==0:
        if not list[i]%2==0:
            list2.append(list[i])   #dodavanje preostalih neparnih elemenata
x=0
z=0
y=0
for i in range(len(list2)):
    if list2[i]%3==0:
        x=x+1
    elif list2[i]%2==0 and list2[i]%3 !=0:  #petlja proverava koliko imamo elemenata deljivih samo sa 3,
        z=z+1                               #elemenata deljivih sa 2(bez onih koji su deljivi i sa 3)
    else:                                   #i koliko ima preostalih elemanata
        y=y+1

print(list2)
print(x,z,y)









