# An efficient Python3 program to find sum
# of all subsquares of size k x k

# A O(n^2) function to find sum of all
# sub-squares of size k x k in a given
# square matrix of size n x n
#

def largestSubsquareSide(square, total):
    n = len(square)
    for k in range(n, -1, -1):
        if printSumTricky(square, k, total) != -1: return k
    return -1


def printSumTricky(mat, k, total):

    n = len(mat)
    # 1: PREPROCESSING
    # To store sums of all strips of size k x 1
    stripSum = [[None] * n for i in range(n)]

    # Go column by column
    for j in range(n):

        # Calculate sum of first k x 1
        # rectangle in this column
        Sum = 0
        for i in range(k):
            Sum += mat[i][j]
        stripSum[0][j] = Sum

        # Calculate sum of remaining rectangles
        for i in range(1, n - k + 1):
            Sum += (mat[i + k - 1][j] -
                    mat[i - 1][j])
            stripSum[i][j] = Sum

    # 2: CALCULATE SUM of Sub-Squares
    # using stripSum[][]
    for i in range(n - k + 1):

        # Calculate and prsum of first
        # subsquare in this row
        Sum = 0
        for j in range(k):
            Sum += stripSum[i][j]
        if Sum > total: return -1

        # Calculate sum of remaining squares
        # in current row by removing the leftmost
        # strip of previous sub-square and adding
        # a new strip
        for j in range(1, n - k + 1):
            Sum += (stripSum[i][j + k - 1] -
                    stripSum[i][j - 1])
            if Sum > total: return -1

    return k



mat = [[1, 1, 1, 1, 1],
       [2, 2, 2, 2, 2],
       [3, 3, 3, 3, 3],
       [4, 4, 4, 4, 4],
       [5, 5, 5, 5, 5]]


print(largestSubsquareSide(mat, 24))