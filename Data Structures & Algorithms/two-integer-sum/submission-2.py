class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        comps = {}

        for i in range(len(nums)):
            comp = target - nums[i] # need 9(10-1)#key = 9(value), value = 0(index)
            if comp in comps: # 
                return [comps[comp], i]
            comps[nums[i]] = i #