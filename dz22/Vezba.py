def sumaVrsta (mat):
    lista=[]
    for i in range(len(mat)):
        sum=0
        for j in range(len(mat[i])):
                sum+=mat[i][j]
        lista.append(sum)
    return lista
mat = [[j for j in range(4)] for i in range(3)]
print(sumaVrsta(mat))