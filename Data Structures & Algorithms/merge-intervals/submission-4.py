class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda pair: pair[0])
        output = [intervals[0]]

        for start, end in intervals:
            lastEnd = output[-1][1]
            if start <= lastEnd: #mergable
                output[-1][1] = max(lastEnd, end)
            else:#not mergable
                output.append([start, end])

        return output
        