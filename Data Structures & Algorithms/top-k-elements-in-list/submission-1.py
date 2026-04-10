class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        heap = []
        for num in count.keys():
            heapq.heappush(heap, (count[num], num)) #first one is used to sort with heap
            if len(heap) > k: #if exceed
                heapq.heappop(heap) #pop the smallest extra

        res = []

        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res

        