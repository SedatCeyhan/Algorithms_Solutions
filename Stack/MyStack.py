# Create a Stack using 2 queues:
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.Q1 = []
        self.Q2 = []
        self.top_item = 0

    def push(self, x):
        """
        Push element x onto stack.
        """
        self.Q1.append(x)
        self.top_item = x


    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        """
        while len(self.Q1) > 1:
            top = self.Q1.pop(0)
            self.Q2.append(top)

        popped = self.Q1.pop(0)
        self.Q1 = self.Q2
        self.Q2 = []
        return popped


    def top(self):
        """
        Get the top element.
        """
        return self.top_item

    def empty(self):
        """
        Returns whether the stack is empty.
        """
        return not self.Q1



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()