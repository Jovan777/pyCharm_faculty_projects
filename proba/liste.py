lista=[]

n=int(input('Unesite broj elemenata liste: '))
for i in range(0, n):
    lista.append(int(input()))
minimum=min(lista)
res=[]
for i in range(len(lista)-2):
    trojka=lista[i:i+3]
    if minimum not in trojka:
        continue
    res.append(trojka)
print(res)

