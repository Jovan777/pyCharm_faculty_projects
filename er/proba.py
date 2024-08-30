def readNumbers ():
    lista = input().split(",")
    for i in range(len(lista)):
        lista[i] = int(lista[i])
    return lista

def readPairs():
    n = int(input())
    lista_parova = []
    for i in range(n):
        parovi = input().split(',')
        parovi[0] = int(parovi[0])
        parovi[1] = int(parovi[1])
        lista_parova.append(parovi)
    return lista_parova
def copyNumbers(arr1):
    arr2 = []
    for i in range(len(arr1)):
        arr2.append(arr1[i])
    return arr2
def swap(ind1, ind2, arr1):
    pomocna = arr1 [ind1]
    arr1 [ind1] = arr1 [ind2]
    arr1 [ind2] = pomocna
    return arr1
def compareArrays(arr1, arr2):
    if len(arr1) != len(arr2):
        return 'Nije isti'
    else:
        for i in range(len(arr1)):
            if arr1[i] != arr2[i]:
                return 'Nije isti'
        return 'Jeste isti'

arr1 = readNumbers()
lista_parova = readPairs()
arr2 = copyNumbers(arr1)
for i in range(len(lista_parova)):
    if (0 < lista_parova[i][0] < len(arr1)) & (0 < lista_parova[i][1] < len(arr1)):
        ind1 = lista_parova[i][0]
        ind2 = lista_parova[i][1]
        arr1 = swap(ind1, ind2, arr1)
provera = compareArrays(arr1, arr2)
print(arr1)
print(arr2)
print(provera)