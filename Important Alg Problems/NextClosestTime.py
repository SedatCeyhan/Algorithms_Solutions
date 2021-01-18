'''
Given a time represented in the format "HH:MM", form the next closest time by reusing the current digits.
There is no limit on how many times a digit can be reused.

You may assume the given input string is always valid. For example, "01:34", "12:09" are all valid. "1:34", "12:9" are all invalid.

Input: "19:34"
Output: "19:39"
Explanation: The next closest time choosing from digits 1, 9, 3, 4, is 19:39, which occurs 5 minutes later.
It is not 19:33, because this occurs 23 hours and 59 minutes later.

Input: "23:59"
Output: "22:22"
Explanation: The next closest time choosing from digits 2, 3, 5, 9, is 22:22.
It may be assumed that the returned time is next day's time since it is smaller than the input time numerically


'''
import itertools

class Solution:
    def nextClosestTime(self, time):
        strTime = time[:2] + time[3:]
        if len(set(strTime)) == 1: return time

        timeHour = int(time[:2])
        timeMin = int(time[3:])
        startTotalMinutes = (60 * timeHour) + timeMin
        dayMinutes = (24 * 60)
        minDifference, closestNextTime = float('inf'), "00:00"

        def isValidTime(time):
            return time != strTime and (int(time[:2]) < 24 and int(time[2:]) < 60)

        for perm in list(itertools.product(strTime, repeat=4)):
            perm = "".join(perm)
            if isValidTime(perm):
                candHours, candMins = int(perm[:2]), int(perm[2:])
                candTotalMinutes = candHours * 60 + candMins
                candTimeDiff = (candTotalMinutes - startTotalMinutes) % dayMinutes
                if candTimeDiff < minDifference:
                    minDifference = candTimeDiff
                    closestNextTime = perm
                    #print(str(minDifference) + "....." + str(closestNextTime))

        return closestNextTime[:2] + ":" + closestNextTime[2:]

sol = Solution()
print(set("1111"))

