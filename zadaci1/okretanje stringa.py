def unos():
    return input().split()

def rotacija(reci,k):
    if abs(k)>0:
        k=k%len(reci)
        string=reci[-k:]+reci[:len(reci)-abs(k)]
        reci.clear()
        reci.extend(string)
    return reci

q=unos()
q=rotacija(q,-2)
print(rotacija(q,-2))
