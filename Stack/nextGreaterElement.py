class Solution:
    # nums1 subset of nums2
    # nums1 = [4,1,2], nums2 = [1,3,4,2] ====> [-1,3,-1]
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        map = {}
        for next in nums2:
            while stack and stack[-1] < next:
                map[stack.pop(-1)] = next

            stack.append(next)

        while stack:
            map[stack.pop(-1)] = -1

        sol = []
        for num in nums1:
            sol.append(map[num])
        return sol

