# PROBLEM: https://leetcode.com/problems/maximum-average-subtree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maximumAverageSubtree(self, root):
        self.maxAvg = 0

        def traverse(node):
            if node:
                L = traverse(node.left)
                R = traverse(node.right)
                self.maxAvg = max(self.maxAvg, (L[0] + R[0] + node.val)/(L[1] + R[1] + 1))
                return (L[0] + R[0] + node.val, L[1] + R[1] + 1)

            return (0, 0)

        traverse(root)
        return self.maxAvg
