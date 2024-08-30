r, c = input().split()
r=int(r)
c=int(c)
list1=[]
v=1
for i in range(r):
    list2=[]
    for j in range(c):
        list2.append(v)
        v=v+1
    list1.append(list2)


for i in range(r):
    for j in range(c):
        print(list1[i][j],end=" ")
    print()   