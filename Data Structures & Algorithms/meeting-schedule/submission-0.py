"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda i:i.start)
        n = len(intervals)
        for i in range(1, n):
            early = intervals[i-1]
            later = intervals[i]
            if early.end > later.start:
                return False


        return True
            
