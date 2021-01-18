'''

Given a binary tree, return the zigzag level order traversal of its nodes' values.
(ie, from left to right, then right to left for the next level and alternate between).

'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root):
        if not root: return []
        sol = []
        stackEven = [root]
        stackOdd = []

        while stackEven or stackOdd:
            currLevel = []

            if stackEven:
                while stackEven:
                    curr = stackEven.pop()
                    currLevel.append(curr.val)
                    if curr.left:
                        stackOdd.append(curr.left)
                    if curr.right:
                        stackOdd.append(curr.right)

            else:
                while stackOdd:
                    curr = stackOdd.pop()
                    currLevel.append(curr.val)
                    if curr.right:
                        stackEven.append(curr.right)
                    if curr.left:
                        stackEven.append(curr.left)

            sol.append(currLevel)

        return sol
