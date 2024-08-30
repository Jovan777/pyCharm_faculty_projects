def unos():
    n = int(input())
    red = list(map(int, input().split(" ")))
    greska = False
    if(len(red) != n):
        greska = True
    return red,greska


def obrada(red):
    salter1 = []
    salter2 = []
    for element in red:
        if(sum(salter1) <= sum(salter2)):
            salter1.append(element)
        else:
            salter2.append(element)
    print(max(sum(salter1), sum(salter2)))


red, greska = unos()
if(not greska):
    obrada(red)