scores=[60,50,60,58,54,54,58,50,52,54,48,69,34,55,51,52,44,51,
        69,64,66,55,52,61,46,31,57,52,44,18,41,53,55,61,51,44]

costs=[.25,.27,.25,.25,.25,.25,.33,.31,.25,.29,.27,.22,.31,.25,
       .25,.33,.21,.25,.25,.25,.28,.25,.24,.22,.20,.25,.30,.25,.24,.25,
       .25,.27,.25,.26,.29]

high_score=0
length=len(scores)
for i in range(length):
    print('Rastvor #'+str(i),'rezultat: ',scores[i])
    if scores[i]>high_score:
        high_score=scores[i]

best_res=[]
for i in range(length):
    if scores[i]==high_score:
        best_res.append(i)

print('Broj testova je:', length)
print('Najbolji rezultat je:',high_score)
print('Rastvori sa najboljim rezultatom su:',best_res)

cost=100.0
most_effective=0
for i in range(length):
    if scores[i]==high_score and costs[i]<cost:
        most_effective=i
        cost=costs[i]
print('Rastvor #'+str(most_effective),' je najisplativiji sa cenom',costs[most_effective])

for i in range(len(best_res)):
    index=best_res[i]
    if costs[index]<cost:
        most_effective=i
        cost=costs[index]
print(most_effective,cost)