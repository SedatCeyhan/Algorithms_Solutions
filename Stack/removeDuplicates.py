def removeDuplicates(S):
    sol = ""
    for c in S:
        if not sol: sol += c
        else:
            if sol[-1] == c:
                sol = sol[:-1]
            else:
                sol += c

    return sol


print(removeDuplicates("abbaca"))
