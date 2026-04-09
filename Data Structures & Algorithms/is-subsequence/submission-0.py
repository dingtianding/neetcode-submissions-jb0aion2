class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l , r = 0, 0

        while l < len(s) and r < len(t):
            if s[l] == t[r]:
                r += 1
                l += 1
            else:
                r += 1

        if l == len(s):
            return True
        else:
            return False

            
        