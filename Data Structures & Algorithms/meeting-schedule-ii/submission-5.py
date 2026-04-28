"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        starts = sorted([i.start for i in intervals])
        ends = sorted([i.end for i in intervals])

        cur = 0
        res = 0
        s = 0
        e = 0

        while s < len(intervals):
            if starts[s] < ends[e]: #if start first
                cur += 1 #start a room
                res = max(res, cur)
                s += 1
            else:#end next
                cur -= 1
                e += 1
        
        return res
        