def editDistance(word1, word2):

    n, m = len(word1), len(word2)

    if n == 0: return m
    if m == 0: return n

    F = []

    for i in range(n + 1):
        F.append([0] * (m + 1))

    # Base case: empty string takes 'm' many operations to convert to word2
    for i in range(m + 1):
        F[0][i] = i

    for i in range(n + 1):
        F[i][0] = i

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if word1[i - 1] == word2[j - 1]:
                F[i][j] = F[i - 1][j - 1]
            else:
                F[i][j] = min(1 + F[i - 1][j - 1], 1 + F[i][j - 1], 1 + F[i - 1][j])

    return F[n][m]


print(editDistance("horse", "ros"))