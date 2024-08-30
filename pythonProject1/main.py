# Python3 implementation of the above approach

# Node structure containing powerer
# and coefficient of variable
class Node:
    def __init__(self):
        self.coeff = None
        self.power = None
        self.next = None


# Function add a new node at the end of list
def addnode(start, coeff, power):
    # Create a new node
    newnode = Node();
    newnode.coeff = coeff;
    newnode.power = power;
    newnode.next = None;

    # If linked list is empty
    if (start == None):
        return newnode;

    # If linked list has nodes
    ptr = start;
    while (ptr.next != None):
        ptr = ptr.next;
    ptr.next = newnode;
    return start;


# Functionn To Display The Linked list
def printList(ptr):
    while (ptr.next != None):
        print(str(ptr.coeff) + 'x^' + str(ptr.power), end='')
        if (ptr.next != None and ptr.next.coeff >= 0):
            print('+', end='')
        ptr = ptr.next
    print(ptr.coeff)


# Function to add coefficients of
# two elements having same powerer
def removeDuplicates(start):
    ptr2 = None
    dup = None
    ptr1 = start;

    # Pick elements one by one
    while (ptr1 != None and ptr1.next != None):
        ptr2 = ptr1;

        # Compare the picked element
        # with rest of the elements
        while (ptr2.next != None):

            # If powerer of two elements are same
            if (ptr1.power == ptr2.next.power):

                # Add their coefficients and put it in 1st element
                ptr1.coeff = ptr1.coeff + ptr2.next.coeff;
                dup = ptr2.next;
                ptr2.next = ptr2.next.next;

            else:
                ptr2 = ptr2.next;

        ptr1 = ptr1.next;

def multiply(poly1,Npoly2, poly3):
    ptr1=poly1
    print("Unesi k i e")
    koeficijent=int(input())
    eksponent=int(input())
    while(ptr1!=None):
            #coeff = ptr1.coeff

            #power = ptr1.power




        ptr1 = ptr1.next

    return ptr1

# Function two Multiply two polynomial Numbers
def saberi(poly1, poly2, poly3):
    # Create two pointer and store the
    # address of 1st and 2nd polynomials
    ptr1 = poly1
    ptr2 = poly2

    while (ptr1 != None):
        while (ptr2 != None):
            if ptr1.power==ptr2.power:
                npower=ptr1.power
                coeff = ptr1.coeff + ptr2.coeff;

                poly3 = addnode(poly3, coeff, npower);

            ptr2 = ptr2.next

        ptr2 = poly2
        ptr1 = ptr1.next

    removeDuplicates(poly3)
    return poly3

def izbrisi_clan(p1):
    temp1=p1
    print("Unesite koeficijent i eksponent")
    koef=int(input())
    eksp=int(input())
    while(temp1!=None):
        if temp1.koef==koef:
            if temp1.eksp==eksp:
                temp1.eksp=0
                temp1.koef=0
        temp1=temp1.sledeci

    return temp1


def vrednost_x(poly1):
    ptr1=poly1
    print("Unesite vrednost za x: \n")
    x=int(input())
    polinom=0
    while(ptr1!=None):

            polinom += (x**ptr1.power)*ptr1.coeff

            ptr1 = ptr1.next;


    return polinom;

def izbrisi(poly1):
    poly1=addnode(poly1,0,0)

# Driver Code
if __name__ == '__main__':
    poly1 = None
    poly2 = None
    poly3 = None
    poly4=None

    # Creation of 1st Polynomial: 3x^2 + 5x^1 + 6
    poly1 = addnode(poly1, 3, 3);
    poly1 = addnode(poly1, 6, 1);
    poly1 = addnode(poly1, -9, 0);

    # Creation of 2nd polynomial: 6x^1 + 8
    poly2 = addnode(poly2, 9, 3);
    poly2 = addnode(poly2, -8, 2);
    poly2 = addnode(poly2, 7, 1);
    poly2 = addnode(poly2, 2, 0);

    # Displaying 1st polynomial
    print("1st Polynomial:- ", end='');
    printList(poly1);

    # Displaying 2nd polynomial
    print("2nd Polynomial:- ", end='');
    printList(poly2);

    # calling multiply function
    #poly3 = multiply(poly1, poly2, poly3);
    poly4=saberi(poly1,poly2,poly4)

    # Displaying Resultant Polynomial
    print("Resultant Polynomial:- ", end='');
    #printList(poly3);

    printList(poly4)

    printList(poly1)
    print("pre")
    izbrisi(poly1)
    print("posle")

