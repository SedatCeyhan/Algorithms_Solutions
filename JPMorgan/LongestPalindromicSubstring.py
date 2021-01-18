def longestPalindrome(s):
    if len(s) <= 1: return s
    n = len(s)
    dp = [[0] * (n + 1) for i in range(n + 1)]

    #Bases:
    for i in range(n + 1):
        for j in range(i + 1):
            dp[i][j] = 1


    longest = s[0]
    for k in range(2, n + 1):
        for i in range(1, n - k + 2):
            if s[i - 1] == s[i + k - 2] and dp[i + 1][i + k - 2] == 1:
                dp[i][i + k - 1] = 1
                longest = s[i - 1:i + k - 1]


    return longest


print(longestPalindrome("bbcbb"))