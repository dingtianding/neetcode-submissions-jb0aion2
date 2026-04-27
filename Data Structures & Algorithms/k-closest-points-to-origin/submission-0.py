class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for x, y in points:
            dist = (x ** 2) + (y ** 2)
            heap.append([dist, [x, y]])

        heapq.heapify(heap)
        res = []
        while k > 0:
            dist, pair = heapq.heappop(heap)
            res.append(pair)
            k -= 1
        return res