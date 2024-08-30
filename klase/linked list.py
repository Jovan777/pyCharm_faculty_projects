class Node():
    def __init__(self, id,nivo,magicni,savrseni,used,matrix):
        self.id=None
        self.nivo=None
        self.magicni=None
        self.matrix=[]
        self.savrseni=None
        self.used=[]
        self.roditelj=None
        self.potomak=None

    def newNode(self, n):
        new=Node()
        matrix=[]
        potomak=[]
        roditelj=[]
        used=[]
        id=0
        nivo=0
        magicni=-1
        savrseni=-1

        return new


class elem(Node()):
    def __init__(self, value):
        self.value=value
        self.next=None

    def newEl(self, data):
        self.new.value=data
        self.new.next=None
