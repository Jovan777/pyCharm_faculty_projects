lista1, lista2 , lista3=[8,3,5,6,7], [9,0,3,8,7],[0,3,2,1,5]

#potrebno je pronaci razliku prva dva skupa
#prvo pravimo skupove od listi

def presek(lista1,lista2):
    set0,set1=set(lista1),set(lista2)
    return set0.intersection(set1)

def unija(*lists):
    sets=[set(list) for list in lists]
    result_set=sets[0]
    for i in range(len(sets)):
        result_set=result_set.intersection(sets[i])
    return result_set

def razlika(*lists):
    sets=[set(list) for list in lists]
    razlike=[] #u ovaj skup smestamo razlike jednog skupa u odsnosu na sve ostale
    for i in range(len(sets)):
        trenutni_set=sets[i]
        for j in range(len(sets)):
            if i != j:
                trenutni_set=trenutni_set.difference(sets[j])
        razlike.append(trenutni_set)
    return set.union(*razlike)

print(razlika(lista1,lista2,lista3))





print(unija(lista1,lista2,lista3))





print(razlika(lista1,lista2))