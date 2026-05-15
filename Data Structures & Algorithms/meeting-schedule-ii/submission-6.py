"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = []
        ends = []

        for i in intervals:
            starts.append(i.start)
            ends.append(i.end)

        starts = sorted(starts)
        ends = sorted(ends)

        res = 0
        count = 0
        s = 0
        e = 0
        while s < len(intervals):
            if starts[s] < ends[e]:
                s += 1
                count += 1
            else:
                e += 1
                count -= 1
            res = max(res, count)

        return res


        