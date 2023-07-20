#スタックの実装
class MyStack:
    def __init__(self,n):
        self.S = [None]*n
        self.size = n
        self.top = -1
        
    def stack_empty(self):
        if self.top == -1:
            return True
        else:
            return False
    
    def pop(self):
        if self.stack_empty():
            print("アンダーフロー")
        else:
            self.top -=1
            return self.S[self.top + 1] #
        
    def push(self,x):
        if self.top == self.size -1:
            print("アンダーフロー")
        else:
            self.top += 1
            self.S[self.top] = x #
            
    def __str__(self):
        return str([str(x) for x in self.S[:self.top + 1]])
       
        
# mystack = MyStack(6)
# print(mystack)
# mystack.push(4)
# print(mystack)
# mystack.push(1)
# print(mystack)
# mystack.push(3)
# print(mystack)
# print('Pop: ' + str(mystack.pop()))
# print(mystack)

#キューの実装
class MyQueue:
    def __init__(self,size):
        self.Q = [0]*size
        self.len = size
        self.head = 1
        self.tail = 1
        
    def enqueue(self,x):
        self.Q[self.tail-1] = x #
        if self.tail == len(self.Q):
            self.tail = 1
        else:
            self.tail = self.tail + 1
            
    def dequeue(self):
        x = self.Q[self.head-1] #
        if self.head == len(self.Q):
            self.head = 1
        else:
            self.head = self.head + 1
        return x
    
    def __str__(self):
        return str([str(x) for x in self.Q[self.head-1:self.tail -1]])
    
myqueue = MyQueue(6)
print(myqueue)
myqueue.enqueue(4)
print(myqueue)
myqueue.enqueue(1)
print(myqueue)
myqueue.enqueue(3)
print(myqueue)
print('Dequeue: ' + str(myqueue.dequeue()))
print(myqueue)
myqueue.enqueue(8)
print(myqueue)
print('Dequeue: ' + str(myqueue.dequeue()))
print(myqueue)