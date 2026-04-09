class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        heap = []

        for key, val in count.items():
            heapq.heappush(heap, (val, key)) #check on the val
            if len(heap) > k:
                heapq.heappop(heap) # smallest
            
        res = []
        while len(res) < k:
            res.append(heapq.heappop(heap)[1])

        return res
