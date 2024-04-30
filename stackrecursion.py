class Stack:
    def __init__(self):
        self.elements=[]

    def push(self,value):
        self.elements.append(value)

    def pop(self):
        return self.elements.pop()

    def empty(self):
        return self.elements == []

    def show(self):
        for value in reversed(self.elements):
            print(value)

    def BottomInsert(self, value):
        if self.empty():
            self.push(value)
        else:
            popped = self.pop()
            self.BottomInsert(value)
            self.push(popped)

    def Reverse(self):
        if self.empty():
            pass
        else:
            popped = self.pop()
            self.Reverse()
            self.BottomInsert(popped)

    def displayReversedStack(self):
        for value in reversed(self.elements):
            print(value)



stk=Stack()
n=int(input('Enter the no of elements'))
for i in range(n):
    ele=int(input('Enter the elements'))
    stk.push(ele)
print("Original Stack:")
stk.show()
print("\nStack after Reversing:")
stk.Reverse()
stk.displayReversedStack()