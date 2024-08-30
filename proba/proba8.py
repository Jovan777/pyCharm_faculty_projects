#provera da li je broj prost

import math
import random

broj=random.randint(0,1000)
n = int(input("Unesite broj: "))
print(broj)



for i in range(2, math.ceil(n**0.5) + 1):
    if n % i == 0:
        print("Prvi broj nije prost!")
        break
    else:
        print("Prvi broj je prost!")

for i in range(2, math.ceil(broj**0.5) + 1):
    if broj % i == 0:
        print("Drugi broj nije prost!")
        break
    else:
        print("Drugi broj je prost!")