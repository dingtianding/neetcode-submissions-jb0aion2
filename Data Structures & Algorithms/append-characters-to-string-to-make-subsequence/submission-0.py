class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        res = 0
        i, j = 0, 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:#match, can be subtring
                i += 1
                j += 1
            else: #no match i search forward in s
                i += 1

        dist_to_end = len(t) - j
        return dist_to_end
        