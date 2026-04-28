class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Input: s = "AAABABB", k = 1
        # Output: 5
        count = defaultdict(int)
        res = 0

        l = 0
        cur = 0
        for r in range(len(s)):
            count[s[r]] += 1
            cur = max(cur, count[s[r]])

            while(r - l + 1) - cur > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res

        