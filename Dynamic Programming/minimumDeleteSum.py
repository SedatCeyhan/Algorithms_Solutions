def minimumDeleteSum(s1, s2):
    n, m = len(s1), len(s2)
    if n == 0: return sum(ord(s) for s in s2)
    if m == 0: return sum(ord(s) for s in s1)

    dp = [[0] * (m + 1) for i in range(n + 1)]

    # Base cases
    for i in range(1, m + 1):
        dp[0][i] = sum(ord(s) for s in s2[:i])

    for i in range(1, n + 1):
        dp[i][0] = sum(ord(s) for s in s1[:i])


    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]

            else:
                dp[i][j] = min((ord(s1[i - 1]) + ord(s2[j - 1]) + dp[i - 1][j - 1]),
                               (ord(s1[i - 1]) + dp[i - 1][j]),
                               (ord(s2[j - 1]) + dp[i][j - 1]))

    return dp[n][m]




def deletion_distance(s1, s2):
    n, m = len(s1), len(s2)

    # If one of the strings is empty, then the distance is basically the length of
    # the other string
    if n == 0: return m
    if m == 0: return n

    # Initialize dynamic programming array
    # dp[i][j] will hold the minimum char deletion length required to make str1[1:i] and str2[1:j] equal
    dp = [[0] * (m + 1) for i in range(n + 1)]

    # Base cases: if one of the strings is empty, then the minimum char deletion length
    # is the length of the non-empty string, e.g., "" and str2[1:j] ====> min length is j
    for i in range(1, m + 1):
        dp[0][i] = i

    for i in range(1, n + 1):
        dp[i][0] = i

    # Recurrence
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]

            else:
                dp[i][j] = min((2 + dp[i - 1][j - 1]),
                               (1 + dp[i - 1][j]),
                               (1 + dp[i][j - 1]))

    return dp[n][m]


print(deletion_distance("", ""))


