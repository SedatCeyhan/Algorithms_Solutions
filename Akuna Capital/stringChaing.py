def longestStrChain(words):
    dp = {}
    for w in sorted(words, key=len):
        dp[w] = max(dp.get(w[:i] + w[i + 1:], 0) + 1 for i in range(len(w)))
    return max(dp.values())


print(longestStrChain(["a", "b", "ba", "bca", "bda", "bdca"]))