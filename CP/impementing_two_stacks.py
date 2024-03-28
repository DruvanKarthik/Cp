class TwoStacks:
    def __init__(self,n):
        self.size = n
        self.arr = [None]*n
        self.top1 = -1
        self.top2 = self.size
    def push1(self,x):
        if self.top1<self.top2-1:
            self.top1+=1
            self.arr[self.top1]=x
            print("Pushed:",x)
        else:
            print("Stack1 overflow")
    def push2(self,x):
        if self.top1<self.top2:
            self.top2-=1
            self.arr[self.top2]= x
            print("Pushed",x)
        else:
            print("Stack2 Overflow")
    def pop1(self):
        if self.top1>=0:
            x = self.arr[self.top1]
            self.top1 +=1
            print("The element removed is:",x)
        else:
            print("Stack1 is Underflow")
    def pop2(self):
        if self.top2<self.size:
            x = self.arr[self.top2]
            self.top2-=1
            print("The removed elemnt is:",x)
        else:
            print("Stack2 Underflow")
Stacks = TwoStacks(5)
Stacks.push1(1)
Stacks.push1(2)
Stacks.push2(11)
Stacks.push2(12)
Stacks.push1(4)
Stacks.push2(8)
Stacks.push1(6)

print("Poped from Stack1",Stacks.pop1())
print("Poped from Stack1",Stacks.pop1())
print("Poped from Stack2",Stacks.pop2())
print("Poped from Stack2",Stacks.pop2())            