"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key = lambda x:x.start)
        #0-40,5-10,15-20

        min_heap = []
        for i in intervals:#15-20
            if min_heap and min_heap[0] <= i.start:# 10 < 15
                heapq.heappop(min_heap) # 10 gets popped
            heapq.heappush(min_heap, i.end)#40,20

        return len(min_heap) #40,20 two room

        