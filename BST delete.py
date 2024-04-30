class Node:
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None


class Tree:
    def __init__(self):
        self.root = None
    def insert(self,root,data):
        if root is None:
            return Node(data)
        elif(data > root.data):
            root.right= self.insert(root.right, data)
        else:
            root.left = self.insert(root.left, data)
        return root
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)
    def dele(self,root,key):
        if root is not None:
            return root
        elif key<root:
            self.dele(root.left,key)
        elif key>root:
            self.dele(root.right,key)
        else:
            temp=root.left
            del(root)
            return temp
            # if root.left is not  None:
            #     temp = root.right
            #     root = None
            #     return temp
            # elif root.right is not None:
            #     temp = root.leftd
            #     root = None
            #     return temp
obj = Tree()
n = list(map(int, input().split()))
m=int(input("Enter the data to delete"))
for i in n:
    obj.root = obj.insert(obj.root, i)
obj.inorder(obj.root)
obj.root=obj.dele(obj.root,m)
obj.inorder(obj.root)