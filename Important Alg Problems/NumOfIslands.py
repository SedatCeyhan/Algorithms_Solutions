class Solution:
    def numIslands(self, grid):
        if not grid or len(grid[0]) == 0: return 0
        rows, cols = len(grid), len(grid[0])
        self.maxIslands, self.localIslands = 0, 0

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0': return
            self.localIslands += 1
            grid[r][c] = '0'

            dfs(r - 1, c)
            dfs(r, c - 1)
            dfs(r + 1, c)
            dfs(r, c + 1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != '0':
                    self.localIslands = 0
                    dfs(r, c)
                    self.maxIslands = max(self.maxIslands, self.localIslands)


        return self.maxIslands



sol = Solution()
print(sol.numIslands([
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]))
