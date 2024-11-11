class Element():
    def __init__(self, v):
        self.payload = v
        self.next = None

class LinkedList():
    def __init__(self):
        self.first = None
    def append(self,v):
        if self.first is None:
            self.first = Element(v)
        else:
            element = self.first
            while element.next is not None:
                element = element.next
            element.next = Element(v)
    def length(self):
        cont = 0
        element = self.first
        while element is not None:
            cont += 1
            element = element.next
        return cont
    def __getitem__(self,i):
        element = self.first
        x = 0
        while x < i:
            element = element.next
            x += 1
        return element.payload

    

x = LinkedList()
x.append(3)
x.append(4)
x.append('ciao')
print(x.length())
print(x[1])