#Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
#Integers in each row are sorted in ascending from left to right.
#Integers in each column are sorted in ascending from top to bottom

class Solution:
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]: return False
        rows, cols = len(matrix), len(matrix[0])

        r, c = 0, cols - 1
        while c >=0 and r < rows:
            if matrix[r][c] > target: c -= 1
            elif matrix[r][c] < target: r += 1
            else: return True

        return False
