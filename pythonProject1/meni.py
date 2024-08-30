
class Node:
    def __init__(self):
        self.koef = None
        self.eksp = None
        self.sledeci = None

def dodaj(pocetak, koef, eksp):
    # Create a new node
    noviP = Node()
    noviP.koef = koef
    noviP.eksp = eksp
    noviP.sledeci = None

    # If linked list is empty
    if (pocetak == None):
        return noviP

    # If linked list has nodes
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

def duplikati(pocetak):
    temp2 = None
    dup = None
    temp1 = pocetak

    while (temp1 != None and temp1.sledeci != None):
        temp2 = temp1

        while (temp2.sledeci != None):

            if (temp1.eksp == temp2.sledeci.eksp):

                # Add their coefficients and put it in 1st element
                temp1.koef = temp1.koef + temp2.sledeci.koef
                dup = temp2.sledeci
                temp2.sledeci = temp2.sledeci.sledeci
            else:
                temp2 = temp2.sledeci

        temp1 = temp1.sledeci

def mnozenje(polinom1, polinom2, polinom3):
    # Create two pointer and store the
    # address of 1st and 2nd polynomials
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


print("Izaberite opciju(0 za kraj rada): ")
print("1.Ucitavanje novog polinoma")
print("2.Dodavanje clana polinomu")
print("3.Brisanje clana polinoma")
print("4.Ispis zadatog polinoma")
print("5.Racunanje vrednosti polinoma za unetu vrednost"
      " promenljive x")
print("6.Sabiranje polinoma")
print("7.Mnozenje polinoma")
print("8.Brisanje polinoma")

print("Izaberite opciju(0 za kraj rada): ")
n=int(input())
while(n!=0):

    if __name__ == '__main__':
        polinom1=None
        polinom2=None
        polinom3=None
        polinom4=None
        polinom5=None

        pomocni1=None
        pomocni2=None
        pomocni3=None
        pomocni4=None
        pomocni5=None

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
                        break
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
                        break
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
                        break
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
                        break
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
                        break

        print("Izaberite novu opciju: ")
        n=int(input())

        #if n==2:

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

        if n==7:
            print("Unesite polionome koje zelite da pomnozite: ")
            prvi=polinom1
            drugi=polinom2
            pomocni3=mnozenje(polinom1,polinom2,polinom3)
            print("Vrednost pomnozenih polinoma je: \n")
            ispisi(pomocni1)

print("Kraj rada.")