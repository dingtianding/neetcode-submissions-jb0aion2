class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0 

        for num in numSet:
            if (num - 1) not in numSet:
                cur = 1
                while(num + cur) in numSet:
                    cur += 1
                longest = max(cur, longest)

        return longest


        