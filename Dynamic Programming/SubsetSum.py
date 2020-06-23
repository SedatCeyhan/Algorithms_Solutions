# Find just 1 set
def subsetSum(numbs, B):

    F = []
    n = len(numbs)

    for i in range(n + 1):
        F.append([0] * (B + 1))

        # Base Case for B = 0
        F[i][0] = 1

    for b in range(1, B + 1):
        for m in range(1, n + 1):
            if b < numbs[m - 1]:
                F[m][b] = F[m - 1][b]
            else:
                F[m][b] = max(F[m - 1][b], F[m - 1][b - numbs[m - 1]])

    if F[n][B] == 0: return []

    m = n
    b = B
    sol = []

    # Recovery
    while b > 0:
        if F[m][b] == F[m - 1][b]:
            m -= 1

        # Then F[m][b] = F[m - 1][b - numbs[m - 1]]
        else:
            sol.append(numbs[m - 1])
            b -= numbs[m - 1]
            m -= 1

    return sol


#print(subsetSum([9,1], 10))



#Find all the sets summing up to B
#def subsetSum_all(numbs, B):




































