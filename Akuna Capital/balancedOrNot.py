def isValidParantheses(exp, reps):
    left = 0
    for paran in exp:
        if paran == "<":
            left += 1
        else:
            left -= 1

        if left < 0:
            left = 0
            reps -= 1

    if left > 0 or reps < 0: return 0
    return 1


def balancedOrNot(expressions, maxReplacements):
    result = []
    for e in range(len(expressions)):
        result.append(isValidParantheses(expressions[e], maxReplacements[e]))
    return result

print(balancedOrNot(["<>>><>", "<>><>>"], [2,2]))

