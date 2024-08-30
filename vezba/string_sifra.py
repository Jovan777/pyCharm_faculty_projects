


string1=input()
string2=input()

def sifra(rec1,rec2):
    rec1=rec1.strip().lower()
    rec2=rec2.strip().lower()
    pomeraj=0
    ar=0
    if len(rec1)!=len(rec2):
        return False
    for i in range(len(rec1)):
        pomeraj+=ord(rec1[i])
        ar+=ord(rec1[i])//len(rec1)

    pomeraj=pomeraj//ar

    for i in range(len(rec1)): #moze se dodati posebno za zadnje reci alfabeta..x da bude b...
        if ord(rec1[i])+5==ord(rec2[i]):
            return True
        else:
            return False




print(sifra(string1,string2))