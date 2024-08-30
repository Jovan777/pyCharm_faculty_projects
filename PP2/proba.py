list=input().split()
for i in range(len(list)):
    list[i]=int(list[i])
list2=[]
for i in range(len(list)):
    if list[i]%3==0:
        list2.append(list[i])
def razlika(lista1, lista2):
    lista3= [i for i in lista1 + lista2 if i not in lista1 or i not in lista2]
    return lista3
list3=razlika(list,list2)
for i in range(len(list3)):
    if list3[i]%2==0:
        list2.append(list3[i])
for i in range(len(list)):
    if not list[i]%3==0:
        if not list[i]%2==0:
            list2.append(list[i])


x=0
z=0
y=0
for i in range(len(list2)):
    if list2[i]%3==0:
        x=x+1
    elif list2[i]%2==0 and list2[i]%3 !=0:
        z=z+1
    else:
        y=y+1
print(str(list2))
print(x,z,y)