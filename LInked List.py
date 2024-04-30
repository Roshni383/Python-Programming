class node:
    def __init__ (self,data):
     self.data=data
     self.next=None
     self.prev=None
class Linked_List:
    def __init__(self,head):
     self.head=None
     self.tail=None
    def create(self,data):
        if (self.head==None):
            self.head=node(data)
            self.tail=self.head
        else:
            newnode=node(data)
            self.tail.next=newnode
            newnode.prev=self.tail
            self.tail=newnode
            self.head.prev=self.tail
            self.tail.next=self.head
    def display(self):
        temp=self.head
        while temp.next is not self.head:
            print(temp.data)
            temp=temp.next
        print(temp.data)

for i in range(n):
    data=int(input("Enter the data"))
    data=node(data)
    def swapNodes(self, x, y):
        if x == y:
            return
        prevX = None
        currX = self.head
        while currX != None and currX.data != x:
            prevX = currX
            currX = currX.next
        prevY = None
        currY = self.head
        while currY != None and currY.data != y:
            prevY = currY
            currY = currY.next
        if currX == None or currY == None:
            return
        if prevX != None:
            prevX.next = currY
        else:
            self.head = currY
        if prevY != None:
            prevY.next = currX
        else:
            self.head = currX
        self.temp = currX.next
        currX.next = currY.next
        currY.next = self.temp