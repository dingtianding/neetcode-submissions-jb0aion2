class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counter = defaultdict(list)
        
        for s in strs:
            sCount = [0] * 26
            for c in s:
                delta = ord(c) - ord('a')
                sCount[delta] += 1
            counter[tuple(sCount)].append(s)

        return list(counter.values())
        