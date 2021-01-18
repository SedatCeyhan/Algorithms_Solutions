'''
Question:   https://leetcode.com/problems/design-hit-counter/
'''

class HitCounter:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.timestampHits = {}
        self.uniqStamps = []


    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: None
        """
        if timestamp not in self.timestampHits:
            self.timestampHits[timestamp] = 1
            self.uniqStamps.append(timestamp)

        else: self.timestampHits[timestamp] += 1


    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """

        startTime = (timestamp - 300) + 1
        total = 0
        if startTime <= 1:
            for time in self.uniqStamps:
                total += self.timestampHits[time]
        else:
            while startTime not in self.timestampHits:
                if startTime == timestamp: return 0
                startTime += 1
            for time in self.uniqStamps[self.uniqStamps.index(startTime):]:
                total += self.timestampHits[time]

        return total



# Your HitCounter object will be instantiated and called as such:
counter = HitCounter()

#hit at timestamp 1.
counter.hit(2)

# hit at timestamp 2.
counter.hit(3)

# hit at timestamp 3.
counter.hit(4)

# get hits at timestamp 4, should return 3.
print(counter.getHits(300))
# hit at timestamp 300.
print(counter.getHits(301))
print(counter.getHits(302))
print(counter.getHits(303))
print(counter.getHits(304))
counter.hit(501)


# get hits at timestamp 300, should return 4.
print(counter.getHits(600))

# get hits at timestamp 301, should return 3.
# print(counter.getHits(301))