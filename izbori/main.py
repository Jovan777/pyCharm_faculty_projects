

def readNumbers ():
        brojevi=input().split(',')
        for i in range(len(brojevi)):
            brojevi[i]=int(brojevi[i])
        return brojevi


def readPairs ():
    lista=[]
    broj_parova=int(input())
    for i in range(broj_parova):
        broj=input().split(',')
        for i in range(len(broj)):
            broj[i]=int(broj[i])
        lista.append(broj)
    return lista


def copyNumbers (arr):
    zed=arr
    return zed

def swap(ind1,ind2,arr):
    if ind1>=len(arr):
        return arr
    elif ind2>=len(arr):
        return arr
    else:
        t=arr[ind1]
        arr[ind1]=arr[ind2]
        arr[ind2]=t
        return  arr

def compareArrays(arr1, arr2):
    if len(arr1)!=len(arr2):
        return False
    d=True
    for i in range(len(arr1)-1):
        if arr1[i]==arr2[i]:
            d=True
        else:
            d=False
    return d

def printArray(arr):
    arr=str(arr)
    arr=arr.replace(' ',"").replace('[',"").replace(']',"")
    print( arr)

n=readNumbers()
k=readPairs()
j=n[:]
for i in range(len(k)):
    z=swap(k[i][0],k[i][1],n)
    printArray(z)
    #printArray(swap(k[i][1],k[i][0],n))

if j==z:
    print('ISTI')
else:
    print('NIJE ISTI')
