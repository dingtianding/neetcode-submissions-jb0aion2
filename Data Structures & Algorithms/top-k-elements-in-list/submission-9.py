from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)#turn the num array into a counter based on frequenc

        heap = []

        for num in count.keys(): #for each ofthe key(num)
            heapq.heappush(heap,(count[num], num)) #push in freq first and number 2nd
            if len(heap) > k:#if its greater our needed size
                heapq.heappop(heap)# we pop the smallest one

        res = []
        #strcuture the res return
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
        