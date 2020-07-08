class NumMatrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def sumRegion(self, row1, col1, row2,  col2):
        sum = 0
        for row in range(row1, row2 + 1):
            for col in range(col1, col2 + 1):
                sum += self.matrix[row][col]

        return sum


numMatrix = NumMatrix([
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
])

print(numMatrix.sumRegion(2,1,4,3))
print(numMatrix.sumRegion(1,1,2,2))
print(numMatrix.sumRegion(1,2,2,4))

