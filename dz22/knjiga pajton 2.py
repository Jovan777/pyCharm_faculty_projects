#program racuna najduzi niz 0 u binarnom broju

def najduzi_niz(x):
    d=0
    maxd=0
    prva_jedinica=True

    while True:
        bin_cifra=x%2
        if bin_cifra==0:
            d = d + 1
            prva_jedinica=True
        elif prva_jedinica:
            prva_jedinica=False
            if d>maxd:
                maxd=d
            d=0

        x//2
        if x==0:
            break
    return maxd

najduzi_niz(44)








