# potrebno je napraviti funkciju koja od zadatog broja pravi paskalov red
def binomni_koef(n,k):
    if k==0 or k==n:
        return 1
    else:
        return binomni_koef(n-1,k-1)+binomni_koef(n-1,k)
def pascal_triangle(n):
    outer=[]
    for i in range(n):
        inner=[]
        for j in range(i+1):
           inner.append(binomni_koef(i,j))
           outer.append(inner)
    return outer

def printpascalt(pascal_triangle):
    for i in range(len(pascal_triangle)):
        for j in range(len(pascal_triangle[i])):
           a= print(pascal_triangle[i][j],end='' if j != len(pascal_triangle[i])-1 else '\n')
    return a

z=printpascalt(pascal_triangle(5))
print(z)
