brojevi = [int(i) for i in input().split(" ") ]

# Ovde dodati kod
brojevi2 = list(brojevi)
lista=[]
for i in brojevi2:
    if i%2==0:
        lista.append(i)
print(min(lista))