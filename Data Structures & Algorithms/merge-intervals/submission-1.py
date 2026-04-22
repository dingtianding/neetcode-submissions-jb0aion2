class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda pair:pair[0]) #sort based on start time

        output = [intervals[0]] #start with something in output

        for start, end in intervals:
            lastEnd = output[-1][1]#the last one in output is our lastEnd

            if start <= lastEnd:#if start is less than lastEnd, did not end
                output[-1][1] = max(lastEnd, end)#we take the larger end(merge)
            else:#if start is greater.
                output.append([start, end]) #add the new intervals as the new last
        return output #once done return

        