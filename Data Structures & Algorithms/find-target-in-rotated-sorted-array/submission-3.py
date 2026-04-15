class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        #[3,4,5,1,2] target = 1
        #
        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid
            if nums[l] <= nums[mid]:#12345
                if target > nums[mid] or target < nums[l]:
                    #go right
                    #1. target is greater than mid point. 
                    #2. target is less than our left bound. Rotated to right
                    l = mid + 1
                else:
                    r = mid - 1
            else:#45123
                if target < nums[mid] or target > nums[r]:
                    #go left:
                    #1. target is less than target
                    #2. target is greater than right bound
                    r = mid -1
                else:
                    l = mid + 1

        return -1
        