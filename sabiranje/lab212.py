

def proveraMag(n,matrix):
    sum = int((n * (n ** 2 + 1)) / 2)
    suma_vrsta=0
    suma_kolona=0
    for i in range(n):
        suma_vrsta=0
        for j in range(n):
            suma_vrsta+=matrix[i][j]
        if suma_vrsta!=sum:
            return False
    for i in range(n):
        for j in range(n):
            suma_kolona+=matrix[j][i]
        if suma_kolona!=sum:
            return False
    return True



class Node():

    def __init__(self, matrix):
        self.matrix=matrix
        self.nivo=None
        self.magicni=None
        self.savrseni=None
        self.roditelj=None
        self.sinovi=[]
        self.used=[]


    def __repr__(self):
        #return repr(self.matrix)
        for i in range(n):
            for j in range(n - 1):
                print(matrica[i][j], end=" ")
            print(matrica[i][n - 1])

class ListaMatrica:
    def __init__(self):
        self.items=[]

    def addItem(self,newItem):
        self.items.append(newItem)

    def __repr__(self):
        return print(self.items)

print("Unesite dimenziju")
n=int(input())

print("Unesite elemente:\n")
lista1=input().split()
for i in range(n*n):
    lista1[i]=int(lista1[i])

sum=int((n*(n**2+1))/2)

for i in range(len(lista1)):
    print(lista1[i], end=" ")

print("\n")

print("Zadajte inicijalno stanje matrice:\n")

matrica=[]
for _ in range(n):
    red = input().split(" ")  # [9,11,13]
    red = [int(i) for i in red]
    matrica.append(red)

for i in range(n):
    for j in range(n-1):
        print(matrica[i][j], end=" ")
    print(matrica[i][n-1])

lista2=[]
for i in range(n):
    for j in range(n):
        lista2.append(matrica[i][j])

new=set(lista1)-set(lista2)

lista=list(new)

print("\n")
print(sum)
print("\n")

root=Node(matrica)


if proveraMag(n,matrica):
    print("Jeste magicni")
else:
    print("Nije")


print("\n")
