'''#Na programskom jeziku Python sastaviti program
koji iz liste celih brojeva izdvaja najdužu podlistu
koja je uređena strogo rastuće. Pretpostaviti da
lista sadrži bar jedan element.'''
#prvo ucitati elemente liste

Lista=input('Lista: ').split()
for i in range(len(Lista)):
    Lista[i]=int(Lista[i]) #pretvaranje elemenata koji su do sad bili string u cele brojeve

tr_duz=max_duz=1
tr_ind=max_ind=0

for i in range(1, len(Lista)):
    if Lista[i]>Lista[i-1]:
        tr_duz =tr_duz+1
    else:
        if tr_duz>max_duz:
            max_duz=tr_duz
            max_ind=tr_ind
    tr_ind=i
    tr_duz=1
if tr_duz > max_duz:
    max_duz = tr_duz
    max_ind = tr_ind

podlista=[]
for i in range(max_ind,max_duz+max_ind):
    podlista.append(Lista[i])

print(podlista)



