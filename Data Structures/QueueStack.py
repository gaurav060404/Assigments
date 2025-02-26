class Stack:
    def __init__(self,size):
        self.size = size
        self.top = -1
        self.stack = []
    def push(self,val):
        self.top += 1
        if self.top == self.size :
            print("Stack Overflow")
            return
        self.stack.append(val)
    def pop(self):
        if self.top == -1 :
            print("Stack Underflow")
            return
        ele = self.stack.pop()
        print("Popped element is ",ele)
        self.top -= 1
        return ele
    def peek(self):
        return self.stack[self.top]
    def printStack(self):
        print(self.stack)

class StackQueue:
    def __init__(self,s):
        self.size = s.size
        self.top = -1
        self.stack1 = []
        self.stk = s

    def enqueue(self):
        self.top += 1
        if self.top == self.size :
            print("Queue Overflow")
            return
        self.stack1.append(self.stk.pop())
    
    def dequeue(self):
        if self.top == -1 :
            print("Stack Underflow")
            return
        ele = self.stack1.pop()
        print("Popped element is ",ele)
        self.top -= 1
    def peek(self):
        return self.stack1[self.top]
    def printStackQueue(self):
        print(self.stack1)

stk = Stack(4)
stk.push(1)
stk.push(2)
stk.push(3)
stk.push(4)

q = StackQueue(stk)
q.enqueue()
q.enqueue()
q.enqueue()
q.enqueue()
q.enqueue()
q.printStackQueue()
q.dequeue()
q.printStackQueue()

    

