def minSumTriangle(triangle):
    n = len(triangle)

    if len(triangle) == 0: return 0

    i = 1
    while i < n:
        for j in range(len(triangle[i])):
            if j == 0:
                triangle[i][j] += triangle[i - 1][j]
            elif j == len(triangle[i]) - 1:
                triangle[i][j] += triangle[i - 1][-1]
            else:
                triangle[i][j] += min(triangle[i - 1][j - 1], triangle[i - 1][j])

        i += 1

    return min(triangle[n - 1])



print(minSumTriangle([
     [1],
    [2,3]
]))



# bottom-up, O(n) space
def minimumTotal(triangle):
    if not triangle: return 0
    dp = triangle[-1]
    for row in range(len(triangle) - 2, -1, -1):
        temp = []
        for i in range(len(triangle[row])):
            temp.append(min(triangle[row][i] + dp[i], triangle[row][i] + dp[i + 1]))
        dp = temp

    return dp[0]