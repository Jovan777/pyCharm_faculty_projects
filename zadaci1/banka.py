def unos():
    n = int(input())
    red = list(map(int, input().split(" ")))
    return red

k=[7,2,3,4,5]


def obrada(klijenti):
    s1=[]
    s2=[]
    for klijent in klijenti:
        if (sum(s1) <= sum(s2)):
            s1.append(klijent)
        else:
            s2.append(klijent)
    r=print(max(sum(s1),sum(s2)))
    return r

z=obrada(k)
print(z)
