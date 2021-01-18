#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sumOfAllNums(root):
    if not root: return 0
    stack = [(root, 0)]
    sum = 0
    while stack:
        curr_node, num = stack.pop()
        num = (num * 10) + curr_node.val
        if curr_node.right: stack.append((curr_node.right, num))
        if curr_node.left: stack.append((curr_node.left, num))
        if not curr_node.left and not curr_node.right: sum += num

    return sum











root = TreeNode(6, TreeNode(3), TreeNode(5))
root.left.left = TreeNode(2)
root.left.right = TreeNode(5)
root.right.right = TreeNode(4)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)
print(sumOfAllNums(root))



