"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([i.start for i in intervals]) #start time increasing
        end = sorted([i.end for i in intervals]) #end time increasing

        res = 0 # room needed
        count = 0 #current room count
        s = e = 0 #start and end pointers

        while s < len(intervals):
            if start[s] < end[e]: #if start is eariler than end, upcoming event is a start
                #start meeting/take a room
                s += 1 #move the pointer af
                count += 1
            else: # if they are equal, we end the meeting before to avoid count going up for a moment
                #if end is greater than start, upc is a end
                e += 1
                count -= 1
            res = max(res, count) #update max room each time a event happen

        return res


        