class QueueUisngSingleStack:
    def __init__(self):
        self.stack = []
    def enqueue(self,data):
        pass
    def dequeue(self):
        if not self.stack:
            return "queue is empty"         
    def peek(self):
        if not self.stack:
            return "Queue is empty"
        else:
            return 
    def is_empty(self):
        return not self.stack
Queue = QueueUisngSingleStack()
Queue.enqueue(1)
Queue.enqueue(2)
Queue.enqueue(12)
Queue.enqueue(22)
Queue.enqueue(52)
Queue.dequeue()
