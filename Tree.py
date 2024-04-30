class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class tree:
    def __init__(self):
        self.root=None
        self.temp=None
    def create(self, data):
        if (self.root == None):
            self.root = node(data)
            self.temp = self.root
        else:
            self.temp=self.root
            flag=0
            temp1=self.root
            while True:
                if self.temp.left == None:
                    self.temp.left=node(data)
                    break
                elif self.temp.right == None:
                    self.temp.right=node(data)
                    break
                elif flag==0:
                    self.temp=temp1.left
                    flag=1
                else:
                    self.temp=temp1.right
                    flag=0
                    temp1=temp1.left

if __name__=="__main__":
    n = int(input("Enter the height of tree"))
    T = tree()
    for data in range(n):
        data = int(input("Enter the data:"))
        T.create(data)
        data=int(input("Enter the left data:"))
        T.create(data)
        data = int(input("Enter the right data:"))
        T.create(data)