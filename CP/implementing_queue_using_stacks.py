class QueueUsingStacks:
    def __init__(self):
        self.stack_enqueue=[]
        self.stack_dequeue=[]
    def enquue(self,item):
        self.stack_enqueue.append(item)
    def dequeue(self):
        if not self.stack_dequeue:
            return 'Queue is empty'
        else:
            while self.stack_enqueue:
                self.stack_dequeue.append(self.stack_enqueue.pop())
        return self.stack_dequeue.pop()
    def peek(self):
        if  not self.stack_dequeue:
            if not self.stack_enqueue:
                return "Queue is empty"
            else:
                while self.stack_enqueue:
                    self.stack_dequeue.append(self.stack_enqueue.pop())
            return self.stack_dequeue[0]
    def is_empty(self):
        return not self.stack_dequeue and not self.stack_enqueue
    
