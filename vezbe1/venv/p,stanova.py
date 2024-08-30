

def read(fajl):
    with open(fajl) as ulaz:
        lista=[]
        lista_soba=[]
        for linija in ulaz:
            ulica,broj,broj_soba,*sobe=linija.split(' ')
            lista.append([ulica,int(broj),int(broj_soba),sobe])
            lista_soba.append(sobe)
        #for i in range(len(lista[3])):
            #lista[3][i]=int(lista[3][i])
        for i in range(len(lista_soba)):
            for j in range(len(lista_soba[i])):
                lista_soba[i][j]=int(lista_soba[i][j])
    '''
    povrsine=[]
    for i in range(len(lista_soba)):
        povrsine.append(povrsina(lista_soba[i]))
    '''
    a=lista
    b=lista_soba

    return a,b

def povrsina(lista):
    s=0
    p=[]
    while s<len(lista):

        p.append(lista[s]*lista[s+1])
        s+=2
    return sum(p)

def ulaz():
    min=int(input('Unesite minimalnu trazenu povrsinu:'))
    max=int(input('Unesite maximalnu trazenu povrsinu:'))
    if min>max:
        while True:
            if min<max:
                min = int(input('Unesite minimalnu trazenu povrsinu:'))
                max = int(input('Unesite maximalnu trazenu povrsinu:'))
                if max>min:
                    break
    return min,max




def provera(lista,min,max):
    #ulaz=list(*ulaz)
    #z1=ulaz[0]
    #z2=ulaz[1]
    pogodne=[]
    for i in range(len(lista)):
        if lista[i]>=min:
            if lista[i]<=max:
                pogodne.append(lista[i])
    return pogodne

#print(provera(lista_p))
'''
def obrada(lista):
    stanovi=[]
    for i in range(len(lista)):
'''
#print(provera(lista_p,ulaz())) radi
s=read('stanovi.txt')
lista_p=[]
lista_soba=s[1]
for i in range(len(s[1])):
    lista_p.append(povrsina(s[1][i]))
lista_stanova=s[0]
lista_filter=[]
'''
for i in range(len(lista_soba)):
    if (provera(povrsina(lista_soba)),ulaz())==lista_p[i]:
        lista_filter.append(lista_stanova[i])
'''
z=ulaz()
min=z[0]
max=z[1]
k=[]

for i in range(len(lista_stanova)):
    k.append(povrsina(lista_stanova[i][3]))
#print(k)
pogodni=[]
for i in range(len(lista_p)):
    if provera(lista_p,min,max)==povrsina(lista_stanova[i][3]):
        pogodni.append(lista_stanova[i])
print(pogodni)


#with open('filter.txt','w') as izlaz:

    #izlaz.write('{}'.format(lista_soba))
