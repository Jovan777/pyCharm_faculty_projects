def unos():
    n, m = input().split(" ")
    n = int(n)
    m = int(m)
    matrica = []
    for _ in range(n):
        red = input().split(" ")  #[9,11,13]
        red = [int(i) for i in red]
        matrica.append(red)
    return matrica
def provera(matrica, i, j): #polje matrica[i,j]
    n = len(matrica)
    m = len(matrica[0])
    brojac = 0
    if(i-1>=0 and matrica[i-1][j] <= matrica[i][j]):
        brojac += 1
    if(i+1<n and matrica[i+1][j] <= matrica[i][j]):
        brojac += 1
    if(j-1>=0 and matrica[i][j-1] <= matrica[i][j]):
        brojac += 1
    if(j+1 < m and matrica[i][j+1] <= matrica[i][j]):
        brojac += 1
    if(i-1>=0 and j-1>=0 and matrica[i-1][j-1] <= matrica[i][j]):
        brojac+=1
    if(i+1<n and j-1>=0 and matrica[i+1][j-1] <= matrica[i][j]):
        brojac+= 1
    if(i+1<n and j+1<m and matrica[i+1][j+1] <= matrica[i][j]):
        brojac+=1
    if(j+1<m and i-1>=0 and matrica[i-1][j+1]<= matrica[i][j]):
        brojac += 1
    return brojac
def obrada(matrica):
    novamatrica = []
    for i in range(len(matrica)):
        novired = []
        for j in range(len(matrica[0])):
            novired.append(provera(matrica,i,j))
        novamatrica.append(novired)
    return novamatrica
def ispis(matrica):
    n = len(matrica)
    m = len(matrica[0])
    for i in range(n):
        for j in range(m-1):
            print(matrica[i][j], end=" ")
        print(matrica[i][m-1],end='\n' if i+1<n else"")
matrica = unos()
matrica = obrada(matrica)
ispis(matrica)
