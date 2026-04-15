class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 3 4 5 1 2
        #  3<5>2
        #

        l = 0
        r = len(nums) - 1

        while l < r: #3 = 3
            m = (l + r)//2
            if nums[m] < nums[r]: # 
                r = m
            else: 
                l = m + 1

        return nums[l]