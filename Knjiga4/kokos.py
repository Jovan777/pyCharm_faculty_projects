smoothies=['coconut','strawberry','banana','tropical','acai berry']
has_coconut=[True,False,False,True,False]
i=0
while i <len(has_coconut):
    if has_coconut[i]:
        print(smoothies[i],' sadrzi kokos')
    i+=1
smothie=''
for smothie in smoothies:
    print('We serve ', smothie)

k=0
length=len(smoothies)
for k in range(length):
    print('Smoothie #'+str(k),smoothies[k])