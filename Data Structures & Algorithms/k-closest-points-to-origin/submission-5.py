class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #create heap
        heap = []
        #add all the points to heap
        #0 index is the dist, min heap so lower on top
        #1 index isthe coordinate to be added later
        for x, y in points:
            dist = x ** 2 + y ** 2
            heapq.heappush(heap, [dist, [x, y]])

        res = []
        #create res
        #push 1 index to res until we have k count
        while k > 0:
            dist, pair = heapq.heappop(heap)
            res.append(pair)
            k -= 1
        return res
        # return
