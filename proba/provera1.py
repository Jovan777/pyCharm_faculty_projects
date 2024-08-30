
lista = input("Lista: ").split( )
for i in range(len(lista)):
    lista[i] = int(lista[i])
tr_duz = max_duz = 1
tr_ind = max_ind = 0


for i in range(1, len(lista)):
    if lista[i] > lista[i - 1]:
        tr_duz += 1
    else:
        if tr_duz > max_duz:
            max_duz = tr_duz
            max_ind = tr_ind
    tr_duz = 1
    tr_ind = i
if tr_duz > max_duz:
    max_duz = tr_duz
    max_ind = tr_ind
podlista = []
z=max_ind+max_duz
for i in range(max_ind, z):
    podlista.append(lista[i])
print("Podlista: {}".format(podlista))
