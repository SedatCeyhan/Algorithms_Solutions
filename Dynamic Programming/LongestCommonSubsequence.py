# def LCS(str1, str2):
#
#     F = []
#     n = len(str1)
#     m = len(str2)
#
#     for i in range(n + 1):
#         F.append([0] * (m + 1))
#
#     # No need for base case cuz alreadt 0's are filled
#
#     for i in range(1, n + 1):
#         for j in range(1, m + 1):
#             if str1[i - 1] == str2[j - 1]:
#                 F[i][j] = F[i - 1][j - 1] + 1
#             else:
#                 F[i][j] = max(F[i][j - 1], F[i - 1][j])
#
#
#     # Recovery step
#     print(F[n][m])
#
#     i = n
#     j = m
#     sol = ""
#
#     while i > 0 and j > 0:
#         #str1[i - 1] == str2[j - 1]:
#         if F[i][j] == F[i - 1][j - 1] + 1:
#             sol = str1[i - 1] + sol
#             i -= 1
#             j -= 1
#
#         elif F[i][j] == F[i - 1][j]:
#             i -= 1
#         else:
#             j -= 1
#
#     return sol

#applkpuuk
def LCS(str1, str2):
    if not str1 or not str2: return ""
    n, m = len(str1), len(str2)

    dp = [[0] * (m + 1) for i in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else: dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    sol, i, j = "", n, m
    while i > 0 and j > 0:
        if dp[i][j] == 1 + dp[i - 1][j - 1]:
            sol = str1[i - 1] + sol
            i -= 1
            j -= 1

        elif dp[i][j] == dp[i - 1][j]: i-=1
        else: j-=1

    return sol









print(LCS("appleketopucuk", "appalorkalakpajfjiusklksulstttk"))