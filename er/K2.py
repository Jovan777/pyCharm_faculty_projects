'''
#n=int(input())

def readArray(n):
    s=0
    lista=[]
    while s<n:
        broj=int(input())
        lista.append(broj)
        s+=1
    return lista

def printArray(arr):
    arr=list(arr)
    return arr


def sortArray(arr):
    arr=sorted(arr,reverse=False)
    return arr

def isArithmeticProgression ( arr ):
    razlika=[]
    zbir=arr[1]-arr[0]
    s=0
    lista=[]
    while s<len(arr)-1:
       razlika.append(arr[s+1]-arr[s])
       s+=1
    for i in range(len(arr)-1):
        if (arr[i+1]-arr[i])==zbir:
            lista.append(True)
        else:
            lista.append(False)
    if all(lista):
        return True
    else:
        return False



n=int(input())
z=readArray(n)
j=sortArray(z)

if isArithmeticProgression(j):
    printArray(j)
    print('MOZE')
else:
    printArray(j)
    print('NE MOZE')
'''

m=int(input())
lista=[]
while len(lista)<m:
    lista=input().split()
for i in range(len(lista)):
    lista[i]=int(lista[i])

lista=sorted(lista)

def ar(lista):
    razlika=lista[1]=lista[0]
    true=[]
    for i in range(len(lista)-1):
        if (lista[i+1]-lista[i])==razlika:
            true.append(True)
        else:
            true.append(False)
    if all(true)==True:
        return print('Moze')
    else:
        return print('Ne moze')


print(ar(lista))