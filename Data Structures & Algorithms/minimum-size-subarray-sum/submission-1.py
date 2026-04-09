class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        total = 0
        res = float("inf")

        for r in range(len(nums)): # continue expanding
            total += nums[r]
            while total >= target:#if satisfy target
                res = min(r - l + 1, res)#log it and see if its better
                total -= nums[l]#shrink reduce total
                l += 1#shrink pointer

        return 0 if res ==float("inf") else res #if never reached, we return 0, else get the best result
        