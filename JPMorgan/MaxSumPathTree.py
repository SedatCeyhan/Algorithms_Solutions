# Python program to find maximum path sum in Binary Tree

# A Binary Tree Node
class Node:

    # Contructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# This function returns overall maximum path sum in 'res'
# And returns max path sum going through root
def findMaxUtil(root):
    # Base Case
    if root is None:
        return 0

    # l and r store maximum path sum going through left
    # and right child of root respetively
    l = findMaxUtil(root.left)
    r = findMaxUtil(root.right)

    # Max path for parent call of root. This path
    # must include at most one child of root
    max_single = max(max(l, r) + root.data, root.data)

    # Max top represents the sum when the node under
    # consideration is the root of the maxSum path and
    # no ancestor of root are there in max sum path
    max_top = max(max_single, l + r + root.data)

    # Static variable to store the changes
    # Store the maximum result
    findMaxUtil.res = max(findMaxUtil.res, max_top)

    return max_single


# Return maximum path sum in tree with given root
def findMaxSum(root):
    # Initialize result
    findMaxUtil.res = float("-inf")

    # Compute and return result
    findMaxUtil(root)
    return findMaxUtil.res


# Driver program
root = Node(-10)
root.left = Node(2)
root.right = Node(10)
root.left.left = Node(20)
root.left.right = Node(1)
root.right.right = Node(-25)
root.right.right.left = Node(3)
root.right.right.right = Node(4)
print("Max path sum is ", findMaxSum(root))
