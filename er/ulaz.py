def readArray(n):
    if n==0:
        return None
    else:
        s = 0
        lista = []
        while s < n:
            lista.append(int(input()))
            s+=1
        return lista

arr=[1,2,3]
num=4

def add(arr,num):
    arr.append(num)
    return arr

num2=123

def reverse(num):
    num=str(num)
    num=num[::-1]
    return int(num)

def palindrom(num):
    if num==reverse(num):
        return True
    else:
        return False


def printArray(arr):
    print(list(arr))

n=int(input())
if n==0:
    print()
else:
    z=readArray(n)
    niz=[]
    for i in range(len(z)):
        if palindrom(z[i]):
            niz.append(z[i])

    printArray(niz)
