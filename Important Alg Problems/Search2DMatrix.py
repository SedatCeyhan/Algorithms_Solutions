class Solution:
    def searchMatrix(self, matrix, target):
        if not matrix: return False
        rows, cols = len(matrix), len(matrix[0])
        r, c = 0, cols - 1

        while r <= rows and c >= 0:
            if matrix[r][c] == target: return True
            elif matrix[r][c] < target: r += 1
            else: c -= 1

        return False

