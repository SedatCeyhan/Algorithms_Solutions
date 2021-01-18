# Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

class Solution:
    def maximalSquare(self, matrix):
        if not matrix or not matrix[0]: return 0
        rows, cols = len(matrix), len(matrix[0])
        maxEdge = 0

        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][c] == '1':
                    matrix[r][c] = min(int(matrix[r][c - 1]), int(matrix[r - 1][c]), int(matrix[r - 1][c - 1])) + 1
                    maxEdge = max(maxEdge, matrix[r][c])

        if maxEdge > 0: return maxEdge ** 2
        if "1" in matrix[0]: return 1
        for r in range(rows):
            if matrix[r][0] == '1': return 1

        return 0
