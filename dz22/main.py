list=input().split()
for i in range(len(list)):
    list[i]=int(list[i])

a=[]
b=[]
c=[]

for i in range(len(list)):
    if list[i]%3==0:
        a.append(list[i])
    elif list[i]%2==0:
        b.append(list[i])
    elif  not list[i]==0:
        c.append(list[i])
print(a+b+c)
print(len(a),len(b),len(c))