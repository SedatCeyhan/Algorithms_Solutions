# Create a Queue using 2 Stacks
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.S1 = []
        self.S2 = []
        self.front = 0

    def push(self, x):
        """
        Push element x to the back of queue.
        """
        if not self.S1:
            self.front = x
        self.S1.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.S2:
            return self.S2.pop(-1)

        while len(self.S1) > 1:
            self.S2.append(self.S1.pop(-1))

        return self.S1.pop(-1)

    def peek(self):
        """
        Get the front element.
        """
        if self.S2:
            return self.S2[-1]

        return self.front

    def empty(self):
        """
        Returns whether the queue is empty.
        """
        return not self.S1 and not self.S2

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()