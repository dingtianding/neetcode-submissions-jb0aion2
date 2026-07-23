class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #create a set from the Nums O(N)
        #create the res
        count = set(nums)
        res = 0

        #go through nums
        for num in nums:
            cur = 1
            if (num - 1) not in count:
                while (num + cur) in count:
                    cur += 1
                res = max(res, cur)

        return res
        #only start a search if its left most honest, num -1 DNE
        



        