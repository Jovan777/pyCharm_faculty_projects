'''
def selectionsort(lista):
    for i in range(len(lista)-1):
        for j in range(i+1,len(lista)):
            if lista[i]>lista[j]:
                lista[i],lista[j]=lista[j], lista[i]
    print(lista)

z=[3,2,5,6,4,7,1]
print(z)
print(selectionsort(z))

list=[1,2]*5
print(list)

for item in list:
    print(item, end='-' if list[item]<len(list)-1 else "")
print()
print(*list,sep=' ')
print()
def f(a,b,c):
    print(a,b,c)

z=[1,2,3]
print(f(*z))


list=[5,3,4,1,2]
print(sorted(list))
print(list)
print(*reversed(list))
print(list!=sorted(list))

for index,value in enumerate(list):
    print('lista[{}]={}'.format(index,value))

print(sum(list))

booleanList=[True,True,True,False,True]
print(any(booleanList))
print(all(booleanList))

stringlist=['A']*5
print(stringlist)

print(*zip(list,booleanList,stringlist), sep='\n',end="")



lista1=[1,2,3,4]
lista2=[x**2 for x in lista1 if x%2==1]
print(lista2)


matrica=[[1,2],[3,4],[5,6]]

lista12=[]

for red in matrica:
    for x in red:
        lista12.append(x)

print(lista12)


#sad je potrebno napraviti istu matricu kao ovu prethodnu

matrica1=[]

for i in range(3):
    red=[]
    for j in range(2):
        red.append(i*2+j+1)
    matrica1.append(red)

print(matrica1,'matrica 1.1')
print(matrica,'matrica 1')


lista=input().split()
lista=[int(x) for x in lista]
print(lista)




#potrebno je uneti vektore i u isto vreme ih pretvoriti u float

def zbir(vector1,vector2):
    return sum(x*y for x, y in zip(vector1,vector2) )

vector1=[float(x) for  x in input().split()]
vector2=[float(x) for  x in input().split()]

print(zbir(vector1,vector2))
'''