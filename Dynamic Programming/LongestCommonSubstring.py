# def LCS(str1, str2):
#     F = []
#     n = len(str1)
#     m = len(str2)
#
#     for i in range(n + 1):
#         F.append([0] * (m + 1))
#
#         # Base case already fulfilled with the 0's
#
#     longest = 0
#
#     # indices holding the last letter of the common substring
#     i_longest= 0
#
#     for i in range(1, n + 1):
#         for j in range(1, m + 1):
#             if str1[i - 1] == str2[j - 1]:
#                 F[i][j] = F[i - 1][j - 1] + 1
#                 if longest < F[i][j]:
#                     longest = F[i][j]
#                     # -1 since its list indices
#                     i_longest = i-1
#
#
#             else:
#                 F[i][j] = 0
#
#     # At this point at some indices i,j ----> F[i][j] = longest
#
#     # Recovery step -- Already know what index we need to backtrack from
#     # choose either i or j, doesnt matter since it's the same substring
#     sol = ""
#     for k in range(longest):
#         sol = str1[i_longest] + sol
#         i_longest -= 1
#
#     return sol

def LCS(str1, str2):
    if not str1 or not str2: return ""
    n, m = len(str1), len(str2)

    dp = [[0] * (m + 1) for i in range(n + 1)]

    longest = 0
    longest_idx = -1
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
                if longest < dp[i][j]:
                    longest = dp[i][j]
                    longest_idx = i - 1

            else: dp[i][j] = 0

    sol = ""
    while longest > 0:
        sol = str1[longest_idx] + sol
        longest -= 1
        longest_idx -= 1

    return sol






print(LCS("romanogreeksosallah", "geeks4greekopallahs"))
