class MinStack:
    def __init__(self):
        self.stack = []
        self.mins = []


    def push(self, x):
        self.stack.append(x)
        if not self.mins:
            self.mins.append(x)
        else:
            self.mins.append(min(x, self.mins[-1]))



    def pop(self):
        if len(self.stack) > 0:
            self.stack.pop(-1)
            self.mins.pop(-1)


    def top(self):
        if len(self.stack) > 0:
            return self.stack[-1]


    def getMin(self):
        if len(self.stack) > 0:
            return self.mins[-1]




# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
obj.push(7)
print(obj.pop())
print(obj.pop())
print(obj.getMin())

