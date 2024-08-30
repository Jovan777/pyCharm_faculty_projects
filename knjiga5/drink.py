def drink_me(param):
    msg='Drinking '+param+' glass'
    print(msg)
    param='empty'
    msg1='The glass is '+param
    print(msg1)

glass='full'
drink_me(glass)
print('The glass is', glass)