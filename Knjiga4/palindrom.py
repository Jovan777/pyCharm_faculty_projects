#unese se lista i napravi se palindrom te liste

lista=['n','a','s','e','b','e','j']

out=''
length=len(lista)
i=0
while i<length:
    out=out+lista[i]
    i=i+1

length=length*-1
i=-2
while i>=length:
    out=out+lista[i]
    i=i-1
print(out)