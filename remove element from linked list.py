class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
        self.temp=None
    def create(self,data):
        if self.head is None:
            self.head=node(data)
            self.temp=self.head
        else:
            newnode=node(data)
            self.temp.next=newnode
            self.temp=newnode
    def remove(self,m):
        renode= self.head
        count=0
        while self.temp is not None:
            if self.temp.data==m:
                count+=1
            self.temp=self.temp.next
        while count>0:
            renode=self.head
            while renode.next is not None:
                if renode.next.data == m:
                    renode.next=renode.next.next
                    break
                else:
                    renode = renode.next
        count-=1

    def display(self):
        self.temp=self.head
        while self.temp is not None:
            print(self.temp.data,end='')
            self.temp=self.temp.next
obj=LinkedList()
n=list(map(int,input().split()))
size=len(n)
for ele in n:
    obj.create(ele)
m=int(input("Enter the element to delete"))
obj.remove(m)
obj.display()
