def removeOuterParentheses(S):
    primitives = []
    left = 0
    i = 0
    for p in range(len(S)):
        if S[p] == "(": left += 1
        else: left -= 1

        if left == 0:
            primitives.append(S[i : p + 1])
            i = p + 1

    sol = ""
    for prim in primitives:
        sol += prim[1 : -1]

    return sol

print(removeOuterParentheses(""))
