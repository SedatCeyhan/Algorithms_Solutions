class Solution:
    def productExceptSelf(self, nums):
        R, L = [1] * (len(nums)), [1] * (len(nums))

        for i in range(len(nums) - 2, -1, -1):
            R[i] = R[i + 1] * nums[i + 1]

        for j in range(1, len(nums)):
            L[j] = L[j - 1] * nums[j - 1]

        for i in range(len(nums)):
            nums[i] = L[i] * R[i]

        return nums

sol = Solution()
print(sol.productExceptSelf([1,2,3,4]))
