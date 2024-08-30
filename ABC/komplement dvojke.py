#program treba da prevede binarni broj u decimalni ali preko komplementa dvojke


n=int(input('Unesite broj bitova: '))
p=input('Unesite binarni broj: ')
k=int(p,2)
c=n-1
if k>(2**c-1):
    k=(2**n-k)*(-1)
elif k<(2**c):
    k=(2**n-k)
else:
    k=k
print(k)
