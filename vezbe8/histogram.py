#funkcija broji koliko se puta koji karakter pojavio u iskazu

def createHistogram(sentence):
    histogram=[0]*26
    for character in sentence:
        if character.isalpha():
            index=ord(character)-ord('a')
            histogram[index]+=1

    return histogram


def isHeterogram(sentence):
    list=[]
    for char in sentence:
        if char.isalpha():
            list.append(char)
    return len(set(list))==len(sentence)

sentence=input()
histogram=(createHistogram(sentence))
#proveriti da li u histogramu ima nesto vece od 1

isHet= not any(value>1 for value in histogram)


if( isHet):
    print('JESTE HETEROGRAM')
else:
    print('NIJE HETEROGRAM')

#sad je potrebno napraviti funkiju za pangram

def isPangram(sentence):
    #sva slova se pojavljuju barem jednom
    alphabet={chr(i) for i in range(ord('a'),ord('z')+1)}
    letters={letter.lower() for letter in sentence}
    return len(letters)==len(alphabet)

print(isPangram('AVSKAS'))

isPAN=not any([vallue==0 for vallue in histogram ])

if isPAN:
    print('Jeste pangraf')
else:
    print('Nije pangraf')