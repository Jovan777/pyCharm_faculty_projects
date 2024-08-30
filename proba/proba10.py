#ispisivanje nekih lista
empty=[]
print(empty)

brojevi=[1,2,3,4,5]
print(brojevi)

pajton = ['python', 3, 3.8, True]
print(pajton)

print(pajton[0] + str(pajton[1]))

print(brojevi[-1])

print('Python verzija: ',pajton[1:3])

print("Neparni brojevi: ", brojevi[0:5:2])

print(brojevi[2:])

print(brojevi[:3])

print(brojevi[4:0:-2])

print(brojevi[-2:])

print(5 in brojevi)

print(15 in brojevi)

print(pajton.index(3))

pajton[0]='pajton_old'
print(pajton)

pajton[1:3]=[2,2.7]
print(pajton)



for i in range(len(brojevi)):
    brojevi[i]=brojevi[i]*10
print(brojevi)


etf=list('ETF')
print(etf)

all_ones=[1]*10
print(all_ones)

brojevi.append(6)

brojevi.insert(0,10)

brojevi+=[7,8,9]

print(brojevi)

brojevi.extend([11,12])

del brojevi[4]

print(brojevi)

print(brojevi.pop())

print(brojevi.pop(2))
print(brojevi)

brojevi.remove(10)

print(brojevi)

print(len(brojevi))

print(sum(brojevi))

print(max(brojevi), min(brojevi))

brojevi.reverse()
print(brojevi)

nova=sorted(brojevi)

print(nova)

brojevi.sort()
print(brojevi)

print(brojevi.count(50))

brojevi2=list(brojevi)
brojevi2[0]=100
print(brojevi2)
print(brojevi)

lista=[1,2,3]
for i in lista:
    print(i)