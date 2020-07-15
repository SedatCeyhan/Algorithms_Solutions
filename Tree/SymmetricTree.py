class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root):
        if not root or (not root.left and not root.right): return True
        if (root.left and not root.right) or (not root.left and root.right): return False
        return self.isMirror(root.left, root.right)

    def isMirror(self, t1, t2):
        if not t1 and not t2: return True
        if (not t1 and t2) or (t1 and not t2): return False
        return (t1.val == t2.val) and \
               (self.isMirror(t1.left, t2.right) and self.isMirror(t1.right, t2.left))