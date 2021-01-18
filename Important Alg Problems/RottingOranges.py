class Solution:
    def orangesRotting(self, grid):
        rows, cols = len(grid), len(grid[0])
        queue, freshNum = [], 0
        days = -1

        def isValid(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols: return False
            return True

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    freshNum += 1

        queue.append((-1, -1))
        while queue:
            row, col = queue.pop(0)
            if row == -1:
                days += 1
                if queue: queue.append((-1, -1))
            else:
                if isValid(row - 1, col) and grid[row - 1][col] == 1:
                    grid[row - 1][col] = 2
                    queue.append((row - 1, col))
                    freshNum -= 1

                if isValid(row + 1, col) and grid[row + 1][col] == 1:
                    grid[row + 1][col] = 2
                    queue.append((row + 1, col))
                    freshNum -= 1

                if isValid(row, col - 1) and grid[row][col - 1] == 1:
                    grid[row][col - 1] = 2
                    queue.append((row, col - 1))
                    freshNum -= 1

                if isValid(row, col + 1) and grid[row][col + 1] == 1:
                    grid[row][col + 1] = 2
                    queue.append((row, col + 1))
                    freshNum -= 1

        return days if freshNum == 0 else -1


