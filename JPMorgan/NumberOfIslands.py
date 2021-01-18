def numIslands(grid):
    if not grid or len(grid[0]) == 0: return 0
    row = len(grid)
    col = len(grid[0])

    def dfs(grid, row, col):
        if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] == '0':
            return

        grid[row][col] = '0'
        dfs(grid, row, col + 1)
        dfs(grid, row + 1, col)
        dfs(grid, row - 1, col)
        dfs(grid, row, col - 1)


    numIslands = 0
    for r in range(row):
        for c in range(col):
            if grid[r][c] == '1':
                dfs(grid, r, c)
                numIslands += 1

    return numIslands



print(numIslands([
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]))