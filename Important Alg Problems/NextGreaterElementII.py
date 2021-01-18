class Solution:
    def nextGreaterElements(self, nums):
        if not nums: return []
        n = len(nums)
        stack = [0]
        numToGreater = {}

        for i in range(1, n):
            while stack and nums[stack[-1]] < nums[i]:
                numToGreater[stack.pop()] = nums[i]
            stack.append(i)

        while stack:
            currIdx = stack.pop()
            numToGreater[currIdx] = -1
            for i in range(currIdx):
                if nums[i] > nums[currIdx]:
                    numToGreater[currIdx] = nums[i]
                    break

        sol = []
        for i in range(n):
            sol.append(numToGreater[i])

        return sol





sol = Solution()
print(sol.nextGreaterElements([100,1,11,1,120,111,123,1,-1,-100]))
