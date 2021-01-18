from collections import defaultdict

#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def findClosestLeaf(self, root, k):
        graph, leaves = defaultdict(list), []
        stack = [root]
        while stack:
            curr = stack.pop()
            if curr.left:
                stack.append(curr.left)
                graph[curr.val].append(curr.left.val)
                graph[curr.left.val].append(curr.val)
            if curr.right:
                stack.append(curr.right)
                graph[curr.val].append(curr.right.val)
                graph[curr.right.val].append(curr.val)

            if not curr.left and not curr.right: leaves.append(curr.val)

        queue = [k]
        while queue:
            curr = queue.pop(0)
            if curr in leaves: return curr
            queue.extend(graph.pop(curr))



root = TreeNode(10, TreeNode(5), TreeNode(-3))
root.left.left = TreeNode(3)
root.left.right = TreeNode(2)
root.right.right = TreeNode(11)
root.left.left.left = TreeNode(3)
root.left.left.right = TreeNode(-2)
root.left.right.right = TreeNode(1)
#print(Solution().findClosestLeaf(root, 3))

graph = {45:['a']}
print(graph.pop(45))
print(graph)
