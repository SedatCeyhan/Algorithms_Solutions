def canMakePaliQueries(s, queries):
    dp = [0] * (len(s) + 1)
    ints = list(map(lambda c: ord(c) - ord('a'), s))

    for i in range(1, len(s) + 1):
        dp[i] = dp[i-1] ^ (1 << ints[i-1])

    ones = lambda x: bin(x).count('1')
    return [
        ones(dp[r+1] ^ dp[l]) >> 1 <= k
        for l, r, k in queries
    ]


# def canMakePaliQueries2(s, l, r, k):
#     queries = []
#     dp = [[0] * 26]
#     for i in range(1, len(s) + 1):
#         new = dp[i - 1][:]
#         j = ord(s[i - 1]) - ord('a')
#         new[j] += 1
#         dp.append(new)
#     ans = []
#     for l, r, k in queries:
#         L = dp[l]
#         R = dp[r + 1]
#         ans.append(sum((R[i] - L[i]) & 1 for i in range(26)) // 2 <= k)
#     return ans



def canMakePaliQueries2(s, l, r, k):
    dp = [[0] * 26]
    for i in range(1, len(s) + 1):
        new = dp[i - 1][:]
        j = ord(s[i - 1]) - ord('a')
        new[j] += 1
        dp.append(new)
    ans = []

    for i in range(len(l)):
        L = dp[l[i]]
        R = dp[r[i] + 1]
        if sum((R[t] - L[t]) & 1 for t in range(26)) // 2 <= k[i]: ans.append(1)
        else:ans.append(0)

    return ans



print(canMakePaliQueries('cdecd', [[0,0,0], [0,1,1], [0,2,1], [0,3,0]]))
print(canMakePaliQueries2('cdecd', [0,0,0,0], [0,1,2,3], [0,1,1,0]))