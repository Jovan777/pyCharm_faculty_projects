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

def remove(poly1):
    temp=poly1
    while(temp!=None):
        xcvor=temp
        temp=temp.next
        xcvor=None




if __name__ == '__main__':
    poly1 = None
    poly2 = None
    poly3 = None


print("unesite za polinom 1:\n")

poly1 = addnode(poly1, int(input()), int(input()))
iskaz1="da"
while(iskaz1=="da"):
        print("Novi broj?\n")
        iskaz1=input()
        if iskaz1=="da":
            poly1 = addnode(poly1,int(input()), int(input()))
        elif iskaz1=="ne":
            break

printList(poly1)
remove(poly1)
printList(poly1)
print("Izbrisano")
