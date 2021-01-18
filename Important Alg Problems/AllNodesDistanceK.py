# PROBLEM:  https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

from collections import defaultdict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        self.graph = defaultdict(list)
        self.discovered = defaultdict(lambda: False)

        def formGraph():
            queue = [root]
            while queue:
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                    self.graph[node.val].append(node.left.val)
                    self.graph[node.left.val].append(node.val)
                if node.right:
                    queue.append(node.right)
                    self.graph[node.val].append(node.right.val)
                    self.graph[node.right.val].append(node.val)

        formGraph()
        sol = []
        queue = [(target.val, 0)]
        self.discovered[target.val] = True
        while queue:
            curr, distance = queue.pop(0)
            if distance == K: sol.append(curr)
            else:
                for nbr in self.graph[curr]:
                    if not self.discovered[nbr]:
                        self.discovered[nbr] = True
                        queue.append((nbr, distance + 1))

        return sol