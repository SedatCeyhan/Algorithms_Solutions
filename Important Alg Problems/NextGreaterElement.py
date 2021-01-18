# nums1 subset of nums2
# nums1 = [4,1,2], nums2 = [1,3,4,2] ====> [-1,3,-1]

class Solution:
    def nextGreaterElement(self, nums1, nums2):
        n = len(nums2)
        if not nums1 or not nums2: return []

        numToGreater = {}
        stack = [nums2[0]]
        for i in range(1, n):
            while stack and stack[-1] < nums2[i]:
                numToGreater[stack.pop()] = nums2[i]
            stack.append(nums2[i])

        while stack:
            numToGreater[stack.pop()] = -1

        sol = []
        for num in nums1:
            sol.append(numToGreater[num])
        return sol

sol = Solution()
print(sol.nextGreaterElement([4], [1]))

