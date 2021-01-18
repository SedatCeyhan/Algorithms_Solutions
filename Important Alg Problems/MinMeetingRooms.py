from collections import defaultdict

class Solution:
    def minMeetingRooms(self, intervals):
        if not intervals: return 0
        n = len(intervals)

        # Sort it in increasing ending time (meeting schedule question stereotype!!!)
        intervals = sorted(intervals, key=lambda item:item[1])
        rooms, discovered = 0, defaultdict(lambda: False)

        for r1 in range(n - 1, -1, -1):
            if not discovered[r1]: rooms += 1
            for r2 in range(r1 - 1, -1, -1):
                if intervals[r2][1] <= intervals[r1][0] and not discovered[r2]:
                    discovered[r2] = True
                    break

        return rooms


sol = Solution()
print(sol.minMeetingRooms([[7,10],[2,4]]))
