def rob(nums):
    n = len(nums)
    if n == 0: return 0
    if n == 1: return nums[0]

    F = []
    for i in range(n + 1):
        F.append([0,0])

    F[1] = [nums[0], 0]
    F[2] = [nums[0], nums[1]]

    for i in range(3, n + 1):
        if i != n:
            F[i][0] = max(nums[i-1] + F[i-2][0], F[i - 1][0])
            F[i][1] = max(nums[i-1] + F[i-2][1], F[i - 1][1])
        else:
            F[i][0] = max(nums[i - 1] + F[i - 2][0] - nums[0], F[i - 1][0])
            F[i][1] = max(nums[i - 1] + F[i - 2][1], F[i - 1][1])


    return max(F[n][0], F[n][1])

#print(rob([1,2,3,1]))



def rob_better(nums):
    if not nums: return 0
    n = len(nums)
    if n <= 3:
        return max(nums)

    used, not_used = [nums[0], nums[0], nums[0] + nums[2]], [0, nums[1], nums[2]]
    max_profit = max(nums[1], nums[0] + nums[2])
    for h in range(3, n - 1):
        used.append(nums[h] + max(used[h - 2], used[h - 3]))
        not_used.append(nums[h] + max(not_used[h - 2], not_used[h - 3]))
        if max_profit < max(used[-1], not_used[-1]): max_profit = max(used[-1], not_used[-1])

    return max(max_profit, nums[-1] + max(not_used[-2], not_used[-3]))


class Solution(object):
    def rob(self, nums):
        n = len(nums)
        if n == 0: return 0
        if n == 1: return nums[0]
        if n == 2: return max(nums[0], nums[1])

        nums[0] = [nums[0], 0]
        nums[1] = [nums[0][0], nums[1]]

        for h in range(2, n):
            robbed = max(nums[h - 2][0] + nums[h], nums[h - 1][0])
            not_robbed = max(nums[h - 2][1] + nums[h], nums[h - 1][1])
            nums[h] = [robbed, not_robbed]

        nums[-1][0] = max(nums[-1][0] - nums[0][0], nums[-2][0])
        return max(nums[-1][0], nums[-1][1])



sol = Solution()
print(sol.rob([1,2,3,1]))