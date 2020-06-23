def longest_substring_wo_rep(str):

    # Realized that this questiyan is actually 95% similar to longest palindo subst.

    if len(str) == 0: return ''

    F = []
    n = len(str)

    for i in range(n + 1):
        F.append([0] * (n + 1))

    # Base case all such e.g., str[4 : 2], empty substrings trivially have NO rep.
    for i in range(n + 1):
        for j in range(i + 1):
            F[i][j] = 1

    longest = str[0]
    for k in range(1, n):
        for i in range(1, n - k + 1):
            curr_idx = i - 1
            next_idx = curr_idx + k
            if str[curr_idx] != str[next_idx] \
                        and (str[curr_idx] not in str[i : i + k - 1] and str[next_idx] not in str[i : i + k - 1]):
                F[i][i + k] = F[i + 1][i + k - 1]
                if F[i][i + k] == 1:
                    longest = str[curr_idx : next_idx + 1]

            else:
                F[i][i + k] = 0



    return longest


#print(longest_substring_wo_rep("sedattatokp"))

def longest_substring_wo_rep_NEW(str):

    if len(str) == 0: return ""

    n = len(str)
    F = []

    for i in range(n + 1):
        F.append(0)

    longest = 0
    idx_longest = 0
    for i in range(1, n + 1):
        curr_idx = i - 1
        prev_longest_length = F[i - 1]
        if str[curr_idx] not in str[(i - prev_longest_length) - 1 : curr_idx]:
            F[i] = prev_longest_length + 1
            if longest < F[i]:
                longest = F[i]
                idx_longest = curr_idx

    sol = ""
    for i in range(longest):
        sol = str[idx_longest] + sol
        idx_longest -= 1

    return sol


print(longest_substring_wo_rep_NEW("w"))


