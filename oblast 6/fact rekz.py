#potrebno je napraviti funkciju koja racuna faktorijel unetog broja preko rekurzije

def fact(n):
    if n==1:
        return n
    else:
        return n * fact(n-1)

a=fact(5)
print(a)
