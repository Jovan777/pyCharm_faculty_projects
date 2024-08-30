#potrebno je napraviti funkciju koja racuna faktorijel unetog broja
#prvo iterativnim postupkom

def faktorijel(n):
    a=1
    for i in range(1,n+1):
        a=a*i
    return a

b=faktorijel(5)
print(b)