import collections
def changedSort(s):
    sol = ""

    min_idx = s.index(min(s))
    min_char = s[min_idx]
    sol += min_char
    temp = s.replace(min_char, "")
    s = s.replace(min_char, "", 1)

    while s:
        while temp and min(temp) > min_char:
            min_char = min(temp)
            sol += min_char
            temp = temp.replace(min_char, "")
            s = s.replace(min_char, "", 1)

        if not s: return sol

        temp = sol
        max_char = min_char

        while temp and max(temp) < max_char:
            max_char = max(temp)
            sol += max_char
            temp = temp.replace(max_char, "")
            s = s.replace(max_char, "", 1)

        if temp and max(temp)

    return sol


def sortString(s):
    d = sorted([c, n] for c, n in collections.Counter(s).items())
    r = []
    while len(r) < len(s):
        for i in range(len(d)):
            if d[i][1]:
                r.append(d[i][0])
                d[i][1] -= 1
        for i in range(len(d)):
            if d[~i][1]:
                r.append(d[~i][0])
                d[~i][1] -= 1
    return ''.join(r)

print(changedSort("aaazzz"))
print(sortString("aaazzz"))
# cdelotee
#letoe
