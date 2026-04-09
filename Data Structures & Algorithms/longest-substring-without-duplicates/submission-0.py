class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l, r, n = 0, 0, len(s)
        count = set()

        while r < n:
            while s[r] in count:
                count.remove(s[l])
                l += 1
            count.add(s[r])
            cur = r - l + 1
            res = max(res, cur)
            r += 1


        return res
        