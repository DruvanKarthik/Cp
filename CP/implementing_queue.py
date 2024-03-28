class Node:
    def __init__(self,data):
        self.data = data
        self.node = None
class Queue:
    def __init__(self):
        self.rear=None
        self.front=None 
    def enqueue(self,data):
        new_node=Node(data)
        if self.is_empty():
            self.front=new_node
            self.rear =new_node
        self.rear.next=new_node
        self.rear=new_node
    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        else:
            data = self.front.data
            if self.front==self.rear:
                self.front = None
                self.rear = None
            else:
                self.front = self.front.next
            return data
    def peek(self):
        if self.is_empty():
            return Exception("The queue is empty")
        else:
            return self.front.data
    def display(self):
        current = self.front
        while current:
            print(current.data,end='')
            current = current.next  
        print()
    def is_empty(self):
        return not self.rear and not self.front
queue=Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
print("elemts")
queue.display()
print("peek",queue.peek()) 
print("Dequeue",queue.dequeue())
queue.display()         