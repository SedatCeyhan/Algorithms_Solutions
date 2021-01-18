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



    def binaryTreePaths2(self, root):
        if not root: return []
        paths = []
        stack = [(root, "")]
        while stack:
            curr_node, prev_path = stack.pop()
            curr_path = prev_path + "->" + str(curr_node.val)
            if curr_node.right: stack.append((curr_node.right, curr_path))
            if curr_node.left: stack.append((curr_node.left, curr_path))
            if not curr_node.left and not curr_node.right: paths.append(curr_path[2:])

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

    # def __init__(self):
    #     self.sum = 0

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


    # Given a binary tree, return the tilt of the whole tree.
    # The tilt of a tree node is defined as the absolute difference between
    # the sum of all left subtree node values and the sum of all right subtree node values. Null node has tilt 0.
    # The tilt of the whole tree is defined as the sum of all nodes' tilt.

    def findTilt(self, root):
        self.tilt = 0

        def sumOfNodes(node):
            if node:
                left_sum = sumOfNodes(node.left)
                right_sum = sumOfNodes(node.right)
                self.tilt += abs(left_sum - right_sum)
                return left_sum + right_sum + node.val
            return 0

        sumOfNodes(root)
        return self.tilt

    #Given two non-empty binary trees s and t, check whether tree t has
    # exactly the same structure and node values with a subtree of s.
    # A subtree of s is a tree consists of a node in s and all of this node's descendants.
    # The tree s could also be considered as a subtree of itself.
    def isSubtree(self, s, t):
        if not t: return True
        if not s: return False
        if self.isSameTree(s, t): return True
        if self.isSubtree(s.left, t) or self.isSubtree(s.right, t): return True
        return False


    # Given an n-ary tree, return the preorder traversal of its nodes' values. (DFS)

   # RECURSION

    # def __init__(self):
    #     self.DFS = []
    #
    # def preorder(self, root):
    #     if not root: return []
    #     self.DFS.append(root.val)
    #     for child in root.children:
    #         if child not in self.DFS:
    #             self.preorder(child)
    #
    #     return self.DFS
    #

    # ITERATIVE
    def preorder(self, root):
        if not root: return []
        DFS = []
        stack = [root]
        while stack:
            curr = stack.pop()
            DFS.append(curr.val)
            stack.extend(curr.children[::-1])

        return DFS


    # Given an n-ary tree, return the postorder traversal of its nodes' values. (DFS)
    def postorder(self, root):
        if not root: return []
        stack = [root]
        DFS = []
        while stack:
            curr = stack.pop()
            DFS.append(curr.val)
            stack.extend(curr.children)

        return DFS[::-1]



    #You need to construct a string consists of parenthesis and integers from a binary tree with the preorder traversing way.
    #The null node needs to be represented by empty parenthesis pair "()".
    # And you need to omit all the empty parenthesis pairs that don't affect
    # the one-to-one mapping relationship between the string and the original binary tree.
    def tree2str(self, t):
        if not t: return ""
        if not t.left and not t.right: return str(t.val)
        if not t.right: return str(t.val) + "(" + self.tree2str(t.left) + ")"
        if not t.left: return str(t.val) + "()" + "(" + self.tree2str(t.right) + ")"
        return str(t.val) + "(" + self.tree2str(t.left) + ")" + "(" + self.tree2str(t.right) + ")"


    # Tree with t1 and t2's nodes summed
    def mergeTrees(self, t1, t2):
        if not t1 and not t2: return t1
        if t1 and not t2: return t1
        if not t1 and t2: return t2
        t1.val += t2.val
        left = self.mergeTrees(t1.left, t2.left)
        right = self.mergeTrees(t1.right, t2.right)
        t1.left = left
        t1.right = right
        return t1



    # list of averages of levels
    def levelOrderTop(self, root):
        if not root: return []
        traversal = [[root.val]]
        l = self.levelOrderTop(root.left)
        r = self.levelOrderTop(root.right)

        i,j = 0, 0
        while i < len(l) and j < len(r):
            combined = l[i] + r[j]
            traversal.append(combined)
            i += 1
            j += 1

        if i == len(l):
            for k in range(j, len(r)):
                traversal.append(r[k])

        else:
            for k in range(i, len(l)):
                traversal.append(l[k])

        return traversal


    def averageOfLevels(self, root):
        if not root: return []
        traversal = self.levelOrderTop(root)
        avg = []
        for level in traversal:
            avg.append(float(sum(level)/len(level)))

        return avg


    # whether there exists 2 nodes summing to target = k
    def findTarget(self, root, k):
        if not root: return False
        vals = []
        queue = [root]
        while queue:
            curr = queue.pop(0)
            vals.append(curr.val)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)

        for i in range(len(vals)):
            if k - vals[i] in vals[i + 1: ]:
                return True

        return False


    # trimmed tree with all node values between L and R
    def trimBST(self, root, L, R):
        if not root: return root
        if root.val == L and root.val == R:
            root.left = None
            root.right = None
            return root
        if L < root.val and R > root.val:
            left = self.trimBST(root.left, L, R)
            right = self.trimBST(root.right, L, R)
            root.left = left
            root.right = right
            return root
        if L == root.val and R > root.val:
            right = self.trimBST(root.right, L, R)
            root.left = None
            root.right = right
            return root
        if L < root.val and R == root.val:
            left = self.trimBST(root.left, L , R)
            root.left = left
            root.right = None
            return root
        if L < root.val and R < root.val:
            return self.trimBST(root.left, L, R)
        else:
            return self.trimBST(root.right, L, R)


    # A special tree where each node has either 0 or 2 children
    # Parent node's value is the smaller of the 2 children if it has children
    # return the second smallest value in the tree if that value exists
    def findSecondMinimumValue(self, root):
        if not root or (not root.left and not root.right): return -1
        if root.left.val == root.right.val:
            L = self.findSecondMinimumValue(root.left)
            R = self.findSecondMinimumValue(root.right)
            if L == -1: return R
            if R == -1: return L
            return min(L, R)
        if root.right.val > root.left.val:
            L = self.findSecondMinimumValue(root.left)
            if L != -1: return min(L, root.right.val)
            return root.right.val
        else:
            R = self.findSecondMinimumValue(root.right)
            if R != -1: return min(R, root.left.val)
            return root.left.val


    # Longest path question where each node in the path has to have the same val
    def longestUnivaluePath(self, root):
        self.uniPath = 0

        def traverseUni(node):
            if node:
                L, R = traverseUni(node.left), traverseUni(node.right)
                if node.left and node.left.val == node.val:
                    L += 1
                else:
                    L = 0
                if node.right and node.right.val == node.val:
                    R += 1
                else:
                    R = 0

                self.uniPath = max(self.uniPath, L + R)
                return max(L, R)
            return 0

        traverseUni(root)
        return self.uniPath



    def searchBST(self, root, val):
        if not root: return None
        while root:
            if root.val < val:
                root = root.right
            elif root.val > val:
                root = root.left
            else: return root
        return None

    # RECURSIVE:

    # def searchBST(self, root, val):
    #     if not root or root.val == val: return root
    #     if val < root.val:
    #         return self.searchBST(root.left, val)
    #     else:
    #         return self.searchBST(root.right, val)


    def insertIntoBST(self, root, val):
        if not root: return TreeNode(val)
        if val < root.val:
            left = self.insertIntoBST(root.left, val)
            root.left = left
        else:
            right = self.insertIntoBST(root.right, val)
            root.right = right

        return root


    # Whether 2 trees have the same sequence of leaves
    def getLeafSequence(self, root):
        if not root: return []
        stack = [root]
        leaves = []
        while stack:
            curr = stack.pop()
            if not curr.left and not curr.right: leaves.append(curr.val)
            if curr.right: stack.append(curr.right)
            if curr.left: stack.append(curr.left)

        return leaves

    def leafSimilar(self, root1, root2):
        leaves1 = self.getLeafSequence(root1)
        leaves2 = self.getLeafSequence(root2)
        return leaves1 == leaves2



    # In order traversal formation of a tree
    def increasingBST(self, root):
        self.nodes = []
        def inOrderTraversal(root):
            if root:
                inOrderTraversal(root.left)
                self.nodes.append(root)
                inOrderTraversal(root.right)

        inOrderTraversal(root)
        if len(self.nodes) == 0: return None
        for i in range(len(self.nodes)-1):
            self.nodes[i].left = None
            self.nodes[i].right = self.nodes[i + 1]

        return self.nodes[0]

    # Sum of all nodes whose values >= L and <= R
    def rangeSumBST(self, root, L, R):
        if not root: return 0
        if L == root.val == R:
            return L
        if L == root.val  and root.val < R:
            return root.val + self.rangeSumBST(root.right, L, R)
        if L < root.val and root.val == R:
            return root.val + self.rangeSumBST(root.left, L, R)
        if L < root.val and R < root.val:
            return self.rangeSumBST(root.left, L, R)
        if L > root.val and R > root.val:
            return self.rangeSumBST(root.right, L, R)
        else:
            return root.val + self.rangeSumBST(root.left, L, root.val) + self.rangeSumBST(root.right, root.val, R)


    # Is tree formed by unique vals
    def isUnivalTree(self, root):
        if not root: return True
        uniVal = root.val
        queue = [root]
        while queue:
            curr = queue.pop(0)
            if uniVal != curr.val: return False
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        return True




    # Given two node values, return whether those nodes are cousins (same height, different parents)
    def isCousins(self, root, x, y):
        queue = [(root, 0, None)]
        depthParent_dict = {}
        while queue:
            curr = queue.pop(0)
            depthParent_dict[curr[0].val] = (curr[1], curr[2])
            if curr[0].left:
                queue.append((curr[0].left, curr[1] + 1, curr[0]))
            if curr[0].right:
                queue.append((curr[0].right, curr[1] + 1, curr[0]))

        return depthParent_dict[x][0] == depthParent_dict[y][0] and depthParent_dict[x][1] != depthParent_dict[y][1]


    # all paths from root to leaf and their sum as integer
    def sumRootToLeaf(self, root):

        def allPaths(root):
            if not root: return ""
            if not root.left and not root.right: return str(root.val)
            paths = []
            if root.left:
                for path in allPaths(root.left):
                    paths.append(str(root.val) + path)

            if root.right:
                for path in allPaths(root.right):
                    paths.append(str(root.val) + path)

            return paths

        paths = allPaths(root)
        sum = 0
        for path in paths:
            sum += int(path, 2)
        return sum

    # Nodes that have no siblings
    def getLonelyNodes(self, root):
        if not root: return []
        queue = [root]
        lonelyNodes = []
        while queue:
            curr = queue.pop(0)
            if curr.left and curr.right:
                queue.append(curr.left)
                queue.append(curr.right)

            elif curr.left:
                queue.append(curr.left)
                lonelyNodes.append(curr.left.val)
            elif curr.right:
                queue.append(curr.right)
                lonelyNodes.append(curr.right.val)

        return lonelyNodes


    def pathSum2(self, root, sum):
        if not root: return []
        paths = []
        stack = [(root, [], 0)]
        while stack:
            curr_node, pathSoFar, sumSoFar = stack.pop()
            sumSoFar += curr_node.val
            path = pathSoFar + [curr_node.val]
            if curr_node.right:
                stack.append((curr_node.right, path, sumSoFar))
            if curr_node.left:
                stack.append((curr_node.left, path, sumSoFar))
            if (not curr_node.left and not curr_node.right) and sumSoFar == sum: paths.append(path)

        return paths

    # Find the number of paths that sum to a given value.
    # The path does not need to start or end at the root or a leaf,
    # but it must go downwards (traveling only from parent nodes to child nodes).
    def pathSum3(self, root, target):
        if not root: return 0
        stack = [(root, [0], 0)]
        sol = 0
        while stack:
            curr_node, sumsSoFar, sum = stack.pop()
            sum += curr_node.val
            if sum - target in sumsSoFar: sol += sumsSoFar.count(sum - target)
            currSums = sumsSoFar + [sum]
            if curr_node.right:
                stack.append((curr_node.right, currSums, sum))
            if curr_node.left:
                stack.append((curr_node.left, currSums, sum))

        return sol


    def maxPathSum(self, root):
        if not root: return 0
        self.maxSum = -float('inf')

        def pathSum(root):
            if root:
                L = pathSum(root.left)
                R = pathSum(root.right)
                self.maxSum = max(self.maxSum, root.val, root.val + L, root.val + R, root.val + L + R)
                return max(root.val, root.val + L, root.val + R)
            return 0

        pathSum(root)
        return self.maxSum



    def sumNumbers(self, root):
        if not root: return 0
        sum = 0
        stack = [(root, 0)]
        while stack:
            curr, prevNum = stack.pop()
            currNum = curr.val + prevNum * 10
            if not curr.left and not curr.right: sum += currNum
            if curr.right: stack.append((curr.right, currNum))
            if curr.left: stack.append((curr.left, currNum))

        return sum









sol = Solution()
root = TreeNode(10, TreeNode(5), TreeNode(-3))
root.left.left = TreeNode(3)
root.left.right = TreeNode(2)
root.right.right = TreeNode(11)
root.left.left.left = TreeNode(3)
root.left.left.right = TreeNode(-2)
root.left.right.right = TreeNode(1)
print(sol.pathSum3(root, 8))



