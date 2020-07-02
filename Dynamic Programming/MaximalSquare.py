def maximalSquare(matrix):
    n = len(matrix)
    if n == 0: return 0

    m = len(matrix[0])
    max_edge = 0

    for i in range(n):
        for j in range(m):
            if (i == 0 or j == 0):
                if int(matrix[i][j]) == 1 and max_edge == 0: max_edge = 1
            else:
                if int(matrix[i][j]) == 1:
                    matrix[i][j] = min(int(matrix[i - 1][j]), int(matrix[i - 1][j - 1]), int(matrix[i][j - 1])) + 1

                if max_edge < int(matrix[i][j]): max_edge = int(matrix[i][j])

    return max_edge ** 2

print(maximalSquare([["1","0","1","0"],["1","0","1","1"],["1","0","1","1"],["1","1","1","1"]]))

