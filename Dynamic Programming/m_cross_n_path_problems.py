def uniquePaths(m, n):

    F = []

    for i in range(n + 1):
        F.append([0] * (m + 1))

    # Base Case 1:  n = 0  -> m = 1,...,M ===> then there is only one path (straight right path)
    for i in range(m + 1):
        F[0][i] = 1

    # Base Case 2:  m = 0  -> n = 1,...,N ===> then there is only one path (straight down path)
    for i in range(n + 1):
        F[i][0] = 1

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            F[i][j] = F[i - 1][j] + F[i][j - 1]

    return F[n - 1][m - 1]

#print(uniquePaths(3,3))


def uniquePathsWithObstacles(obstacleGrid):
    F = []

    m = len(obstacleGrid[0])
    n = len(obstacleGrid)

    for i in range(n + 1):
        F.append([0] * (m + 1))

    if obstacleGrid[0][0] == 1:
        return 0

    F[0][0] = 1

    # EDGES
    # Base Case 1:  n = 0  -> m = 1,...,M   ===>  then there is only one path (straight right path)
    for i in range(1, m):
        if obstacleGrid[0][i] == 0:
            F[0][i] = F[0][i - 1]
        if i == m - 1:
            if obstacleGrid[0][i] == 0:
                F[0][m] = F[0][m - 1]


    # Base Case 2:  m = 0  -> n = 1,...,N   ===>  then there is only one path (straight down path)
    for i in range(1, n):
        if obstacleGrid[i][0] == 0:
            F[i][0] = F[i - 1][0]
        if i == n - 1:
            if obstacleGrid[i][0] == 0:
                F[n][0] = F[n - 1][0]

    for i in range(1, n):
        for j in range(1, m):
            if obstacleGrid[i][j] == 0:
                F[i][j] = F[i - 1][j] + F[i][j - 1]

    F[n][m] = F[n - 1][m] + F[n][m - 1]

    return F[n - 1][m - 1]


# print(uniquePathsWithObstacles([
#   [0,0,0],
#   [0,0,0],
#   [0,0,0]
# ]))


def minPathSum(grid):

    F = []

    m = len(grid[0])
    n = len(grid)

    for i in range(n + 1):
        F.append([0] * (m + 1))

    # Base Case 1:  n = @@ 1 @@ -> m = 1,...,M ===> total so far + the value of the cell
    for i in range(1, m + 1):
        F[1][i] = F[1][i - 1] + grid[0][i - 1]

    # Base Case 2:  m = @@ 1 @@  -> n = 1,...,N ===> total so far + the value of the cell
    for i in range(1, n + 1):
        F[i][1] = F[i - 1][1] + grid[i - 1][0]


    for i in range(2, n + 1):
        for j in range(2, m + 1):
            F[i][j] = grid[i - 1][j - 1] + min(F[i - 1][j], F[i][j - 1])

    return F[n][m]


print(minPathSum([
  []
]))