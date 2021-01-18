def wordBreak(s, wordDict):
    if not wordDict or not s: return False
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(1, n + 1):
        for j in range(i, 0, -1):
            dp[i] = (s[j-1:i] in wordDict) and dp[j - 1]
            if dp[i]: break

    return dp[n]






print(wordBreak("dogscat", ['cat', 'cats', 'and', 'dog', 'dogs']))