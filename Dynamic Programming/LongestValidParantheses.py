def isValidParantheses(str):
    left = 0
    for paran in str:
        if paran ==  "(": left += 1
        else: left -= 1

        if left < 0: return False

    if left != 0: return False
    return True


def longestValidParantheses(s):

    if len(s) == 0: return 0

    F = []
    n = len(s)

    # The base case: empty string (F[0]) has length 0 of longest valid parantheses
    for i in range(n + 1):
        F.append(0)

    longest = 0
    #idx_longest = 0
    for i in range(1, n + 1):
        if s[i - 1] == '(':
            F[i] = 0
        else:
            longest_so_far = F[i - 1]
            if (i - longest_so_far - 1) - 1 >= 0:
                possible_start_idx = (i - longest_so_far - 1) - 1
                if s[possible_start_idx] == '(':
                    if possible_start_idx > 0:
                        prev_longest_so_far = F[(i - longest_so_far - 1) - 1]
                        F[i] = prev_longest_so_far + longest_so_far + 2
                    else:
                        F[i] =  longest_so_far + 2

                    if longest < F[i]:
                        longest = F[i]
                        #idx_longest = i - 1

                else:
                    F[i] = 0
            else:
                F[i] = 0
    return longest
    # sol = ""
    # for i in range(longest):
    #     sol = s[idx_longest] + sol
    #     idx_longest -= 1
    #
    # return [sol, longest]





print(longestValidParantheses("(((((()())()()))()(()))"))
#print(isValidParantheses("(((((()())()()))()(()))"))