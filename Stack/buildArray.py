def buildArray(target, n):
    ordered = range(1, n + 1)
    i = 0
    sol = []
    for num in ordered:
        if i == len(target): break
        if num < target[i]:
            sol.extend(["Push", "Pop"])
        else:
            sol.append("Push")
            i += 1

    return sol



print(buildArray([1,3], 3))

