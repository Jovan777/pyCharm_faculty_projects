#program za prozvodi vektora

p=input('p: ').split(', ')
q=input('q: ').split(', ')

p[0] = float(p[0])
p[1] = float(p[1])
p[2] = float(p[2])
q[0] = float(q[0])
q[1] = float(q[1])
q[2] = float(q[2])

s=p[0]*q[0]+p[1]*q[1]+p[2]*q[2] #skalarni proizvod
#za vektorski proizvod nam treba nova lista posto vektor ima vise parametara
v=[]
v.append(p[1]*q[2]+p[2]*q[1])
v.append(p[0]*q[2]+p[2]*q[0])
v.append(p[1]*q[0]+p[0]*q[1])


