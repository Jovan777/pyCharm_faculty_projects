#program koji nasumicno generise broj i uzima korisnikov i gleda da li se poklapaju
import random as r

def kviz():
    n=int(input('Unesite broj: '))
    m=int(input('Unesite maximalni broj ponavljanja: '))
    a=n
    p=r.randint(1,n)
    pokusaj=1
    while True:
        z = int(input('Unesite broj: '))
        if pokusaj!=m:
            if z==p:
                if pokusaj==1:
                    return print('Uspeli ste, trebao vam je jedan pokusaj!')
                else:
                    return print('Uspeli ste, trebalo vam je {} pokusaja!'.format(pokusaj))
            else:
                pokusaj+=1

        else:
            p=r.randint(1,a)
            pokusaj=0


z=kviz()
print(z)
