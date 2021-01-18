
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head):
        if not head: return head

        self.copyDict = {}

        def copyOfNode(node):
            if not node: return node
            if node in self.copyDict: return self.copyDict[node]
            self.copyDict[node] = Node(node.val, None, None)
            return self.copyDict[node]

        old_node = head
        while old_node:
            new_node = copyOfNode(old_node)
            new_node.next = copyOfNode(old_node.next)
            new_node.random = copyOfNode(old_node.random)

            old_node = old_node.next

        return self.copyDict[head]


