def maxScheduleProfit(programs):
    # Pre-Computing to order the programs by their end time
    n = len(programs)
    programs = sorted(programs, key=lambda program:program[1])
    compatiblity = {}
    for p1 in range(n - 1, 0, -1):
        for p2 in range(p1 - 1, -1, -1):
            # program p2 is ending before p1 starts so it's compatible
            if programs[p2][1] <= programs[p1][0]:
                compatiblity[p1] = p2
                break
        # No program ending before p1 is compatible with p1
        if p1 not in compatiblity:
            compatiblity[p1] = -1

    # Since the program with the smallest end time has no compatible program ending before it
    compatiblity[0] = -1

    #Initialize dp array where dp[i] holds, max profit reached from a subset of [p[1], p[2], ..., p[i]]
    dp = [0] * (n + 1)

    for p in range(1, n + 1):
        dp[p] = max(dp[p - 1], programs[p - 1][-1] + dp[compatiblity[p - 1] + 1])


    # RECOVERY STEP to find those programs that maximize profit:
    sol, profit, p = [], dp[n], n
    while profit > 0:
        if dp[p] == dp[compatiblity[p - 1] + 1] + programs[p - 1][-1]:
            profit -= programs[p - 1][-1]
            sol.append(programs[p - 1])
            p = compatiblity[p - 1] + 1
        else: p-= 1

    return sorted(sol, key=lambda program:program[0])





print(maxScheduleProfit([[1, 2, 50], [3, 10, 20], [6, 19, 100], [2, 100, 200]]))





