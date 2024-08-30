

class NebeskaTela(object):
    galaksija="Mlecni put" #podrazumevana vrednost za tu klasu
    def __init__(self,tip,precnik,otkrivac):
        self.tip=tip
        self.precnik=precnik
        self.otkrivac=otkrivac

    def podaci(self):
        return "Ovo je %s precnika %d i otkrili su ga %s"%(self.tip, self.precnik, self.otkrivac)

    def citat(self):
        return "Postoji teorija koja kaze da ce, ukoliko ikada iko bude"

    def __repr__(self):
        return "Ovo je %s ima precnik %d i otkrili su je %s"%(self.tip, self.precnik, self.otkrivac)

sunce=NebeskaTela("zvezda", 1369000, "svi")

sunce.otkrivac+=" i niko"

class zivotinje(object):
    def __init__(self,vrsta, ime , godine):
        self.vrsta=vrsta
        self.ime=ime
        self.godine=godine

    def oglasavanje(self):
        return print(input())

    #def __repr__(self):
        #return "Ovo je "+self.vrsta+" zove se "+self.ime+"i ima "+self.godine


pas=zivotinje("pas", "Bagzi", 3)

class Planete(NebeskaTela):
    tip="Planeta"
    def __init__(self,precnik, otkrivac, zvezda):
        self.precnik=precnik
        self.otkrivac=otkrivac
        self.zvezda=zvezda

    def citat(self):
        return "Ispis planete"

    def podaci(self):
        stari=super(Planete, self).podaci()
        return stari+" Okrece se oko zvezde "+self.zvezda
        


'''
print(sunce.precnik)
print(zemlja.otkrivac)
print(sunce.citat())
print(zemlja.citat())
print(zemlja.tip)
'''



class Pas(zivotinje):
    vrsta="pas"

    def __init__(self, ime, ime_vlasnika):
        self.ime=ime
        self.ime_vlasnike=ime_vlasnika

    def oglasavanje(self):
        return "AV AV"


macka=zivotinje("Macka", "Tom", 3)
#macka.oglasavanje()

pas=zivotinje("pas", "Bagzi", 3)

#pas.oglasavanje()

pas2=Pas("Astor", "Jovan")


#print(pas2.oglasavanje())

print(pas)
print("\n");

print(pas2)


zemlja=Planete(6370, "svi mi", "Sunce")

print(zemlja)
print(sunce)