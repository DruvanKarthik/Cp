from collections import deque
class StcakWithQueue:
    def __init__(self):
        self.queue1=  deque()
        self.queue2 = deque()
    def push(self,x):
        self.queue2.append(x)
        while not len(self.queue1)==0:
            self.queue2.append(self.queue1.pop())
        self.queue1,self.queue2 = self.queue2,self.queue1
    def pop(self):
        if len(self.queue1)==0:
            raise IndexError("Pop from an empty stack")
        return self.queue1.pop()
    def top(self):
        if self.queue1():
            raise IndexError("pop from an empty stack")
        return self.queue1[0]
    def isEmpty(self):
         return len(self.queue1)==0

stack = StcakWithQueue()
stack.push(1)
stack.push(2)
stack.push(3)

print("The poped elememt",stack.pop())
