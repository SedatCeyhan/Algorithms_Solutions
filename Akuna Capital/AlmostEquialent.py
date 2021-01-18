def areAlmostEquivalent(s, t):
    # Write your code here
    sol = []
    for w in range(len(s)):
        flag = True
        if len(s[w]) != len(t[w]):
            sol.append("NO")
            continue
        uniqCharsS = list(set(s[w]))
        for uniqChar in uniqCharsS:
            if abs(s[w].count(uniqChar) - t[w].count(uniqChar)) > 3:
                sol.append("NO")
                flag = False
                break

        uniqCharsT = list(set(t[w]).difference(s[w]))
        for uniqChar in uniqCharsT:
            if t[w].count(uniqChar) > 3:
                sol.append("NO")
                flag = False
                break

        if flag: sol.append("YES")

    return sol


#print(areAlmostEquivalent([''], ['']))


# examples of lists
list1 = 'aab'
list2 = 'bbc'

# prints the missing and additional elements in list2
print("Missing values in second list:", (set(list1).difference(list2)))
print("Additional values in second list:", (set(list2).difference(list1)))