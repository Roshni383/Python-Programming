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
    # def search(self,root,key):
    #     # if root is not None and root.data==key:
    #     #     return True
    #     if root is None:
    #         return False
    #     elif root.data == key:
    #         return True
    #     elif(key > root.data):
    #         self.search(root.right,key)
    #     else:
    #         self.search(root.left, key)
    # def search(self, root, key):
    #     if root is None:
    #         return False
    #     elif root.data == key:
    #         return True
    #     elif key > root.data:
    #         return self.search(root.right, key)
    #     else:
    #         return self.search(root.left, key)
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)


obj = Tree()
n = list(map(int, input().split()))
m=int(input("Enter the data to search"))
for i in n:
    obj.root = obj.insert(obj.root, i)
# if obj.search(obj.root, m):
#     print("Yes")
# else:
#     print("No")
obj.inorder(obj.root)