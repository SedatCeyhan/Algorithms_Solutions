import math

#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    # Are the trees the same?
    def isSameTree(self, p, q):
        if not p and not q:return True
        if not p or not q: return False
        if p.val != q.val: return False
        return self.isSameTree(p.left, q.left) and \
            self.isSameTree(p.right, q.right)

    # Is symmetric question
    def isSymmetric(self, root):
        if not root or (not root.left and not root.right): return True
        if (root.left and not root.right) or (not root.left and root.right): return False
        return self.isMirror(root.left, root.right)

    def isMirror(self, t1, t2):
        if not t1 and not t2: return True
        if (not t1 and t2) or (t1 and not t2): return False
        return (t1.val == t2.val) and \
               (self.isMirror(t1.left, t2.right) and self.isMirror(t1.right, t2.left))

    # Maximum Depth of Binary Tree
    def maxDepth(self, root):
        if not root: return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    # Return the bottom up level order traversal of trees' nodes' values
    def levelOrderBottom(self, root):
        if not root: return []
        traversal = [[root.val]]
        l = self.levelOrderBottom(root.left)
        r = self.levelOrderBottom(root.right)

        i,j = len(l) - 1,len(r) - 1
        while i >= 0 and j >= 0:
            combined = l[i] + r[j]
            traversal.insert(0, combined)
            i -= 1
            j -= 1

        if i < 0:
            for k in range(j, -1, -1):
                traversal.insert(0, r[k])

        if j < 0:
            for k in range(i, -1, -1):
                traversal.insert(0, l[k])

        return traversal

    # Convert Sorted Array to height balanced BST
    def sortedArrayToBST(self, nums):
        if len(nums) == 0: return None
        root_idx = int(math.ceil((len(nums) - 1) / 2))
        root = TreeNode(nums[root_idx])
        root.left = self.sortedArrayToBST(nums[:root_idx])
        root.right = self.sortedArrayToBST(nums[root_idx + 1:])
        return root

    # Return whether the tree is balanced or not (children heights differ no more than 1)
    def isBalanced(self, root):
        if not root: return True
        return abs(self.height(root.left) - self.height(root.right)) <= 1 and \
               (self.isBalanced(root.left) and self.isBalanced(root.right))


    def height(self, root):
        if not root: return 0
        return 1 + max(self.height(root.left), self.height(root.right))


    # find the minimum depth of a tree
    def minDepth(self, root):
        if not root: return 0
        if not root.left and not root.right: return 1
        if not root.left and root.right: return 1 + self.minDepth(root.right)
        if root.left and not root.right: return 1 + self.minDepth(root.left)
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))


    # Given a binary tree and a sum, determine if the tree has a root-to-leaf path
    # such that adding up all the values along the path equals the given sum
    def hasPathSum(self, root, sum):
        if not root: return False
        sum -= root.val
        if not root.left and not root.right: return sum == 0
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)


    # Invert a binary tree.
    def invertTree(self, root):
        if not root or (not root.left and not root.right): return root
        left = self.invertTree(root.right)
        right = self.invertTree(root.left)
        root.left = left
        root.right = right
        return root

    # Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.
    def lowestCommonAncestor(self, root, p, q):
        curr = root
        while curr:
            if p.val < curr.val and q.val < curr.val:
                curr = curr.left
            elif p.val > curr.val and q.val > curr.val:
                curr = curr.right
            else: return curr


    # Given a binary tree, return all root-to-leaf paths.
    def binaryTreePaths(self, root):
        if not root: return []
        if not root.left and not root.right: return [str(root.val)]
        paths = []
        path = str(root.val)
        if root.left:
            for p in self.binaryTreePaths(root.left):
                paths.append(path + "->" + p)

        if root.right:
            for p in self.binaryTreePaths(root.right):
                paths.append(path + "->" + p)

        return paths

    # Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.
    def closestValue(self, root, target):
        min_distance = abs(root.val - target)
        min_val = root.val
        curr = root

        while curr:
            if min_distance > abs(curr.val - target):
                min_val = curr.val
                min_distance = abs(curr.val - target)

            if target < curr.val:
                curr = curr.left
            elif target > curr.val:
                curr = curr.right
            else:
                return curr.val

        return min_val


    # Find the sum of all left leaves in a given binary tree.
    def sumOfLeftLeaves(self, root):
        if not root: return 0
        if root.left and (not root.left.left and not root.left.right):
            return root.left.val + self.sumOfLeftLeaves(root.right)
        return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

    # Find the number of paths that sum to a given value.
    # The path does not need to start or end at the root or a leaf,
    # but it must go downwards (traveling only from parent nodes to child nodes).
    def pathSum(self, root, sum):
        if not root: return 0
        if not root.left and not root.right:
            if root.val == sum: return 1
            else: return 0

        return self.pathSum(root.left, sum - root.val) + \
               self.pathSum(root.left, sum) + \
               self.pathSum(root.right, sum - root.val) + \
               self.pathSum(root.right, sum ) -1

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@



    # Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) in the given BST.
    def findMode(self, root):
        if not root: return []
        freq_dict = {}
        queue = [root]
        while queue:
            curr = queue.pop(0)
            if curr.val in freq_dict:
                freq_dict[curr.val] += 1
            else: freq_dict[curr.val] = 1
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)

        sorted_tuples = [(k, v) for k, v in sorted(freq_dict.items(), key=lambda kv:kv[1], reverse=True)]
        for node in sorted_tuples:
            if node[1] == sorted_tuples[0][1]:
                queue.append(node[0])
            else: break

        return queue



    # Given a binary search tree with non-negative values, find the minimum absolute difference between values of any two nodes
    def getMinimumDifference(self, root):
        queue = [root]
        values = []
        while queue:
            curr = queue.pop(0)
            values.append(curr.val)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)

        values = sorted(values)
        min_diff = float('inf')
        for i in range(len(values) - 1):
            if min_diff > values[i + 1] - values[i]:
                min_diff = values[i + 1] - values[i]

        return min_diff


    # Given a Binary Search Tree (BST), convert it to a Greater Tree such that
    # every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.
    def __init__(self):
        self.sum = 0

    def convertBST(self, root):
        if root:
            self.convertBST(root.right)
            self.sum += root.val
            root.val = self.sum
            self.convertBST(root.left)

        return root

    # Given a binary tree, you need to compute the length of the diameter of the tree.
    # The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
    # This path may or may not pass through the root.
    def diameterOfBinaryTree(self, root):
        if not root: return 0
        self.path = 0

        def depthOfNode(node):
            if not node: return 0
            left_depth = depthOfNode(node.left)
            right_depth = depthOfNode(node.right)
            self.path = max(self.path, left_depth + right_depth)
            return 1 + max(left_depth, right_depth)

        depthOfNode(root)
        return self.path


    # Given a n-ary tree, find its maximum depth.
    # Definition for a Node.
    class Node_n_ary:
        def __init__(self, val=None, children=None):
            self.val = val
            self.children = children


    def maxDepth_n_ary(self, root):
        if not root: return 0
        child_depth = 0
        for child in root.children:
            cand_depth = self.maxDepth_n_ary(child)
            if child_depth < cand_depth: child_depth = cand_depth

        return child_depth + 1


    def findTilt(self, root):
        if not root: return 0
        if not root.left and not root.right: return 0
        self.findTilt(root.left) + self.findTilt(root.right)








































































