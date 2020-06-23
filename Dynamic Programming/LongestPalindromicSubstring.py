def LongestPalindromicSubstring(str):

    if len(str) == 0: return ""

    F = []
    n = len(str)

    for i in range(n + 1):
        F.append([0] * (n + 1))

    # Base case: empty substring is trivially palindrome  +  F[i][i] all palindrome
    for i in range(n + 1):
        for j in range(i + 1):
            F[i][j] = 1

    longest_palindrome = str[0]
    for k in range(1, n):
        for i in range(1, n - k + 1):
            curr_idx = i - 1
            next_idx = curr_idx + k
            if str[curr_idx] == str[next_idx]:
                F[i][i + k] = F[i + 1][i + k - 1]
                if F[i][i + k] == 1: longest_palindrome = str[i - 1: i + k]
            else:
                F[i][i + k] = 0

    return longest_palindrome

print(LongestPalindromicSubstring("seddessrt"))

