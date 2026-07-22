class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #make hash
        #key = count
        #value = all string with same count as a array
        count = defaultdict(list)
        
        #go through stach string
        for s in strs:
            sCount = [0] * 26
        #create a count array
        #for each of the char of the string
            for c in s:
        #increase the delta index of that char
                delta = ord(c) - ord('a')
                sCount[delta] += 1
        #set counter's key as the tuple of the count
        #add the string the counter's value
            count[tuple(sCount)].append(s)

        return list(count.values())
        #return the values in a list

        