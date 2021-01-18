'''
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]

Return corresponding root node
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder, inorder):
        if not preorder: return None
        root = TreeNode(preorder[0])
        stack = [root]
        preorder = preorder[1:]

        inOrderToidx = {}
        for idx in range(len(inorder)):
            inOrderToidx[inorder[idx]] = idx

        for po in preorder:
            currNode = stack[-1]
            poNode = TreeNode(po)
            if inOrderToidx[po] < inOrderToidx[currNode.val]:
                currNode.left = poNode
            else:
                while stack and inOrderToidx[stack[-1].val] < inOrderToidx[po]:
                    curr = stack.pop()
                curr.right = poNode
            stack.append(poNode)

        return root




