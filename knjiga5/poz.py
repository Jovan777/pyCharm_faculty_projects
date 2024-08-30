greeting='Pozdrav'

def greet(name ,message):
    global greeting
    greeting='Hej'
    print(greeting,name+'.'+message)

greet('Goku','Vidimo se uskoro')
print(greeting)