import heapq

class Solution:
    def connectSticks(self, A):
        heapq.heapify(A)
        print(A)
        res = 0
        while len(A) > 1:
            x, y = heapq.heappop(A), heapq.heappop(A)
            res += x + y
            heapq.heappush(A, x + y)
        return res


sol = Solution()
print(sol.connectSticks([2,8,3,7,1]))