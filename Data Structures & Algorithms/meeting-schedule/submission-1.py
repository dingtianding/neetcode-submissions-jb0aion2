"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
# INPUT = [(start1,end1),(start2,end2)...]
# interval[0] = interval.start Englishy

# in side of pair, end time cames after start time
# we get a bunch of meeting time(in form of start time and end time), we perform a check
# if these meeting times have any overlaps
# context meeting start time and meeting end
# 0 8, 8-10 is good. This not a overlap
# Contraints
# intervals = [(15,20),(0,30),(5,10)] in different order
# 1. Sort it based on starting # Log N @@ underhood sorting why it is Log N
# [(0-5,30),(5,10),(15,20)]
# 2. iterate end1 > start2 aka early meeting did not finsh return false N
# 3. finish all meeting -> no overlap
# 
# Big O Complexity 
# Time Log N * N(length of the intervals) * 2
# space 1
#[(null,30),(5,10),(15,20)]
class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda i:i.start)
        n = len(intervals)

        for i in range(n - 1): # 0,1,2 -> 0,1
            end1 = intervals[i].end
            start2 = intervals[i+1].start

            if end1 > start2:
                return False

        return True
