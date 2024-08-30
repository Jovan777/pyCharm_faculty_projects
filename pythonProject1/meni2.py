
class Node:
    def __init__(self):
        self.koef = None
        self.eksp = None
        self.sledeci = None
class KruznaLista:
    def __init__(self):
        self.head=Node()
        self.head.sledeci=self.head

def dodaj(pocetak, koef, eksp):
    KruznaLista.head=pocetak
    noviP = Node()
    noviP.koef = koef
    noviP.eksp = eksp
    noviP.sledeci = None

    if (pocetak == None):
        return noviP

    temp = pocetak
    while (temp.sledeci != None):
        temp = temp.sledeci
    temp.sledeci = noviP
    return pocetak

def ispisi(temp):
    while (temp.sledeci != None):
        print(str(temp.koef) + 'x^' + str(temp.eksp), end='')
        if (temp.sledeci != None and temp.sledeci.koef >= 0):
            print('+', end='')
        temp = temp.sledeci
    print(temp.koef)

def vrednost_x(poly1):
    temp1=poly1
    print("Unesite vrednost za x: \n")
    x=int(input())
    polinom=0
    while(temp1!=None):

            polinom += (x**temp1.eksp)*temp1.koef

            temp1 = temp1.sledeci


    return polinom

def duplikati(pocetak):
    temp2 = None
    dup = None
    temp1 = pocetak

    while (temp1 != None and temp1.sledeci != None):
        temp2 = temp1

        while (temp2.sledeci != None):

            if (temp1.eksp == temp2.sledeci.eksp):

                temp1.koef = temp1.koef + temp2.sledeci.koef
                dup = temp2.sledeci
                temp2.sledeci = temp2.sledeci.sledeci
            else:
                temp2 = temp2.sledeci

        temp1 = temp1.sledeci
def izbrisi(p1):
    p1=dodaj(p1,0,0)

def saberi(p1, p2, p3):
    t1 = p1
    t2 = p2

    while (t1 != None):
        while (t2 != None):
            if t1.eksp == t2.eksp:
                neksp = t1.eksp
                koef = t1.koef + t2.koef

                p3 = dodaj(p3, koef, neksp)

            t2 = t2.sledeci

        t2 = p2
        t1 = t1.sledeci

    duplikati(p3)
    return p3

def mnozenje(polinom1, polinom2, polinom3):
    temp1 = polinom1
    temp2 = polinom2

    while (temp1 != None):
        while (temp2 != None):
            koef = temp1.koef * temp2.koef

            eksp = temp1.eksp + temp2.eksp
            polinom3 = dodaj(polinom3, koef, eksp)

            temp2 = temp2.sledeci
        temp2 = polinom2

        temp1 = temp1.sledeci

    duplikati(polinom3)
    return polinom3

if __name__ == '__main__':
        polinom1=None
        polinom2=None
        polinom3=None
        polinom4=None
        polinom5=None
        polinom6=None

        #pomocni1=None
        #pomocni2=None
        #pomocni3=None
        #pomocni4=None
        #pomocni5=None

print("Izaberite opciju(0 za kraj rada): ")
print("1.Ucitavanje novog polinoma")
print("2.Dodavanje clana polinomu")
print("4.Ispis zadatog polinoma")
print("5.Racunanje vrednosti polinoma za unetu vrednost"
      " promenljive x")
print("7.Mnozenje polinoma")
print("8.Brisanje polinoma")

print("Izaberite opciju(0 za kraj rada): ")
n=int(input())
while(n!=0):


        if n==1:
            print("Izaberite polinom(1-5): \n")
            print("npr. polinom1")
            p=input()
            if p=="polinom1":
                print("Unesite prve podatke za odabrani polinom:\n")
                polinom1 = dodaj(polinom1, int(input()), int(input()))
                iskaz1 = "da"
                while (iskaz1 == "da"):
                    print("Novi broj?\n")
                    iskaz1 = input()
                    if iskaz1 == "da":
                        polinom1 = dodaj(polinom1, int(input()), int(input()))
                    elif iskaz1 == "ne":
                        prvi=polinom1
                        continue
            if p == "polinom2":
                print("Unesite prve podatke za odabrani polinom:\n")
                polinom2 = dodaj(polinom2, int(input()), int(input()))
                iskaz1 = "da"
                while (iskaz1 == "da"):
                    print("Novi broj?\n")
                    iskaz1 = input()
                    if iskaz1 == "da":
                        polinom2 = dodaj(polinom2, int(input()), int(input()))
                    elif iskaz1 == "ne":
                        drugi=polinom2
                        continue
            if p == "polinom3":
                print("Unesite prve podatke za odabrani polinom:\n")
                polinom3 = dodaj(polinom3, int(input()), int(input()))
                iskaz1 = "da"
                while (iskaz1 == "da"):
                    print("Novi broj?\n")
                    iskaz1 = input()
                    if iskaz1 == "da":
                        polinom3 = dodaj(polinom3, int(input()), int(input()))
                    elif iskaz1 == "ne":
                        treci=polinom3
                        continue
            if p == "polinom4":
                print("Unesite prve podatke za odabrani polinom:\n")
                polinom4 = dodaj(polinom4, int(input()), int(input()))
                iskaz1 = "da"
                while (iskaz1 == "da"):
                    print("Novi broj?\n")
                    iskaz1 = input()
                    if iskaz1 == "da":
                        polinom4 = dodaj(polinom4, int(input()), int(input()))
                    elif iskaz1 == "ne":
                        cetrvti=polinom4
                        continue
            if p == "polinom5":
                print("Unesite prve podatke za odabrani polinom:\n")
                polinom5 = dodaj(polinom5, int(input()), int(input()))
                iskaz1 = "da"
                while (iskaz1 == "da"):
                    print("Novi broj?\n")
                    iskaz1 = input()
                    if iskaz1 == "da":
                        polinom5 = dodaj(polinom5, int(input()), int(input()))
                    elif iskaz1 == "ne":
                        peti=polinom5
                        continue

        print("Izaberite novu opciju: ")
        n=int(input())

        if n==2:
            print("Unesite polinom kojem zelite da dodate clan: \n")
            print("npr. polinom1")
            j=input()
            if j=="polinom1":
                print("Unesite koeficijent i eksponent")
                polinom1=dodaj(polinom1,int(input()),int(input()))
            if j=="polinom2":
                print("Unesite koeficijent i eksponent")
                polinom2=dodaj(polinom2,int(input()),int(input()))
            if j=="polinom3":
                print("Unesite koeficijent i eksponent")
                polinom3=dodaj(polinom3,int(input()),int(input()))
            if j=="polinom4":
                print("Unesite koeficijent i eksponent")
                polinom4=dodaj(polinom4,int(input()),int(input()))
            if j=="polinom5":
                print("Unesite koeficijent i eksponent")
                polinom5=dodaj(polinom5,int(input()),int(input()))


        #if n==3:

        if n==4:
            print("Unesite polinom koji zelite da se napise(polinom prethodno mora biti definisan): \n")
            print("npr. polinom1")
            izbor=input()
            if izbor=="polinom1":
                ispisi(polinom1)
            elif izbor=="polinom2":
                ispisi(polinom2)
            elif izbor=="polinom3":
                ispisi(polinom3)
            elif izbor=="polinom4":
                ispisi(polinom4)
            elif izbor=="polinom5":
                ispisi(polinom5)

        if n==5:
            print("Unesite za koji polinom treba da se racuna vrednost po x: \n")
            print("npr. polinom1")
            k=input()
            if k=="polinom1":
                z=vrednost_x(polinom1)
                print(z)
            if k=="polinom2":
                z = vrednost_x(polinom2)
                print(z)

        if n==6:
            print("Unesite polinome koje zelite da saberete: \n")
            print("Prvi polinom: \n")
            p1 = input()
            a = 0
            b = 0
            if p1=="polinom1":
                a=polinom1
            elif p1=="polinom2":
                a=polinom2
            elif p1=="polinom3":
                a=polinom3
            elif p1=="polinom4":
                a=polinom4
            else:
                print("Neispravan unos")
                continue
            print("Drugi polinom: \n")
            p2=input()
            if p2=="polinom1":
                b=polinom1
            elif p2=="polinom2":
                b=polinom2
            elif p2=="polinom3":
                b=polinom3
            elif p2=="polinom4":
                b=polinom4
            else:
                print("Neispravan unos")
            polinom6 = saberi(a, b, polinom6)
            print("Vrednost sabranih polinoma je: \n")
            ispisi(polinom6)



        if n==7:
            print("Unesite polinome koje zelite da pomnozite: \n")
            print("Prvi polinom: \n")
            p1=input()
            m=0
            n=0
            if p1=="polinom1":
                m=polinom1
            elif p1=="polinom2":
                m=polinom2
            elif p1=="polinom3":
                m=polinom3
            elif p1=="polinom4":
                m=polinom4
            else:
                print("Neispravan unos")
                continue
            print("Drugi polinom: \n")
            p2=input()
            if p2=="polinom1":
                n=polinom1
            elif p2=="polinom2":
                n=polinom2
            elif p2=="polinom3":
                n=polinom3
            elif p2=="polinom4":
                n=polinom4
            else:
                print("Neispravan unos")

            #print("Unesite polionome koje zelite da pomnozite: ")
            polinom5=mnozenje(m,n,polinom5)
            print("Vrednost pomnozenih polinoma je: \n")
            ispisi(polinom5)

        if n==8:
            print("Unesite polinom koji zelite da obrisete: ")
            unos=input()
            if unos=="polinom1":
                izbrisi(polinom1)
            elif unos=="polinom2":
                izbrisi(polinom2)
            elif unos=="polinom3":
                izbrisi(polinom3)
            elif unos=="polinom4":
                izbrisi(polinom4)
            else:
                print("Neispravan unos")

print("Kraj rada.")