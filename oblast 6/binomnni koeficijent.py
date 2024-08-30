#potrebno je napraviti funkciju koja izracunava binomni koeficijent po formuli
#(n, k)=(n-1,k-1)+(n-1,k)

def binomni_koef(n,k):
    if k==0 or k==n:
        return 1
    else:
        return binomni_koef(n-1,k-1)+binomni_koef(n-1,k)

a=binomni_koef(5,3)
print(a)