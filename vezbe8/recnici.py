'''
opstine={
    'Vracar':123,
    'Palilula':12,
    'Zvezdara':1,
}

for k in opstine:
    print(k,opstine[k])

for k in opstine.keys():
    print(k, opstine[k])

for v in opstine.values():
    print(v)

for k,v in opstine.items():
    print(k,v)
'''

recnik3={
    'a':5,
    'b':9,
    'c':10
}

def printthree(a,b,c):
    print(a,b,c)

print(printthree(**recnik3))

def printcollection(**collection):
      print(collection)

printcollection(first_key=15,second_key=10)