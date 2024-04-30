class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class stack:
    def __init__(self):
        self.head=None
        self.tail=None
    def push(self,data):
        if self.head is None:
            self.head=node(data)
            self.tail=self.head
        else:
            newnode=node(data)
            newnode.next=self.head
            self.head=newnode
    def pop(self):
        temp=self.head
        self.head=self.head.next
    def peek(self):
        print(self.head.data)
    def display(self):
        temp=self.head
        while temp !=None:
            print(temp.data)
            temp=temp.next
obj=stack()
n=int(input("Enter no of elements"))
for i in range(n):
    ele=int(input("Enter elements"))
    obj.push(ele)
print("STACK ELEMENTS")
obj.display()
# obj.pop()
# obj.pop()
# obj.display()
# obj.peek()
# obj.display()


