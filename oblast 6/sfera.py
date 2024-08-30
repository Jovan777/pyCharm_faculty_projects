#program treba da racuna poluprecnik i povrsinu upisane sfere od zadate duzine ivice kocke a

import math

def povrsina_sfere(o):
    return 4 * o**2 * math.pi

a=int(input('Unesite ivicu kocke: '))

r=a*math.sqrt(3)/2

p=povrsina_sfere(r)

print('r={:.2f},P={:.2f}'.format(r,p))
