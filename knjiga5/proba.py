def get_bark(weight):
    if weight>20:
        return 'V V'
    else:
        return 'v v'
pas=get_bark(21)
print(pas)

def make_greeting(name):
    return 'Zdravo '+name+'!'
poz=make_greeting('Goku')
print(poz)

def compute(x,y):
    total=x+y
    if total>10:
        total=10
    print(total)
    return total
sabiranje=compute(-2,9)
print(sabiranje)

def allow_acces(person):
    if person=='Dr':
        answer='True'
    else:
        answer=False
    return answer

ulazak=allow_acces('Dr')
print(ulazak)