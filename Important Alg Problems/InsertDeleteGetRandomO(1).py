import random
from collections import defaultdict

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.set, self.idxDict = [], defaultdict(lambda: -1)

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if self.idxDict[val] == -1:
            self.set.append(val)
            self.idxDict[val] = len(self.set) - 1
            return True
        return False


    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if self.idxDict[val] == -1: return False
        idxToRem, itemToRem = self.idxDict[val], self.set[self.idxDict[val]]
        self.set[idxToRem] = self.set[-1]
        self.idxDict[self.set[idxToRem]] = idxToRem
        self.idxDict[itemToRem] = -1
        self.set.pop()
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return self.set[random.randint(0, len(self.set) - 1)]





# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()