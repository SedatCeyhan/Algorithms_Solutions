'''
You have a queue of integers, you need to retrieve the first unique integer in the queue.

Implement the FirstUnique class:

FirstUnique(int[] nums) Initializes the object with the numbers in the queue.
int showFirstUnique() returns the value of the first unique integer of the queue, and returns -1 if there is no such integer.
void add(int value) insert value to the queue.

'''

from collections import deque


class FirstUnique:

    def __init__(self, nums):
        self.queue, self.isUnique = deque(), {}
        for n in nums:
            if n in self.isUnique: self.isUnique[n] = False
            else: self.isUnique[n] = True

        for n in self.isUnique:
            if self.isUnique[n]:
                self.queue.append(n)


    def showFirstUnique(self):
        while self.queue and not self.isUnique[self.queue[0]]:
            self.queue.popleft()
        if self.queue: return self.queue[0]
        return -1


    def add(self, value):
        if value in self.isUnique: self.isUnique[value] = False
        else:
            self.isUnique[value] = True
            self.queue.append(value)



# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)




# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)