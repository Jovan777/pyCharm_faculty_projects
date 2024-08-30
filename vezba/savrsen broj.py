# napisati broj koji ispituje da li je naki broj savrsen

def savrsen_broj(n):
    p=0
    i=1
    while i<n:
        if n%i==0:
            p+=i
        i+=1
    if p==n:
        return True
    else:
        return False

n=input().split()
for i in range(len(n)):
    n[i]=int(n[i])

lista_savrsenih=[]
for i in range(len(n)):
    if savrsen_broj(n[i]):
        lista_savrsenih.append(n[i])
    else:
        continue
print('Od unetih brojeva u listu, savrseni brojevi su {} i ima ih {}'.format(lista_savrsenih,len(lista_savrsenih)))