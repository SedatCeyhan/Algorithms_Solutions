'''
You are given a binary tree in which each node contains an integer value.
Find the number of paths that sum to a given value.
The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).
The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root, sum):
        if not root: return 0
        total = 0
        stack = [(root, 0, {0:1})]
        while stack:
            node, prevSum, prevDict = stack.pop()
            prevSum += node.val
            newDict = prevDict.copy()

            if (prevSum - sum) in newDict: total += newDict[prevSum - sum]

            if prevSum in newDict: newDict[prevSum] += 1
            else: newDict[prevSum] = 1

            if node.left: stack.append((node.left, prevSum, newDict))
            if node.right: stack.append((node.right, prevSum, newDict))

        return total
