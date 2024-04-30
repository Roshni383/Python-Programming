class Node:
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root == None:
            self.root = Node(data)
        else:
            temp = self.root
            flag = 0
            temp1 = self.root
            while True:
                if temp.left is None:
                    temp.left = Node(data)
                    break
                elif temp.right == None:
                    temp.right = Node(data)
                    break
                elif flag == 0:
                    temp = temp1.left
                    flag = 1
                else:
                    temp = temp1.right
                    flag = 0
                    temp1 = temp1.left

    def display(self):
        temp = self.root
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.left

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)

    def preorder(self, root):
        if root:
            print(root.data, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, end=" ")


obj = Tree()
n = list(map(int, input().split()))
for i in n:
    obj.insert(i)
print("Preorder:")
obj.preorder(obj.root)
print("\nInorder:")
obj.inorder(obj.root)
print("\nPostorder:")
obj.postorder(obj.root)