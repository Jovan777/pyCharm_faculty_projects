#napisati program koji ce unete tacke u jednom redu raspakovati na koordinate x i y

def tacke():
    n=input().split()
    xtacke=[]
    ytacke=[]
    koordinate=[]
    for i in range(0,len(n),2):
        xtacke.append(n[i])
    for i in range(1,len(n),2):
        ytacke.append(n[i])
    for i in range(len(xtacke)):
        koordinate.append(int(xtacke[i]))
        koordinate.append(int(ytacke[i]))



    return koordinate



q=tacke()
print(q)