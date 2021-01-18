# Question: https://leetcode.com/problems/design-circular-queue/

class SLLNode:
    def __init__(self, val=-1, next=None):
        self.val = val
        self.next = next


class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.size, self.cap = 0, k
        self.head = SLLNode()
        self.tail = self.head

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.size < self.cap:
            if self.size == 0:
                self.head = SLLNode(value)
                self.tail = self.head
            else:
                self.tail.next = SLLNode(value)
                self.tail = self.tail.next
            self.size += 1
            return True
        return False


    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.size > 0:
            self.head = self.head.next
            self.size -= 1
            return True

        return False

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.size > 0: return self.head.val
        return -1

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.size > 0: return self.tail.val
        return -1


    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.size == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self.size == self.cap

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()