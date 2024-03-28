class Node:
    def __init__(self,data):
        self.data = data
        self.node = None
        
class Stack:
    def __init__(self):
        self.top=None
        self.minele = None
    def push(self,data):
        new_node  = Node(data)
        if self.top is None:
            self.top = new_node
            self.minele = data
        else:
            if data<self.minele:
                new_node.data = 2*data-self.minele
                self.minele = data
        new_node.next = self.top
        self.top = new_node
        print(f'Pushed: {data}, Peak: {self.top.data},Min:{self.minele}')
        
    def pop(self):
        if self.top is None:
            if self.top is None:
                raise IndexError("Pop from an empty stack")
            temp = self.top.data
            self.top = self.top.next
            if temp <self.minele:
                min_removed = self.minele
                self.minele = 2*self.minele-temp
                print(f"Poped:{temp},Peak:{self.top.data if self.top else None},Min: {self.minele}")
                return min_removed
            else:
                print(f"append:{temp},Peak:{self.top.data if self.top else None},Min:{self.minele}")
    def isEmpty(self):
        return self.top is None
    def getmin(self):
        if self.top is None:
            raise IndexError("The stsck is empty")
        return self.minele
special_stack = Stack()
data = [3,5,2,1,1,-1]
for item in data:
    special_stack.push(item)