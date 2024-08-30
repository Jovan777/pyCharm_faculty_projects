p = input("p: ").split(", ")
q = input("q: ").split(", ")

#preko for petlje proci kroz sve elemente

for i in range(len(p)):
    p[i]=float(p[i])
    q[i]=float(q[i])

s=0
for i in range(len(p)):
    s=s+p[i]*q[i]



print("{} * {} = {}".format(p, q, s))
