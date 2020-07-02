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