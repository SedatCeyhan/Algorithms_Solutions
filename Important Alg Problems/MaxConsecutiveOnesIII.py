'''
Given an array A of 0s and 1s, we may change up to K values from 0 to 1.
Return the length of the longest (contiguous) subarray that contains only 1s.

[1,1,1,0,0,0,1,1,1,1,0], K = 2 ==> [1,1,1,0,0,1,1,1,1,1,1]
'''

class Solution:
    def longestOnes(self, A, K):
        if not A: return 0
        n = len(A)
        maxOnes = 0
        curr, last0 = 1, -1
        zeroDict = {}
        for i in range(n):
            if A[i] == 0:
                zeroDict[curr] = i
                last0 = curr - K
                if last0 > 0:
                    maxOnes = max(maxOnes, i - zeroDict[last0])
                else: maxOnes = max(maxOnes, i + 1)
                curr += 1
            else:
                if last0 > 0:
                    maxOnes = max(maxOnes, i - zeroDict[last0])
                else: maxOnes = max(maxOnes, i + 1)

        return maxOnes


class Solution2:
    def longestOnes(self, A, K):
        left = 0
        for right in range(len(A)):
            # If we included a zero in the window we reduce the value of K.
            # Since K is the maximum zeros allowed in a window.
            K -= 1 - A[right]
            # A negative K denotes we have consumed all allowed flips and window has
            # more than allowed zeros, thus increment left pointer by 1 to keep the window size same.
            if K < 0:
                # If the left element to be thrown out is zero we increase K.
                K += 1 - A[left]
                left += 1
        return right - left + 1



sol = Solution()
print(sol.longestOnes([1,1,1,1,1,], 3))