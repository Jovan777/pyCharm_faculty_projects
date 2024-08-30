
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


class elem(Node):
    def __init__(self, value):
        self.value=value
        self.next=None

    def newEl(self, data):
        new.value=data
        new.next=None
        return new


