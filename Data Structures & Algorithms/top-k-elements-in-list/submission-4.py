class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Input: nums = [1,2,2,3,3,3], k = 2
        # Output: [2,3]
        # count{3:3, 2:2, 1:1}
        # any order so 3 and 2 = [2,3]
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        heap = []
        for num in counter.keys():
            heapq.heappush(heap, (counter[num], num))
            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res




        