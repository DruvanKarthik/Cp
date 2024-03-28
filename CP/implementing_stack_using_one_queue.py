from collections import deque
class StackusingQueue:
    def __init__(self):
        self.queue= deque()
    def push(self,x):
        self.queue.append(x)
        for i in range(len(self.queue)-1):
            self.queue.append(self.queue.popleft())
        print("Pushed element to stack:",x)
    def pop(self):
        if not self.queue:
            return None
        return self.queue.popleft()
    def top(self):
        if len(self.queue)==0:
            raise IndexError("pop from an empty stack")
        return self.queue[0]
    def isEmpty(self):
         return len(self.queue)==0
stack = StackusingQueue()
print("//Pushing//")
stack.push(12)
stack.push(13)
stack.push(1)
stack.push(8)
print("//Poping//")
print("Poped element from stack",stack.pop())
print("Poped element from stack",stack.pop())
print("Poped element from stack",stack.pop())
print("//Top Element//")
print("the topelemts is:",stack.top())