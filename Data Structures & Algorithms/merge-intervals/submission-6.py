class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #sort the interval on start
        #init a result array we can have the first interval in there
        intervals.sort(key=lambda pair: pair[0])
        res = [intervals[0]]
        #go through each
        #check the previous end againist current start
        # if prev didn't end(greater then cur start) 
        # merge:
        # update prev end to the new end
        # if not merge:
        # append the current interval to res
        for start, end in intervals:
            lastEnd = res[-1][1]
            if lastEnd >= start:
                res[-1][1] = max(lastEnd, end)
            else:
                res.append([start,end])

        return res
        # return the res

        