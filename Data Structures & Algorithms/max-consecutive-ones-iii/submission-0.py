class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

#         Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2

# Output: 6

        l = 0
        res = 0
        
        for r in range(len(nums)):
            # k -= (1 if nums[r] == 0 else 0)
            if nums[r] == 0:
                k -= 1
            while k < 0:
                if nums[l] == 0:
                    k += 1
                # k += (1 if nums[l] == 0 else 0)
                l += 1
            cur = r - l + 1
            res = max(res, cur)

        return res

        