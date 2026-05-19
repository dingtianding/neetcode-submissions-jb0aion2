# Example 1:

# Input: nums = [1,2,2,3,3,3], k = 2
# Output: [2,3] = Top 2 Frequenc number from nums
# counter = {3:3, 2:2, 1:1}
# Top 1 freq = number 3
# Top 2 freq = number 2
# Thats top K, we stop here
# return [3,2]
# Python min Heap -> heappop(it pop lowest one)
# two pass
# one pass create counter likehas
# counter = {3:3, 2:2, 1:1}
# two pass
# go thorugh all number vs freq (key/value)
# push them into the heap
# we attemp keep this heap at size of k
# if we ever reach k + 1, we eject by heappop(remove the lowest)
# lowest has to be lowest in frequency(place freq in front for heap to sort it)
# Time N(number of num) Log K(unique K)
# Space N = N

from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        # counter = {3:3, 2:2, 1:1}
        heap = []

        for num, freq in count.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap) #eject lowest freq out of the heap

        res = []
        for _, num in heap:
            res.append(num)
        return res



        