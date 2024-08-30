def unos():
    n = input()
    n = int(n)
    matrica = []
    for _ in range(n):
        red = input()
        matrica.append(red)
    return matrica

def obrada(matrica):
    for i in range(len(matrica)):
        matrica[i]=sorted(matrica[i])
    return matrica
def ispis(matrica):
    n = len(matrica)
    m = len(matrica[0])
    for i in range(n):
        for j in range(m-1):
            print(matrica[i][j], end="")
        print(matrica[i][m-1],end='\n' if i+1<n else"")
    print()
    print('Da',end="")

matrica=unos()
matrica=obrada(matrica)
ispis(matrica)