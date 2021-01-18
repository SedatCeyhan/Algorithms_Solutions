class Solution:
    def numDistinctIslands(self, grid):
        if not grid or not grid[0]: return 0
        rows, cols = len(grid), len(grid[0])
        self.island, self.uniqIslands = [], set()

        def dfs(row, col):
            if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] == 0: return
            self.island.append((row - self.curr[0], col - self.curr[1]))
            grid[row][col] = 0
            dfs(row, col + 1)
            dfs(row, col - 1)
            dfs(row - 1, col)
            dfs(row + 1, col)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    self.curr = (r, c)
                    dfs(r, c)
                    self.uniqIslands.add(tuple(self.island))
                    self.island = []

        return len(self.uniqIslands)

sol = Solution()
print(sol.numDistinctIslands([[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]))
