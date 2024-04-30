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
    # def removeindex(self,value):
    #     current = self.head
    #     if index<0:
    #         return

    def removeindex(self, index):
        print(index)
        # if self.head == None:
        #     return
        #
        # current_node = self.head
        # position = index
        # # if position == index:
        # #     self.remove_first_node()
        # if position>index:
        #     while (current_node != None and position + 1 != index):
        #         position = position+1
        #         current_node = current_node.next
        #
        #     if current_node != None:
        #         current_node.next = current_node.next.next
        #     else:
        #         print("Index not present")

    def delete(self):
        n = int(input("Enter the skipping data to delete"))
        self.temp=self.head
        position=0
        while self.temp!=None:
            position=position+1
            self.temp=self.temp.next
        for i in range(1,position+1,n):
            print(i)
            self.removeindex(i)
        # self.display()
    def display(self):
        self.temp=self.head
        ele=[]
        while self.temp is not None:
            ele.append(str(self.temp.data))
            # print("->",self.temp.data)
            self.temp=self.temp.next
        print("->".join(ele))
        print(ele)

if __name__=="__main__":
    n=int(input("Enter the number of data"))
    ll=LinkedList()
    for data in range(n):
        data=int(input("Enter the data:"))
        ll.create(data)
    ll.display()
    ll.delete()

