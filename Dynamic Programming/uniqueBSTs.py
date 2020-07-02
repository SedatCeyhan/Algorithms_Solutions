# Python3 code to find number of unique
# BSTs Dynamic Programming solution

# Function to find number of unique BST
def numberOfBST(n):

	F = []

	for i in range(n + 1):
		F.append(0)

	# Base case: No node => 1 way of creating BST (empty BST)
	F[0] = 1

	for i in range(1, n + 1):
		for j in range(1, i + 1):
			# j is the current root

			# how many nodes on the left of root = j
			l = j - 1
			# how many nodes on the right of root = j
			r = i - j

			F[i] += F[l] * F[r]

	return F[n]


print(numberOfBST(7))
# Definition for a binary tree node.


class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	def generateTrees(self, n):

		return self.generate_trees(1, n) if n >= 1 else []

	# Creating all trees with smallest node = start, largest node = end
	def generate_trees(self, start, end):
		if start > end:
			return [None]

		all_trees = []

		# All possible trees will have a start <= root <= end
		# Choose a root for each iter
		for root in range(start, end + 1):
			left_subTrees = self.generate_trees(start, root - 1)
			right_subTrees = self.generate_trees(root + 1, end)

			for left_sub in left_subTrees:
				for right_sub in right_subTrees:
					root_node = TreeNode(root)
					root_node.left = left_sub
					root_node.right = right_sub
					all_trees.append(root_node)


		return all_trees

sol = Solution()
print(sol.generateTrees(3))