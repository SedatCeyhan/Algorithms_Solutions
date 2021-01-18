class Solution:
    def merge(self, intervals):
        intervals = sorted(sorted(intervals, key=lambda item:item[0]), key=lambda item:item[1])
        i = len(intervals) - 1
        while i > 0:
            if intervals[i][0] <= intervals[i - 1][1]:
                intervals[i - 1] = [min(intervals[i - 1][0], intervals[i][0]), intervals[i][1]]
                intervals[i] = intervals[-1]
                intervals.pop()

            i-= 1

        return intervals

sol = Solution()
print(sol.merge([[1,3],[2,6],[8,10],[15,18]]))
