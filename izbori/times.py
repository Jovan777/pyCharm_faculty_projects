


def readClientTimes():
    vremena=[]
    times=input().split()
    for i in range(len(times)):
        vremena.append(times[i])
    for i in range(len(vremena)):
        vremena[i]=int(vremena[i])
    return vremena

q = [1, 2, 3, 4, 5]
def writeQueue(q):
    if len(q)==0:
        return None
    else:
        ispis=''
        for i in range(len(q)-1):
            ispis+=str(q[i])+'->'
        ispis+=str(q[-1])
        print(ispis,end="")

#clientTimes = [7 , 2, 3, 4, 5]
clientTimes=readClientTimes()

def totalWorkHours(clientTimes):

    salter1=[]
    salter2=[]
    for klijent in clientTimes:
        if sum(salter1)<=sum(salter2):
            salter1.append(klijent)
        else:
            salter2.append(klijent)
    z = (max(sum(salter1), sum(salter2)))
    if len(salter1) == 0:
        return None
    else:
        s1 = ''
        for i in range(len(salter1) - 1):
            s1 += str(salter1[i]) + '->'
        s1 += str(salter1[-1])
    if len(salter2) == 0:
        return None
    else:
        s2 = ''
        for i in range(len(salter2) - 1):
            s2 += str(salter2[i]) + '->'
        s2 += str(salter2[-1])

    ispis='{}\n{}\n{}'.format(s1,s2,z)
    return ispis

print(totalWorkHours(clientTimes))