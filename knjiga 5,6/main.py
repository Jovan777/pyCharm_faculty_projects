
'''
for i in range(0,4):
    for j  in range(0,4):
        print(i*j)


for word in ['ox','bobcat','tiger','lion','cat']:
    for i in range(2,7):
        letters=len(word)
        if letters%i==0:
            print(i,word)
'''

#rastuci redosled
def sortlist(list):
    zamena=True
    while zamena:
        zamena=False
        for i in range(len(list)-1):
            if lista[i]>lista[i+1]:
                x=list[i]
                list[i]=list[i+1]
                list[i+1]=x
                zamena=True
    return list

lista=[6,2,3,5,9]
x=sortlist(lista)
print(x)

#opadajuci redosled
def sortlist1(list, index):
    zamena=True
    while zamena:
        zamena=False
        for i in range(len(list)-1):
            if lista[i]<lista[i+1]:
                x=list[i]
                list[i]=list[i+1]
                list[i+1]=x
                y=index[i]
                index[i]=index[i+1]
                index[i+1]=y
                zamena=True
    return print('Rezultat', lista,'index',index)



lista2=[6,2,3,5,9]
number_of_scores=len(lista2)#pravi duzini jednku duzini liste 2
numbers=list(range(number_of_scores))#pravi listu sa rangom od 0 do duzina liste2 - 1
y=sortlist1(lista2,number_of_scores)
print(y)


for i in range(0,5):
    print(str(i+1)+') ','Rezultat #'+str(numbers[i]),'index je'+str(lista2[i]))
