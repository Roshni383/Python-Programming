class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
        self.temp=None
    def create(self,data):
        if self.head==None:
            self.head=Node(data)
            self.temp=self.head
        else:
            newnode=Node(data)
            self.temp.next=newnode
            self.temp=newnode
    def display(self):
        self.temp=self.head
        ele=[]
        while self.temp is not None:
            ele.append(str(self.temp.data))
            # print("->",self.temp.data)
            self.temp=self.temp.next
        print("->".join(ele))
        print(ele)

    def swaping(self):

        x = int(input("Enter swap data"))
        y = int(input("Enter swap data"))
        if x == y:
            return

        # Search for x (keep track of prevX and CurrX)
        prevX = None
        currX = self.head
        while currX != None and currX.data != x:
            prevX = currX
            currX = currX.next

        # Search for y (keep track of prevY and currY)
        prevY = None
        currY = self.head
        while currY != None and currY.data != y:
            prevY = currY
            currY = currY.next

        # If either x or y is not present, nothing to do
        if currX == None or currY == None:
            return
        # If x is not head of linked list
        if prevX != None:
            prevX.next = currY
        else:  # make y the new head
            self.head = currY

        # If y is not head of linked list
        if prevY != None:
            prevY.next = currX
        else:  # make x the new head
            self.head = currX

        # Swap next pointers
        temp = currX.next
        currX.next = currY.next
        currY.next = temp

if __name__=="__main__":
    n=int(input("Enter the number of data"))
    ll=LinkedList()
    for data in range(n):
        data=int(input("Enter the data:"))
        ll.create(data)
    ll.display()
    print("Swap")
    ll.swaping()
    ll.display()
