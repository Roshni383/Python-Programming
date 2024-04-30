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
            while True:
                if (data<self.temp.data):
                    if self.temp.left is None:
                        self.temp.left=node(data)
                        break
                    else:
                        self.temp=self.temp.left
                elif data>self.temp.data:
                    if self.temp.right is None:
                        self.temp.right=node(data)
                        break
                    else:
                        self.temp=self.temp.right


