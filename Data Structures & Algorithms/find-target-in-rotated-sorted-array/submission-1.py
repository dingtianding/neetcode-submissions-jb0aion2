class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l , r = 0, len(nums) - 1

        # target 1
        # 3,4,5,6,1,2 
        # l.  m     r
        # 1. 3 < 5 = increasing
        # 2. 1 > 5. or 1 < 2 on the right
        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid

            if nums[l] <= nums[mid]: #left is increasing
                if target > nums[mid] or target < nums[l]:#if target is greater(to right), or target is less than first(to right)
                    l = mid + 1 #move to right
                else:
                    r = mid -1

            else:#if left is greater 5,1,2,3,4
                if target < nums[mid] or target > nums[r]: #if target is less(og left) if target is greater(if 5, go left)
                    r = mid - 1 #go left
                else:
                    l = mid + 1

        return -1

        