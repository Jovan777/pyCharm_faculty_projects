#potrebno je napraviti fukciju koja racuna binomni koeficijent (n, k) po formuli (n+1-i)/i dok i ne bude jednako k


def binomni_koef(n, k):
    a=1
    for i in range(1,k+1):
        a*=(n+1-i)
        a//=i
    return a

z=binomni_koef(2,1)
print(z)