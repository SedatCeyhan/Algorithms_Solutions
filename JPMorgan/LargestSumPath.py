class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Sol:
    def maxPathSum(self, root):
        if not root: return 0
        self.largest = -float("inf")
        def traverse(root):
            if not root: return 0
            L = traverse(root.left)
            R = traverse(root.right)
            self.largest = max(self.largest, root.val, root.val + L, root.val + R, root.val + L + R)
            return max(root.val, root.val + L, root.val + R)

        traverse(root)
        return self.largest